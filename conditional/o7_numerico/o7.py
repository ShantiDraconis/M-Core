import mpmath as mp, cypari2, json, subprocess
mp.mp.dps = 40
pari = cypari2.Pari()
E = pari.ellinit([0,0,0,-1,0])
tors = pari.elltors(E)
gr = pari.ellglobalred(E)
N = int(gr[0]); c_prod = int(gr[2])
w = int(pari.ellrootno(E))
L_pari = mp.mpf(str(pari.lfun(pari.lfuncreate(E), 1)))
omega_pari = E.omega()
disc = int(E.disc())
# independent: Omega = integral over E(R) of |dx/2y| = sum over x-intervals with x^3-x>0 of dx/sqrt(x^3-x)
f = lambda x: 1/mp.sqrt(x**3 - x)
I1 = mp.quad(f, [-1, -0.5, 0]); I2 = mp.quad(f, [1, 2, mp.inf])
Omega = I1 + I2
# independent: L(E,1) = 2 sum a_n/n exp(-2 pi n / sqrt(N)), valid for root number +1
def ap(p):
    if p == 2: return 0
    cnt = 1  # point at infinity
    for x in range(p):
        r = (x**3 - x) % p
        cnt += 1 if r == 0 else (2 if pow(r, (p-1)//2, p) == 1 else 0)
    return p + 1 - cnt
M = 400
an = [0]*(M+1); an[1] = 1
primes = [p for p in range(2, M+1) if all(p % q for q in range(2, int(p**0.5)+1))]
apv = {p: ap(p) for p in primes}
for n in range(2, M+1):
    m, fac = n, {}
    for p in primes:
        while m % p == 0: fac[p] = fac.get(p, 0) + 1; m //= p
        if m == 1: break
    val = 1
    for p, k in fac.items():
        a = [1, apv[p]]
        for j in range(2, k+1):
            a.append(apv[p]*a[-1] - (0 if p == 2 else p)*a[-2])
        val *= a[k]
    an[n] = val
L_series = 2*mp.fsum(mp.mpf(an[n])/n*mp.exp(-2*mp.pi*n/mp.sqrt(N)) for n in range(1, M+1))
tors_order = int(tors[0]); tors_sq = tors_order**2
sha = L_series*tors_sq/(Omega*c_prod)
rec = {
 "curve": "y^2 = x^3 - x", "conductor": N, "root_number": w,
 "torsion_structure": [int(x) for x in tors[1]], "torsion_order": tors_order, "torsion_sq": tors_sq,
 "discriminant": disc, "real_components": 2 if disc > 0 else 1,
 "Omega_integral": mp.nstr(Omega, 25), "Omega_component_(-1,0)": mp.nstr(I1, 20), "Omega_component_(1,inf)": mp.nstr(I2, 20),
 "pari_omega": str(omega_pari),
 "L_E_1_series": mp.nstr(L_series, 25), "L_E_1_pari": mp.nstr(L_pari, 25),
 "Tamagawa_product": c_prod, "Sha_analytic": mp.nstr(sha, 25),
 "BSD_rank0_residual": mp.nstr(abs(sha - 1), 5),
 "tool": f"mpmath {mp.__version__}; PARI via cypari2 ({pari.version()})",
}
print(json.dumps(rec, indent=1, ensure_ascii=False))
