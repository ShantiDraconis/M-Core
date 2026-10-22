"""Periodograma de x(u) = D_N log N - tendência linear em u = log N (N em [100, Nmax]), amostrado em u uniforme.
Procura picos em gamma ~ ordenadas dos zeros (14.13, 21.02, 25.01, 30.42, 32.94)."""
import sys, math, cmath
D = {}
for line in open(sys.argv[1]):
    if line.startswith("N"): continue
    p = line.split("\t"); D[int(p[0])] = float(p[1])
Nmax = max(D); lo = 100
us = [math.log(lo) + i * 0.002 for i in range(int((math.log(Nmax) - math.log(lo)) / 0.002))]
xs = []
for u in us:
    n = int(math.exp(u)); n = max(lo, min(n, Nmax)); xs.append(D[n] * math.log(n))
m = len(us); ub = sum(us) / m; xb = sum(xs) / m
sl = sum((u - ub) * (x - xb) for u, x in zip(us, xs)) / sum((u - ub) ** 2 for u in us)
r = [x - xb - sl * (u - ub) for u, x in zip(us, xs)]
print(f"u em [{us[0]:.2f},{us[-1]:.2f}], tendência dx/du = {sl:.2e}, rms resíduo = {math.sqrt(sum(v*v for v in r)/m):.2e}")
han = [0.5 - 0.5 * math.cos(2 * math.pi * i / (m - 1)) for i in range(m)]
res = []
for k in range(10, 801):
    g = k * 0.05
    s = sum(h * v * cmath.exp(-1j * g * u) for h, v, u in zip(han, r, us))
    res.append((abs(s) * 2 / sum(han), g))
top = sorted(res, reverse=True)[:12]
print("12 maiores amplitudes (amp, gamma):", ", ".join(f"({a:.2e}, {g:.2f})" for a, g in sorted(top, key=lambda t: t[1])))
for g0 in [14.13, 21.02, 25.01, 30.42, 32.94]:
    a = max(a for a, g in res if abs(g - g0) < 0.3)
    print(f"amp perto de {g0}: {a:.2e}")
print("amp mediana em [1,40]:", f"{sorted(a for a,_ in res)[len(res)//2]:.2e}")
