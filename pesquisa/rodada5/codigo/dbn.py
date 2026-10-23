#!/usr/bin/env python3
"""Companheiro numérico de ATK/DeBruijnNewman.lean e ATK/LaguerrePolya.lean (rodada 12).

Só biblioteca padrão. Nada aqui é certificado e nada prova HR: `Λ ≤ 0` é HR, e os teoremas de de Bruijn
(fechamento para cima), Newman (limitação) e Hurwitz (fechamento) usados nas pontes do Lean estão
`BUILD_PENDING`.

* H_t(x) = ∫₀^∞ e^{tu²}Φ(u)cos(xu)du (Simpson): H₀(0) = ξ(½)/2, troca de sinal de H₀ em γ₁ = 14,1347…,
  e a equação do calor reversa ∂H/∂t = −∂²H/∂x² por diferenças finitas (`ATK.DBN.calor`).
* Laguerre em ℚ exato (Sturm): p + c·p', (1 − λD²)^N p e e^{−λD²}p (λ ≥ 0, `realRooted_calorExato`) conservam
  raízes reais; X² + 2 = (1 + D²)X² = e^{D²}X² não tem raízes reais (`calor_direto_falha`).
"""
import json
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import edrei  # noqa: E402


def H(t, x, umax=4.0, passos=4000):
    h = umax / passos
    f = lambda u: math.exp(t * u * u) * edrei.phi(u) * math.cos(x * u)  # noqa: E731
    s = f(0) + f(umax) + sum((4 if i % 2 else 2) * f(i * h) for i in range(1, passos))
    return s * h / 3


def residuo_calor(t, x, h=1e-3, k=1e-2):
    dt = (H(t + h, x) - H(t - h, x)) / (2 * h)
    dxx = (H(t, x + k) - 2 * H(t, x) + H(t, x - k)) / (k * k)
    return dt, -dxx


# ---- polinômios em ℚ (coeficientes do grau 0 para cima) ----

def norm(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def mul(p, q):
    r = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] += a * b
    return norm(r)


def add(p, q):
    n = max(len(p), len(q))
    return norm([(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(n)])


def esc(c, p):
    return norm([c * a for a in p])


def der(p):
    return norm([i * p[i] for i in range(1, len(p))])


def divmod_(p, q):
    p, q = norm(p), norm(q)
    quo = [F(0)] * max(len(p) - len(q) + 1, 1)
    r = list(p)
    while len(r) >= len(q) and r:
        c = r[-1] / q[-1]
        d = len(r) - len(q)
        quo[d] = c
        r = norm([r[i] - (c * q[i - d] if 0 <= i - d < len(q) else 0) for i in range(len(r))])
    return norm(quo), r


def gcd(p, q):
    p, q = norm(p), norm(q)
    while q:
        p, q = q, divmod_(p, q)[1]
    return esc(1 / p[-1], p)


def ev(p, x):
    s = F(0)
    for a in reversed(p):
        s = s * x + a
    return s


def raizes_reais_distintas(p):
    """Sturm em ℚ: número de raízes reais distintas."""
    seq = [norm(p), der(p)]
    while seq[-1] and len(seq[-1]) > 1:
        r = divmod_(seq[-2], seq[-1])[1]
        if not r:
            break
        seq.append(esc(-1, r))
    M = 1 + sum(abs(a) for a in p) / abs(p[-1])

    def var(x):
        sg = [ev(s, x) for s in seq if s]
        sg = [v for v in sg if v != 0]
        return sum(1 for a, b in zip(sg, sg[1:]) if a * b < 0)

    return var(-M) - var(M)


def raizes_reais(p):
    """`ATK.Laguerre.RealRooted`: grau da parte livre de quadrados = nº de raízes reais distintas."""
    g = gcd(p, der(p)) if len(p) > 2 else [F(1)]
    livre = divmod_(p, g)[0]
    return raizes_reais_distintas(livre) == len(livre) - 1


def produto(rs):
    p = [F(1)]
    for r in rs:
        p = mul(p, [-F(r), F(1)])
    return p


P_TESTE = produto([F(-1), F(1, 2), F(1, 2), F(3)])


def calor_exato(l, p):
    """`ATK.PolyaCalor.calorExato`: e^{−λD²}p = Σ_m (−λ)^m/m!·D^{2m}p (soma finita)."""
    r, q, m = [], list(p), 0
    while q:
        r = add(r, esc(F(-l) ** m / math.factorial(m), q))
        q = der(der(q))
        m += 1
    return r


def main(saida=None):
    p = P_TESTE
    lag = {str(c): raizes_reais(add(p, esc(F(c), der(p)))) for c in (F(1, 3), F(-2), F(5))}
    q = p
    for _ in range(10):
        q = add(q, esc(F(-1, 10), der(der(q))))
    res = {
        "H0(0)": format(H(0, 0), ".12g"),
        "xi(1/2)/2": format(edrei.XI_MEIO / 2, ".12g"),
        "H0(14.13)_H0(14.14)": [format(H(0, 14.13), ".4g"), format(H(0, 14.14), ".4g")],
        "calor_(t,x)=(0,5)": [format(v, ".6g") for v in residuo_calor(0.0, 5.0)],
        "calor_(t,x)=(0.2,10)": [format(v, ".6g") for v in residuo_calor(0.2, 10.0)],
        "laguerre_p+cp'_raizes_reais": lag,
        "(1-D^2/10)^10_p_raizes_reais": raizes_reais(q),
        "X^2+2_raizes_reais": raizes_reais([F(2), F(0), F(1)]),
        "exp(-lD^2)p_raizes_reais_l=1/3,1,5": [raizes_reais(calor_exato(F(x), p)) for x in (F(1, 3), F(1), F(5))],
        "exp(+D^2)X^2": [str(c) for c in calor_exato(F(-1), [F(0), F(0), F(1)])],
        "aviso": "consistência numérica; Λ ≤ 0 é HR (OPEN_MATH)",
    }
    if saida:
        json.dump(res, open(saida, "w"), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
