#!/usr/bin/env python3
"""
Teste de escala para cotas do tipo  S ≤ Σ cᵢ · y^αᵢ · z^βᵢ  (Navier–Stokes em ℝ³).

Sob amplitude u ↦ a·u e dilatação u ↦ λ·u(λ·):  S ~ a³λ³,  y ~ a²λ,  z ~ a²λ³,
logo o monômio y^α z^β tem vetor de escala (2α + 2β, α + 3β) e S tem (3, 3).
Uma cota que vale em toda a órbita (a, λ) de um estado com S > 0 exige que (3, 3) esteja no fecho
convexo dos vetores do lado direito (senão, numa direção de (log a, log λ), S cresce mais rápido que
todos os termos). Condição NECESSÁRIA: quem não passa é falso; quem passa ainda precisa de prova.
Teorema correspondente no kernel: ATK.Correcao_20261012.only_cubic_survives.

uso: python3 scaling_check.py proposed_bounds.json
"""
import json, os, sys
from fractions import Fraction as F
from itertools import combinations

TARGET = (F(3), F(3))

def vec(t):
    a, b = F(t["alpha"]), F(t["beta"])
    return (2 * a + 2 * b, a + 3 * b)

def cross(o, p, q):
    return (p[0] - o[0]) * (q[1] - o[1]) - (p[1] - o[1]) * (q[0] - o[0])

def in_hull(P, pts):
    pts = list(dict.fromkeys(pts))
    if P in pts:
        return True
    for p, q in combinations(pts, 2):            # sobre um segmento
        if cross(p, q, P) == 0 and min(p[0], q[0]) <= P[0] <= max(p[0], q[0]) \
                and min(p[1], q[1]) <= P[1] <= max(p[1], q[1]):
            return True
    for p, q, r in combinations(pts, 3):         # dentro de um triângulo (Carathéodory em 2D)
        d1, d2, d3 = cross(p, q, P), cross(q, r, P), cross(r, p, P)
        if (d1 >= 0 and d2 >= 0 and d3 >= 0) or (d1 <= 0 and d2 <= 0 and d3 <= 0):
            if cross(p, q, r) != 0:
                return True
    return False

bounds = json.load(open(sys.argv[1], encoding="utf-8"))
lines, bad = [], 0
for b in bounds:
    pts = [vec(t) for t in b["rhs"]]
    verdict = "ADMISSIVEL" if in_hull(TARGET, pts) else "REJEITADA"
    fail = verdict != b["expected"] or (b.get("status") == "ACEITA_NO_ATK" and verdict == "REJEITADA")
    bad += fail
    lines.append(f"{'FALHA ' if fail else ''}{b['id']}: {b['bound']} → {verdict} "
                 f"(vetores {[(str(p[0]), str(p[1])) for p in pts]}; esperado {b['expected']})")
print("\n".join(lines))
if os.environ.get("GITHUB_ACTIONS"):
    print(f"::notice title=Teste de escala ({len(bounds) - bad}/{len(bounds)} conforme)::" + "%0A".join(lines))
sys.exit(1 if bad else 0)
