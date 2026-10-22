"""NS T1 — auditoria de escala da explosao forcada OpenAI (NS_frontier.md §5 T1).

Modelo de nucleo (anzats dimensional, nu = 1, tau = T* - t -> 0):
  l_r = tau^a, l_z = tau^b, U_theta = U_z = tau^-c, U_r = tau^-d, d = c + b - a (incompressibilidade).
  Volume do nucleo = l_r^2 l_z (nucleo junto ao eixo).  |grad u| ~ max_i U_i / min(l_r, l_z).
INSUMOS QUE SAO ALEGACOES DE FONTE (frontier §1.2, PDF OpenAI Thm 1.1 / mecanismo):
  (a,b,c) = (1/2, 1/2-h, 1/2+h), 0<h<1/100;  u_r = O(tau^-1/2);  sup_t ||u||_2 < inf;  f in C_c^inf.
Tudo o mais e calculo deste script.
"""
import sys
from fractions import Fraction as Fr
import sympy as sp

h = sp.symbols('h', positive=True)
H = sp.Interval.open(0, sp.Rational(1, 100))

def exps(a, b, c, Max=sp.Max):
    d = c + b - a
    cu = Max(c, d)                     # expoente (negativo) da maior velocidade
    V = 2 * a + b                      # volume
    g = Max(c + a, c + b, d + a, d + b)  # gradiente
    E = dict(
        d=d, u_inf=-cu, V=V,
        energia=V - 2 * cu,
        L3=-cu + V / 3,
        Lq={q: -cu + V / q for q in (4, 6, 9)},
        enstrofia=-2 * g + V,
        omega_inf=-g,
        H12=-2 * cu + a + b,           # ||u||_{H^1/2}^2 ~ U^2 l_r l_z (direcao fina = l_r)
        ReLoc=-(cu - a),               # Re_loc = U l_r / nu ~ tau^(a - cu)
        tipoII=-cu + sp.Rational(1, 2) if Max is sp.Max else -cu + 0.5,
        aspecto=b - a,                 # l_z / l_r
    )
    return E

def ckn_trunc_exponent(a, b, g, V):
    """expoente em tau0 de r^-1 int int_{Q_r} |grad u|^2, r = tau0^(1/2), com o nucleo truncado a B_r.
    Principio de Laplace para leis de potencia: tau = tau0^x, x>=1;
    phi(x) = (1-2g)x + 2 max(a x, 1/2) + max(b x, 1/2); resultado = inf_x phi - 1/2."""
    pts = [1.0]
    for s in (a, b):
        if s > 0 and 1 / (2 * s) > 1: pts.append(1 / (2 * s))
    phi = lambda x: (1 - 2 * g) * x + 2 * max(a * x, 0.5) + max(b * x, 0.5)
    slope_inf = 1 - 2 * g + 2 * a + b
    if slope_inf < 0: return float('-inf')
    return min(phi(x) for x in pts) - 0.5

def openai_point():
    a, b, c = sp.Rational(1, 2), sp.Rational(1, 2) - h, sp.Rational(1, 2) + h
    # em 0<h<1/100: c > d, c + a e o maior gradiente; substituimos o Max explicitamente e conferimos
    E = exps(a, b, c)
    E = {k: (sp.simplify(v.subs(h, h)) if not isinstance(v, dict) else {q: sp.simplify(w) for q, w in v.items()}) for k, v in E.items()}
    out = []
    out.append(('d (U_r = tau^-d)', E['d']))
    out.append(('||u||_inf', E['u_inf']))
    out.append(('energia do nucleo', E['energia']))
    out.append(('||u||_L3', E['L3']))
    out.append(('||u||_H1/2^2', E['H12']))
    out.append(('enstrofia', E['enstrofia']))
    out.append(('||omega||_inf', E['omega_inf']))
    out.append(('Re_loc', E['ReLoc']))
    out.append(('||u||_inf sqrt(tau)', E['tipoII']))
    out.append(('l_z/l_r', E['aspecto']))
    for k, v in out:
        print(f'  {k:28s} tau^({sp.simplify(v)})')
    # integrais temporais: int_0 tau^e dtau diverge sse e <= -1
    def diverges(e): return sp.solve_univariate_inequality(e <= -1, h, relational=False).intersect(H)
    def holds(expr): return sp.solve_univariate_inequality(expr, h, relational=False).intersect(H)
    checks = []
    checks.append(('energia limitada (expoente >= 0)', holds(E['energia'] >= 0)))
    checks.append(('int enstrofia < inf (desig. de energia)', holds(E['enstrofia'] > -1)))
    checks.append(('Leray: ||u||_inf >~ tau^-1/2', holds(E['u_inf'] <= -sp.Rational(1, 2))))
    checks.append(('Leray enstrofia >~ tau^-1/2', holds(E['enstrofia'] <= -sp.Rational(1, 2))))
    checks.append(('ESS/Seregin: ||u||_L3 -> inf', holds(E['L3'] < 0)))
    checks.append(('BKM: int ||omega||_inf = inf', diverges(E['omega_inf'])))
    checks.append(('int ||u||_inf^2 = inf', diverges(2 * E['u_inf'])))
    for q, p in ((4, 8), (6, 4), (9, 3)):
        checks.append((f'Serrin q={q},p={p}: int ||u||_q^p = inf', diverges(p * E['Lq'][q])))
    e_ckn_naive = E['enstrofia'] + sp.Rational(1, 2)
    checks.append(('CKN (nucleo inteiro em B_r) >= eps', holds(e_ckn_naive <= 0)))
    # truncado: para a=1/2, b=1/2-h<1/2: min em x_b = 1/(1-2h) (ver ckn_trunc_exponent)
    g = 1 + h
    xb = 1 / (1 - 2 * h)
    e_ckn_tr = sp.simplify((1 - 2 * g) * xb + 2 * (xb / 2) + sp.Rational(1, 2) - sp.Rational(1, 2))
    checks.append(('CKN (truncado a B_r) >= eps', holds(e_ckn_tr <= 0)))
    checks.append(('Tipo II: ||u||_inf sqrt(tau) -> inf', holds(E['tipoII'] < 0)))
    checks.append(('Re_loc -> inf', holds(E['ReLoc'] < 0)))
    checks.append(('balanco d_t <~ inercia (c >= 1-a)', holds(sp.Rational(1, 2) + h >= 1 - sp.Rational(1, 2))))
    checks.append(('viscosidade <~ inercia (c >= a)', holds(sp.Rational(1, 2) + h >= sp.Rational(1, 2))))
    print('  expoente CKN ingenuo  :', sp.simplify(e_ckn_naive))
    print('  expoente CKN truncado :', sp.simplify(e_ckn_tr), ' (~', sp.series(e_ckn_tr, h, 0, 3).removeO(), ')')
    for hv in (Fr(1, 1000), Fr(1, 200), Fr(1, 101)):
        num = ckn_trunc_exponent(0.5, 0.5 - float(hv), 1 + float(hv), 1.5 - float(hv))
        print(f'    conferencia numerica h={float(hv):.4f}: generico={num:.6f} simbolico={float(e_ckn_tr.subs(h, sp.Rational(hv.numerator, hv.denominator))):.6f}')
    print('  condicao -> conjunto de h em (0,1/100) onde vale:')
    allok = True
    for k, s in checks:
        ok = (s == H)
        allok &= ok
        print(f'    [{"OK" if ok else "FALHA"}] {k}: {s}')
    return allok

def b4_scaling():
    """Expoentes de tau0 apos a escala v(x,s) = lam u(lam x, t0 + lam^2 s).
    Insumos: E(t0) = O(1) (sup_t ||u||_2 < inf, alegacao da fonte); energia do nucleo tau0^(1/2-3h);
    f C_c^inf => int_{t0}^1 ||grad^k f||_p dt <= C tau0 (cota superior, nao usa a planicidade)."""
    t0 = sp.symbols('tau0', positive=True)
    for name, lam_exp in (('(i)  lam = tau0^(-1/2) [convencao do frontier]', -sp.Rational(1, 2)),
                          ('(ii) lam = tau0^(+1/2) [explosao em s = 1, nu fixo]', sp.Rational(1, 2))):
        print('  ' + name)
        print(f'     tempo de explosao s* = tau0/lam^2 = tau0^({1 - 2 * lam_exp})')
        print(f'     ||v0||_2^2 (total)  ~ tau0^({-lam_exp})')
        print(f'     ||v0||_2^2 (nucleo) ~ tau0^({sp.simplify(-lam_exp + sp.Rational(1, 2) - 3 * h)})')
        print(f'     ||v0||_L3            ~ tau0^({-sp.Rational(4, 3) * h})  (invariante)')
        row = []
        for k in range(4):
            for p in (3, sp.oo):
                e = 1 + lam_exp * (1 + k - (0 if p == sp.oo else sp.Rational(3, p)))
                row.append(f'k={k},p={"inf" if p == sp.oo else p}: {e}')
        print('     ||g||_{L^1_s W^{k,p}} <= C tau0^(...): ' + '; '.join(row))

def sweep(step=0.005, lo=0.3, hi=1.0):
    n = int(round((hi - lo) / step)) + 1
    vals = [lo + i * step for i in range(n)]
    eps = 1e-12
    viable = []
    cnt = 0
    for a in vals:
        for b in vals:
            for c in vals:
                cnt += 1
                d = c + b - a
                cu = max(c, d)
                V = 2 * a + b
                g = max(c + a, c + b, d + a, d + b)
                if V - 2 * cu < -eps: continue                    # energia limitada
                ens = -2 * g + V
                if ens <= -1 + eps: continue                       # int enstrofia < inf
                if cu < 0.5 - eps: continue                        # Leray
                if -cu + V / 3 >= -eps: continue                   # L3 -> inf
                if g < 1 - eps: continue                           # BKM
                if any(p * (-cu + V / q) > -1 + eps for q, p in ((4, 8), (6, 4), (9, 3))): continue
                if 2 * (-cu) > -1 + eps: continue                  # Serrin q = inf
                if ckn_trunc_exponent(a, b, g, V) > eps: continue  # CKN
                if cu <= 0.5 + eps: continue                       # Tipo II
                if c < 1 - a - eps: continue                       # d_t <~ inercia
                if c < a - eps: continue                           # viscosidade <~ inercia
                viable.append((a, b, c, cu - a, cu - 0.5, b - a))
    return cnt, viable

if __name__ == '__main__':
    print('== Ponto OpenAI (a,b,c) = (1/2, 1/2-h, 1/2+h), 0<h<1/100 ==')
    ok = openai_point()
    print('  TODAS AS CONDICOES NECESSARIAS VALEM EM (0,1/100):', ok)
    print('== B4: expoentes apos a escala ==')
    b4_scaling()
    print('== Varredura (a,b,c) em [0.3,1]^3, passo 0.005 ==')
    cnt, V = sweep()
    print(f'  pontos: {cnt}; viaveis: {len(V)}')
    if V:
        re = [v[3] for v in V]; t2 = [v[4] for v in V]
        print(f'  Re_loc expoente (cu - a): min={min(re):.4f} max={max(re):.4f}; viaveis com Re_loc = O(1) (cu=a): {sum(1 for x in re if abs(x) < 1e-9)}')
        print(f'  margem Tipo II (cu - 1/2): min={min(t2):.4f} max={max(t2):.4f}')
        for nm, idx in (('a', 0), ('b', 1), ('c', 2)):
            xs = [v[idx] for v in V]
            print(f'  faixa de {nm}: [{min(xs):.3f}, {max(xs):.3f}]')
        asp = [v[5] for v in V]
        print(f'  aspecto b-a: min={min(asp):.3f} max={max(asp):.3f}; com l_z >= l_r (b<=a): {sum(1 for x in asp if x <= 1e-9)}')
        ex = [v for v in V if abs(v[3]) < 1e-9][:5]
        print('  exemplos com Re_loc = O(1):', [(round(x[0], 3), round(x[1], 3), round(x[2], 3)) for x in ex])
        # ponto mais proximo do OpenAI com h = 0.005
        near = [v for v in V if abs(v[0] - 0.5) < 1e-9 and abs(v[1] - 0.495) < 1e-9 and abs(v[2] - 0.505) < 1e-9]
        print('  (0.5, 0.495, 0.505) [OpenAI com h=0.005] viavel na grade:', bool(near))
        # margem tipo II minima por fatia a = 1/2
        sl = [v for v in V if abs(v[0] - 0.5) < 1e-9]
        print(f'  fatia a=1/2: {len(sl)} viaveis; margem Tipo II minima {min(v[4] for v in sl):.4f}' if sl else '  fatia a=1/2 vazia')
