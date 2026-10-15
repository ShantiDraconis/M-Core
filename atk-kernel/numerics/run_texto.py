"""D_N da família do texto ATK-I (Bagchi): pesos 1/(n(n+1)), geradores {n/q}, q = 2..N+1.

Uso: python3 run_texto.py NMAX PREC SAIDA.csv

Pela isometria de Bagchi (provada no kernel em ATK/ATKIBagchi.lean, `residualSq_coefBD`),
o gerador {n/q} corresponde em L^2(0, inf) a v_q = rho_q - rho_1/q e a constante 1 a chi. Logo

    G^T_{pq} = <v_p, v_q> = G_{pq} - G_{p1}/q - G_{1q}/p + G_{11}/(pq)
    b^T_q    = <chi, v_q> = b_q - b_1/q
    D^T_N    = 1 - (b^T)' (G^T)^{-1} b^T

com G, b de Báez-Duarte calculados por nb_gram (Vasyunin, aritmética decimal).
Cada D^T_N é o mínimo de um polinômio quadrático nos coeficientes:
    Q_N(c) = 1 - 2 b'c + c'Gc.
"""
import os
import sys
import time
from decimal import Decimal, getcontext

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nb_gram as nb


def residuos_texto(nmax, K, progress=None):
    cache = {}

    def G(j, k):
        return nb.gram_entry(j, k, K, cache)

    b1 = nb.b_entry(1, K)
    G11 = G(1, 1)

    def GT(p, q):
        return G(p, q) - G(p, 1) / q - G(1, q) / p + G11 / (p * q)

    def bT(q):
        return nb.b_entry(q, K) - b1 / q

    L, y, out = [], [], []
    acc = Decimal(0)
    for n in range(1, nmax + 1):
        q = n + 1
        g = [GT(j + 1, q) for j in range(1, n + 1)]
        row = []
        for j in range(n - 1):
            s = g[j]
            Lj = L[j]
            for i in range(j):
                s -= row[i] * Lj[i]
            row.append(s / Lj[j])
        d = g[n - 1]
        for i in range(n - 1):
            d -= row[i] * row[i]
        if d <= 0:
            raise ArithmeticError(f"G^T_{n} perdeu positividade (pivo^2={d}); aumente a precisao")
        piv = d.sqrt()
        row.append(piv)
        L.append(row)
        s = bT(q)
        for i in range(n - 1):
            s -= row[i] * y[i]
        yn = s / piv
        y.append(yn)
        acc += yn * yn
        out.append((n, 1 - acc))
        if progress and n % progress == 0:
            print(f"  N={n}  D_N={float(1 - acc):.12f}", flush=True)
    return out


if __name__ == "__main__":
    nmax, prec, saida = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    getcontext().prec = prec
    K = nb.Constants()
    t0 = time.time()
    rows = residuos_texto(nmax, K, progress=100)
    with open(saida, "w") as f:
        f.write("N,D_N_texto,D_N_texto_log_N_plus_2\n")
        for n, d in rows:
            f.write(f"{n},{d},{d * Decimal(n + 2).ln()}\n")
    d1 = rows[0][1]
    print(f"OK prec={prec} N={nmax} tempo={time.time() - t0:.0f}s")
    print(f"D_1 = {d1}   1 - ln 2 = {1 - Decimal(2).ln()}   diferenca = {abs(d1 - (1 - Decimal(2).ln())):.2e}")
