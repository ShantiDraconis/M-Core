#!/usr/bin/env python3
"""Conferência numérica de `pesquisa/fronteira/CONJECTURAS_EM_S.md` (só biblioteca padrão, precisão dupla).

Nada aqui é certificado; é aritmética de conferência dos parâmetros citados no documento.

* `ζ(½)` pela série alternada de Borwein para `η(s) = (1 − 2^{1−s}) ζ(s)`;
* `11a1` (`y² + y = x³ − x² − 10x − 20`, rank 0) e `37a1` (`y² + y = x³ − x`, rank 1): `a_n` por contagem de pontos,
  `ε = a_N` (condutor primo, redução multiplicativa), `L(E, 1) = 2 Σ a_n/n · e^{−2πn/√N}` (`ε = +1`),
  `L′(E, 1) = 2 Σ a_n/n · E₁(2πn/√N)` (`ε = −1`), `Ω = ∫_{E(ℝ)} |ω|` por quadratura; BSD:
  `L(11a1, 1)/Ω = 1/5` e `L′(37a1, 1)/Ω = Reg(37a1)`;
* o produto `Z = ζ · L*(11a1) · L*(37a1)`: grau, condutor, sinal e ordem central somados/multiplicados;
* `χ(x, y, z) = 1/x + 1/y + 1/z − 1` de Beal (`x, y, z ≥ 3`) e `s_c = d/2 − 1` de Navier–Stokes.
"""
import json
import math
import os
from fractions import Fraction

AQUI = os.path.dirname(os.path.abspath(__file__))
TOL_ZETA = 1e-12
TOL_BSD = 1e-9
ZETA_MEIO = -1.4603545088095868
REG_37A1 = 0.0511114082399688  # regulador de 37a1 (Cremona)


class FalhaConferencia(Exception):
    pass


def confere(ok, msg):
    if not ok:
        raise FalhaConferencia(msg)


def zeta_borwein(s, n=60):
    d = [0.0] * (n + 1)
    soma = 0.0
    for i in range(n + 1):
        soma += math.factorial(n + i - 1) * 4 ** i / (math.factorial(n - i) * math.factorial(2 * i)) if i else 1 / n
        d[i] = n * soma
    eta = sum((-1) ** k * (d[k] - d[n]) / (k + 1) ** s for k in range(n)) / -d[n]
    return eta / (1 - 2 ** (1 - s))


def primos(n):
    crivo = [True] * (n + 1)
    crivo[0] = crivo[1] = False
    for p in range(2, int(n ** 0.5) + 1):
        if crivo[p]:
            crivo[p * p::p] = [False] * len(crivo[p * p::p])
    return [p for p in range(n + 1) if crivo[p]]


def ap(a, p):
    a1, a2, a3, a4, a6 = a
    pts = 1
    for x in range(p):
        for y in range(p):
            if (y * y + a1 * x * y + a3 * y - (x ** 3 + a2 * x * x + a4 * x + a6)) % p == 0:
                pts += 1
    return p + 1 - pts


def coef(a, N, M):
    an = [0] * (M + 1)
    an[1] = 1
    ps = primos(M)
    apv = {p: ap(a, p) for p in ps}
    for n in range(2, M + 1):
        p = n
        for q in ps:
            if q * q > n:
                break
            if n % q == 0:
                p = q
                break
        k, m = 0, n
        while m % p == 0:
            m //= p
            k += 1
        # a_{p^k}
        apk = [1, apv[p]]
        for j in range(2, k + 1):
            apk.append(apv[p] * apk[-1] - (0 if N % p == 0 else p) * apk[-2])
        an[n] = apk[k] * an[m]
    return an, apv


def E1(x):
    if x <= 2:
        g = 0.5772156649015329
        s, t = 0.0, 1.0
        for k in range(1, 60):
            t *= -x / k
            s += t / k
        return -g - math.log(x) - s
    f, C, D = 0.0, 0.0, 0.0  # fração contínua de Lentz
    b = x + 1
    C, D = 1e300, 1 / b
    h = D
    for i in range(1, 200):
        an = -i * i
        b += 2
        D = 1 / (an * D + b)
        C = b + an / C
        h *= C * D
    return h * math.exp(-x)


def raizes_reais(c3, c2, c1, c0):
    """Raízes reais de c3 x³ + c2 x² + c1 x + c0 (c3 > 0), em ordem decrescente: Newton a partir de x grande dá a
    maior raiz real; o quociente quadrático dá as outras."""
    x = 1.0 + max(abs(c2), abs(c1), abs(c0)) / c3
    for _ in range(200):
        x -= (((c3 * x + c2) * x + c1) * x + c0) / ((3 * c3 * x + 2 * c2) * x + c1)
    b, c = c2 + c3 * x, c1 + (c2 + c3 * x) * x
    disc = b * b - 4 * c3 * c
    if disc <= 0:
        return [x]
    r1, r2 = (-b + math.sqrt(disc)) / (2 * c3), (-b - math.sqrt(disc)) / (2 * c3)
    return sorted([x, r1, r2], reverse=True)


def periodo(a):
    """Ω = ∫_{E(ℝ)} |dx/(2y + a1 x + a3)|."""
    a1, a2, a3, a4, a6 = a
    b2, b4, b6 = a1 * a1 + 4 * a2, 2 * a4 + a1 * a3, a3 * a3 + 4 * a6
    f = lambda x: 4 * x ** 3 + b2 * x * x + 2 * b4 * x + b6
    reais = raizes_reais(4, b2, 2 * b4, b6)
    e1 = reais[0]

    def integral(a_, b_):
        # ∫_{a_}^{b_} dx/√|f| com x = a_ + (b_−a_)·sin²(θ) nas pontas, ou cauda infinita com x = e1 + 1/u²
        n = 20000
        if b_ == math.inf:
            # x = e1 + t², dx = 2t dt; f = (x − e1)·q ⇒ ∫ 2 dt/√q(e1 + t²); t = tan(φ)
            def q(x):
                return f(x) / (x - e1)
            tot = 0.0
            for k in range(n):
                phi = (k + 0.5) * (math.pi / 2) / n
                t = math.tan(phi)
                tot += 2 / math.sqrt(q(e1 + t * t)) / math.cos(phi) ** 2
            return tot * (math.pi / 2) / n
        tot = 0.0
        for k in range(n):
            th = (k + 0.5) * (math.pi / 2) / n
            x = a_ + (b_ - a_) * math.sin(th) ** 2
            dx = 2 * (b_ - a_) * math.sin(th) * math.cos(th)
            tot += dx / math.sqrt(abs(f(x)))
        return tot * (math.pi / 2) / n

    if len(reais) == 1:
        return 2 * integral(e1, math.inf), 1
    e1, e2, e3 = reais
    return 2 * integral(e1, math.inf) + 2 * integral(e3, e2), 2


def curva(nome, a, N, rank, M=400):
    an, apv = coef(a, N, M)
    eps = apv[N]  # condutor primo, redução multiplicativa: ε = a_N
    x = 2 * math.pi / math.sqrt(N)
    if eps == 1:
        Lval = 2 * sum(an[n] / n * math.exp(-x * n) for n in range(1, M + 1))
    else:
        Lval = 2 * sum(an[n] / n * E1(x * n) for n in range(1, M + 1))
    Om, comps = periodo(a)
    return {"curva": nome, "N": N, "a_N": apv[N], "epsilon": eps, "rank": rank,
            "a_p_ate_13": {p: apv[p] for p in (2, 3, 5, 7, 11, 13)},
            ("L(E,1)" if eps == 1 else "L'(E,1)"): Lval, "Omega": Om, "componentes_reais": comps,
            "razao": Lval / Om}


def main(saida=None):
    z12 = zeta_borwein(0.5)
    c11 = curva("11a1", (0, -1, 1, -10, -20), 11, 0)
    c37 = curva("37a1", (0, 0, 1, -1, 0), 37, 1)
    confere(abs(z12 - ZETA_MEIO) < TOL_ZETA, f"ζ(½) = {z12!r}, esperado {ZETA_MEIO!r}")
    confere(c11["epsilon"] == 1, f"ε(11a1) = {c11['epsilon']}, esperado +1")
    confere(abs(c11["razao"] - 0.2) < TOL_BSD, f"L(11a1, 1)/Ω = {c11['razao']!r}, esperado 1/5")
    confere(c37["epsilon"] == -1, f"ε(37a1) = {c37['epsilon']}, esperado −1")
    confere(abs(c37["razao"] - REG_37A1) < TOL_BSD, f"L′(37a1, 1)/Ω = {c37['razao']!r}, esperado Reg = {REG_37A1!r}")
    produto = {"fatores": ["zeta", "L*(11a1)", "L*(37a1)"], "grau": 1 + 2 + 2, "condutor": 1 * 11 * 37,
               "epsilon": 1 * c11["epsilon"] * c37["epsilon"], "polo_em_1": 1 + 0 + 0,
               "ordem_em_meio": 0 + 0 + 1}
    confere(produto["epsilon"] == (-1) ** produto["ordem_em_meio"], "paridade ε = (−1)^r falhou no produto")
    chi = {f"{x},{y},{z}": str(Fraction(1, x) + Fraction(1, y) + Fraction(1, z) - 1)
           for (x, y, z) in ((3, 3, 3), (3, 3, 4), (3, 3, 5), (3, 4, 4), (4, 4, 4), (3, 3, 6))}
    out = {"zeta_meio": z12, "curvas": [c11, c37], "produto": produto, "beal_chi": chi,
           "ns_s_c": {d: d / 2 - 1 for d in (2, 3, 4)}, "primons_lacuna": math.log(2),
           "aviso": "conferência numérica; nada aqui é certificado"}
    if saida is None:
        saida = os.path.join(AQUI, "conjecturas_em_s.json")
    with open(saida, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(json.dumps(main(), ensure_ascii=False, indent=1))
