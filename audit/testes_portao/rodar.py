#!/usr/bin/env python3
"""Teste do portão: 12 casos plantados (4 limpos, 8 com defeito) contra cinco verificadores.

Verificadores:
  G  grep do `ci.yml`/`audit.yml` do M-Core até 11/11/2026: `\\bsorry\\b|\\badmit\\b` no texto da fonte;
  T  a busca que o substitui (`.github/scripts/sem_sorry.py`): a mesma palavra, fora de comentários e strings;
  L  aviso do elaborador no log de compilação (`declaration uses 'sorry'`);
  M  o portão do M-Core, `atk-kernel/scripts/check_axioms.py`, sem alteração: compila, `#print axioms`
     só com os três padrões, e a fonte sem comentários não contém `sorry`, `admit` nem linha `axiom`;
  V  o detector de enunciados vazios do MVEI (expressões de `tools/garimpo_enunciados.py`);
  K  o verificador de referência `Auditoria.lean`: axiomas pelo kernel, conclusão vazia depois de
     desdobrar definições, hipóteses contraditórias.

Uso: python3 rodar.py [--lean "lean +leanprover/lean4:v4.34.1"]. Grava resultados.json e resultados.md.
Sai com erro se K errar algum caso ou se M deixar de pegar um defeito visível no kernel (C02–C06).
"""
import argparse
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
PORTAO = os.path.join(AQUI, "..", "..", "atk-kernel", "scripts", "check_axioms.py")
sys.path.insert(0, os.path.join(AQUI, "..", "..", ".github", "scripts"))
from sem_sorry import codigo  # noqa: E402

CASOS = {
    "C01": ("limpo", None),
    "C02": ("sorry tático", "sorry"),
    "C03": ("sorryAx escrito direto", "sorry"),
    "C04": ("axioma com atributo na linha", "axioma"),
    "C05": ("axioma privado", "axioma"),
    "C06": ("native_decide", "confia no compilador"),
    "C07": ("limpo; 'sorry' em comentário e docstring", None),
    "C08": ("limpo; 'sorry' dentro de uma string", None),
    "C09": ("enunciado `True`", "vazio"),
    "C10": ("vazio escondido numa definição", "vazio"),
    "C11": ("hipótese contraditória", "vazio"),
    "C12": ("limpo; condicional honesto", None),
}
VERIFICADORES = {
    "G": "grep do ci.yml",
    "T": "busca sem comentários",
    "L": "aviso de sorry no log",
    "M": "portão do M-Core",
    "V": "vazios do MVEI",
    "K": "referência (kernel)",
}
# MVEI, tools/garimpo_enunciados.py
TRUE_FIM = re.compile(r"(?:^:?|:|→|,)\s*True\s*$")
EXISTE_TRUE = re.compile(r"∃[^,]*,\s*True\s*$")


def roda(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lean", default="lean")
    a = ap.parse_args()
    lean = shlex.split(a.lean)
    tmp = tempfile.mkdtemp(prefix="portao_")
    raiz = os.path.join(tmp, "raiz")
    for d in ("ATK", "scripts", "reports"):
        os.makedirs(os.path.join(raiz, d))
    shutil.copy(PORTAO, os.path.join(raiz, "scripts", "check_axioms.py"))
    with open(os.path.join(raiz, "scripts", "expected_theorems.txt"), "w") as f:
        f.writelines(f"ATK.{c}.alvo\n" for c in CASOS)
    with open(os.path.join(raiz, "ATK.lean"), "w") as f:  # o portão inclui o módulo raiz no hash das fontes
        f.writelines(f"import ATK.{c}\n" for c in CASOS)
    with open(os.path.join(raiz, "lean-toolchain"), "w") as f:
        f.write(roda(lean + ["--version"]).stdout.strip() + "\n")

    r = roda(lean + ["-o", os.path.join(tmp, "Auditoria.olean"), os.path.join(AQUI, "Auditoria.lean")])
    if r.returncode != 0:
        sys.exit("Auditoria.lean não compilou:\n" + r.stdout + r.stderr)

    marcou = {v: {} for v in VERIFICADORES}
    status = []
    for c in CASOS:
        fonte = open(os.path.join(AQUI, "casos", f"{c}.lean"), encoding="utf-8").read()
        alvo = os.path.join(raiz, "ATK", f"{c}.lean")
        open(alvo, "w", encoding="utf-8").write(fonte)
        r = roda(lean + [alvo])
        log = r.stdout + r.stderr
        open(os.path.join(raiz, "reports", f"audit_{c}.log"), "w").write(log)
        status.append(f"ATK/{c}.lean {'OK' if r.returncode == 0 else 'FAIL'}\n")
        marcou["G"][c] = re.search(r"\bsorry\b|\badmit\b", fonte) is not None
        marcou["T"][c] = re.search(r"\b(sorry|admit)\b", codigo(fonte)) is not None
        marcou["L"][c] = re.search(r"declaration uses .sorry.", log) is not None or r.returncode != 0
        enunciado = re.search(r"theorem\s+alvo(.*?):=", fonte, re.S).group(1).strip()
        marcou["V"][c] = bool(TRUE_FIM.search(enunciado) or EXISTE_TRUE.search(enunciado))
        emb = os.path.join(tmp, f"W{c}.lean")
        open(emb, "w", encoding="utf-8").write("import Auditoria\n" + fonte + "\n#auditar\n")
        k = roda(lean + [emb], env={**os.environ, "LEAN_PATH": tmp})
        m = re.search(rf"AUDITORIA ATK\.{c}\.alvo: (.*)", k.stdout)
        if not m:
            sys.exit(f"{c}: o verificador de referência não respondeu\n{k.stdout}{k.stderr}")
        marcou["K"][c] = m.group(1).strip() != "OK"
        CASOS[c] = CASOS[c] + (m.group(1).strip(),)
    open(os.path.join(raiz, "reports", "file_status.txt"), "w").writelines(status)
    roda([sys.executable, os.path.join(raiz, "scripts", "check_axioms.py")], env={**os.environ, "ATK_ENSAIO": "0"})
    rep = json.load(open(os.path.join(raiz, "reports", "report.json")))
    for t in rep["theorems"]:
        marcou["M"][t["theorem"].split(".")[1]] = t["verdict"] != "CERTIFIED"
    motivoM = {t["theorem"].split(".")[1]: t["reason"] for t in rep["theorems"]}

    resumo = {}
    for v in VERIFICADORES:
        pegou = sum(1 for c, (_, d, *_) in CASOS.items() if d and marcou[v][c])
        falsos = sum(1 for c, (_, d, *_) in CASOS.items() if not d and marcou[v][c])
        resumo[v] = {"defeitos_pegos": pegou, "defeitos": sum(1 for x in CASOS.values() if x[1]),
                     "alarmes_falsos": falsos, "limpos": sum(1 for x in CASOS.values() if not x[1])}
    lin = ["| Caso | Defeito | " + " | ".join(f"{k}: {n}" for k, n in VERIFICADORES.items()) + " |",
           "|---|---|" + "---|" * len(VERIFICADORES)]
    for c, (desc, d, kv) in CASOS.items():
        cel = []
        for v in VERIFICADORES:
            x = marcou[v][c]
            cel.append(("pegou" if x else "**deixou passar**") if d else ("**alarme falso**" if x else "ok"))
        lin.append(f"| {c} {desc} | {d or '—'} | " + " | ".join(cel) + " |")
    lin.append("| **Total** | | " + " | ".join(
        f"{resumo[v]['defeitos_pegos']}/{resumo[v]['defeitos']} pegos, {resumo[v]['alarmes_falsos']} falsos"
        for v in VERIFICADORES) + " |")
    versao = open(os.path.join(raiz, "lean-toolchain")).read().strip()
    md = "\n".join([f"# Teste do portão ({versao})", ""] + lin) + "\n"
    open(os.path.join(AQUI, "resultados.md"), "w", encoding="utf-8").write(md)
    json.dump({"lean": versao, "resumo": resumo, "marcou": marcou, "motivo_M": motivoM,
               "veredito_K": {c: x[2] for c, x in CASOS.items()}},
              open(os.path.join(AQUI, "resultados.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(md)
    erros = [c for c, (_, d, *_) in CASOS.items() if marcou["K"][c] != bool(d)]
    erros += [f"M deixou passar {c}" for c in ("C02", "C03", "C04", "C05", "C06") if not marcou["M"][c]]
    shutil.rmtree(tmp, ignore_errors=True)
    if erros:
        sys.exit("falhou: " + ", ".join(erros))


if __name__ == "__main__":
    main()
