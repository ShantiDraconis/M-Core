"""Checagens dos lemas analiticos (referee Lei-Lin):
1) T(r,theta) <= T(1,theta) = 2 sin(theta/2) + 2 cos(theta/2) = |x-y|+|x+y| (x,y unitarios), max 2*sqrt2.
2) Coeficientes de Legendre de K(t) = sqrt(2-2t)+sqrt(2+2t): k_0 = 8/3, k_n = -8/((2n-1)(2n+3)) para n par >= 2, 0 para n impar.
   => para toda medida mu >= 0 em S^2:  int int K dmu dmu <= (8/3) mu(S^2)^2  (teorema de adicao).
3) Valor esperado de K para a medida uniforme = 8/3.
"""
import math
import mpmath as mp

mp.mp.dps = 30

def T(r, th):
    s, c = math.sin(th), math.cos(th)
    return (1 + r) * s * (1 / math.sqrt(1 + r * r + 2 * r * c) + 1 / math.sqrt(1 + r * r - 2 * r * c))

# 1) grade
best, arg, viol = 0.0, None, 0
for i in range(1, 2001):
    th = math.pi * i / 2001
    t1 = 2 * math.sin(th / 2) + 2 * math.cos(th / 2)
    for j in range(1, 1001):
        r = 10 ** (-3 + 6 * j / 1000)  # r em (1e-3, 1e3)
        t = T(r, th)
        if t > t1 * (1 + 1e-12):
            viol += 1
        if t > best:
            best, arg = t, (r, th)
print("max T na grade = %.9f em r=%.4f th/pi=%.4f ; 2sqrt2 = %.9f ; violacoes T(r)>T(1): %d" % (best, arg[0], arg[1] / math.pi, 2 * math.sqrt(2), viol))

# 2) Legendre
K = lambda t: mp.sqrt(2 - 2 * t) + mp.sqrt(2 + 2 * t)
for n in range(0, 13):
    c = (2 * n + 1) / mp.mpf(2) * mp.quad(lambda t: K(t) * mp.legendre(n, t), [-1, 0, 1])
    pred = mp.mpf(8) / 3 if n == 0 else (0 if n % 2 else -mp.mpf(8) / ((2 * n - 1) * (2 * n + 3)))
    print("n=%2d  k_n = %s   previsto = %s" % (n, mp.nstr(c, 12), mp.nstr(pred, 12)))

# 3) media uniforme: (1/2) int_{-1}^{1} K(t) dt
print("media uniforme de K =", mp.nstr(mp.quad(K, [-1, 1]) / 2, 15), " 8/3 =", mp.nstr(mp.mpf(8) / 3, 15))
