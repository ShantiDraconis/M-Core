/* RH T1(reduced)+T2: weighted Baez-Duarte distance on Re s = sigma.
 *   D_N^F(sigma) = min_{c in R^N} (1/pi) int_0^inf |1 + F(s) sum_{k<=N} c_k k^-s|^2 / |s|^2 dtau,  s = sigma + i tau
 *   E_N(sigma)   = same with c_k = -mu(k) g(k/N)  (smooth Mobius mollifier: an UPPER BOUND for D_N, not the infimum)
 *   F = zeta * R_b, R_b(s) = (s-r0)(s-conj r0)/((s-r1)(s-conj r1)), r1 = 1/2 + i g1, r0 = b + i g1 (b = 0.5: F = zeta).
 * Quadrature: trapezoid, step h1 on [0,tau1], h2 on [tau1,TE] (integrand even in tau -> spectral accuracy at 0).
 * Tail beyond T: mean-value formula (1/pi) (atan-tail) * [1 + 2 c_1 + zeta(2 sigma) sum c_j c_k lcm(j,k)^-2sigma].
 * zeta: Euler-Maclaurin, M = ceil(tau/2)+50 terms, J = 12 Bernoulli corrections; n^-i tau by rotation, exact refresh.
 * Gram (N <= NOPT) only on [0,TG]; mollifier on [0,TE].
 * usage: bd sigma TE TG NOPT h1 h2 tau1 outprefix
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include <string.h>

#define NV 3
#define KMAX 800
#define NNM 41
static const double G1 = 14.134725141734693790;
static const double BETA[NV] = {0.5, 0.65, 0.75};
static int NM[NNM]; /* N_j = round(25*2^(j/8)), j = 0..40: 25..800, log-spaced */
#define NSEL 6
static const int NSELV[NSEL] = {10, 20, 40, 80, 160, 240};

static double EMC[13];
static void init_em(void) {
    double B[13] = {0, 1.0 / 6, -1.0 / 30, 1.0 / 42, -1.0 / 30, 5.0 / 66, -691.0 / 2730, 7.0 / 6, -3617.0 / 510,
                    43867.0 / 798, -174611.0 / 330, 854513.0 / 138, -236364091.0 / 2730};
    double f = 1;
    for (int k = 1; k <= 12; k++) { f *= (2.0 * k - 1) * (2.0 * k); EMC[k] = B[k] / f; }
}
static double complex em_tail(double complex s, double M) {
    double lM = log(M);
    double complex Ms = cexp(-s * lM);
    double complex r = Ms * M / (s - 1.0) + 0.5 * Ms;
    double complex term = s * Ms / M;
    for (int k = 1; k <= 12; k++) {
        r += EMC[k] * term;
        term *= (s + 2.0 * k - 1) * (s + 2.0 * k) / (M * M);
    }
    return r;
}
static double complex zeta_direct(double complex s) { /* for checks / zeta(2 sigma) */
    long M = (long)ceil(cabs(s) / 2) + 50; double complex S = 0;
    for (long n = 1; n < M; n++) S += cexp(-s * log((double)n));
    return S + em_tail(s, (double)M);
}
static char MODE = 'R'; /* 'R': spec F = zeta*R (rational R); 'D': F = zeta*(1 - 2^(beta-s)) (Dirichlet-type planted zeros) */
static double complex Rf(int v, double complex s) {
    if (v == 0) return 1.0;
    if (MODE == 'D') return 1.0 - exp(BETA[v] * M_LN2) * cexp(-s * M_LN2);
    double complex r1 = 0.5 + I * G1, r0 = BETA[v] + I * G1;
    return (s - r0) * (s - conj(r0)) / ((s - r1) * (s - conj(r1)));
}
/* Dirichlet coefficients of the multiplier: d(1)=1, d(2)=-2^beta (mode D); R-mode: treated as 1 in tails (R -> 1) */
static double dco(int v, int a) { if (a == 1) return 1.0; if (MODE == 'D' && v > 0 && a == 2) return -exp(BETA[v] * M_LN2); return 0.0; }
static long gcdl(long a, long b) { while (b) { long t = a % b; a = b; b = t; } return a; }
static double gsm(double x) {
    if (x <= 0.5) return 1.0;
    if (x >= 1.0) return 0.0;
    double u = 2 - 2 * x, a = exp(-1 / u), b = exp(-1 / (1 - u));
    return a / (a + b);
}

int main(int argc, char **argv) {
    if (argc < 9) { fprintf(stderr, "usage\n"); return 1; }
    double sigma = atof(argv[1]), TE = atof(argv[2]), TG = atof(argv[3]);
    int NOPT = atoi(argv[4]);
    double h1 = atof(argv[5]), h2 = atof(argv[6]), tau1 = atof(argv[7]);
    const char *out = argv[8];
    if (argc > 9) MODE = argv[9][0];
    for (int j = 0; j < NNM; j++) NM[j] = (int)lround(25.0 * pow(2.0, j / 8.0));
    init_em();
    /* Mobius */
    int mu[KMAX + 1]; { for (int k = 0; k <= KMAX; k++) mu[k] = 1; char comp[KMAX + 1]; memset(comp, 0, sizeof comp);
        for (int p = 2; p <= KMAX; p++) if (!comp[p]) { for (int m = 2 * p; m <= KMAX; m += p) comp[m] = 1;
            for (int m = p; m <= KMAX; m += p) mu[m] = -mu[m]; for (long m = (long)p * p; m <= KMAX; m += (long)p * p) mu[m] = 0; } }
    /* mollifier coefficients per variant: approximate 1/F. R-mode: mu(k) g(k/N). D-mode: (mu * 2^{beta j} on powers of 2)(k) g(k/N) */
    static double mcv[NV][NNM][KMAX + 1];
    for (int v = 0; v < NV; v++) for (int t = 0; t < NNM; t++) for (int k = 1; k <= KMAX; k++) {
        double m = 0;
        if (MODE == 'D' && v > 0) { double p = 1; for (int q = 1; q <= k; q *= 2) { if (k % q == 0) m += p * mu[k / q]; p *= exp(BETA[v] * M_LN2); } }
        else m = mu[k];
        mcv[v][t][k] = (k <= NM[t]) ? m * gsm((double)k / NM[t]) : 0.0;
    }
    /* grid */
    long n1 = lround(tau1 / h1), n2 = lround((TE - tau1) / h2), NP = n1 + n2 + 1;
    long iG = n1 + lround((TG - tau1) / h2);
    double TGr = tau1 + (iG - n1) * h2;
    long Mmax = (long)ceil(TE / 2) + 52; if (Mmax < KMAX + 2) Mmax = KMAX + 2;
    double *amp = malloc(sizeof(double) * Mmax), *lg = malloc(sizeof(double) * Mmax);
    double *pr = malloc(sizeof(double) * Mmax), *pi_ = malloc(sizeof(double) * Mmax);
    double *rr = malloc(sizeof(double) * Mmax), *ri = malloc(sizeof(double) * Mmax);
    for (long n = 1; n < Mmax; n++) { lg[n] = log((double)n); amp[n] = exp(-sigma * lg[n]); }
    double complex *zs = malloc(sizeof(double complex) * (iG + 1));
    /* accumulators */
    int NO = NOPT;
    double *Gt = calloc((size_t)NV * (NO + 1) * (NO + 1), sizeof(double));
    long double *Gm = calloc((size_t)NV * (NO + 1) * (NO + 1), sizeof(long double));
    long double bm[NV][241]; double bt[NV][241]; memset(bm, 0, sizeof bm); memset(bt, 0, sizeof bt);
    long double am = 0; double at = 0;
    long double eacc[NV][NNM]; memset(eacc, 0, sizeof eacc);
    double vr[KMAX + 1], vi[KMAX + 1];
    FILE *fz = NULL; { char fn[512]; snprintf(fn, sizeof fn, "%s_zeta_samples.txt", out); fz = fopen(fn, "w"); }
    long Mcur = 1; double hcur = -1; int blk = 0;
    for (long i = 0; i < NP; i++) {
        double tau = (i <= n1) ? i * h1 : tau1 + (i - n1) * h2;
        double hnext = (i < n1) ? h1 : h2;
        double wE = (i == 0 || i == NP - 1) ? 0.5 * ((i == 0) ? h1 : h2) : ((i < n1) ? h1 : (i == n1 ? 0.5 * (h1 + h2) : h2));
        double wG = 0;
        if (i < iG) wG = wE; else if (i == iG) wG = (iG == n1) ? 0.5 * h1 : 0.5 * h2;
        long M = (long)ceil(tau / 2) + 50; long Mneed = M > KMAX + 1 ? M : KMAX + 1;
        int refresh = (i % 64 == 0) || (hnext != hcur);
        if (Mneed > Mcur) { for (long n = Mcur; n < Mneed; n++) { pr[n] = cos(tau * lg[n]); pi_[n] = -sin(tau * lg[n]); } Mcur = Mneed; }
        if (refresh) for (long n = 1; n < Mcur; n++) { pr[n] = cos(tau * lg[n]); pi_[n] = -sin(tau * lg[n]); }
        double Sr = 0, Si = 0;
#pragma omp simd reduction(+ : Sr, Si)
        for (long n = 1; n < M; n++) { Sr += amp[n] * pr[n]; Si += amp[n] * pi_[n]; }
        double complex s = sigma + I * tau;
        double complex z = Sr + I * Si + em_tail(s, (double)M);
        if (i % (NP / 200) == 0 || (i < n1 && i % 97 == 0)) fprintf(fz, "%.6f %.17g %.17g\n", tau, creal(z), cimag(z));
        for (int k = 1; k <= KMAX; k++) { vr[k] = amp[k] * pr[k]; vi[k] = amp[k] * pi_[k]; }
        double invs2 = 1.0 / (sigma * sigma + tau * tau);
        double complex F[NV]; for (int v = 0; v < NV; v++) F[v] = z * Rf(v, s);
        /* mollifier */
        for (int t = 0; t < NNM; t++) {
            int N = NM[t];
            for (int v = 0; v < NV; v++) {
                if (MODE == 'R' && v > 0) { /* same mollifier as v=0 */ }
                double Mr = 0, Mi = 0;
                for (int k = 1; k <= N; k++) { Mr += mcv[v][t][k] * vr[k]; Mi += mcv[v][t][k] * vi[k]; }
                double complex w = 1.0 - F[v] * (Mr + I * Mi);
                eacc[v][t] += (long double)(wE * invs2 * (creal(w) * creal(w) + cimag(w) * cimag(w)));
            }
        }
        /* Gram */
        if (wG > 0) {
            zs[i] = z;
            double om[NV];
            for (int v = 0; v < NV; v++) { om[v] = wG * invs2 * (creal(F[v]) * creal(F[v]) + cimag(F[v]) * cimag(F[v]));
                for (int k = 1; k <= NO; k++) bt[v][k] += wG * invs2 * (creal(F[v]) * vr[k] - cimag(F[v]) * vi[k]); }
            at += wG * invs2;
            double *G0 = Gt, *G1p = Gt + (size_t)(NO + 1) * (NO + 1), *G2 = Gt + 2 * (size_t)(NO + 1) * (NO + 1);
            for (int j = 1; j <= NO; j++) {
                double a = vr[j], b = vi[j]; size_t row = (size_t)j * (NO + 1);
#pragma omp simd
                for (int k = j; k <= NO; k++) {
                    double hh = a * vr[k] + b * vi[k];
                    G0[row + k] += om[0] * hh; G1p[row + k] += om[1] * hh; G2[row + k] += om[2] * hh;
                }
            }
            if (++blk == 256 || i == iG) {
                size_t tot = (size_t)NV * (NO + 1) * (NO + 1);
                for (size_t q = 0; q < tot; q++) { Gm[q] += Gt[q]; Gt[q] = 0; }
                for (int v = 0; v < NV; v++) for (int k = 1; k <= NO; k++) { bm[v][k] += bt[v][k]; bt[v][k] = 0; }
                am += at; at = 0; blk = 0;
            }
        }
        /* advance phases */
        if (hnext != hcur) { for (long n = 1; n < Mmax; n++) { rr[n] = cos(hnext * lg[n]); ri[n] = -sin(hnext * lg[n]); } hcur = hnext; }
#pragma omp simd
        for (long n = 1; n < Mcur; n++) { double t = pr[n] * rr[n] - pi_[n] * ri[n]; pi_[n] = pr[n] * ri[n] + pi_[n] * rr[n]; pr[n] = t; }
    }
    fclose(fz);
    double z2s = creal(zeta_direct(2 * sigma + 0 * I));
    /* tails */
    double twE = (M_PI / 2 - atan(TE / sigma)) / sigma, twG = (M_PI / 2 - atan(TGr / sigma)) / sigma;
    char fn[512]; snprintf(fn, sizeof fn, "%s_summary.txt", out); FILE *fs = fopen(fn, "w");
    fprintf(fs, "sigma %.3f TE %.1f TG %.1f NOPT %d h1 %.4f h2 %.4f tau1 %.1f points %ld zeta(2sigma) %.15f\n", sigma, TE, TGr, NO, h1, h2, tau1, NP, z2s);
    fprintf(fs, "MODE %c\n", MODE);
    for (int t = 0; t < NNM; t++) {
        int N = NM[t]; double tl[NV];
        for (int v = 0; v < NV; v++) {
            /* q = d * (mollifier coeffs), length <= 2N; mean |1 - zeta q|^2 = zeta(2s) sum q_j q_k lcm^-2s - 1 */
            static double q[2 * KMAX + 2]; memset(q, 0, sizeof q);
            for (int k = 1; k <= N; k++) for (int a = 1; a <= 2; a++) q[a * k] += dco(v, a) * mcv[v][t][k];
            double L2 = 0;
            for (int j = 1; j <= 2 * N; j++) if (q[j] != 0) for (int k = 1; k <= 2 * N; k++) if (q[k] != 0) {
                long l = (long)j / gcdl(j, k) * k; L2 += q[j] * q[k] * pow((double)l, -2 * sigma); }
            tl[v] = twE * (z2s * L2 - 1.0);
        }
        fprintf(fs, "E N %d", N);
        for (int v = 0; v < NV; v++) fprintf(fs, " b%.2f %.10e", BETA[v], (double)((eacc[v][t] + tl[v]) / M_PI));
        fprintf(fs, " tail0 %.3e\n", tl[0] / M_PI);
    }
    /* Gram tails + normalization, Cholesky (long double) */
    long double a_ = (am + twG) / M_PI;
    long double *L = malloc(sizeof(long double) * (NO + 1) * (NO + 1));
    long double DN[NV][241]; double csel[NV][NSEL][241];
    for (int v = 0; v < NV; v++) {
        long double *G = Gm + (size_t)v * (NO + 1) * (NO + 1);
        long double b[241];
        for (int j = 1; j <= NO; j++) for (int k = j; k <= NO; k++) {
            long double tg = 0;
            for (int a = 1; a <= 2; a++) for (int bb = 1; bb <= 2; bb++) {
                double da = dco(v, a), db = dco(v, bb); if (da == 0 || db == 0) continue;
                long ja = (long)a * j, kb = (long)bb * k; long l = ja / gcdl(ja, kb) * kb;
                tg += da * db * powl((long double)l, -2 * (long double)sigma);
            }
            long double val = (G[(size_t)j * (NO + 1) + k] + twG * z2s * tg) / M_PI;
            G[(size_t)j * (NO + 1) + k] = val; G[(size_t)k * (NO + 1) + j] = val;
        }
        for (int k = 1; k <= NO; k++) b[k] = (bm[v][k] + (k == 1 ? twG : 0)) / M_PI;
        /* Cholesky */
        int ok = 1;
        for (int j = 1; j <= NO && ok; j++) {
            long double d = G[(size_t)j * (NO + 1) + j];
            for (int k = 1; k < j; k++) d -= L[(size_t)j * (NO + 1) + k] * L[(size_t)j * (NO + 1) + k];
            if (d <= 0) { ok = 0; fprintf(fs, "CHOLESKY FAIL v=%d at j=%d d=%Lg\n", v, j, d); break; }
            L[(size_t)j * (NO + 1) + j] = sqrtl(d);
            for (int i2 = j + 1; i2 <= NO; i2++) {
                long double x = G[(size_t)i2 * (NO + 1) + j];
                for (int k = 1; k < j; k++) x -= L[(size_t)i2 * (NO + 1) + k] * L[(size_t)j * (NO + 1) + k];
                L[(size_t)i2 * (NO + 1) + j] = x / L[(size_t)j * (NO + 1) + j];
            }
        }
        long double zv[241]; long double acc = a_;
        for (int j = 1; j <= NO; j++) {
            long double x = b[j];
            for (int k = 1; k < j; k++) x -= L[(size_t)j * (NO + 1) + k] * zv[k];
            zv[j] = x / L[(size_t)j * (NO + 1) + j];
            acc -= zv[j] * zv[j]; DN[v][j] = acc;
        }
        for (int t = 0; t < NSEL; t++) {
            int N = NSELV[t]; if (N > NO) continue;
            long double y[241], c[241];
            for (int j = 1; j <= N; j++) y[j] = -zv[j];
            for (int j = N; j >= 1; j--) { long double x = y[j]; for (int k = j + 1; k <= N; k++) x -= L[(size_t)k * (NO + 1) + j] * c[k]; c[j] = x / L[(size_t)j * (NO + 1) + j]; }
            for (int j = 1; j <= N; j++) csel[v][t][j] = (double)c[j];
        }
    }
    /* direct re-evaluation of the discrete objective at c* (sum of non-negative terms; solver-independent upper bound) */
    double qd[NV][NSEL]; memset(qd, 0, sizeof qd);
    for (long i = 0; i <= iG; i++) {
        double tau = (i <= n1) ? i * h1 : tau1 + (i - n1) * h2;
        double wE = (i == 0) ? 0.5 * h1 : ((i < n1) ? h1 : (i == n1 ? 0.5 * (h1 + h2) : h2));
        double wG = (i < iG) ? wE : ((iG == n1) ? 0.5 * h1 : 0.5 * h2);
        double complex s = sigma + I * tau; double invs2 = 1.0 / (sigma * sigma + tau * tau);
        double cr[241], ci[241];
        for (int k = 1; k <= NO; k++) { double ph = tau * log((double)k); double a = exp(-sigma * log((double)k)); cr[k] = a * cos(ph); ci[k] = -a * sin(ph); }
        for (int v = 0; v < NV; v++) {
            double complex Fv = zs[i] * Rf(v, s);
            for (int t = 0; t < NSEL; t++) {
                int N = NSELV[t]; if (N > NO) continue;
                double Pr = 0, Pi = 0; for (int k = 1; k <= N; k++) { Pr += csel[v][t][k] * cr[k]; Pi += csel[v][t][k] * ci[k]; }
                double complex w = 1.0 + Fv * (Pr + I * Pi);
                qd[v][t] += wG * invs2 * (creal(w) * creal(w) + cimag(w) * cimag(w));
            }
        }
    }
    for (int v = 0; v < NV; v++) for (int t = 0; t < NSEL; t++) {
        int N = NSELV[t]; if (N > NO) continue;
        double L2 = 0, nrm = 0, P1 = 0;
        for (int j = 1; j <= N; j++) { nrm += csel[v][t][j] * csel[v][t][j]; P1 += csel[v][t][j] / j;
            for (int k = 1; k <= N; k++) for (int a = 1; a <= 2; a++) for (int bb = 1; bb <= 2; bb++) {
                double da = dco(v, a), db = dco(v, bb); if (da == 0 || db == 0) continue;
                long ja = (long)a * j, kb = (long)bb * k; long l = ja / gcdl(ja, kb) * kb;
                L2 += da * db * csel[v][t][j] * csel[v][t][k] * pow((double)l, -2 * sigma); } }
        double tail = twG * (1 + 2 * csel[v][t][1] + z2s * L2);
        fprintf(fs, "OPT b%.2f N %d D_chol %.12e D_direct %.12e |c|2 %.3e c1 %.6f P(1) %.6f c2..c6", BETA[v], N, (double)DN[v][N], (qd[v][t] + tail) / M_PI, sqrt(nrm), csel[v][t][1], P1);
        for (int k = 2; k <= 6; k++) fprintf(fs, " %.4f", csel[v][t][k]);
        fprintf(fs, "\n");
    }
    fclose(fs);
    snprintf(fn, sizeof fn, "%s_DN.txt", out); FILE *fd = fopen(fn, "w");
    fprintf(fd, "# N D_N(zeta) D_N(b=0.65) D_N(b=0.75)   sigma=%.3f TG=%.1f\n", sigma, TGr);
    for (int N = 1; N <= NO; N++) fprintf(fd, "%d %.14Le %.14Le %.14Le\n", N, DN[0][N], DN[1][N], DN[2][N]);
    fclose(fd);
    return 0;
}
