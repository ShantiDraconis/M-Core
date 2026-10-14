#!/usr/bin/env python3
"""Verde universal (UNIVERSAL_GREEN) e raiz final (FINAL_ROOT), calculados — nunca escritos à mão.

Para cada uma das 7 linhas de `scripts/terminal_gates.json`, a linha só é verde se:
  1. o arquivo do portão existe e compilou (`reports/file_status.txt` = OK);
  2. a fonte declara literalmente `theorem <nome> : <enunciado> :=` (sem hipóteses);
  3. `#print axioms <teorema>` ⊆ {propext, Classical.choice, Quot.sound};
  4. a fonte não tem sorry/admit/axiom fora de comentários;
  5. o TIPO elaborado do teorema é o enunciado oficial: `example : _root_.<enunciado> := <teorema>`
     compila num arquivo à parte (bloqueia sombreamento de nomes no namespace do portão);
  6. nas linhas paramétricas, a ligação (L1–L5) está CLOSED no relatório do auditor.
UNIVERSAL_GREEN = as 7 linhas verdes. FINAL_ROOT = SHA-256 do certificado terminal só se
UNIVERSAL_GREEN e o portão de CLOSED_MATH estiverem verdes; senão `null`.

Uso: chamado por `check_axioms.py` (função `compute`) ou sozinho, depois dele.
"""
import glob
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

ALLOWED = {"propext", "Classical.choice", "Quot.sound"}


def _axioms_from_logs(rep):
    axioms = {}
    for log in sorted(glob.glob(os.path.join(rep, "audit_*.log"))):
        text = open(log, encoding="utf-8", errors="replace").read()
        for m in re.finditer(r"'([^']+)' depends on axioms: \[([^\]]*)\]", text, re.S):
            axioms[m.group(1)] = [a.strip() for a in m.group(2).replace("\n", " ").split(",") if a.strip()]
        for m in re.finditer(r"'([^']+)' does not depend on any axioms", text):
            axioms[m.group(1)] = []
    return axioms


def _file_status(rep):
    st = {}
    fs = os.path.join(rep, "file_status.txt")
    if os.path.exists(fs):
        for line in open(fs, encoding="utf-8"):
            parts = line.split()
            if len(parts) >= 2:
                st[parts[0]] = parts[1]
    return st


def _flags(path):
    if not os.path.exists(path):
        return ["ausente"]
    code = re.sub(r"/-.*?-/", "", open(path, encoding="utf-8").read(), flags=re.S)
    code = re.sub(r"--.*", "", code)
    flags = [w for w in ("sorry", "admit") if re.search(rf"\b{w}\b", code)]
    if re.search(r"^\s*axiom\s", code, re.M):
        flags.append("axiom")
    return flags


def default_runner(root):
    """Compila um arquivo com `lake env lean` (None se não houver lake)."""
    if shutil.which("lake") is None:
        return None

    def run(path):
        p = subprocess.run(["lake", "env", "lean", path], cwd=root, capture_output=True, text=True,
                           timeout=900)
        return p.returncode, p.stdout + p.stderr
    return run


def typecheck(root, gate_file, gate_thm, statement_root, runner):
    """`example : <enunciado oficial com _root_> := <teorema>` precisa compilar."""
    if runner is None:
        return False, "verificação de tipo indisponível (sem Lean)"
    mod = gate_file[:-len(".lean")].replace("/", ".")
    d = os.path.join(root, "reports")
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, "VerificaPortao_" + gate_thm.replace(".", "_") + ".lean")
    open(path, "w", encoding="utf-8").write(
        f"import {mod}\n\nexample : {statement_root} := _root_.{gate_thm}\n")
    code, log = runner(path)
    ok = code == 0 and ": error" not in log
    return ok, "" if ok else "o tipo do teorema não é o enunciado oficial (sombreamento ou enunciado diferente)"


def _gate(root, axioms, fstatus, gate_file, gate_thm, statement, statement_root=None, runner=None):
    path = os.path.join(root, gate_file)
    present = os.path.exists(path)
    compiled = present and fstatus.get(gate_file) == "OK"
    literal = False
    if present and statement:
        src = open(path, encoding="utf-8").read()
        short = gate_thm.split(".")[-1]
        literal = re.search(r"theorem\s+" + re.escape(short) + r"\s*:\s*" + re.escape(statement)
                            + r"\s*:=", src) is not None
    ax = axioms.get(gate_thm)
    certified = ax is not None and set(ax) <= ALLOWED
    flags = _flags(path) if present else []
    pre = present and compiled and literal and certified and not flags
    typed, twhy = False, "não verificado"
    if pre:
        if statement_root:
            typed, twhy = typecheck(root, gate_file, gate_thm, statement_root, runner)
        else:
            typed, twhy = False, "sem enunciado oficial registrado"
    ok = pre and typed
    if not present:
        why = "portão ausente (nenhuma prova sem hipóteses foi fornecida)"
    elif not compiled:
        why = "não compilou"
    elif not literal:
        why = "a fonte não declara literalmente o enunciado sem hipóteses"
    elif not certified:
        why = "axiomas fora do padrão ou sem #print axioms"
    elif flags:
        why = "fonte com " + ", ".join(flags)
    elif not typed:
        why = twhy
    else:
        why = ""
    return {"file": gate_file, "theorem": gate_thm, "present": present, "compiled": compiled,
            "literal": literal, "certified": certified, "flags": flags, "typed": typed, "ok": ok,
            "reason": why, "axioms": ax}


def compute(root, report=None, axioms=None, fstatus=None, runner="default"):
    rep = os.path.join(root, "reports")
    gates = json.load(open(os.path.join(root, "scripts", "terminal_gates.json"), encoding="utf-8"))
    if report is None:
        rp = os.path.join(rep, "report.json")
        report = json.load(open(rp, encoding="utf-8")) if os.path.exists(rp) else {}
    if axioms is None:
        axioms = _axioms_from_logs(rep)
    if fstatus is None:
        fstatus = _file_status(rep)
    if runner == "default":
        runner = default_runner(root)
    obl = {o["id"]: o for o in report.get("obligations", [])}
    if not obl:
        op = os.path.join(root, "scripts", "obligations.json")
        if os.path.exists(op):
            obl = {o["id"]: o for o in json.load(open(op, encoding="utf-8")).get("obligations", [])}

    def st(i):
        return obl.get(i, {}).get("status", "?")

    lines = []
    for ln in gates["lines"]:
        g = _gate(root, axioms, fstatus, ln["gate_file"], ln["gate_theorem"], ln["statement"],
                  ln.get("statement_root"), runner)
        link_ok = ln["linking"] is None or st(ln["linking"]) == "CLOSED"
        rg = None
        if ln.get("refutation_gate_file"):
            rg = _gate(root, axioms, fstatus, ln["refutation_gate_file"], ln["refutation_gate_theorem"],
                       ln.get("refutation_statement"), ln.get("refutation_statement_root"), runner)
        proved = g["ok"] and link_ok
        refuted = bool(rg and rg["ok"]) and link_ok
        estado = ("INCONSISTENTE" if proved and refuted else "PROVADA" if proved
                  else "REFUTADA" if refuted else "ABERTA")
        green = proved and not refuted
        lines.append({
            "id": ln["id"], "problem": ln["problem"], "faithful": ln["faithful"],
            "statement": ln["statement"], "green": green, "gate": g, "estado": estado,
            "refutation_gate": rg, "refutation_meaning": ln.get("refutation_meaning"),
            "bridges": [{"id": b, "status": st(b)} for b in ln["bridges"]],
            "obligations": [{"id": o, "status": st(o)} for o in ln["obligations"]],
            "producer": ln["producer"], "producer_equivalence": ln["producer_equivalence"],
            "linking": None if ln["linking"] is None else {"id": ln["linking"], "status": st(ln["linking"])},
        })
    fiel = gates["universal_green_fiel"]
    gf = _gate(root, axioms, fstatus, fiel["gate_file"], fiel["gate_theorem"], fiel["statement"],
               fiel.get("statement_root"), runner)
    fr = gates["final_root"]
    gr = _gate(root, axioms, fstatus, fr["gate_file"], fr["gate_theorem"], fr.get("statement"),
               fr.get("statement_root"), runner)
    closed_math = bool(report.get("status", {}).get("CLOSED_MATH", False)) and gr["ok"]
    n_green = sum(l["green"] for l in lines)
    n_refuted = sum(l["estado"] == "REFUTADA" for l in lines)
    n_incons = sum(l["estado"] == "INCONSISTENTE" for l in lines)
    universal = n_green == len(lines) and n_incons == 0
    fiel_green = gf["ok"] or all(l["green"] for l in lines if l["faithful"])
    final_root = None
    if universal and closed_math and n_incons == 0:
        payload = {"sources_sha256": report.get("sources_sha256"),
                   "gates": sorted((l["gate"]["theorem"], tuple(l["gate"]["axioms"] or ())) for l in lines),
                   "closed_math": fr["gate_theorem"], "commit": report.get("commit")}
        final_root = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()

    bridges = sorted({b["id"]: b["status"] for l in lines for b in l["bridges"]}.items())
    obligs = sorted({o["id"]: o["status"] for l in lines for o in l["obligations"]}.items())
    links = sorted({l["linking"]["id"]: l["linking"]["status"] for l in lines if l["linking"]}.items())
    proved_b = sum(1 for _, s in bridges if s in ("CLOSED", "PROVADA_NO_KERNEL"))
    open_o = sum(1 for _, s in obligs if s != "CLOSED")
    open_l = sum(1 for _, s in links if s != "CLOSED")
    summary = {
        "UNIVERSAL_GREEN": universal, "UNIVERSAL_GREEN_FIEL": fiel_green,
        "FINAL_ROOT": final_root, "CLOSED_MATH": closed_math,
        "LINES_GREEN": f"{n_green}/{len(lines)}",
        "RESOLVED": f"{n_green + n_refuted}/{len(lines)}",
        "REFUTED": n_refuted, "INCONSISTENT": n_incons,
        "BRIDGES_IN_KERNEL": f"{proved_b}/{len(bridges)}",
        "PRODUCERS_OPEN": f"{open_o}/{len(obligs)}",
        "LINKINGS_OPEN": f"{open_l}/{len(links)}",
    }
    md = [f"### Verde universal e raiz final — `UNIVERSAL_GREEN = {str(universal).lower()}` · "
          f"`FINAL_ROOT = {final_root or 'null'}`",
          "",
          f"Linhas verdes: **{summary['LINES_GREEN']}** · pontes no kernel: {summary['BRIDGES_IN_KERNEL']} · "
          f"produtores abertos: {summary['PRODUCERS_OPEN']} · ligações abertas: {summary['LINKINGS_OPEN']} · "
          f"verde fiel (RH ∧ Beal): `{str(fiel_green).lower()}` · resolvidas (provadas + refutadas): "
          f"{summary['RESOLVED']}" + (f" · **INCONSISTENTES: {n_incons}**" if n_incons else ""),
          "",
          "| Linha | Enunciado | Portão terminal | Pontes | Produtor (o que falta) | Ligação | Estado |",
          "|---|---|---|---|---|---|---|"]
    for l in lines:
        g = l["gate"]
        md.append(f"| {l['problem']} | `{l['statement']}` | `{g['theorem']}` — {g['reason'] or 'OK'} | "
                  + ", ".join(f"{b['id']} {b['status']}" for b in l["bridges"]) + " | "
                  + f"`{l['producer']}` (" + ", ".join(f"{o['id']} {o['status']}" for o in l["obligations"]) + ") | "
                  + (f"{l['linking']['id']} {l['linking']['status']}" if l["linking"] else "—")
                  + " | " + {"PROVADA": "✅ PROVADA", "REFUTADA": "🔻 REFUTADA", "INCONSISTENTE": "⚠️ INCONSISTENTE"}.get(l["estado"], "❌ ABERTA") + " |")
    md += ["", f"Raiz final: `{fr['gate_theorem']}` — {gr['reason'] or 'OK'}; redução certificada "
           f"`{fr['reduction']}`. Verde fiel: `{fiel['gate_theorem']}` — {gf['reason'] or 'OK'}; forma exata "
           f"`{fiel['exact_form']}`.",
           "O estado é calculado: só um teorema terminal sem hipóteses, certificado, acende uma linha. "
           "Cada linha também aceita a **refutação** (`theorem refutacao : ¬ <enunciado>` em "
           "`ATK/Terminal/<Linha>Refutacao.lean`, mesmas exigências): conta como RESOLVIDA, não como verde."]
    return {"summary": summary, "lines": lines, "fiel": gf, "final_root_gate": gr, "md": md}


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    res = compute(root)
    rep = os.path.join(root, "reports")
    os.makedirs(rep, exist_ok=True)
    json.dump(res, open(os.path.join(rep, "universal_green.json"), "w"), indent=2, ensure_ascii=False)
    open(os.path.join(rep, "universal_green.md"), "w").write("\n".join(res["md"]) + "\n")
    print("\n".join(res["md"]))
    s = res["summary"]
    print(json.dumps(s, ensure_ascii=False))


if __name__ == "__main__":
    sys.exit(main())
