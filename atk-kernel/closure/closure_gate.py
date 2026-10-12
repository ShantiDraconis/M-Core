#!/usr/bin/env python3
"""
Portão de fechamento ATK (meta-nível) — decide o valor de OPEN_MATH.

OPEN_MATH não é uma proposição matemática (ver ATK/Closure.lean: `openMath_prop_iff` mostra que
`¬ ClosedMath` como Prop afirma que alguma conjectura é FALSA). É um estado de conhecimento:

  OPEN_MATH = false  ⇔  para cada um dos 7 problemas há, em closure/registry.json, uma declaração
                        nomeada que o kernel aceita com tipo EXATAMENTE igual a um alvo admissível
                        (o enunciado oficial ou sua negação) e cujos axiomas ⊆
                        {propext, Classical.choice, Quot.sound}.

Alvos admissíveis (strings Lean, definidos em ATK/Exact.lean ou na Mathlib):
  RH    : RiemannHypothesis | ¬ RiemannHypothesis
  NS    : ClayA | ClayB | ClayC | ClayD | ¬ ClayA          (NUNCA a disjunção: é teorema)
  Beal  : Beal | ¬ Beal
  PNP   : P_ne_NP | P_eq_NP
  BSD, YM, Hodge : não enunciáveis na Mathlib v4.34.1  ⇒ OPEN_MATH = true necessariamente.

Controles (rodam sempre; se algum se comportar errado, o portão é inválido e o script sai com 1):
  + aceita uma decisão verdadeira de um problema-brinquedo (Beal com expoente 2 é falso);
  − recusa a disjunção de NS (é teorema do kernel, mas não é alvo admissível);
  − recusa tipo errado (flt_of_beal oferecido como prova de Beal);
  − recusa `axiom` (RH introduzida como axioma);
  − recusa `sorry`;
  − recusa a "resolução" clássica vazia (Nonempty (Resolution RH)).
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GEN = os.path.join(ROOT, "closure", "_gen")
REP = os.path.join(ROOT, "reports")
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}

TARGETS = {
    "RH": {"RH": "RiemannHypothesis", "¬RH": "¬ RiemannHypothesis"},
    "NS": {"A": "ATK.Exact.ClayA", "B": "ATK.Exact.ClayB", "C": "ATK.Exact.ClayC",
           "D": "ATK.Exact.ClayD", "¬A": "¬ ATK.Exact.ClayA"},
    "Beal": {"Beal": "ATK.Exact.Beal", "¬Beal": "¬ ATK.Exact.Beal"},
    "PNP": {"P≠NP": "ATK.Exact.P_ne_NP", "P=NP": "ATK.Exact.P_eq_NP"},
    "BSD": None,
    "YM": None,
    "Hodge": None,
}
NOT_STATABLE = {
    "BSD": "falta a função L de uma curva elíptica com continuação analítica e ordem em s=1",
    "YM": "falta a teoria quântica de campos de Yang–Mills em ℝ⁴ (Wightman/Osterwalder–Schrader)",
    "Hodge": "falta cohomologia de Hodge de variedades projetivas complexas, ciclos algébricos e mapa de classe",
}
NEGATION = {("RH", "RH"): "¬RH", ("RH", "¬RH"): "RH", ("Beal", "Beal"): "¬Beal",
            ("Beal", "¬Beal"): "Beal", ("PNP", "P≠NP"): "P=NP", ("PNP", "P=NP"): "P≠NP",
            ("NS", "A"): "¬A", ("NS", "¬A"): "A"}

# Falsificador exato de cada fechamento (o caso que o tornaria falso) + teorema do kernel.
FALSIFIERS = {
    "RH": ("um zero s de ζ, não trivial, s ≠ 1, com Re s ≠ 1/2 — necessariamente com 0 < Re s < 1",
           "ATK.Closure.rh_false_iff, ATK.Closure.rh_counterexample_in_open_strip"),
    "NS": ("(A) cai ⇔ existe ν>0 e dado u0 suave, div u0 = 0, decaimento rápido, sem solução suave "
           "de energia limitada; então (C) vale",
           "ATK.Closure.clayA_false_iff, ATK.Closure.clayA_or_clayC"),
    "Beal": ("Aˣ+Bʸ=Cᶻ com x,y,z>2 e gcd(A,B,C)=1 (certificado finito)",
             "ATK.Closure.beal_false_iff, ATK.Closure.beal_refuted_by_witness"),
    "PNP": ("P ≠ NP cai ⇔ P = NP: toda linguagem NP decidida por máquina TM2 em tempo polinomial",
            "ATK.Closure.pnp_false_iff"),
    "BSD": ("uma curva E/ℚ com posto(E(ℚ)) ≠ ord_{s=1} L(E,s), ou coeficiente líder ≠ fórmula BSD",
            "não enunciável na Mathlib"),
    "YM": ("um grupo de gauge compacto simples G para o qual a teoria quântica em ℝ⁴ não existe ou "
           "tem espectro sem lacuna (inf spec H∖{0} = 0)", "não enunciável na Mathlib"),
    "Hodge": ("uma classe de Hodge racional em H^{2p}(X,ℚ)∩H^{p,p} de uma variedade projetiva lisa "
              "que não é combinação racional de classes de ciclos algébricos",
              "não enunciável na Mathlib"),
}


def run_check(name, decl_type, term, prelude=""):
    """Compila `theorem atkGate_<name> : <decl_type> := <term>` e audita os axiomas."""
    os.makedirs(GEN, exist_ok=True)
    thm = f"atkGate_{name}"
    path = os.path.join(GEN, f"Check_{name}.lean")
    src = (
        "import ATK\n\n"
        f"{prelude}\n"
        f"theorem {thm} : {decl_type} := {term}\n\n"
        f"#print axioms {thm}\n"
    )
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(src)
    try:
        proc = subprocess.run(["lake", "env", "lean", path], cwd=ROOT, capture_output=True,
                              text=True, timeout=1200)
        out = proc.stdout + proc.stderr
        code = proc.returncode
    except Exception as exc:  # noqa: BLE001
        out, code = f"falha ao executar lean: {exc}", 99
    errors = [l for l in out.splitlines() if ": error" in l or l.startswith("error")]
    axioms = None
    m = re.search(rf"'{thm}' depends on axioms: \[([^\]]*)\]", out, re.S)
    if m:
        axioms = [a.strip() for a in m.group(1).replace("\n", " ").split(",") if a.strip()]
    elif re.search(rf"'{thm}' does not depend on any axioms", out):
        axioms = []
    kernel_ok = code == 0 and not errors and axioms is not None
    extra = sorted(set(axioms or []) - ALLOWED)
    accepted = kernel_ok and not extra
    if not kernel_ok:
        why = "kernel recusou (erro de tipo/elaboração)" if errors else f"lean saiu com {code}"
    elif extra:
        why = "axiomas proibidos: " + ", ".join(extra)
    else:
        why = "aceito: tipo exato e axiomas padrão"
    with open(os.path.join(REP, f"closure_{name}.log"), "w", encoding="utf-8") as fh:
        fh.write(src + "\n----\n" + out)
    return {"name": name, "type": decl_type, "term": term, "kernel_ok": kernel_ok,
            "axioms": axioms, "accepted": accepted, "reason": why,
            "errors": errors[:5]}


def main():
    os.makedirs(REP, exist_ok=True)
    reg_path = os.path.join(ROOT, "closure", "registry.json")
    registry = json.load(open(reg_path, encoding="utf-8"))
    entries = registry.get("entries", [])

    # ---------- controles do portão ----------
    beal2 = ("¬ ∀ A B C x y z : ℕ, 0 < A → 0 < B → 0 < C → 1 < x → 1 < y → 1 < z → "
             "A ^ x + B ^ y = C ^ z → 1 < Nat.gcd A (Nat.gcd B C)")
    controls = [
        ("pos_toy_decision", beal2, "ATK.Exact.beal_needs_exponents_gt_two", "", True,
         "decisão verdadeira de problema-brinquedo (Beal com expoente 2)"),
        ("neg_wrong_type", "ATK.Exact.Beal", "ATK.Exact.flt_of_beal", "", False,
         "flt_of_beal oferecido como prova de Beal"),
        ("neg_axiom", "RiemannHypothesis", "atkFakeRH",
         "axiom atkFakeRH : RiemannHypothesis\n", False, "RH introduzida como axioma"),
        ("neg_sorry", "RiemannHypothesis", "sorry", "", False, "sorry"),
        ("neg_vacuous_resolution", "RiemannHypothesis",
         "ATK.Closure.resolution_nonempty RiemannHypothesis", "", False,
         "Nonempty (Resolution RH) — vazio pelo terceiro excluído"),
    ]
    control_rows, gate_valid = [], True
    for name, typ, term, prelude, expect, label in controls:
        r = run_check(name, typ, term, prelude)
        r["label"], r["expected"] = label, expect
        r["ok"] = r["accepted"] == expect
        gate_valid &= r["ok"]
        control_rows.append(r)

    # A disjunção de NS: o kernel ACEITA como teorema, o portão RECUSA como alvo.
    r = run_check("vacuous_ns_disjunction", "ATK.Exact.ClayA ∨ ATK.Exact.ClayC",
                  "ATK.Closure.clayA_or_clayC")
    r["label"] = "disjunção (A) ∨ (C) de NS — teorema do kernel, alvo NÃO admissível"
    r["expected"] = False
    gate_accepts = False  # "A∨C" não está em TARGETS["NS"]
    r["kernel_says_theorem"] = r["accepted"]
    r["accepted"] = gate_accepts
    r["ok"] = r["kernel_says_theorem"] and not gate_accepts
    r["reason"] = ("kernel prova a disjunção (logo ela é vazia como fechamento); portão recusa: "
                   "alvo não admissível") if r["kernel_says_theorem"] else r["reason"]
    gate_valid &= r["ok"]
    control_rows.append(r)

    # ---------- registro de fechamentos ----------
    entry_rows = []
    for i, ent in enumerate(entries):
        prob, claim, decl = ent.get("problem"), ent.get("claim"), ent.get("decl")
        row = {"problem": prob, "claim": claim, "decl": decl}
        if prob not in TARGETS:
            row.update(accepted=False, reason="problema desconhecido")
        elif TARGETS[prob] is None:
            row.update(accepted=False, reason="NÃO_ENUNCIÁVEL na Mathlib: " + NOT_STATABLE[prob])
        elif claim not in TARGETS[prob]:
            row.update(accepted=False, reason=f"alvo não admissível; use um de {list(TARGETS[prob])}")
        elif not decl or not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_.'₀-₉]*", decl):
            row.update(accepted=False, reason="nome de declaração inválido")
        else:
            r = run_check(f"entry{i}", TARGETS[prob][claim], f"@{decl}")
            row.update(accepted=r["accepted"], reason=r["reason"], axioms=r["axioms"])
        entry_rows.append(row)

    status = {}
    for prob in TARGETS:
        if TARGETS[prob] is None:
            status[prob] = {"status": "NÃO_ENUNCIÁVEL", "by": None}
            continue
        acc = [e for e in entry_rows if e["problem"] == prob and e["accepted"]]
        claims = {e["claim"] for e in acc}
        bad = [c for c in claims if NEGATION.get((prob, c)) in claims]
        if bad:
            status[prob] = {"status": "INCONSISTENTE", "by": sorted(claims)}
            gate_valid = False
        elif acc:
            status[prob] = {"status": "FECHADO", "by": [f"{e['claim']} ← {e['decl']}" for e in acc]}
        else:
            status[prob] = {"status": "ABERTO", "by": None}
    closed = sum(1 for s in status.values() if s["status"] == "FECHADO")
    open_math = closed < len(TARGETS)

    out = {"open_math": open_math, "closed": closed, "total": len(TARGETS),
           "gate_valid": gate_valid, "status": status, "controls": control_rows,
           "entries": entry_rows, "criterion": __doc__.strip().splitlines()[0]}
    json.dump(out, open(os.path.join(REP, "closure_gate.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    L = ["## Portão de fechamento ATK (meta-nível)", "",
         f"**OPEN_MATH = {'true' if open_math else 'false'}** — fechados {closed}/{len(TARGETS)}"
         f" · portão {'VÁLIDO' if gate_valid else 'INVÁLIDO'}", "",
         "Critério: um problema fecha só com uma declaração cujo tipo é EXATAMENTE o enunciado "
         "oficial ou sua negação, aceita pelo kernel, com axiomas ⊆ {propext, Classical.choice, "
         "Quot.sound}. Disjunções demonstráveis, `Nonempty (Resolution P)`, `axiom` e `sorry` "
         "são recusados.", "",
         "| Problema | Estado | Por | O que tornaria o fechamento FALSO | Kernel |",
         "|---|---|---|---|---|"]
    for prob, st in status.items():
        fal, thm = FALSIFIERS[prob]
        by = "; ".join(st["by"]) if st["by"] else "—"
        if st["status"] == "NÃO_ENUNCIÁVEL":
            by = NOT_STATABLE[prob]
        L.append(f"| {prob} | {st['status']} | {by} | {fal} | `{thm}` |")
    L += ["", "### Controles do portão", "",
          "| Controle | Esperado | Obtido | OK | Motivo |", "|---|---|---|---|---|"]
    for c in control_rows:
        L.append(f"| {c['label']} | {'aceitar' if c['expected'] else 'recusar'} | "
                 f"{'aceito' if c['accepted'] else 'recusado'} | {'✅' if c['ok'] else '❌'} | "
                 f"{c['reason']} |")
    L += ["", f"Entradas no registro: {len(entry_rows)}"]
    for e in entry_rows:
        L.append(f"- {e['problem']} / {e['claim']} ← `{e['decl']}`: "
                 f"{'ACEITA' if e['accepted'] else 'RECUSADA'} — {e['reason']}")
    md = "\n".join(L) + "\n"
    open(os.path.join(REP, "closure_gate.md"), "w", encoding="utf-8").write(md)
    print(md)
    print(f"OPEN_MATH={'true' if open_math else 'false'}  GATE_VALID={gate_valid}")
    return 0 if gate_valid else 1


if __name__ == "__main__":
    sys.exit(main())
