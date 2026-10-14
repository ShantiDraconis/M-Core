#!/usr/bin/env python3
"""ENSAIO de ponta a ponta do portão do verde universal — com enunciados de BRINQUEDO.

Mostra que a máquina (`universal_green.compute`) chega a `UNIVERSAL_GREEN = true` e calcula
`FINAL_ROOT` quando os sete portões existem e são válidos, e que fica vermelha em cada tentativa de
fraude. Os portões do ensaio provam fatos triviais (`2 + 2 = 4`, …) numa pasta temporária, com
registro próprio; o registro real (`scripts/terminal_gates.json`) nunca é tocado. Os arquivos são
compilados de verdade pelo Lean (núcleo, sem Mathlib).

ISTO NÃO PROVA NENHUMA CONJECTURA: é um teste do auditor.
"""
import copy
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import universal_green as ug  # noqa: E402

TOY = {"RH": "2 + 2 = 4", "Beal": "3 ^ 3 + 6 ^ 3 = 3 ^ 5", "NS": "10 - 3 = 7",
       "PNP": "2 ^ 10 = 1024", "Hodge": "7 * 6 = 42", "BSD": "5 % 3 = 2", "YM": "1 + 1 = 2"}
LINKING = {"NS": "L1", "PNP": "L2", "Hodge": "L3", "BSD": "L4", "YM": "L5"}
IDS = list(TOY)

ALVOS = ("/-! Enunciados-alvo do ENSAIO (brinquedo): fazem o papel das constantes oficiais. -/\n\n"
         + "".join(f"def Alvo{k} : Prop := {v}\n" for k, v in TOY.items())
         + "def AlvoFiel : Prop := AlvoRH ∧ AlvoBeal\n"
         + "def AlvoFinal : Prop := " + " ∧ ".join(f"Alvo{k}" for k in IDS) + "\n")


def registry():
    lines = []
    for k in IDS:
        lines.append({"id": k, "problem": f"{k} (ensaio)", "faithful": k in ("RH", "Beal"),
                      "statement": f"Alvo{k}", "statement_root": f"_root_.Alvo{k}",
                      "gate_file": f"ATK/Terminal/{k}.lean", "gate_theorem": f"ATK.Terminal.{k}.terminal",
                      "bridges": [], "obligations": [], "producer": "—", "producer_equivalence": None,
                      "linking": LINKING.get(k)})
    return {"rule": "ensaio", "lines": lines,
            "final_root": {"gate_file": "ATK/ClosedMathGate.lean", "gate_theorem": "ATK.ClosedMathGate.closed_math",
                           "statement": "AlvoFinal", "statement_root": "_root_.AlvoFinal",
                           "structure": "AlvoFinal", "reduction": "composição dos sete portões"},
            "universal_green_fiel": {"gate_file": "ATK/Terminal/VerdeFiel.lean",
                                     "gate_theorem": "ATK.Terminal.VerdeFiel.verde_fiel",
                                     "statement": "AlvoFiel", "statement_root": "_root_.AlvoFiel",
                                     "exact_form": "AlvoRH ∧ AlvoBeal"}}


def gate_src(k, proof=None, pre="", header=None, stmt=None):
    proof = proof or f"by unfold Alvo{k}; decide"
    head = header if header is not None else f"theorem terminal : {stmt or 'Alvo' + k} := {proof}"
    return (f"import Alvos\n\n{pre}namespace ATK.Terminal.{k}\n\n{head}\n\nend ATK.Terminal.{k}\n\n"
            f"#print axioms ATK.Terminal.{k}.terminal\n")


def base_files():
    files = {"Alvos.lean": ALVOS}
    for k in IDS:
        files[f"ATK/Terminal/{k}.lean"] = gate_src(k)
    files["ATK/Terminal/VerdeFiel.lean"] = (
        "import ATK.Terminal.RH\nimport ATK.Terminal.Beal\n\nnamespace ATK.Terminal.VerdeFiel\n\n"
        "theorem verde_fiel : AlvoFiel := ⟨ATK.Terminal.RH.terminal, ATK.Terminal.Beal.terminal⟩\n\n"
        "end ATK.Terminal.VerdeFiel\n\n#print axioms ATK.Terminal.VerdeFiel.verde_fiel\n")
    files["ATK/ClosedMathGate.lean"] = (
        "".join(f"import ATK.Terminal.{k}\n" for k in IDS) + "\nnamespace ATK.ClosedMathGate\n\n"
        "theorem closed_math : AlvoFinal :=\n  ⟨" + ", ".join(f"ATK.Terminal.{k}.terminal" for k in IDS)
        + "⟩\n\nend ATK.ClosedMathGate\n\n#print axioms ATK.ClosedMathGate.closed_math\n")
    return files


SCENARIOS = [
    ("verde", "todos os portões válidos", {}, None, {"UNIVERSAL_GREEN": True, "root": True}),
    ("sorry", "RH provado com `sorry`", {"ATK/Terminal/RH.lean": gate_src("RH", "by sorry")}, None,
     {"UNIVERSAL_GREEN": False, "red": "RH"}),
    ("sombra", "RH sombreia o enunciado (`def AlvoRH := True` no namespace do portão)",
     {"ATK/Terminal/RH.lean": gate_src("RH", "trivial", pre="", header="def AlvoRH : Prop := True\n\n"
                                       "theorem terminal : AlvoRH := trivial")}, None,
     {"UNIVERSAL_GREEN": False, "red": "RH"}),
    ("hipotese", "Beal com hipótese no teorema terminal",
     {"ATK/Terminal/Beal.lean": gate_src("Beal", header="theorem terminal (h : 1 = 1) : AlvoBeal := "
                                         "by unfold AlvoBeal; decide")}, None,
     {"UNIVERSAL_GREEN": False, "red": "Beal"}),
    ("axioma", "NS provado por um axioma próprio",
     {"ATK/Terminal/NS.lean": gate_src("NS", "atalho", pre="axiom atalho : AlvoNS\n\n")}, None,
     {"UNIVERSAL_GREEN": False, "red": "NS"}),
    ("enunciado_trocado", "P≠NP prova outro enunciado (`True`)",
     {"ATK/Terminal/PNP.lean": gate_src("PNP", "trivial", stmt="True")}, None,
     {"UNIVERSAL_GREEN": False, "red": "PNP"}),
    ("ligacao_aberta", "Hodge com a ligação L3 aberta", {}, {"L3": "NAO_EXISTE_NA_MATHLIB"},
     {"UNIVERSAL_GREEN": False, "red": "Hodge"}),
    ("nao_compila", "BSD com erro de compilação", {"ATK/Terminal/BSD.lean": gate_src("BSD", "by exact 0")}, None,
     {"UNIVERSAL_GREEN": False, "red": "BSD"}),
    ("ausente", "portão de YM ausente", {"ATK/Terminal/YM.lean": None}, None,
     {"UNIVERSAL_GREEN": False, "red": "YM"}),
    ("sem_raiz", "sete linhas verdes, sem o portão de CLOSED_MATH", {"ATK/ClosedMathGate.lean": None}, None,
     {"UNIVERSAL_GREEN": True, "root": False}),
]

ORDER = ["Alvos.lean"] + [f"ATK/Terminal/{k}.lean" for k in IDS] + ["ATK/Terminal/VerdeFiel.lean",
                                                                  "ATK/ClosedMathGate.lean"]


def make_runner(lean, tmp):
    env = dict(os.environ)
    env["LEAN_PATH"] = os.path.join(tmp, "build")

    def run(path, out=None):
        cmd = [lean, f"--root={tmp}"] + (["-o", out] if out else []) + [path]
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=300, env=env)
        return p.returncode, p.stdout + p.stderr
    return run


def compile_all(tmp, files, runner):
    fstatus = {}
    rep = os.path.join(tmp, "reports")
    os.makedirs(rep, exist_ok=True)
    for rel in ORDER:
        text = files.get(rel)
        if text is None:
            continue
        path = os.path.join(tmp, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w", encoding="utf-8").write(text)
        out = os.path.join(tmp, "build", rel[:-len(".lean")] + ".olean")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        code, log = runner(path, out)
        fstatus[rel] = "OK" if code == 0 and ": error" not in log else "FAIL"
        open(os.path.join(rep, "audit_" + rel.replace("/", "_")[:-len(".lean")] + ".log"), "w").write(log)
    return fstatus


def run(lean=None):
    lean = lean or shutil.which("lean")
    if lean is None:
        return {"ran": False, "reason": "lean não encontrado"}
    results = []
    for sid, desc, mut, links, expect in SCENARIOS:
        tmp = tempfile.mkdtemp(prefix=f"ensaio_{sid}_")
        try:
            os.makedirs(os.path.join(tmp, "scripts"))
            json.dump(registry(), open(os.path.join(tmp, "scripts", "terminal_gates.json"), "w"), ensure_ascii=False)
            files = base_files()
            files.update(mut)
            runner = make_runner(lean, tmp)
            fstatus = compile_all(tmp, files, runner)
            axioms = ug._axioms_from_logs(os.path.join(tmp, "reports"))
            check = lambda path: runner(path)  # noqa: E731
            closed = ug._gate(tmp, axioms, fstatus, "ATK/ClosedMathGate.lean", "ATK.ClosedMathGate.closed_math",
                              "AlvoFinal", "_root_.AlvoFinal", check)["ok"]
            statuses = {l: "CLOSED" for l in LINKING.values()}
            statuses.update(links or {})
            report = {"obligations": [{"id": k, "status": v} for k, v in statuses.items()],
                      "status": {"CLOSED_MATH": closed}, "sources_sha256": "ensaio", "commit": "ensaio"}
            res = ug.compute(tmp, report, axioms, fstatus, runner=check)
            s = res["summary"]
            red = [l["id"] for l in res["lines"] if not l["green"]]
            reasons = {}
            for l in res["lines"]:
                if not l["green"]:
                    r = l["gate"]["reason"]
                    if not r and l["linking"] and l["linking"]["status"] != "CLOSED":
                        r = "ligação " + l["linking"]["id"] + " " + l["linking"]["status"]
                    reasons[l["id"]] = r
            passed = s["UNIVERSAL_GREEN"] == expect["UNIVERSAL_GREEN"]
            if "root" in expect:
                passed = passed and ((s["FINAL_ROOT"] is not None) == expect["root"])
            if "red" in expect:
                passed = passed and red == [expect["red"]] and s["FINAL_ROOT"] is None
            results.append({"id": sid, "description": desc, "UNIVERSAL_GREEN": s["UNIVERSAL_GREEN"],
                            "LINES_GREEN": s["LINES_GREEN"], "FINAL_ROOT": s["FINAL_ROOT"], "red": red,
                            "reasons": reasons, "passed": passed})
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    n = sum(r["passed"] for r in results)
    return {"ran": True, "ok": n == len(results), "passed": f"{n}/{len(results)}", "scenarios": results}


def markdown(res):
    if not res.get("ran"):
        return [f"Ensaio do portão: não executado ({res.get('reason')})."]
    md = [f"### Ensaio do portão (enunciados de brinquedo) — {res['passed']} cenários corretos",
          "",
          "| Cenário | Situação | `UNIVERSAL_GREEN` | Linhas | `FINAL_ROOT` | Motivo do vermelho | Esperado |",
          "|---|---|---|---|---|---|---|"]
    for r in res["scenarios"]:
        why = "; ".join(f"{k}: {v}" for k, v in r["reasons"].items()) or "—"
        root = (r["FINAL_ROOT"][:16] + "…") if r["FINAL_ROOT"] else "null"
        md.append(f"| `{r['id']}` | {r['description']} | `{str(r['UNIVERSAL_GREEN']).lower()}` | {r['LINES_GREEN']} | "
                  f"`{root}` | {why} | {'✅' if r['passed'] else '❌'} |")
    md += ["", "O ensaio usa fatos triviais (`AlvoRH := 2 + 2 = 4`, …) no lugar das conjecturas: mostra que a "
           "máquina acende quando há provas válidas e bloqueia `sorry`, sombreamento de nomes, hipóteses, "
           "axiomas próprios, enunciado trocado, ligação aberta, erro de compilação e portão ausente. "
           "Não prova nenhuma conjectura."]
    return md


def main():
    res = run()
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    rep = os.path.join(root, "reports")
    os.makedirs(rep, exist_ok=True)
    json.dump(res, open(os.path.join(rep, "ensaio_universal_green.json"), "w"), indent=2, ensure_ascii=False)
    print("\n".join(markdown(res)))
    return 0 if res.get("ok") or not res.get("ran") else 1


if __name__ == "__main__":
    sys.exit(main())
