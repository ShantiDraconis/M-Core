#!/usr/bin/env python3
"""Status calculado do ATK — nada aqui é digitado à mão.

Uso (de dentro de atk-kernel/, com o toolchain do lean-toolchain no PATH e a biblioteca compilada):

    python3 scripts/status_calculado.py --rodar      # roda o kernel e grava audits/auditoria_axiomas.tsv
    python3 scripts/status_calculado.py              # só recalcula a partir do TSV já gravado

Saídas: audits/status_calculado.json e audits/status_calculado.md.

O que é calculado:
* por teorema `ATK.*`: axiomas de que depende (Lean.collectAxioms, via audits/AuditoriaAxiomas.lean);
  permitido = {propext, Classical.choice, Quot.sound};
* na fonte de ATK/: tokens `sorry`/`admit` fora de comentários, declarações `axiom`, `native_decide`;
* por linha de scripts/terminal_gates.json: o arquivo-portão existe? o teorema-portão está certificado?
* por obrigação de scripts/obligations.json: se tem `proof_theorem`, ele está certificado? o status
  declarado bate com o calculado?
"""
import json, os, re, subprocess, sys, datetime

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PERMITIDOS = {"propext", "Classical.choice", "Quot.sound"}
TSV = os.path.join(RAIZ, "audits", "auditoria_axiomas.tsv")


def rodar_kernel():
    src = open(os.path.join(RAIZ, "audits", "AuditoriaAxiomas.lean"), encoding="utf-8").read()
    src = re.sub(r"^import Lean\s*$", "", src, flags=re.M)
    driver = os.path.join(RAIZ, ".lake", "auditoria_driver.lean")
    os.makedirs(os.path.dirname(driver), exist_ok=True)
    with open(driver, "w", encoding="utf-8") as f:
        f.write("import ATK\nimport Lean\n" + src + "\n#auditoria_atk\n")
    r = subprocess.run(["lake", "env", "lean", driver], cwd=RAIZ, capture_output=True, text=True)
    with open(TSV, "w", encoding="utf-8") as f:
        f.write(r.stdout)
    if r.returncode != 0:
        sys.stderr.write(r.stderr[-4000:])
        sys.exit("falha ao rodar o kernel (ver stderr acima)")


def limpar_lean(s):
    out, i, n, prof = [], 0, len(s), 0
    while i < n:
        if prof == 0 and s.startswith("--", i):
            j = s.find("\n", i)
            i = n if j < 0 else j
            continue
        if s.startswith("/-", i):
            prof += 1; i += 2; continue
        if prof and s.startswith("-/", i):
            prof -= 1; i += 2; continue
        if prof == 0 and s[i] == '"':
            j = i + 1
            while j < n and s[j] != '"':
                j += 2 if s[j] == "\\" else 1
            out.append('""'); i = j + 1; continue
        if prof == 0 or s[i] == "\n":
            out.append(s[i])
        i += 1
    return "".join(out)


def varrer_fonte():
    achados = []
    base = os.path.join(RAIZ, "ATK")
    for dp, _, fs in os.walk(base):
        for f in fs:
            if not f.endswith(".lean"):
                continue
            p = os.path.join(dp, f)
            s = limpar_lean(open(p, encoding="utf-8", errors="replace").read())
            rel = os.path.relpath(p, RAIZ)
            for tok, pat in [("sorry", r"\bsorry\b"), ("admit", r"\badmit\b"),
                             ("axiom", r"^\s*axiom\s"), ("native_decide", r"\bnative_decide\b")]:
                k = len(re.findall(pat, s, flags=re.M))
                if k:
                    achados.append({"arquivo": rel, "token": tok, "ocorrencias": k})
    return achados


def ler_tsv():
    tms, axs, resumo = {}, [], ""
    for l in open(TSV, encoding="utf-8"):
        p = l.rstrip("\n").split("\t")
        if p[0] == "TEOREMA":
            ax = [a.strip() for a in p[3].strip("[]").split(",") if a.strip()]
            tms[p[2]] = ax
        elif p[0] == "AXIOMA_ATK":
            axs.append(p[1])
        elif p[0] == "RESUMO":
            resumo = l.strip()
    return tms, axs, resumo


def main():
    if "--rodar" in sys.argv:
        rodar_kernel()
    tms, axs, resumo = ler_tsv()
    certificado = lambda n: n in tms and set(tms[n]) <= PERMITIDOS
    proibidos = {n: a for n, a in tms.items() if not set(a) <= PERMITIDOS}
    fonte = varrer_fonte()

    gates = json.load(open(os.path.join(RAIZ, "scripts", "terminal_gates.json"), encoding="utf-8"))
    linhas = []
    for l in gates["lines"]:
        existe = os.path.exists(os.path.join(RAIZ, l["gate_file"]))
        linhas.append({
            "linha": l["id"], "produtor": l["producer"],
            "equivalencia": l.get("producer_equivalence"),
            "equivalencia_certificada": certificado(l["producer_equivalence"]) if l.get("producer_equivalence") else None,
            "arquivo_portao": l["gate_file"], "arquivo_portao_existe": existe,
            "teorema_portao_certificado": certificado(l["gate_theorem"]),
            "produtor_material": existe and certificado(l["gate_theorem"]),
        })

    obr = json.load(open(os.path.join(RAIZ, "scripts", "obligations.json"), encoding="utf-8"))["obligations"]
    obrig = []
    for o in obr:
        pt = o.get("proof_theorem")
        calc = ("PROVADA_NO_KERNEL" if pt and certificado(pt) else
                ("PROVA_DECLARADA_MAS_NAO_CERTIFICADA" if pt else "SEM_PROVA_NO_KERNEL"))
        decl = o.get("status")
        obrig.append({"id": o["id"], "problema": o.get("problem"), "status_declarado": decl,
                      "status_calculado": calc, "teorema": pt,
                      "divergente": (decl == "PROVADA_NO_KERNEL") != (calc == "PROVADA_NO_KERNEL")})

    status = {
        "gerado_em_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "kernel": {"resumo": resumo, "teoremas": len(tms),
                   "certificados": sum(1 for n in tms if certificado(n)),
                   "proibidos": sorted(proibidos), "axiomas_declarados_sob_ATK": axs},
        "fonte": fonte,
        "linhas": linhas,
        "produtores_materiais": sum(1 for l in linhas if l["produtor_material"]),
        "obrigacoes": obrig,
    }
    json.dump(status, open(os.path.join(RAIZ, "audits", "status_calculado.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    md = ["# Status calculado do ATK", "",
          f"Gerado por `scripts/status_calculado.py` em {status['gerado_em_utc']}. Nada aqui é digitado.", "",
          f"* Teoremas `ATK.*` no ambiente: {len(tms)}; certificados (só axiomas padrão): {status['kernel']['certificados']}; "
          f"proibidos: {len(proibidos)}; axiomas declarados sob `ATK`: {len(axs)}.",
          f"* Produtores materiais (portão existe e certificado): {status['produtores_materiais']} de {len(linhas)}.", "",
          "| Linha | Produtor | Equivalência certificada | Arquivo-portão existe | Produtor material |",
          "| --- | --- | --- | --- | --- |"]
    for l in linhas:
        md.append(f"| {l['linha']} | `{l['produtor']}` | {l['equivalencia_certificada']} | "
                  f"{l['arquivo_portao_existe']} | {l['produtor_material']} |")
    md += ["", "| Obrigação | Declarado | Calculado | Teorema |", "| --- | --- | --- | --- |"]
    for o in obrig:
        flag = " ⚠" if o["divergente"] else ""
        md.append(f"| {o['id']} | {o['status_declarado']} | {o['status_calculado']}{flag} | `{o['teorema'] or '—'}` |")
    if proibidos:
        md += ["", "## Teoremas com axiomas proibidos", ""] + [f"* `{n}`: {a}" for n, a in sorted(proibidos.items())]
    if fonte:
        md += ["", "## Tokens na fonte (fora de comentários)", ""] + \
              [f"* `{x['arquivo']}`: {x['token']} × {x['ocorrencias']}" for x in fonte]
    open(os.path.join(RAIZ, "audits", "status_calculado.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
    print("\n".join(md[:8]))


if __name__ == "__main__":
    main()
