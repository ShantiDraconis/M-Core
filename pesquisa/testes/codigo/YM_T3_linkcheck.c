/* Independent control for YM_T3.c at L=3: work in the full LINK basis (2^(2L^2) configurations),
 * T' = D'^{1/2} prod_l (1 + e^{-2beta} X_l) D'^{1/2},  D' = exp(beta sum_p sigma_p - beta L^2),
 * restrict to gauge-invariant vectors with the gauge projector prod_s (1+G_s)/2 and to flux sectors with
 * (1 + e F)/2, both re-applied after every matrix-vector product (charged sectors have LARGER eigenvalues).
 * usage: YM_T3_linkcheck L beta...    prints beta lam0(++) lam1(++) lam0(-+)  (normalised as in YM_T3.c) */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
static int L, NL, N, NS;
static int plaq[64][4];
static unsigned *gmask, Fx, Fy;
static double *Dh;
static unsigned long long rng = 1234567891234567ULL;
static double urand(void) { rng ^= rng << 13; rng ^= rng >> 7; rng ^= rng << 17; return (rng >> 11) * (1.0 / 9007199254740992.0); }
static int XL(int x, int y) { return ((x + L) % L) + L * ((y + L) % L); }
static int YL(int x, int y) { return L * L + ((x + L) % L) + L * ((y + L) % L); }
static void apply_T(const double *in, double *out, double t) {
    for (int c = 0; c < N; c++) out[c] = Dh[c] * in[c];
    for (int l = 0; l < NL; l++) {
        unsigned m = 1u << l;
        for (int c = 0; c < N; c++) if (!(c & m)) { double a = out[c], b = out[c | m]; out[c] = a + t * b; out[c | m] = b + t * a; }
    }
    for (int c = 0; c < N; c++) out[c] *= Dh[c];
}
static unsigned smask[64];
static void gauge_proj(double *v, double *tmp) { /* prod_s (1+G_s)/2 */
    for (int s = 0; s < L * L; s++) {
        unsigned m = smask[s];
        for (int c = 0; c < N; c++) tmp[c] = 0.5 * (v[c] + v[c ^ m]);
        memcpy(v, tmp, sizeof(double) * N);
    }
}
static void flux_proj(double *v, int ex, int ey, double *tmp) {
    gauge_proj(v, tmp);
    for (int c = 0; c < N; c++) tmp[c] = 0.5 * (v[c] + ex * v[c ^ Fx]);
    for (int c = 0; c < N; c++) v[c] = 0.5 * (tmp[c] + ey * tmp[c ^ Fy]);
}
static void tqli(double *d, double *e, int n) { /* same NR algorithm, eigenvalues only */
    double *E = calloc(n + 1, sizeof(double)); for (int i = 0; i < n - 1; i++) E[i] = e[i];
    for (int l = 0; l < n; l++) { int iter = 0, m; do {
        for (m = l; m < n - 1; m++) { double dd = fabs(d[m]) + fabs(d[m + 1]); if (fabs(E[m]) <= 1e-16 * dd) break; }
        if (m != l) { if (iter++ == 200) break;
            double g = (d[l + 1] - d[l]) / (2.0 * E[l]), r = hypot(g, 1.0);
            g = d[m] - d[l] + E[l] / (g + (g >= 0 ? fabs(r) : -fabs(r)));
            double s = 1, c = 1, p = 0; int i;
            for (i = m - 1; i >= l; i--) { double f = s * E[i], b = c * E[i]; E[i + 1] = (r = hypot(f, g));
                if (r == 0.0) { d[i + 1] -= p; E[m] = 0.0; break; }
                s = f / r; c = g / r; g = d[i + 1] - p; r = (d[i] - g) * s + 2.0 * c * b; d[i + 1] = g + (p = s * r); g = c * r - b; }
            if (r == 0.0 && i >= l) continue; d[l] -= p; E[l] = g; E[m] = 0.0; }
    } while (m != l); }
    free(E);
}
static int cmpd(const void *a, const void *b) { double x = *(double *)a, y = *(double *)b; return (x < y) - (x > y); }
static void run(double beta, int ex, int ey, int M, double *l0, double *l1) {
    double t = exp(-2 * beta);
    for (int c = 0; c < N; c++) { double s = 0; for (int p = 0; p < L * L; p++) {
        int sg = 1; for (int k = 0; k < 4; k++) if (c >> plaq[p][k] & 1) sg = -sg; s += sg; }
        Dh[c] = exp(0.5 * beta * (s - L * L)); }
    double *V = malloc(sizeof(double) * (size_t)N * (M + 1)), *w = malloc(sizeof(double) * N), *tmp = malloc(sizeof(double) * N);
    double *al = calloc(M + 1, sizeof(double)), *be = calloc(M + 1, sizeof(double)), *d = malloc(sizeof(double) * (M + 1)), *e = malloc(sizeof(double) * (M + 1));
    for (int c = 0; c < N; c++) tmp[c] = urand() - 0.5;
    for (int c = 0; c < N; c++) { double s = 0; for (int g = 0; g < NS; g++) s += tmp[c ^ gmask[g]]; V[c] = s / NS; }
    flux_proj(V, ex, ey, tmp);
    double nr = 0; for (int c = 0; c < N; c++) nr += V[c] * V[c]; nr = sqrt(nr); for (int c = 0; c < N; c++) V[c] /= nr;
    int m = 0;
    for (int j = 0; j < M; j++) {
        double *vj = V + (size_t)j * N; apply_T(vj, w, t); flux_proj(w, ex, ey, tmp);
        double a = 0; for (int c = 0; c < N; c++) a += w[c] * vj[c]; al[j] = a;
        for (int pass = 0; pass < 2; pass++) for (int k = 0; k <= j; k++) { double *vk = V + (size_t)k * N, h = 0;
            for (int c = 0; c < N; c++) h += w[c] * vk[c]; for (int c = 0; c < N; c++) w[c] -= h * vk[c]; }
        double b = 0; for (int c = 0; c < N; c++) b += w[c] * w[c]; b = sqrt(b); be[j] = b; m = j + 1;
        if (b < 1e-12 * fabs(al[0])) break;
        double *vn = V + (size_t)(j + 1) * N; for (int c = 0; c < N; c++) vn[c] = w[c] / b;
    }
    for (int i = 0; i < m; i++) { d[i] = al[i]; e[i] = be[i]; }
    tqli(d, e, m); qsort(d, m, sizeof(double), cmpd);
    *l0 = d[0]; *l1 = d[1];
    free(V); free(w); free(tmp); free(al); free(be); free(d); free(e);
}
int main(int argc, char **argv) {
    L = atoi(argv[1]); NL = 2 * L * L; N = 1 << NL; NS = 1 << (L * L);
    for (int y = 0; y < L; y++) for (int x = 0; x < L; x++) {
        int p = x + L * y; plaq[p][0] = XL(x, y); plaq[p][1] = YL(x + 1, y); plaq[p][2] = XL(x, y + 1); plaq[p][3] = YL(x, y); }
    gmask = malloc(sizeof(unsigned) * NS);
    for (int g = 0; g < NS; g++) { unsigned m = 0;
        for (int s = 0; s < L * L; s++) if (g >> s & 1) { int x = s % L, y = s / L;
            m ^= 1u << XL(x, y); m ^= 1u << XL(x - 1, y); m ^= 1u << YL(x, y); m ^= 1u << YL(x, y - 1); }
        gmask[g] = m; }
    for (int s = 0; s < L * L; s++) smask[s] = gmask[1u << s];
    Fx = 0; for (int y = 0; y < L; y++) Fx ^= 1u << XL(0, y);
    Fy = 0; for (int x = 0; x < L; x++) Fy ^= 1u << YL(x, 0);
    Dh = malloc(sizeof(double) * N);
    for (int i = 2; i < argc; i++) {
        double beta = atof(argv[i]), a0, a1, b0, b1;
        run(beta, 1, 1, 70, &a0, &a1); run(beta, -1, 1, 40, &b0, &b1);
        printf("%.6f %.15e %.15e %.15e  m=%.12f split=%.12f\n", beta, a0, a1, b0, log(a0 / a1), log(a0 / b0)); fflush(stdout);
    }
    return 0;
}
