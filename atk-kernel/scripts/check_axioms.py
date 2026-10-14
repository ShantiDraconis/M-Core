#!/usr/bin/env python3
"""
Auditoria ATK: transforma a saída do kernel Lean em uma tabela de certificação.

Entradas (em reports/):
  file_status.txt   linhas "ATK/X.lean OK" ou "ATK/X.lean FAIL"
  audit_<X>.log     saída de `lake env lean ATK/X.lean` (inclui #print axioms)
  build.log         saída de `lake build`
Saídas:
  reports/report.md, reports/report.json
Código de saída 0 só se TODOS os teoremas esperados estiverem CERTIFIED.

CERTIFIED  = arquivo compilou sem erro E #print axioms ⊆ {propext, Classical.choice, Quot.sound}
NOT_CERTIFIED = qualquer outra coisa (erro, sorryAx, axioma próprio, teorema ausente)
"""
import hashlib, json, os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REP = os.path.join(ROOT, "reports")
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}

expected = [l.strip() for l in open(os.path.join(ROOT, "scripts", "expected_theorems.txt")) if l.strip()]

status = {}
fs = os.path.join(REP, "file_status.txt")
if os.path.exists(fs):
    for line in open(fs):
        parts = line.split()
        if len(parts) == 2:
            status[parts[0]] = parts[1]

axioms, errors = {}, {}
for log in sorted(glob.glob(os.path.join(REP, "audit_*.log"))):
    text = open(log, encoding="utf-8", errors="replace").read()
    for m in re.finditer(r"'([^']+)' depends on axioms: \[([^\]]*)\]", text, re.S):
        axioms[m.group(1)] = [a.strip() for a in m.group(2).replace("\n", " ").split(",") if a.strip()]
    for m in re.finditer(r"'([^']+)' does not depend on any axioms", text):
        axioms[m.group(1)] = []
    mod = os.path.basename(log)[len("audit_"):-len(".log")]
    errs = [l for l in text.splitlines() if ": error" in l or "error:" in l]
    if errs:
        errors[mod] = errs[:20]

# proibições textuais extras (sorry/admit/axiom declarados)
src_flags = {}
for f in sorted(glob.glob(os.path.join(ROOT, "ATK", "**", "*.lean"), recursive=True)):
    code = re.sub(r"/-.*?-/", "", open(f, encoding="utf-8").read(), flags=re.S)
    code = re.sub(r"--.*", "", code)
    flags = [w for w in ("sorry", "admit") if re.search(rf"\b{w}\b", code)]
    if re.search(r"^\s*axiom\s", code, re.M):
        flags.append("axiom")
    if flags:
        src_flags[os.path.relpath(f, ROOT)] = flags

def module_file(thm):
    # ATK.X.thm -> ATK/X.lean ; ATK.Conditional.X.thm -> ATK/Conditional/X.lean ;
    # ATK.X.Sub.thm (namespace interno) -> ATK/X.lean  (prefixo mais longo que existe)
    parts = thm.split(".")
    for k in range(len(parts) - 1, 1, -1):
        cand = "/".join(parts[:k]) + ".lean"
        if os.path.exists(os.path.join(ROOT, cand)):
            return cand
    return "/".join(parts[:-1]) + ".lean"

rows, certified = [], 0
for thm in expected:
    f = module_file(thm)
    fstat = status.get(f, "NOT_RUN")
    ax = axioms.get(thm)
    if fstat != "OK":
        verdict, why = "NOT_CERTIFIED", f"arquivo {fstat}"
    elif ax is None:
        verdict, why = "NOT_CERTIFIED", "sem saída de #print axioms"
    elif not set(ax) <= ALLOWED:
        verdict, why = "NOT_CERTIFIED", "axiomas extras: " + ", ".join(sorted(set(ax) - ALLOWED))
    elif f in src_flags:
        verdict, why = "NOT_CERTIFIED", "fonte contém " + ", ".join(src_flags[f])
    else:
        verdict, why = "CERTIFIED", ""
        certified += 1
    rows.append({"theorem": thm, "file": f, "file_status": fstat,
                 "axioms": ax, "verdict": verdict, "reason": why})

sha = hashlib.sha256()
for f in sorted(glob.glob(os.path.join(ROOT, "ATK", "**", "*.lean"), recursive=True)) + [os.path.join(ROOT, "ATK.lean")]:
    sha.update(open(f, "rb").read())
src_sha = sha.hexdigest()

def read(p):
    p = os.path.join(ROOT, p)
    return open(p).read().strip() if os.path.exists(p) else "?"

report = {
    "certified": certified, "total": len(expected),
    "lean_toolchain": read("lean-toolchain"),
    "lean_version": read("reports/toolchain.txt"),
    "mathlib_rev": "v4.34.1",
    "sources_sha256": src_sha,
    "commit": os.environ.get("GITHUB_SHA", "local"),
    "theorems": rows, "errors": errors, "source_flags": src_flags,
}
json.dump(report, open(os.path.join(REP, "report.json"), "w"), indent=2, ensure_ascii=False)

state = "CERTIFIED" if certified == len(expected) else "PARTIAL" if certified else "NOT_CERTIFIED"
md = [f"## ATK-KERNEL: {state} — {certified}/{len(expected)} teoremas",
      "",
      f"- Lean: `{report['lean_version']}` · Mathlib `v4.34.1`",
      f"- SHA-256 das fontes: `{src_sha}`",
      f"- Commit: `{report['commit']}`",
      "",
      "| Teorema | Veredito | Axiomas | Motivo |",
      "|---|---|---|---|"]
for r in rows:
    ax = "—" if r["axioms"] is None else (", ".join(r["axioms"]) or "nenhum")
    md.append(f"| `{r['theorem']}` | {'✅' if r['verdict']=='CERTIFIED' else '❌'} {r['verdict']} | {ax} | {r['reason']} |")
cond_path = os.path.join(ROOT, "scripts", "conditionals.json")
conditionals = json.load(open(cond_path, encoding="utf-8")) if os.path.exists(cond_path) else []
verdict_of = {r["theorem"]: r["verdict"] for r in rows}
if conditionals:
    md += ["", "### Problemas em forma condicional: PONTE → ABERTA → ENUNCIADO",
           "",
           "Pontes e hipóteses abertas entram como argumentos explícitos (não como `axiom`).",
           "",
           "| Problema | Teorema | Veredito | Ponte (literatura) | Hipótese aberta | Fidelidade |",
           "|---|---|---|---|---|---|"]
    for c in conditionals:
        v = verdict_of.get(c["theorem"], "NOT_LISTED")
        md.append(f"| {c['problem']} | `{c['theorem']}` | {'✅' if v == 'CERTIFIED' else '❌'} {v} | "
                  + "<br>".join(c["bridge"]) + " | " + "<br>".join(c["open"]) + f" | {c['fidelity']} |")
report["conditionals"] = [dict(c, verdict=verdict_of.get(c["theorem"], "NOT_LISTED")) for c in conditionals]
closed = sum(1 for c in conditionals if verdict_of.get(c["theorem"]) == "CERTIFIED")

# Portão de CLOSED_MATH: só um teorema SEM hipóteses, certificado, no arquivo do portão.
obl_path = os.path.join(ROOT, "scripts", "obligations.json")
obl = json.load(open(obl_path, encoding="utf-8")) if os.path.exists(obl_path) else {}
gate = obl.get("gate") or {}
gate_file, gate_thm = gate.get("file"), gate.get("theorem")
gate_present = bool(gate_file) and os.path.exists(os.path.join(ROOT, gate_file))
gate_ok = (gate_present and status.get(gate_file) == "OK" and gate_thm in axioms
           and set(axioms[gate_thm]) <= ALLOWED and gate_file not in src_flags)
obligations = obl.get("obligations", [])
# Estado das obrigações é CALCULADO: CLOSED só com teorema certificado cujo enunciado na fonte é
# literalmente a proposição da obrigação (`theorem <nome> : <lean>`). Declarar "CLOSED" à mão não vale.
for o in obligations:
    if o.get("kind") == "LIGAÇÃO":
        # Ligação: o estado é o que o titular registrou (decisão humana sobre a fidelidade do modelo).
        rev = o.get("revisao_humana") or {}
        if o["status"] == "CLOSED" and rev.get("por"):
            o["closed_by"] = f"titular ({rev['por']}, {rev.get('data', '?')})"
        continue
    p = o.get("proof_theorem")
    ok = False
    if p and verdict_of.get(p) == "CERTIFIED":
        src_path = os.path.join(ROOT, module_file(p))
        short = p.split(".")[-1]
        src = open(src_path, encoding="utf-8").read() if os.path.exists(src_path) else ""
        pat = r"theorem\s+" + re.escape(short) + r"\s*:\s*" + re.escape(o["lean"]) + r"\s*:="
        ok = re.search(pat, src) is not None
        if ok:  # o tipo elaborado tem de ser a proposição oficial (bloqueia sombreamento de nomes)
            try:
                sys.path.insert(0, os.path.join(ROOT, "scripts"))
                import universal_green as _ug
                ok, _why = _ug.typecheck(ROOT, module_file(p), p, "_root_." + o["lean"], _ug.default_runner(ROOT))
            except Exception:
                ok = False
    if ok:
        o["status"] = "CLOSED"
        o["closed_by"] = p
    elif o["status"] == "CLOSED":
        o["status"] = "CLAIM_WITHOUT_CERTIFIED_PROOF"
report["status"] = {"CONDITIONALS_CLOSED": f"{closed}/{len(conditionals)}",
                    "OPEN_MATH": not gate_ok, "CLOSED_MATH": gate_ok,
                    "GATE_FILE_PRESENT": gate_present,
                    "OBLIGATIONS_OPEN": sum(1 for o in obligations if o["status"] != "CLOSED"),
                    "OBLIGATIONS_TOTAL": len(obligations)}
report["obligations"] = obligations
md += ["", f"`CONDITIONALS_CLOSED = {closed}/{len(conditionals)}` · "
       f"`OPEN_MATH = {str(not gate_ok).lower()}` · `CLOSED_MATH = {str(gate_ok).lower()}`",
       "",
       f"Portão: `{gate_file}` → `{gate_thm}` "
       + ("presente" if gate_present else "AUSENTE (nenhuma prova sem hipóteses foi fornecida)") + ".",
       "Um condicional certificado prova *hipótese aberta → enunciado*; o problema só fecha "
       "quando a hipótese aberta for provada."]
if obligations:
    md += ["", f"### Obrigações para CLOSED_MATH ({report['status']['OBLIGATIONS_OPEN']}/{len(obligations)} em aberto)",
           "", "| Id | Problema | Tipo | Proposição Lean | Estado | Referência |", "|---|---|---|---|---|---|"]
    for o in obligations:
        md.append(f"| {o['id']} | {o['problem']} | {o['kind']} | `{o['lean']}` | {o['status']} | {o['ref']} |")
# Verde universal e raiz final: calculados a partir dos portões terminais (scripts/terminal_gates.json).
ug = None
try:
    sys.path.insert(0, os.path.join(ROOT, "scripts"))
    import universal_green
    ug = universal_green.compute(ROOT, report, axioms, status)
    report["universal_green"] = ug["summary"]
    if gate_ok and not ug["final_root_gate"]["ok"]:
        gate_ok = False
        report["status"]["OPEN_MATH"], report["status"]["CLOSED_MATH"] = True, False
        md += ["", "Portão de CLOSED_MATH **rejeitado**: " + ug["final_root_gate"]["reason"] + "."]
    md += [""] + ug["md"]
    if os.environ.get("ATK_ENSAIO", "1") == "1":
        import verificar_fiacao
        import ensaio_universal_green
        fia = verificar_fiacao.run(ROOT)
        ens = ensaio_universal_green.run()
        report["fiacao"], report["ensaio"] = fia, ens
        md += [""] + verificar_fiacao.markdown(fia) + [""] + ensaio_universal_green.markdown(ens)
    import termos
    tm = termos.compute(ROOT, verdict_of, report.get("fiacao"))
    report["termos"] = {k: v for k, v in tm.items() if k not in ("terms", "linhas")}
    md += [""] + termos.markdown(tm)
    import plano
    pl = plano.compute(ROOT, report)
    report["plano"] = pl
    md += [""] + plano.markdown(pl)
    json.dump(ug, open(os.path.join(REP, "universal_green.json"), "w"), indent=2, ensure_ascii=False)
except Exception as exc:  # o relatório principal não depende deste cálculo
    md += ["", f"Verde universal: não calculado ({exc})."]
json.dump(report, open(os.path.join(REP, "report.json"), "w"), indent=2, ensure_ascii=False)
if errors:
    md += ["", "### Erros de compilação (primeiras linhas)"]
    for mod, errs in errors.items():
        md.append(f"**{mod}**")
        md.append("```")
        md += errs
        md.append("```")
md += ["", "Escopo: lemas auxiliares e teoremas CONDICIONAIS. Nenhum deles prova uma conjectura; "
       "cada condicional só fecha o problema se a hipótese aberta for provada. "
       "`OPEN_MATH` continua verdadeiro para RH, P≠NP, NS, YM, BSD, Hodge e Beal."]
open(os.path.join(REP, "report.md"), "w").write("\n".join(md) + "\n")
print("\n".join(md))

# Anotações do Actions (legíveis pela API e na interface): 1 resumo + 1 por módulo (≤ 10 por passo)
if os.environ.get("GITHUB_ACTIONS"):
    def esc(s):
        return s.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    print(f"::notice title=ATK-KERNEL {state} {certified}/{len(expected)}::"
          + esc(f"sha256 fontes {src_sha}\nlean {report['lean_version']} · mathlib v4.34.1"))
    if ug:
        u = ug["summary"]
        print(f"::notice title=UNIVERSAL_GREEN {str(u['UNIVERSAL_GREEN']).lower()} {u['LINES_GREEN']} · "
              f"FINAL_ROOT {u['FINAL_ROOT'] or 'null'}::"
              + esc(f"pontes no kernel {u['BRIDGES_IN_KERNEL']} · produtores abertos {u['PRODUCERS_OPEN']} · "
                    f"ligações abertas {u['LINKINGS_OPEN']} · verde fiel {str(u['UNIVERSAL_GREEN_FIEL']).lower()}"))
        fia, ens = report.get("fiacao") or {}, report.get("ensaio") or {}
        if fia.get("ran"):
            print(f"::notice title=FIAÇÃO {fia['templates_ok']} · prova: faltam {fia['n_missing']} termos · "
                  f"refutação: {fia.get('n_missing_refutation', '?')}::"
                  + esc("prova: " + ", ".join(fia["missing_terms"])
                        + "\nrefutação: " + ", ".join(fia.get("missing_refutation", []))))
        tm = report.get("termos")
        if tm:
            print(f"::notice title=TERMOS {tm.get('catalogo', tm['distintos'])} no catálogo · abertos {tm['distintos']} "
                  f"(prova {tm['prova']} · refutação {tm['refutacao']}) · preenchidos {tm.get('preenchidas', 0)} · "
                  f"tipos {tm['tipos_conferidos']}/{tm['tipos_total']} · fechados {tm['fechadas']}/{tm.get('catalogo', tm['distintos'])}::"
                  + esc(f"teoremas do catálogo certificados {tm['teoremas_certificados']}/{tm['teoremas']}"
                        + ("\ncatálogo OK" if tm["ok"] else "\nINCONSISTENTE: " + "; ".join(tm["problems"]))
                        + "\nsensibilidade: " + str(((report.get("fiacao") or {}).get("sensibilidade") or {}).get("detectada"))))
        pl = report.get("plano")
        if pl:
            cnt = " · ".join(f"{k} {v}" for k, v in sorted(pl["contagem"].items()))
            print(f"::notice title=PLANO T1–T9 biblioteca {'VERDE' if pl['VERDE_BIBLIOTECA'] else 'ABERTA'} · "
                  f"conjecturas {'VERDE' if pl['VERDE_UNIVERSAL_CONJECTURAS'] else 'ABERTAS'}::"
                  + esc(cnt + "\n" + "\n".join(f"{k} {v['estado']}: {v['detalhe']}" for k, v in pl["etapas"].items())))
        if ens.get("ran"):
            print(f"::notice title=ENSAIO DO PORTÃO {ens['passed']}::"
                  + esc("; ".join(f"{r['id']}={'ok' if r['passed'] else 'FALHOU'}" for r in ens["scenarios"])))
    by_mod = {}
    for r in rows:
        by_mod.setdefault(r["file"], []).append(r)
    for f, rs in by_mod.items():
        ok = sum(r["verdict"] == "CERTIFIED" for r in rs)
        lines = [f"{r['verdict']} {r['theorem']} [{', '.join(r['axioms']) if r['axioms'] is not None else '—'}]"
                 + (f" ({r['reason']})" if r["reason"] else "") for r in rs]
        print(f"::notice title={f} {ok}/{len(rs)}::" + esc("\n".join(lines)))
sys.exit(0 if certified == len(expected) else 1)
