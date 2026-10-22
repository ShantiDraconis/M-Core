/* YM T3 (reduced) — exact transfer-matrix spectrum of 2+1D Z2 lattice gauge theory (Wilson action,
 * isotropic coupling beta) on an L x L spatial torus, gauge-invariant sector.
 *
 * Basis of the gauge-invariant sector: plaquette variables P_p in {0,1} (prod sigma_p = 1) and the two
 * holonomies (W_x on row y=0, W_y on column x=0): dim 2^(L^2+1).  Electric-flux ('t Hooft) sectors
 * e=(ex,ey): eigenvalues of F_x, F_y (flip W_x / W_y), each of dim 2^(L^2-1); inside a sector
 * X_l flips the two plaquettes containing l and picks up ex (ey) if l lies on the W_x (W_y) loop.
 *   T = D^{1/2} K D^{1/2},  D = exp(beta sum_p sigma_p),  K = prod_l (e^beta + e^-beta X_l)  (temporal gauge).
 * We use the normalised T' = D'^{1/2} K' D'^{1/2}, D' = exp(-2 beta #flipped), K' = prod_l (1 + e^{-2beta} X_l).
 * Lanczos with full reorthogonalisation, random start (all lattice-symmetry sectors), QL on the tridiagonal.
 * usage: YM_T3 L beta_min beta_max nbeta [all]   -> prints per beta: lam0(e) for the 4 sectors, lam1(e=0)
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

static int L, NP, NL, DIM;
static int lmask[64], lflipx[64], lflipy[64];
static double *Dh; /* D'^{1/2} */

static unsigned long long rng = 88172645463325252ULL;
static double urand(void) { rng ^= rng << 13; rng ^= rng >> 7; rng ^= rng << 17; return (rng >> 11) * (1.0 / 9007199254740992.0); }

static void setup(void) {
    NP = L * L; NL = 2 * L * L; DIM = 1 << (NP - 1);
    int last = NP - 1, l = 0;
    for (int y = 0; y < L; y++) for (int x = 0; x < L; x++) {
        /* x-link (x,y): plaquettes (x,y) and (x,y-1) */
        int p1 = x + L * y, p2 = x + L * ((y - 1 + L) % L);
        lmask[l] = (p1 != last ? 1 << p1 : 0) ^ (p2 != last ? 1 << p2 : 0);
        lflipx[l] = (y == 0); lflipy[l] = 0; l++;
        /* y-link (x,y): plaquettes (x,y) and (x-1,y) */
        p1 = x + L * y; p2 = ((x - 1 + L) % L) + L * y;
        lmask[l] = (p1 != last ? 1 << p1 : 0) ^ (p2 != last ? 1 << p2 : 0);
        lflipx[l] = 0; lflipy[l] = (x == 0); l++;
    }
    Dh = malloc(sizeof(double) * DIM);
}

static void set_beta(double beta) {
    for (int i = 0; i < DIM; i++) {
        int c = __builtin_popcount(i);
        int lastbit = c & 1; /* parity fixes the last plaquette */
        Dh[i] = exp(-beta * (c + lastbit));
    }
}

static void apply_T(const double *in, double *out, double t, int ex, int ey) {
    for (int i = 0; i < DIM; i++) out[i] = Dh[i] * in[i];
    for (int l = 0; l < NL; l++) {
        int m = lmask[l];
        double ts = t * ((lflipx[l] && ex < 0) ? -1 : 1) * ((lflipy[l] && ey < 0) ? -1 : 1);
        for (int i = 0; i < DIM; i++) {
            int j = i ^ m;
            if (j > i) { double a = out[i], b = out[j]; out[i] = a + ts * b; out[j] = b + ts * a; }
        }
    }
    for (int i = 0; i < DIM; i++) out[i] *= Dh[i];
}

/* eigenvalues of symmetric tridiagonal (d diag, e offdiag e[0..n-2]); NR tqli, eigenvalues only */
static void tqli(double *d, double *e, int n) {
    for (int i = 1; i < n; i++) e[i - 1] = e[i - 1]; /* e[i] couples i,i+1 */
    double *E = calloc(n + 1, sizeof(double));
    for (int i = 0; i < n - 1; i++) E[i] = e[i];
    E[n - 1] = 0;
    for (int l = 0; l < n; l++) {
        int iter = 0, m;
        do {
            for (m = l; m < n - 1; m++) { double dd = fabs(d[m]) + fabs(d[m + 1]); if (fabs(E[m]) <= 1e-16 * dd) break; }
            if (m != l) {
                if (iter++ == 200) break;
                double g = (d[l + 1] - d[l]) / (2.0 * E[l]);
                double r = hypot(g, 1.0);
                g = d[m] - d[l] + E[l] / (g + (g >= 0 ? fabs(r) : -fabs(r)));
                double s = 1, c = 1, p = 0; int i;
                for (i = m - 1; i >= l; i--) {
                    double f = s * E[i], b = c * E[i];
                    E[i + 1] = (r = hypot(f, g));
                    if (r == 0.0) { d[i + 1] -= p; E[m] = 0.0; break; }
                    s = f / r; c = g / r; g = d[i + 1] - p; r = (d[i] - g) * s + 2.0 * c * b;
                    d[i + 1] = g + (p = s * r); g = c * r - b;
                }
                if (r == 0.0 && i >= l) continue;
                d[l] -= p; E[l] = g; E[m] = 0.0;
            }
        } while (m != l);
    }
    free(E);
}

static int cmpd(const void *a, const void *b) { double x = *(double *)a, y = *(double *)b; return (x < y) - (x > y); }

/* returns number of Ritz values written to ev (sorted descending) */
static int lanczos(double t, int ex, int ey, int maxit, double *ev) {
    int M = maxit < DIM ? maxit : DIM;
    double *V = malloc(sizeof(double) * (size_t)DIM * (M + 1));
    double *w = malloc(sizeof(double) * DIM);
    double *al = calloc(M + 1, sizeof(double)), *be = calloc(M + 1, sizeof(double));
    double nrm = 0;
    for (int i = 0; i < DIM; i++) { V[i] = urand() - 0.5; nrm += V[i] * V[i]; }
    nrm = sqrt(nrm); for (int i = 0; i < DIM; i++) V[i] /= nrm;
    double prev0 = 0, prev1 = 0; int m = 0, nev = 0;
    double *d = malloc(sizeof(double) * (M + 1)), *e = malloc(sizeof(double) * (M + 1));
    for (int j = 0; j < M; j++) {
        double *vj = V + (size_t)j * DIM;
        apply_T(vj, w, t, ex, ey);
        double a = 0; for (int i = 0; i < DIM; i++) a += w[i] * vj[i];
        al[j] = a;
        for (int pass = 0; pass < 2; pass++)
            for (int k = 0; k <= j; k++) {
                double *vk = V + (size_t)k * DIM, h = 0;
                for (int i = 0; i < DIM; i++) h += w[i] * vk[i];
                for (int i = 0; i < DIM; i++) w[i] -= h * vk[i];
            }
        double b = 0; for (int i = 0; i < DIM; i++) b += w[i] * w[i];
        b = sqrt(b); be[j] = b; m = j + 1;
        int minit = DIM < 60 ? DIM : 60;
        int check = (j >= minit - 1 && j % 4 == 3) || b < 1e-12 * fabs(al[0]) || j == M - 1;
        if (check) {
            for (int i = 0; i < m; i++) { d[i] = al[i]; e[i] = be[i]; }
            tqli(d, e, m);
            qsort(d, m, sizeof(double), cmpd);
            double l0 = d[0], l1 = m > 1 ? d[1] : 0;
            int conv = (fabs(l0 - prev0) <= 1e-15 * l0) && (fabs(l1 - prev1) <= 1e-13 * l0 + 1e-300);
            prev0 = l0; prev1 = l1;
            if (conv || b < 1e-12 * fabs(al[0]) || j == M - 1) { nev = m; memcpy(ev, d, sizeof(double) * m); break; }
        }
        double *vn = V + (size_t)(j + 1) * DIM;
        for (int i = 0; i < DIM; i++) vn[i] = w[i] / b;
    }
    free(V); free(w); free(al); free(be); free(d); free(e);
    return nev;
}

/* light Lanczos (no reorthogonalisation) for large DIM: returns lam0 and the largest Ritz value that is
   not a (ghost) copy of lam0 */
static void lanczos_light(double t, int ex, int ey, int its, double *l0out, double *l1out) {
    double *v0 = calloc(DIM, sizeof(double)), *v1 = malloc(sizeof(double) * DIM), *w = malloc(sizeof(double) * DIM);
    double *al = calloc(its + 1, sizeof(double)), *be = calloc(its + 1, sizeof(double));
    double *d = malloc(sizeof(double) * (its + 1)), *e = malloc(sizeof(double) * (its + 1));
    double nrm = 0;
    for (int i = 0; i < DIM; i++) { v1[i] = urand() - 0.5; nrm += v1[i] * v1[i]; }
    nrm = sqrt(nrm); for (int i = 0; i < DIM; i++) v1[i] /= nrm;
    double bprev = 0, p0 = 0, p1 = 0; int m = 0;
    for (int j = 0; j < its; j++) {
        apply_T(v1, w, t, ex, ey);
        double a = 0; for (int i = 0; i < DIM; i++) a += w[i] * v1[i];
        double b = 0;
        for (int i = 0; i < DIM; i++) { w[i] -= a * v1[i] + bprev * v0[i]; b += w[i] * w[i]; }
        b = sqrt(b); al[j] = a; be[j] = b; m = j + 1;
        for (int i = 0; i < DIM; i++) { v0[i] = v1[i]; v1[i] = w[i] / b; }
        bprev = b;
        if (j >= 20 && j % 5 == 4) {
            for (int i = 0; i < m; i++) { d[i] = al[i]; e[i] = be[i]; }
            tqli(d, e, m); qsort(d, m, sizeof(double), cmpd);
            double l0 = d[0], l1 = 0;
            for (int i = 1; i < m; i++) if (d[i] < l0 * (1 - 1e-9)) { l1 = d[i]; break; }
            fprintf(stderr, "  it=%d lam0=%.15e lam1=%.15e\n", m, l0, l1);
            if (fabs(l0 - p0) <= 1e-14 * l0 && fabs(l1 - p1) <= 1e-12 * l0) { p0 = l0; p1 = l1; break; }
            p0 = l0; p1 = l1;
        }
    }
    *l0out = p0; *l1out = p1;
    free(v0); free(v1); free(w); free(al); free(be); free(d); free(e);
}

int main(int argc, char **argv) {
    L = atoi(argv[1]);
    double b0 = atof(argv[2]), b1 = atof(argv[3]); int nb = atoi(argv[4]);
    int all = argc > 5;
    setup();
    double *ev = malloc(sizeof(double) * (DIM + 1));
    int sect[4][2] = {{1, 1}, {-1, 1}, {1, -1}, {-1, -1}};
    printf("# L=%d dim/sector=%d links=%d\n# beta lam0(++) lam1(++) lam0(-+) lam0(+-) lam0(--)  [normalised T']  m_L=log(lam0/lam1)  split_x=log(lam0(++)/lam0(-+))  split_xy\n", L, DIM, NL);
    for (int ib = 0; ib < nb; ib++) {
        double beta = nb > 1 ? b0 + (b1 - b0) * ib / (nb - 1) : b0;
        set_beta(beta);
        double t = exp(-2 * beta);
        double l0[4], l1 = 0;
        if (DIM > (1 << 20)) { /* L=5: light mode, sectors (++) and (-+) only */
            double a0, a1, c0, c1;
            lanczos_light(t, 1, 1, 300, &a0, &a1);
            lanczos_light(t, -1, 1, 300, &c0, &c1);
            printf("%.6f %.15e %.15e %.15e nan nan  %.12f %.12f nan\n", beta, a0, a1, c0, log(a0 / a1), log(a0 / c0));
            fflush(stdout); continue;
        }
        for (int s = 0; s < 4; s++) {
            int n = lanczos(t, sect[s][0], sect[s][1], 400, ev);
            l0[s] = ev[0];
            if (s == 0) l1 = n > 1 ? ev[1] : 0;
            if (all) { printf("#ALL beta=%.6f e=(%+d,%+d):", beta, sect[s][0], sect[s][1]); for (int i = 0; i < n; i++) printf(" %.15e", ev[i]); printf("\n"); }
        }
        printf("%.6f %.15e %.15e %.15e %.15e %.15e  %.12f %.12f %.12f\n", beta, l0[0], l1, l0[1], l0[2], l0[3],
               log(l0[0] / l1), log(l0[0] / l0[1]), log(l0[0] / l0[3]));
        fflush(stdout);
    }
    return 0;
}
