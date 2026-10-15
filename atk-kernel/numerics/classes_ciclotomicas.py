#!/usr/bin/env python3
"""Classes de ℚ(ζ_p): número de classes relativo h⁻ e primos irregulares (cálculo numérico, fora do kernel).

Uso:
  python3 numerics/classes_ciclotomicas.py hmenos 300   > numerics/hmenos_p300.csv
  python3 numerics/classes_ciclotomicas.py bernoulli 10000 > numerics/irregulares_p10000.csv

Dependências: `hmenos` usa só a biblioteca padrão; `bernoulli` precisa de NumPy
(`pip install numpy`), importado só nesse modo.

* `hmenos P`: para cada primo ímpar 3 ≤ p ≤ P, h⁻(ℚ(ζ_p)) exato, pela fórmula
  h⁻ = 2p · ∏_{χ ímpar} (−½ B_{1,χ}),  p·B_{1,χ} = Σ_j r_j χ(g)^j  (r_j = g^j mod p, g raiz primitiva);
  o produto sobre os caracteres ímpares é o determinante (inteiro, Bareiss) da multiplicação por
  F(x) = Σ r_j x^j em ℤ[x]/(x^{(p−1)/2} + 1).  p é regular ⟺ p ∤ h⁻ (Kummer: p | h⁺ ⟹ p | h⁻).
* `bernoulli N`: para cada primo 5 ≤ p ≤ N, os pares irregulares (p, k), k par, 2 ≤ k ≤ p − 3,
  p | B_k, pela congruência de Voronoi com a = g raiz primitiva:
  (g^k − 1)·B_k/k ≡ Σ_{j=1}^{p−1} j^{k−1}·⌊jg/p⌋ (mod p).
  p é regular ⟺ não há par irregular (critério de Kummer).

Nada disto é certificado pelo kernel: o critério de Kummer e a fórmula analítica de h⁻ não estão
formalizados.  As duas listas concordam para todo p ≤ 300 (conferência cruzada).
"""
import sys


def isprime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


def primroot(p):
    fs = [q for q in range(2, p) if (p - 1) % q == 0 and isprime(q)]
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in fs):
            return g


def bareiss_det(M):
    M = [row[:] for row in M]
    n = len(M)
    sign, prev = 1, 1
    for k in range(n - 1):
        if M[k][k] == 0:
            for i in range(k + 1, n):
                if M[i][k] != 0:
                    M[k], M[i] = M[i], M[k]
                    sign = -sign
                    break
            else:
                return 0
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] = (M[i][j] * M[k][k] - M[i][k] * M[k][j]) // prev
        prev = M[k][k]
    return sign * M[n - 1][n - 1]


def hmenos(p):
    g = primroot(p)
    m = (p - 1) // 2
    r = [pow(g, j, p) for j in range(p - 1)]
    G = [r[j] - r[j + m] for j in range(m)]
    M = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            k = i + j
            if k < m:
                M[k][i] += G[j]
            else:
                M[k - m][i] -= G[j]
    R = bareiss_det(M)
    num, den = 2 * p * R, (p ** m) * (2 ** m)
    assert num % den == 0
    return abs(num // den)


def pares_irregulares(p):
    import numpy as np  # só o modo `bernoulli` precisa de NumPy
    j = np.arange(1, p, dtype=np.int64)
    w = (primroot(p) * j) // p
    jk = j.copy()
    j2 = (j * j) % p
    out = []
    for k in range(2, p - 2, 2):
        if int((jk * w).sum() % p) == 0:
            out.append(k)
        jk = (jk * j2) % p
    return out


def main(argv):
    modo, N = argv[1], int(argv[2])
    if modo == "hmenos":
        print("p,h_menos,regular")
        for p in range(3, N + 1):
            if isprime(p):
                h = hmenos(p)
                print(f"{p},{h},{'sim' if h % p else 'nao'}", flush=True)
    elif modo == "bernoulli":
        print("p,indice,k_irregulares")
        for p in range(5, N + 1):
            if isprime(p):
                ks = pares_irregulares(p)
                print(f"{p},{len(ks)},{' '.join(map(str, ks))}", flush=True)


if __name__ == "__main__":
    main(sys.argv)
