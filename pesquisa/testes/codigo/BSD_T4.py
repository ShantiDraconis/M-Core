# BSD T4 (a): checagem do fator 2 em ATK.BSDRefinada.formula_E32_iff para E: y^2 = x^3 - x.
# Tudo calculado a partir de primeiros principios (contagem de pontos, FE numerica, Tate, quadratura).
import sys
from math import gcd
import mpmath as mp

mp.mp.dps = 40

# ---------- 1. a_p por duas implementacoes independentes ----------
def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1

def ap_legendre(p):  # a_p = -sum_x (x^3-x | p)
    return -sum(legendre(x * x * x - x, p) for x in range(p))

def ap_brute(p):  # #E(F_p) por forca bruta, incluindo O
    sq = {}
    for y in range(p):
        sq.setdefault(y * y % p, []).append(y)
    n = 1 + sum(len(sq.get((x * x * x - x) % p, [])) for x in range(p))
    return p + 1 - n

def primes(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, int(n ** .5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]

NMAX = 600
P = primes(NMAX)
ap = {}
for p in P:
    if p == 2:
        ap[p] = 0  # reducao aditiva (verificado abaixo pelo algoritmo de Tate): fator local 1
        continue
    a1 = ap_legendre(p)
    if p < 400:
        a2 = ap_brute(p)
        assert a1 == a2, (p, a1, a2)
    assert a1 * a1 <= 4 * p, ("Hasse", p)
    if p % 4 == 3:
        assert a1 == 0, ("CM supersingular", p)
    ap[p] = a1
print("a_p ok (Legendre == forca bruta p<400; Hasse; a_p=0 p=3 mod 4). Primeiros:",
      [(p, ap[p]) for p in P[:12]])

# a_n multiplicativo; bons primos: a_{p^k} = a_p a_{p^{k-1}} - p a_{p^{k-2}}; p=2 aditivo: a_{2^k}=0
an = [0] * (NMAX + 1)
an[1] = 1
for n in range(2, NMAX + 1):
    m = n; f = {}
    for p in P:
        if p * p > m:
            break
        while m % p == 0:
            f[p] = f.get(p, 0) + 1; m //= p
    if m > 1:
        f[m] = f.get(m, 0) + 1
    v = 1
    for p, k in f.items():
        if p == 2:
            v = 0; break
        a = [1, ap[p]]
        for j in range(2, k + 1):
            a.append(ap[p] * a[-1] - p * a[-2])
        v *= a[k]
    an[n] = v

# ---------- 2. L(E,1) e teste da equacao funcional (fixa N e epsilon) ----------
def L1(N, eps, A, nmax=NMAX):
    sN = mp.sqrt(N)
    s = mp.mpf(0)
    for n in range(1, nmax + 1):
        if an[n]:
            s += mp.mpf(an[n]) / n * (mp.e ** (-2 * mp.pi * n * A / sN) + eps * mp.e ** (-2 * mp.pi * n / (A * sN)))
    return s

print("\nTeste FE: L(1) = sum a_n/n [e^{-2pi n A/sqrtN} + eps e^{-2pi n/(A sqrtN)}] deve independer de A")
fe = {}
for N in (16, 32, 64):
    for eps in (1, -1):
        vals = [L1(N, eps, mp.mpf(A)) for A in ("1", "0.7", "1.3", "2")]
        spread = max(vals) - min(vals)
        fe[(N, eps)] = (vals[0], spread)
        print(f"  N={N:3d} eps={eps:+d}: L(A=1)={mp.nstr(vals[0], 20):>24s}  spread(A)={mp.nstr(spread, 3)}")
Lval = fe[(32, 1)][0]
assert fe[(32, 1)][1] < mp.mpf(10) ** -30, "FE falhou para N=32, eps=+1"

# ---------- 3. Periodo ----------
g = lambda x: 4 * x ** 3 - 4 * x
# 2/sqrt(g(x)) = 1/sqrt(x^3-x); substituicoes que removem as singularidades nas raizes:
#  (1,inf): x = 1+u^2           -> 2 du / sqrt((1+u^2)(2+u^2)),  u in (0,inf)
#  (-1,-1/2): x = -1+u^2        -> 2 du / sqrt((1-u^2)(2-u^2)),  u in (0,1/sqrt2)
#  (-1/2,0): x = -v^2           -> 2 dv / sqrt(1-v^4),           v in (0,1/sqrt2)
r = 1 / mp.sqrt(2)
I_ovo = (mp.quad(lambda u: 2 / mp.sqrt((1 - u * u) * (2 - u * u)), [0, r])
         + mp.quad(lambda v: 2 / mp.sqrt(1 - v ** 4), [0, r]))
I_inf = mp.quad(lambda u: 2 / mp.sqrt((1 + u * u) * (2 + u * u)), [0, 1, mp.inf])
# conferencia grosseira com a integral original (sem substituicao)
I_raw = mp.quad(lambda x: 2 / mp.sqrt(g(x)), [-1, -0.5, 0]) + mp.quad(lambda x: 2 / mp.sqrt(g(x)), [1, 2, mp.inf])
Omega_ATK = I_ovo + I_inf  # periodoModelo: int_{g>0} 2/sqrt(g)
varpi = mp.gamma(0.25) ** 2 / (2 * mp.sqrt(2 * mp.pi))  # constante lemniscata
omega1_agm = mp.pi / mp.agm(mp.sqrt(2), 1)  # menor periodo real de dx/(2y)
print("\nPeriodo:")
print("  int_{-1}^{0} 2/sqrt(g) =", mp.nstr(I_ovo, 30))
print("  int_{1}^{inf} 2/sqrt(g) =", mp.nstr(I_inf, 30))
print("  Omega_ATK (soma)        =", mp.nstr(Omega_ATK, 30))
print("  (quadratura direta, sem substituicao =", mp.nstr(I_raw, 30), ")")
print("  menor periodo real (AGM) omega1 = pi/AGM(sqrt2,1) =", mp.nstr(omega1_agm, 30))
print("  constante lemniscata varpi       =", mp.nstr(varpi, 30))
assert abs(I_ovo - varpi) < 1e-30 and abs(I_inf - varpi) < 1e-30 and abs(omega1_agm - varpi) < 1e-30

# ---------- 4. Tamagawa em 2 (algoritmo de Tate, passo a passo) ----------
def invariants(a1, a2, a3, a4, a6):
    b2 = a1 * a1 + 4 * a2; b4 = 2 * a4 + a1 * a3; b6 = a3 * a3 + 4 * a6
    b8 = a1 * a1 * a6 + 4 * a2 * a6 - a1 * a3 * a4 + a2 * a3 * a3 - a4 * a4
    D = -b2 * b2 * b8 - 8 * b4 ** 3 - 27 * b6 * b6 + 9 * b2 * b4 * b6
    c4 = b2 * b2 - 24 * b4
    return b2, b4, b6, b8, D, c4

def v2(n):
    if n == 0:
        return 99
    k = 0
    while n % 2 == 0:
        n //= 2; k += 1
    return k

a = (0, 0, 0, -1, 0)
b2, b4, b6, b8, D, c4 = invariants(*a)
print("\nTate em p=2: Delta =", D, "v2(Delta) =", v2(D), " c4 =", c4, "v2(c4) =", v2(c4),
      "-> modelo minimal (v(Delta)<12)")
# ponto singular mod 2
sing = [(x, y) for x in range(2) for y in range(2)
        if (y * y - (x ** 3 - x)) % 2 == 0 and (2 * y) % 2 == 0 and (3 * x * x - 1) % 2 == 0]
print("  ponto singular de E mod 2:", sing)
# translada x -> x+1 (ponto singular para (0,0)): y^2 = x^3 + 3x^2 + 2x
a1_, a2_, a3_, a4_, a6_ = 0, 3, 0, 2, 0
b2_, b4_, b6_, b8_, D_, _ = invariants(a1_, a2_, a3_, a4_, a6_)
assert D_ == D
print(f"  apos x->x+1: a2={a2_}, a4={a4_}, a6={a6_}; 2|a3,a4,a6: "
      f"{a3_ % 2 == 0 and a4_ % 2 == 0 and a6_ % 2 == 0}; 2|b2={b2_}: {b2_ % 2 == 0} (nao e multiplicativa)")
print(f"  4|a6: {a6_ % 4 == 0} (nao e tipo II); v2(b8)={v2(b8_)} < 3 -> tipo III, m=2, c_2=2, f=v(Delta)-1={v2(D)-1}")
# Ogg com o condutor vindo do teste FE (N=32 => f=5): m = v(Delta) - f + 1
print("  Ogg: m = v(Delta) - f + 1 =", v2(D) - 5 + 1, "(f=5 do teste FE com N=32)")
# Pontos de torcao em E0(Q_2)? (1,0),(-1,0) reduzem ao ponto singular (1,0) mod 2; (0,0) nao.
for (x, y) in [(0, 0), (1, 0), (-1, 0)]:
    print(f"  ({x},{y}) mod 2 = ({x % 2},{y % 2}) -> {'singular (fora de E0)' if (x % 2, y % 2) in sing else 'nao singular (em E0)'}")
c2 = 2

# ---------- 5. Comparacao com a formula do kernel ----------
tors = 4; reg = 1
rhs_ATK = Omega_ATK * c2 / tors ** 2  # com #Sha = 1
sha_an_ATK = Lval * tors ** 2 / (Omega_ATK * c2 * reg)
print("\nL(E,1) (FE, 600 termos)   =", mp.nstr(Lval, 35))
print("varpi/4                   =", mp.nstr(varpi / 4, 35))
print("Omega_ATK*c2/16 (#Sha=1)  =", mp.nstr(rhs_ATK, 35))
print("#Sha_an com Omega_ATK     =", mp.nstr(sha_an_ATK, 35))
print("L(E,1)/Omega_ATK          =", mp.nstr(Lval / Omega_ATK, 35), "(=1/8 ?)")
print("\nConvencoes alternativas (#Sha_an = L*16/(Omega*c2)):")
for nome, Om, c in [("Omega_ATK = 2*varpi (int sobre E(R), kernel)", Omega_ATK, 2),
                    ("omega1 = varpi (so 1 componente; '2.622057' do enunciado)", omega1_agm, 2),
                    ("Omega_ATK, sem c2 (c2=1)", Omega_ATK, 1),
                    ("omega1 com c2*c_inf = 2*2", omega1_agm, 4)]:
    print(f"  {nome:58s}: #Sha_an = {mp.nstr(Lval * 16 / (Om * c), 25)}")
