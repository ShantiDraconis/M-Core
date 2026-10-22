#!/usr/bin/env python3
"""Uma cauda ε em Re ρ = 1/2 + ε, na altura γ: o piso B que ela deixa em D_∞ (ATK.CaudaMeio.cauda_piso)
e o N que o produtor D_N precisaria para enxergá-lo, supondo a queda observada D_N ≈ C0/log N
(C0 = 2 + γ_E − log 4π; rodada 2: D_N·log N ∈ [0,96; 1,01]·C0 até N = 8000). Heurístico na parte de N.
"""
import math, json, sys
C0 = 2 + 0.5772156649015329 - math.log(4 * math.pi)
def B(eps, g):
    s = 0.5 + eps
    return (2 * s - 1) * ((1 - s) ** 2 + g * g) / ((s * s + g * g) ** 2)
linhas = []
for g in (14.13, 1e3, 1e6, 3e12, 1e20):
    for eps in (0.25, 1e-2, 1e-6, 1e-12):
        b = B(eps, g)
        log10N = C0 / b / math.log(10)
        linhas.append({"gamma": g, "eps": eps, "B": b, "cota_2eps_sobre_g2": 2 * eps / g ** 2, "log10_N_necessario": log10N})
        print(f"γ={g:<8g} ε={eps:<6g} B={b:.3e} (≤ 2ε/γ² = {2*eps/g**2:.3e})  N ≈ 10^{log10N:.3g}")
print("C0 =", C0, "; D_8000 = 0,00507 já é menor que B quando B > 0,00507")
json.dump({"C0": C0, "linhas": linhas}, open(sys.argv[1], "w"), indent=1)
