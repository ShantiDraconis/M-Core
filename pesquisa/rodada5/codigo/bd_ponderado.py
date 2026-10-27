#!/usr/bin/env python3
"""Companheiro numérico da rodada 59: Báez-Duarte ponderado (ATK/ZeroClasses/BDPonderado.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

`D_N(σ) = inf_c ∫_0^∞ (χ − Σ_{k ≤ N} c_k ρ_k)² t^{2σ−1} dt` pela matriz de Gram. Com `x = 1/t`, `ρ_k = {x/k}`,
`χ = 1[x ≥ 1]` e o peso vira `x^{−1−2σ}`; em cada intervalo entre múltiplos de `j` e `k` o produto `{x/j}{x/k}` é um
polinômio do segundo grau, integrado em forma fechada até `X`, e a cauda usa a média `1/4 + mdc(j,k)²/(12jk)`.

* `DNσ_meio`: em `σ = ½`, `D₁ = 0,858212…` e `D₂ = 0,289964…` (os valores de `gram2.json`);
* `semZeros_of_DNσ` (lado numérico): `D_N(σ)` decresce em `N` para `σ = 0,4; 0,5; 0,6; 0,75`;
* `piso_DNσ`: para `σ = 0,4 < ½`, `D_N(σ)` fica longe de `0` (o ínfimo é positivo — teorema, não dado).
"""
import json
import math
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
X = 3000.0


def int_pot(u, v, e):
    """∫_u^v x^e dx (u ≥ 0; e > −1 se u = 0)."""
    if abs(e + 1) < 1e-14:
        return math.log(v / u)
    if u == 0:
        return v ** (e + 1) / (e + 1)
    return (v ** (e + 1) - u ** (e + 1)) / (e + 1)


def gram(j, k, s):
    e = -1 - 2 * s
    pts = sorted(set([m * j for m in range(1, int(X // j) + 1)] + [m * k for m in range(1, int(X // k) + 1)]))
    tot = 0.0
    u = 0.0
    for v in pts:
        p = math.floor(u / j + 1e-12)
        q = math.floor(u / k + 1e-12)
        # {x/j}{x/k} = (x/j − p)(x/k − q) = x²/(jk) − (q/j + p/k) x + pq
        tot += int_pot(u, v, e + 2) / (j * k)
        if p or q:
            tot += -(q / j + p / k) * int_pot(u, v, e + 1) + p * q * int_pot(u, v, e)
        u = v
    media = 0.25 + math.gcd(j, k) ** 2 / (12 * j * k)
    return tot + media * u ** (-2 * s) / (2 * s)


def bvec(k, s):
    e = -1 - 2 * s
    pts = [1.0] + [m * k for m in range(1, int(X // k) + 1) if m * k > 1]
    tot = 0.0
    for u, v in zip(pts, pts[1:]):
        p = math.floor(u / k + 1e-12)
        tot += int_pot(u, v, e + 1) / k - p * int_pot(u, v, e)
    return tot + 0.5 * pts[-1] ** (-2 * s) / (2 * s)


def resolve(A, b):
    n = len(b)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        piv = max(range(c, n), key=lambda r: abs(M[r][c]))
        M[c], M[piv] = M[piv], M[c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            for cc in range(c, n + 1):
                M[r][cc] -= f * M[c][cc]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        x[r] = (M[r][n] - sum(M[r][cc] * x[cc] for cc in range(r + 1, n))) / M[r][r]
    return x


def DN(N, s):
    G = [[gram(j, k, s) for k in range(1, N + 1)] for j in range(1, N + 1)]
    b = [bvec(k, s) for k in range(1, N + 1)]
    c = resolve(G, b)
    return 1 / (2 * s) - sum(ci * bi for ci, bi in zip(c, b))


def main(saida=None):
    tab = {}
    for s in (0.4, 0.5, 0.6, 0.75):
        tab[str(s)] = [DN(N, s) for N in range(1, 9)]
    res = {"X": X, "D": tab, "G11_meio": gram(1, 1, 0.5), "log2pi_menos_gamma": math.log(2 * math.pi) - 0.5772156649015329}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "bd_ponderado.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
