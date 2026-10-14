#!/usr/bin/env python3
"""Valores numéricos das larguras sem zeros certificadas no kernel (ilustração, NÃO certificação).

c_poly(t) = 1/(256 (9+4|t|)^4 (3+3|t|))                 ATK.ZetaRegiao.faixa_estreitada
c_log(t)  = 1/(256 e^5 (l^2+7l+13)^4 (l+7)), l = log 3|t|   ATK.ZetaLog.faixa_log (|t| >= 4)
c_simp(t) = 1/(1e9 l^9)                                    ATK.ZetaLog.faixa_log_simples
m-piso    = 1/(|rho| (1/sqrt(2s-1) + 1/c(t)))              ATK.ValleePoussin.m_ge_log

Os teoremas são do kernel; os números abaixo são só avaliação em ponto flutuante das fórmulas.
"""
from math import e, exp, log, sqrt


def c_poly(t):
    t = abs(t)
    return 1 / (256 * (9 + 4 * t) ** 4 * (3 + 3 * t))


def c_log(t):
    l = log(3 * abs(t))
    return 1 / (256 * e ** 5 * (l * l + 7 * l + 13) ** 4 * (l + 7))


def c_simp(t):
    return 1 / (1e9 * log(3 * abs(t)) ** 9)


def m_floor(sigma, t, c):
    r = sqrt(sigma * sigma + t * t)
    return 1 / (r * (1 / sqrt(2 * sigma - 1) + 1 / c))


def crossover():
    lo, hi = log(4), 50.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if c_log(exp(mid)) > c_poly(exp(mid)):
            hi = mid
        else:
            lo = mid
    return exp(hi)


def main():
    ts = [14.134725, 100, 1e3, 1e4, 1e5, 1e6, 1e9, 1e12, 3e12, 1e20]
    print("| t | c_poly(t) | c_log(t) | 1/(10^9 l^9) | c_log/c_poly |")
    print("|---|---|---|---|---|")
    for t in ts:
        print(f"| {t:.6g} | {c_poly(t):.3e} | {c_log(t):.3e} | {c_simp(t):.3e} | {c_log(t)/c_poly(t):.3e} |")
    print()
    print(f"cruzamento numérico c_log = c_poly em |t| ≈ {crossover():.4f} (kernel: |t| >= 2000)")
    print()
    print("| t | piso de m(ρ) com σ = 1 − c(t) (poly) | idem (log) |")
    print("|---|---|---|")
    for t in [100, 1e6, 1e12]:
        cp, cl = c_poly(t), c_log(t)
        print(f"| {t:.0e} | {m_floor(1 - cp, t, cp):.3e} | {m_floor(1 - cl, t, cl):.3e} |")
    print()
    print("Piso para σ ≥ 1/2 + c(t)²/2 (abaixo disso 1/√(2σ−1) domina e o piso vai a 0 em σ → 1/2):")
    for t in [100, 1e6, 1e12]:
        c = c_log(t)
        print(f"t = {t:.0e}: m(ρ) ≥ c/(2|ρ|) ≈ {c / (2 * sqrt(1 + t * t)):.3e}  "
              f"(limiar σ − 1/2 = c²/2 ≈ {c * c / 2:.1e})")

if __name__ == "__main__":
    main()
