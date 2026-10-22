/* NS T2 — constante de Lei–Lin kappa* em T^3 (NS_frontier.md §3 Q4, §5 T2).
 *
 * u(x) = sum_k v_k e^{ik.x}, k em Z^3\0, k.v_k = 0, v_{-k} = conj(v_k).
 * Euler/NS: d/dt v_k = -nu|k|^2 v_k + G_k,  G_k = -i P_k W_k,  W_k = sum_{p+q=k} (k.v_p) v_q.
 * A_s = sum |k|^s |v_k|.
 * N = sum_{v_k != 0} |k|^-1 Re<v_k/|v_k|, G_k> + sum_{v_k = 0, k in S+S} |k|^-1 |G_k|
 *   (= d+/dt A_{-1} da parte nao linear; o segundo termo e a derivada a direita nos modos nulos).
 * rho = A_{-1} A_1 / N  (N > 0).  kappa* = inf rho.  Lei–Lin: N <= A_0^2 <= A_{-1}A_1 => kappa* >= 1.
 * Cota angular (deste teste): N <= Ntil := sum_{p,q} sin<(p+q,p) |v_p||v_q| <= A_0^2/sqrt2.
 *
 * Suporte: modos com |k_i| <= M (opcionalmente uma mascara). Saidas W_k em |k_i| <= 2M.
 * Otimizacao: L-BFGS em f = log A_{-1} + log A_1 - log N, gradiente analitico (conferido por DF).
 *
 * Uso:
 *   NS_T2 check M seed
 *   NS_T2 opt M nrestarts seed maxit inittype     (inittype: 0 gauss, 1 lei de potencia, 2 casca aleatoria,
 *                                                    3 suporte esparso aleatorio)
 *   NS_T2 shell M s nrestarts seed maxit          (suporte = casca |k|^2 = s)
 *   NS_T2 small M nmodes nsupports nrestarts seed maxit  (suportes aleatorios com nmodes pares +-k)
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <complex.h>

typedef double complex cplx;

static int M, B, NB;           /* B = 4M+1 lado da caixa grande, NB = B^3 */
static int nall;               /* modos na caixa pequena (com sinal) */
static int (*kall)[3];         /* vetores */
static int *bigidx;            /* indice na caixa grande de cada modo */
static int *negof;             /* indice do -k */
static double *kn;             /* |k| */
static double (*e1)[3], (*e2)[3];
static int *insupp;            /* mascara */
static int nh, *hidx;          /* modos independentes (metade positiva) no suporte */
static int ns, *sidx;          /* todos os modos do suporte (com sinal) */
static int *bigToMode;         /* caixa grande -> modo (ou -1) */

static int bindex(int a, int b, int c) { return ((a + 2 * M) * B + (b + 2 * M)) * B + (c + 2 * M); }

static unsigned long long rng = 88172645463325252ULL;
static double urand(void) { rng ^= rng << 13; rng ^= rng >> 7; rng ^= rng << 17; return (rng >> 11) * (1.0 / 9007199254740992.0); }
static double grand(void) { double u = urand() + 1e-300, v = urand(); return sqrt(-2 * log(u)) * cos(2 * M_PI * v); }

static int ispos(const int *k) { if (k[0]) return k[0] > 0; if (k[1]) return k[1] > 0; return k[2] > 0; }

static void setup(int m) {
    M = m; B = 4 * M + 1; NB = B * B * B;
    int side = 2 * M + 1;
    nall = side * side * side - 1;
    kall = malloc(sizeof(int[3]) * nall); bigidx = malloc(sizeof(int) * nall); negof = malloc(sizeof(int) * nall);
    kn = malloc(sizeof(double) * nall); e1 = malloc(sizeof(double[3]) * nall); e2 = malloc(sizeof(double[3]) * nall);
    insupp = calloc(nall, sizeof(int)); hidx = malloc(sizeof(int) * nall); sidx = malloc(sizeof(int) * nall);
    bigToMode = malloc(sizeof(int) * NB);
    for (int i = 0; i < NB; i++) bigToMode[i] = -1;
    int n = 0;
    for (int a = -M; a <= M; a++) for (int b = -M; b <= M; b++) for (int c = -M; c <= M; c++) {
        if (!a && !b && !c) continue;
        kall[n][0] = a; kall[n][1] = b; kall[n][2] = c;
        bigidx[n] = bindex(a, b, c); bigToMode[bigidx[n]] = n;
        kn[n] = sqrt((double)(a * a + b * b + c * c));
        n++;
    }
    for (int i = 0; i < nall; i++) negof[i] = bigToMode[bindex(-kall[i][0], -kall[i][1], -kall[i][2])];
    /* bases ortonormais reais de k^perp, iguais para k e -k */
    for (int i = 0; i < nall; i++) {
        int j = ispos(kall[i]) ? i : negof[i];
        double k[3] = {kall[j][0], kall[j][1], kall[j][2]}, nk = kn[j];
        double t[3] = {1, 0, 0};
        if (fabs(k[0]) / nk > 0.8) { t[0] = 0; t[1] = 1; }
        double d = (t[0] * k[0] + t[1] * k[1] + t[2] * k[2]) / (nk * nk);
        double a[3] = {t[0] - d * k[0], t[1] - d * k[1], t[2] - d * k[2]};
        double na = sqrt(a[0] * a[0] + a[1] * a[1] + a[2] * a[2]);
        for (int r = 0; r < 3; r++) a[r] /= na;
        double b[3] = {k[1] * a[2] - k[2] * a[1], k[2] * a[0] - k[0] * a[2], k[0] * a[1] - k[1] * a[0]};
        for (int r = 0; r < 3; r++) { b[r] /= nk; e1[i][r] = a[r]; e2[i][r] = b[r]; }
    }
}

static void set_support_all(void) { for (int i = 0; i < nall; i++) insupp[i] = 1; }

static void finalize_support(void) {
    nh = 0; ns = 0;
    for (int i = 0; i < nall; i++) if (insupp[i]) { sidx[ns++] = i; if (ispos(kall[i])) hidx[nh++] = i; }
}

/* buffers */
static cplx (*V)[3], (*GV)[3], (*W)[3], (*LAM)[3];
static int *Wtouched, nWt; static int *Wlist;

static void alloc_buffers(void) {
    V = calloc(nall, sizeof(cplx[3])); GV = calloc(nall, sizeof(cplx[3]));
    W = calloc(NB, sizeof(cplx[3])); LAM = calloc(NB, sizeof(cplx[3]));
    Wtouched = calloc(NB, sizeof(int)); Wlist = malloc(sizeof(int) * NB);
}

static void params_to_v(const double *x) {
    for (int i = 0; i < nall; i++) for (int r = 0; r < 3; r++) V[i][r] = 0;
    for (int h = 0; h < nh; h++) {
        int i = hidx[h];
        cplx al = x[4 * h] + I * x[4 * h + 1], be = x[4 * h + 2] + I * x[4 * h + 3];
        for (int r = 0; r < 3; r++) { V[i][r] = al * e1[i][r] + be * e2[i][r]; V[negof[i]][r] = conj(V[i][r]); }
    }
}

typedef struct { double Am1, A0, A1, N, Nsupp, Nzero, Ntil, energy_res, hel_res, scale; } Stats;

/* calcula W para o suporte atual */
static void compute_W(void) {
    for (int t = 0; t < nWt; t++) { int K = Wlist[t]; Wtouched[K] = 0; for (int r = 0; r < 3; r++) W[K][r] = 0; }
    nWt = 0;
    for (int a = 0; a < ns; a++) {
        int p = sidx[a];
        for (int b = 0; b < ns; b++) {
            int q = sidx[b];
            int K0 = kall[p][0] + kall[q][0], K1 = kall[p][1] + kall[q][1], K2 = kall[p][2] + kall[q][2];
            if (!K0 && !K1 && !K2) continue;
            int Ki = bindex(K0, K1, K2);
            cplx kv = K0 * V[p][0] + K1 * V[p][1] + K2 * V[p][2];
            if (!Wtouched[Ki]) { Wtouched[Ki] = 1; Wlist[nWt++] = Ki; }
            for (int r = 0; r < 3; r++) W[Ki][r] += kv * V[q][r];
        }
    }
}

static void bcoords(int Ki, int *K) { K[2] = Ki % B - 2 * M; K[1] = (Ki / B) % B - 2 * M; K[0] = Ki / (B * B) - 2 * M; }

/* projeta W em K^perp */
static void projW(const int *K, const cplx *w, cplx *out) {
    double k2 = K[0] * K[0] + K[1] * K[1] + K[2] * K[2];
    cplx d = (K[0] * w[0] + K[1] * w[1] + K[2] * w[2]) / k2;
    for (int r = 0; r < 3; r++) out[r] = w[r] - d * K[r];
}

static const double VZERO = 0.0; /* modo considerado nulo se |v| == 0 exatamente */

/* f e gradiente; retorna +inf se N <= 0 */
static double objective(const double *x, double *grad, Stats *st) {
    params_to_v(x);
    double Am1 = 0, A1 = 0, A0 = 0;
    for (int a = 0; a < ns; a++) { int i = sidx[a]; double n = 0; for (int r = 0; r < 3; r++) n += creal(V[i][r] * conj(V[i][r])); n = sqrt(n); Am1 += n / kn[i]; A1 += n * kn[i]; A0 += n; }
    compute_W();
    double Ns = 0, Nz = 0;
    for (int t = 0; t < nWt; t++) {
        int Ki = Wlist[t], K[3]; bcoords(Ki, K);
        double kk = sqrt((double)(K[0] * K[0] + K[1] * K[1] + K[2] * K[2]));
        int md = bigToMode[Ki];
        for (int r = 0; r < 3; r++) LAM[Ki][r] = 0;
        double nv = 0;
        if (md >= 0 && insupp[md]) { for (int r = 0; r < 3; r++) nv += creal(V[md][r] * conj(V[md][r])); nv = sqrt(nv); }
        if (md >= 0 && insupp[md] && nv > VZERO) {
            cplx z = 0; for (int r = 0; r < 3; r++) z += conj(V[md][r]) * W[Ki][r];
            double R = cimag(z);  /* Re(-i conj(v).W) */
            Ns += R / (kk * nv);
        } else {
            cplx pw[3]; projW(K, W[Ki], pw);
            double npw = 0; for (int r = 0; r < 3; r++) npw += creal(pw[r] * conj(pw[r])); npw = sqrt(npw);
            Nz += npw / kk;
        }
    }
    double N = Ns + Nz;
    if (st) { st->Am1 = Am1; st->A1 = A1; st->A0 = A0; st->N = N; st->Nsupp = Ns; st->Nzero = Nz; }
    if (!(N > 0)) return INFINITY;
    double f = log(Am1) + log(A1) - log(N);
    if (!grad) return f;
    /* backward */
    for (int a = 0; a < ns; a++) { int i = sidx[a]; for (int r = 0; r < 3; r++) GV[i][r] = 0; }
    for (int t = 0; t < nWt; t++) {
        int Ki = Wlist[t], K[3]; bcoords(Ki, K);
        double kk = sqrt((double)(K[0] * K[0] + K[1] * K[1] + K[2] * K[2]));
        int md = bigToMode[Ki];
        double nv = 0;
        if (md >= 0 && insupp[md]) { for (int r = 0; r < 3; r++) nv += creal(V[md][r] * conj(V[md][r])); nv = sqrt(nv); }
        if (md >= 0 && insupp[md] && nv > VZERO) {
            cplx z = 0; for (int r = 0; r < 3; r++) z += conj(V[md][r]) * W[Ki][r];
            double R = cimag(z), c = 1.0 / kk;
            for (int r = 0; r < 3; r++) {
                GV[md][r] += (-1.0 / N) * c * (-I * W[Ki][r] / nv - R * V[md][r] / (nv * nv * nv));
                LAM[Ki][r] = (-1.0 / N) * c * I * V[md][r] / nv;
            }
        } else {
            cplx pw[3]; projW(K, W[Ki], pw);
            double npw = 0; for (int r = 0; r < 3; r++) npw += creal(pw[r] * conj(pw[r])); npw = sqrt(npw);
            if (npw > 0) for (int r = 0; r < 3; r++) LAM[Ki][r] = (-1.0 / N) * pw[r] / (kk * npw);
        }
    }
    for (int a = 0; a < ns; a++) {
        int p = sidx[a];
        for (int b = 0; b < ns; b++) {
            int q = sidx[b];
            int K0 = kall[p][0] + kall[q][0], K1 = kall[p][1] + kall[q][1], K2 = kall[p][2] + kall[q][2];
            if (!K0 && !K1 && !K2) continue;
            int Ki = bindex(K0, K1, K2);
            cplx *lam = LAM[Ki];
            cplx s = lam[0] * conj(V[q][0]) + lam[1] * conj(V[q][1]) + lam[2] * conj(V[q][2]);
            GV[p][0] += s * K0; GV[p][1] += s * K1; GV[p][2] += s * K2;
            cplx kv = conj(K0 * V[p][0] + K1 * V[p][1] + K2 * V[p][2]);
            for (int r = 0; r < 3; r++) GV[q][r] += kv * lam[r];
        }
    }
    for (int a = 0; a < ns; a++) {
        int i = sidx[a]; double n = 0; for (int r = 0; r < 3; r++) n += creal(V[i][r] * conj(V[i][r])); n = sqrt(n);
        if (n > 0) for (int r = 0; r < 3; r++) GV[i][r] += V[i][r] / n * (1.0 / (kn[i] * Am1) + kn[i] / A1);
    }
    for (int h = 0; h < nh; h++) {
        int i = hidx[h], j = negof[i];
        cplx ga = 0, gb = 0, gan = 0, gbn = 0;
        for (int r = 0; r < 3; r++) { ga += e1[i][r] * GV[i][r]; gb += e2[i][r] * GV[i][r]; gan += e1[i][r] * GV[j][r]; gbn += e2[i][r] * GV[j][r]; }
        ga += conj(gan); gb += conj(gbn);
        grad[4 * h] = creal(ga); grad[4 * h + 1] = cimag(ga); grad[4 * h + 2] = creal(gb); grad[4 * h + 3] = cimag(gb);
    }
    return f;
}

/* estatisticas extras: Ntil, residuos de energia e helicidade */
static void extra_stats(Stats *st) {
    double Ntil = 0;
    for (int a = 0; a < ns; a++) {
        int p = sidx[a]; double np = 0; for (int r = 0; r < 3; r++) np += creal(V[p][r] * conj(V[p][r])); np = sqrt(np);
        for (int b = 0; b < ns; b++) {
            int q = sidx[b]; double nq = 0; for (int r = 0; r < 3; r++) nq += creal(V[q][r] * conj(V[q][r])); nq = sqrt(nq);
            double K[3] = {kall[p][0] + kall[q][0], kall[p][1] + kall[q][1], kall[p][2] + kall[q][2]};
            double kk = sqrt(K[0] * K[0] + K[1] * K[1] + K[2] * K[2]);
            if (kk == 0) continue;
            double c[3] = {K[1] * kall[p][2] - K[2] * kall[p][1], K[2] * kall[p][0] - K[0] * kall[p][2], K[0] * kall[p][1] - K[1] * kall[p][0]};
            double sn = sqrt(c[0] * c[0] + c[1] * c[1] + c[2] * c[2]) / (kk * kn[p]);
            Ntil += sn * np * nq;
        }
    }
    st->Ntil = Ntil;
    /* energia: sum_K Re(conj v_K . G_K) = 0 ; helicidade: sum_K Re(conj(i K x v_K) . G_K) = 0 */
    double en = 0, he = 0, sc = 0;
    for (int a = 0; a < ns; a++) {
        int i = sidx[a]; int Ki = bigidx[i]; int K[3] = {kall[i][0], kall[i][1], kall[i][2]};
        if (!Wtouched[Ki]) continue;
        cplx pw[3], G[3]; projW(K, W[Ki], pw);
        for (int r = 0; r < 3; r++) G[r] = -I * pw[r];
        cplx om[3] = {I * (K[1] * V[i][2] - K[2] * V[i][1]), I * (K[2] * V[i][0] - K[0] * V[i][2]), I * (K[0] * V[i][1] - K[1] * V[i][0])};
        for (int r = 0; r < 3; r++) { en += creal(conj(V[i][r]) * G[r]); he += creal(conj(om[r]) * G[r]); sc += cabs(V[i][r]) * cabs(G[r]) * (1 + kn[i]); }
    }
    st->energy_res = en; st->hel_res = he; st->scale = sc;
}

/* ---------- L-BFGS ---------- */
#define LM 12
static double lbfgs(double *x, int n, int maxit, Stats *st) {
    double *g = malloc(sizeof(double) * n), *gn = malloc(sizeof(double) * n), *d = malloc(sizeof(double) * n), *xn = malloc(sizeof(double) * n);
    double *S = malloc(sizeof(double) * n * LM), *Y = malloc(sizeof(double) * n * LM), rhoh[LM], alph[LM];
    int mem = 0, head = 0, stall = 0;
    double f = objective(x, g, NULL);
    for (int it = 0; it < maxit && isfinite(f); it++) {
        for (int i = 0; i < n; i++) d[i] = -g[i];
        for (int k = 0; k < mem; k++) { int j = (head - 1 - k + LM) % LM; double s = 0; for (int i = 0; i < n; i++) s += S[j * n + i] * d[i]; alph[j] = rhoh[j] * s; for (int i = 0; i < n; i++) d[i] -= alph[j] * Y[j * n + i]; }
        if (mem) { int j = (head - 1 + LM) % LM; double sy = 0, yy = 0; for (int i = 0; i < n; i++) { sy += S[j * n + i] * Y[j * n + i]; yy += Y[j * n + i] * Y[j * n + i]; } for (int i = 0; i < n; i++) d[i] *= sy / yy; }
        else { double gn2 = 0, xn2 = 0; for (int i = 0; i < n; i++) { gn2 += g[i] * g[i]; xn2 += x[i] * x[i]; } double sc = 1e-2 * sqrt(xn2 / (gn2 + 1e-300)); for (int i = 0; i < n; i++) d[i] *= sc; }
        for (int k = mem - 1; k >= 0; k--) { int j = (head - 1 - k + LM) % LM; double s = 0; for (int i = 0; i < n; i++) s += Y[j * n + i] * d[i]; double b = rhoh[j] * s; for (int i = 0; i < n; i++) d[i] += S[j * n + i] * (alph[j] - b); }
        double gd = 0; for (int i = 0; i < n; i++) gd += g[i] * d[i];
        if (gd >= 0) { mem = 0; head = 0; continue; }
        double step = 1, fn = INFINITY; int ok = 0;
        for (int ls = 0; ls < 40; ls++) {
            for (int i = 0; i < n; i++) xn[i] = x[i] + step * d[i];
            fn = objective(xn, gn, NULL);
            if (isfinite(fn) && fn <= f + 1e-4 * step * gd) { ok = 1; break; }
            step *= 0.5;
        }
        if (!ok) { if (mem == 0) break; mem = 0; head = 0; continue; }
        double sy = 0;
        for (int i = 0; i < n; i++) { S[head * n + i] = xn[i] - x[i]; Y[head * n + i] = gn[i] - g[i]; sy += S[head * n + i] * Y[head * n + i]; }
        if (sy > 1e-14) { rhoh[head] = 1 / sy; head = (head + 1) % LM; if (mem < LM) mem++; }
        if (f - fn < 1e-11) stall++; else stall = 0;
        memcpy(x, xn, sizeof(double) * n); memcpy(g, gn, sizeof(double) * n); f = fn;
        /* renormaliza (rho invariante por escala) */
        double xn2 = 0; for (int i = 0; i < n; i++) xn2 += x[i] * x[i]; xn2 = sqrt(xn2);
        if (xn2 > 1e3 || xn2 < 1e-3) { for (int i = 0; i < n; i++) x[i] /= xn2; mem = 0; head = 0; f = objective(x, g, NULL); }
        if (stall > 30) break;
    }
    f = objective(x, NULL, st);
    free(g); free(gn); free(d); free(xn); free(S); free(Y);
    return f;
}

static void random_init(double *x, int type) {
    int n = 4 * nh;
    double sh = 0; int shell = 0;
    if (type == 2) { int i = hidx[(int)(urand() * nh)]; shell = kall[i][0] * kall[i][0] + kall[i][1] * kall[i][1] + kall[i][2] * kall[i][2]; (void)sh; }
    for (int h = 0; h < nh; h++) {
        int i = hidx[h]; int k2 = kall[i][0] * kall[i][0] + kall[i][1] * kall[i][1] + kall[i][2] * kall[i][2];
        double amp = 1;
        if (type == 1) amp = pow(kn[i], -1.0 - 2 * urand());
        if (type == 2) amp = (k2 == shell) ? 1 : 1e-3;
        if (type == 3) amp = (urand() < 0.15) ? 1 : 1e-4;
        for (int r = 0; r < 4; r++) x[4 * h + r] = amp * grand();
    }
    (void)n;
}

static void report(const char *tag, double f, Stats *st) {
    Stats s2 = *st; extra_stats(&s2);
    printf("%s rho=%.6f Am1A1/A0^2=%.4f N/A0^2=%.4f Ntil/A0^2=%.4f N/Ntil=%.4f Nzero/N=%.3f nmodes=%d\n", tag, exp(f),
           s2.Am1 * s2.A1 / (s2.A0 * s2.A0), s2.N / (s2.A0 * s2.A0), s2.Ntil / (s2.A0 * s2.A0), s2.N / s2.Ntil, s2.Nzero / s2.N, ns);
}

static void structure(void) {
    /* massa por casca e numero de modos relevantes */
    double tot = 0, mx = 0; double shellmass[64] = {0};
    for (int a = 0; a < ns; a++) { int i = sidx[a]; double n = 0; for (int r = 0; r < 3; r++) n += creal(V[i][r] * conj(V[i][r])); n = sqrt(n); tot += n; if (n > mx) mx = n; int k2 = kall[i][0] * kall[i][0] + kall[i][1] * kall[i][1] + kall[i][2] * kall[i][2]; if (k2 < 64) shellmass[k2] += n; }
    int big = 0; for (int a = 0; a < ns; a++) { int i = sidx[a]; double n = 0; for (int r = 0; r < 3; r++) n += creal(V[i][r] * conj(V[i][r])); if (sqrt(n) > 0.05 * mx) big++; }
    printf("   cascas(|k|^2:fracao de A0):");
    for (int s = 1; s < 64; s++) if (shellmass[s] > 0.01 * tot) printf(" %d:%.3f", s, shellmass[s] / tot);
    printf("  | modos com |v|>5%%max: %d\n", big);
}

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "uso\n"); return 1; }
    const char *mode = argv[1];
    setup(atoi(argv[2]));
    alloc_buffers();
    if (!strcmp(mode, "check")) {
        rng ^= (unsigned long long)atoi(argv[3]) * 2654435761ULL;
        set_support_all(); finalize_support();
        int n = 4 * nh; double *x = malloc(sizeof(double) * n), *g = malloc(sizeof(double) * n);
        random_init(x, 0);
        Stats st; double f = objective(x, g, &st);
        if (!isfinite(f)) { for (int i = 0; i < n; i++) x[i] = -x[i]; f = objective(x, g, &st); }
        printf("check M=%d modos=%d params=%d f=%.10f rho=%.6f\n", M, ns, n, f, exp(f));
        /* 1. gradiente por diferencas finitas */
        double maxrel = 0;
        for (int t = 0; t < 12; t++) {
            int i = (int)(urand() * n); double h = 1e-6 * (fabs(x[i]) + 1e-3), xi = x[i];
            x[i] = xi + h; double fp = objective(x, NULL, NULL); x[i] = xi - h; double fm = objective(x, NULL, NULL); x[i] = xi;
            double fd = (fp - fm) / (2 * h); double rel = fabs(fd - g[i]) / (fabs(fd) + fabs(g[i]) + 1e-12);
            if (rel > maxrel) maxrel = rel;
        }
        printf("  [grad] erro relativo max (12 coords) = %.2e\n", maxrel);
        objective(x, NULL, &st); extra_stats(&st);
        printf("  [energia] sum Re<v,G> = %.3e (escala %.3e)\n  [helicidade] sum Re<omega,G> = %.3e\n", st.energy_res, st.scale, st.hel_res);
        printf("  [Lei-Lin] N=%.6f <= A0^2=%.6f <= Am1*A1=%.6f ; [angular] N <= Ntil=%.6f <= A0^2/sqrt2=%.6f\n", st.N, st.A0 * st.A0, st.Am1 * st.A1, st.Ntil, st.A0 * st.A0 / sqrt(2));
        /* 2. conferencia fisica: (u.grad u)(x) = sum_K i W_K e^{iK.x} */
        params_to_v(x); compute_W();
        double maxerr = 0, mag = 0;
        for (int t = 0; t < 3; t++) {
            double X[3] = {6.28 * urand(), 6.28 * urand(), 6.28 * urand()};
            cplx u[3] = {0}, du[3][3] = {{0}}, nl[3] = {0}, nl2[3] = {0};
            for (int a = 0; a < ns; a++) { int i = sidx[a]; cplx e = cexp(I * (kall[i][0] * X[0] + kall[i][1] * X[1] + kall[i][2] * X[2]));
                for (int r = 0; r < 3; r++) { u[r] += V[i][r] * e; for (int j = 0; j < 3; j++) du[r][j] += I * kall[i][j] * V[i][r] * e; } }
            for (int r = 0; r < 3; r++) for (int j = 0; j < 3; j++) nl[r] += u[j] * du[r][j];
            for (int tt = 0; tt < nWt; tt++) { int Ki = Wlist[tt], K[3]; bcoords(Ki, K); cplx e = cexp(I * (K[0] * X[0] + K[1] * X[1] + K[2] * X[2])); for (int r = 0; r < 3; r++) nl2[r] += I * W[Ki][r] * e; }
            for (int r = 0; r < 3; r++) { double er = cabs(nl[r] - nl2[r]); if (er > maxerr) maxerr = er; if (cabs(nl[r]) > mag) mag = cabs(nl[r]); }
        }
        printf("  [fisico] max |(u.grad u)(x) - sum iW e^{iKx}| = %.3e (magnitude %.3e)\n", maxerr, mag);
        /* 3. derivada temporal: A_{-1}(v + dt G) - A_{-1}(v) ~ N dt (nu=0), G em toda a caixa grande */
        objective(x, NULL, &st);
        double Am1_0 = st.Am1;
        for (int k = 3; k <= 7; k += 2) {
            double dt = pow(10, -k), Am1 = 0;
            for (int tt = 0; tt < nWt; tt++) {
                int Ki = Wlist[tt], K[3]; bcoords(Ki, K); double kk = sqrt((double)(K[0] * K[0] + K[1] * K[1] + K[2] * K[2]));
                cplx pw[3]; projW(K, W[Ki], pw); int md = bigToMode[Ki]; double nn = 0;
                for (int r = 0; r < 3; r++) { cplx vv = (md >= 0 ? V[md][r] : 0) + dt * (-I * pw[r]); nn += creal(vv * conj(vv)); }
                Am1 += sqrt(nn) / kk;
            }
            for (int a = 0; a < ns; a++) { int i = sidx[a]; if (!Wtouched[bigidx[i]]) { double nn = 0; for (int r = 0; r < 3; r++) nn += creal(V[i][r] * conj(V[i][r])); Am1 += sqrt(nn) / kn[i]; } }
            printf("  [d/dt] dt=1e-%d: (A_{-1}(t+dt)-A_{-1})/dt = %.6f vs N = %.6f\n", k, (Am1 - Am1_0) / dt, st.N);
        }
        /* 4. invariancia por escala u -> s u */
        for (int i = 0; i < n; i++) x[i] *= 3.7;
        double f2 = objective(x, NULL, NULL);
        printf("  [escala] rho(3.7u)/rho(u) - 1 = %.2e\n", exp(f2 - f) - 1);
        return 0;
    }
    if (!strcmp(mode, "opt") || !strcmp(mode, "shell") || !strcmp(mode, "small") || !strcmp(mode, "support")) {
        int nrest, maxit, inittype = 0, shell = 0, nmodes = 0, nsup = 1, grow = 0;
        if (!strcmp(mode, "opt")) { nrest = atoi(argv[3]); rng ^= (unsigned long long)atoi(argv[4]) * 2654435761ULL; maxit = atoi(argv[5]); inittype = atoi(argv[6]); set_support_all(); }
        else if (!strcmp(mode, "shell")) { shell = atoi(argv[3]); nrest = atoi(argv[4]); rng ^= (unsigned long long)atoi(argv[5]) * 2654435761ULL; maxit = atoi(argv[6]);
            for (int i = 0; i < nall; i++) insupp[i] = (kall[i][0] * kall[i][0] + kall[i][1] * kall[i][1] + kall[i][2] * kall[i][2] == shell); }
        else if (!strcmp(mode, "small")) { nmodes = atoi(argv[3]); nsup = atoi(argv[4]); nrest = atoi(argv[5]); rng ^= (unsigned long long)atoi(argv[6]) * 2654435761ULL; maxit = atoi(argv[7]); grow = argc > 8 ? atoi(argv[8]) : 0; }
        else { /* support M nrest seed maxit grow k1x k1y k1z ... */
            nrest = atoi(argv[3]); rng ^= (unsigned long long)atoi(argv[4]) * 2654435761ULL; maxit = atoi(argv[5]); grow = atoi(argv[6]);
            for (int a = 7; a + 2 < argc; a += 3) { int i = bigToMode[bindex(atoi(argv[a]), atoi(argv[a + 1]), atoi(argv[a + 2]))]; if (i >= 0) { insupp[i] = 1; insupp[negof[i]] = 1; } }
        }
        int *base = malloc(sizeof(int) * nall); memcpy(base, insupp, sizeof(int) * nall);
        double best = INFINITY; double *bP = calloc(nall * 4, sizeof(double)); int *bsupp = malloc(sizeof(int) * nall);
        double *P = calloc(nall * 4, sizeof(double)), *x = malloc(sizeof(double) * 4 * nall);
        for (int sp = 0; sp < nsup; sp++) {
            if (!strcmp(mode, "small")) {
                memset(insupp, 0, sizeof(int) * nall);
                int cnt = 0;
                while (cnt < nmodes) { int i = (int)(urand() * nall); if (!insupp[i]) { insupp[i] = 1; insupp[negof[i]] = 1; cnt++; } }
            } else memcpy(insupp, base, sizeof(int) * nall);
            finalize_support();
            for (int r = 0; r < nrest; r++) {
                memcpy(insupp, sp >= 0 ? insupp : base, sizeof(int) * nall); finalize_support();
                random_init(x, strcmp(mode, "opt") ? 0 : inittype);
                int n = 4 * nh;
                Stats st; double f0 = objective(x, NULL, &st);
                if (!isfinite(f0)) { for (int i = 0; i < n; i++) x[i] = -x[i]; f0 = objective(x, NULL, &st); }
                if (!isfinite(f0)) continue;
                double f = lbfgs(x, n, maxit, &st);
                /* poda: zera classes com |v| < 1e-3 max e reotimiza (aumenta N ou mantem) */
                for (int pr = 0; pr < 6; pr++) {
                    double mx = 0; for (int h = 0; h < nh; h++) { double s = 0; for (int q = 0; q < 4; q++) s += x[4 * h + q] * x[4 * h + q]; if (s > mx) mx = s; }
                    int removed = 0;
                    for (int h = 0; h < nh; h++) P[4 * hidx[h]] = NAN;
                    for (int h = 0; h < nh; h++) { int i = hidx[h]; double s = 0; for (int q = 0; q < 4; q++) { s += x[4 * h + q] * x[4 * h + q]; P[4 * i + q] = x[4 * h + q]; }
                        if (s < 1e-6 * mx && nh - removed > 2) { insupp[i] = 0; insupp[negof[i]] = 0; removed++; } }
                    if (!removed) break;
                    finalize_support();
                    for (int h = 0; h < nh; h++) for (int q = 0; q < 4; q++) x[4 * h + q] = P[4 * hidx[h] + q];
                    n = 4 * nh;
                    double f2 = objective(x, NULL, NULL);
                    if (!isfinite(f2)) break;
                    f = lbfgs(x, n, maxit, &st);
                }
                /* crescimento guloso: tenta acrescentar cada classe da caixa (amplitude pequena) */
                for (int gstep = 0; gstep < grow; gstep++) {
                    for (int h = 0; h < nh; h++) for (int q = 0; q < 4; q++) P[4 * hidx[h] + q] = x[4 * h + q];
                    int *cur = malloc(sizeof(int) * nall); memcpy(cur, insupp, sizeof(int) * nall);
                    double bestadd = f; int bi = -1; double *bxx = malloc(sizeof(double) * 4 * nall);
                    for (int c = 0; c < nall; c++) {
                        if (!ispos(kall[c]) || cur[c]) continue;
                        memcpy(insupp, cur, sizeof(int) * nall); insupp[c] = 1; insupp[negof[c]] = 1; finalize_support();
                        double mx = 0; for (int h = 0; h < nh; h++) if (hidx[h] != c) for (int q = 0; q < 4; q++) if (fabs(P[4 * hidx[h] + q]) > mx) mx = fabs(P[4 * hidx[h] + q]);
                        for (int tr = 0; tr < 2; tr++) {
                            for (int h = 0; h < nh; h++) for (int q = 0; q < 4; q++) x[4 * h + q] = (hidx[h] == c) ? 0.3 * mx * grand() : P[4 * hidx[h] + q];
                            if (!isfinite(objective(x, NULL, NULL))) continue;
                            double fa = lbfgs(x, 4 * nh, maxit, &st);
                            if (fa < bestadd - 1e-9) { bestadd = fa; bi = c; memcpy(bxx, x, sizeof(double) * 4 * nh); }
                        }
                    }
                    memcpy(insupp, cur, sizeof(int) * nall);
                    if (bi < 0) { finalize_support(); for (int h = 0; h < nh; h++) for (int q = 0; q < 4; q++) x[4 * h + q] = P[4 * hidx[h] + q]; free(cur); free(bxx); break; }
                    insupp[bi] = 1; insupp[negof[bi]] = 1; finalize_support();
                    memcpy(x, bxx, sizeof(double) * 4 * nh); f = bestadd;
                    printf("    [cresce] +(%d,%d,%d) -> classes=%d rho=%.6f\n", kall[bi][0], kall[bi][1], kall[bi][2], nh, exp(f)); fflush(stdout);
                    free(cur); free(bxx);
                }
                f = objective(x, NULL, &st);
                if (f < best) {
                    best = f; memset(bP, 0, sizeof(double) * 4 * nall);
                    for (int h = 0; h < nh; h++) for (int q = 0; q < 4; q++) bP[4 * hidx[h] + q] = x[4 * h + q];
                    memcpy(bsupp, insupp, sizeof(int) * nall);
                    char tag[64]; snprintf(tag, sizeof tag, "  [suporte %d reinicio %d] melhor", sp, r);
                    report(tag, f, &st); structure(); fflush(stdout);
                }
            }
        }
        if (isfinite(best)) {
            memcpy(insupp, bsupp, sizeof(int) * nall); finalize_support();
            for (int h = 0; h < nh; h++) for (int q = 0; q < 4; q++) x[4 * h + q] = bP[4 * hidx[h] + q];
            Stats st; double f = objective(x, NULL, &st); report("FINAL", f, &st); structure();
            if (nh <= 40) { printf("   suporte(classes):"); for (int h = 0; h < nh; h++) { int i = hidx[h]; printf(" (%d,%d,%d)", kall[i][0], kall[i][1], kall[i][2]); } printf("\n");
                printf("   amplitudes |v|:"); for (int h = 0; h < nh; h++) { double s = 0; for (int q = 0; q < 4; q++) s += x[4 * h + q] * x[4 * h + q]; printf(" %.3f", sqrt(s)); } printf("\n"); }
        }
        return 0;
    }
    return 1;
}
