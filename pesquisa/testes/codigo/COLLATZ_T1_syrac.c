/* COLLATZ T1: exact law of Syrac(Z/3^n), n = 1..NMAX, via the discrete-log recursion
 *   P_n(l) = 1/2 Q_n(l+1) + 1/2 P_n(l+1)   (cyclic, l in Z/L_n, L_n = 2*3^(n-1), unit u = 2^l mod 3^n)
 *   Q_n(m) = P_{n-1}(dlog_{n-1}((2^m-1)/3)) if m even and (2^m-1)/3 is a unit mod 3^(n-1), else 0;  Q_1 = delta_0.
 * Fourier: phi_n(xi) = sum_x P(x) e(-xi x/3^n). For xi = 1+3*eta: phi = FFT_{3^(n-1)} of f(x mod 3^(n-1)) += P(x) e(-x/3^n).
 * xi = 2 mod 3 gives conj(phi(-xi)), so M_n = max_{3 !| xi}|phi_n(xi)| = max_eta |FFT(f)(eta)|.
 * Usage: syrac NMAX NFFT dumpdir
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <complex.h>
#include <string.h>

static int64_t P3[40];

static void fft3(double complex *x, int K) {
    int64_t N = P3[K];
    if (N == 1) return;
    for (int64_t i = 0; i < N; i++) {
        int64_t j = 0, t = i;
        for (int d = 0; d < K; d++) { j = j * 3 + t % 3; t /= 3; }
        if (i < j) { double complex tmp = x[i]; x[i] = x[j]; x[j] = tmp; }
    }
    const double complex w3 = cexp(-2.0 * M_PI * I / 3.0), w3b = cexp(-4.0 * M_PI * I / 3.0);
    for (int64_t len = 3; len <= N; len *= 3) {
        int64_t third = len / 3;
        for (int64_t k = 0; k < third; k++) {
            double ang = -2.0 * M_PI * (double)k / (double)len;
            double complex w1 = cexp(I * ang), w2 = w1 * w1;
            for (int64_t st = 0; st < N; st += len) {
                double complex a = x[st + k], b = x[st + k + third] * w1, c = x[st + k + 2 * third] * w2;
                x[st + k] = a + b + c;
                x[st + k + third] = a + w3 * b + w3b * c;
                x[st + k + 2 * third] = a + w3b * b + w3 * c;
            }
        }
    }
}

int main(int argc, char **argv) {
    int NMAX = atoi(argv[1]), NFFT = atoi(argv[2]);
    const char *dump = argc > 3 ? argv[3] : NULL;
    P3[0] = 1;
    for (int i = 1; i < 40; i++) P3[i] = P3[i - 1] * 3;

    double *Pprev = NULL;       /* P_{n-1} indexed by l */
    double complex *specPrev = NULL; /* phi_{n-1}(1+3 eta), eta < 3^(n-2) */
    printf("# n  L_n  c_n  rho_n=c_n*L_n  maxP*L_n  sum-1  M_n  xi*  minus_log3(c_n)\n");
    for (int n = 1; n <= NMAX; n++) {
        int64_t mod = P3[n], L = 2 * P3[n - 1];
        double *P = malloc(sizeof(double) * L);
        /* ---- Q_n into P (in place) ---- */
        if (n == 1) {
            P[0] = 1.0; P[1] = 0.0;
        } else {
            int64_t modp = P3[n - 1], Lp = 2 * P3[n - 2];
            int32_t *dl = malloc(sizeof(int32_t) * modp);
            for (int64_t i = 0; i < modp; i++) dl[i] = -1;
            int64_t x = 1;
            for (int64_t l = 0; l < Lp; l++) { dl[x] = (int32_t)l; x = (x * 2) % modp; }
            x = 1; /* 2^m mod 3^n */
            for (int64_t m = 0; m < L; m++) {
                double q = 0.0;
                if ((m & 1) == 0) {
                    int64_t y = (x - 1) / 3; /* x = 1 mod 3 */
                    if (y % 3 != 0) { int32_t d = dl[y]; if (d < 0) { fprintf(stderr, "dlog miss\n"); return 1; } q = Pprev[d]; }
                }
                P[m] = q;
                x = (x * 2) % mod;
            }
            free(dl);
        }
        /* ---- cyclic recurrence P(l) = 1/2 Q(l+1) + 1/2 P(l+1), in place, downward ---- */
        {
            int W = 80; /* warm-up: P(L)=P(0) ~ sum_{a=1}^{W} 2^-a Q(a mod L) (+ wraps) */
            double pnext = 0.0, wgt = 0.5;
            for (int a = 1; a <= W + 200; a++) { pnext += wgt * P[a % L]; wgt *= 0.5; if (wgt == 0) break; }
            /* pnext approximates P(0) = P(L); exact up to 2^-(W+200) relative (wraps included for tiny L) */
            /* for tiny L the geometric tail wraps many times: handle exactly via 1/(1-2^-L) */
            if (L < 64) {
                pnext = 0.0;
                for (int64_t a = 1; a <= L; a++) pnext += ldexp(1.0, -(int)a) * P[a % L];
                pnext /= (1.0 - ldexp(1.0, -(int)L));
            }
            double qnext = P[0]; /* Q(L) = Q(0) */
            for (int64_t l = L - 1; l >= 0; l--) {
                double ql = P[l];
                double pl = 0.5 * qnext + 0.5 * pnext;
                P[l] = pl;
                qnext = ql; pnext = pl;
            }
        }
        /* ---- stats ---- */
        double mn = 2, mx = -1; long double sum = 0; int64_t argl = -1;
        for (int64_t l = 0; l < L; l++) { sum += P[l]; if (P[l] < mn) { mn = P[l]; argl = l; } if (P[l] > mx) mx = P[l]; }
        int64_t argu = 1; { int64_t x = 1; for (int64_t l = 0; l < argl; l++) x = (x * 2) % mod; argu = x; }
        /* ---- dump small n ---- */
        if (dump && n <= 7) {
            char fn[512]; snprintf(fn, sizeof fn, "%s/syrac_P%d.txt", dump, n);
            FILE *f = fopen(fn, "w"); int64_t x = 1;
            for (int64_t l = 0; l < L; l++) { fprintf(f, "%lld %.17g\n", (long long)x, P[l]); x = (x * 2) % mod; }
            fclose(f);
        }
        /* ---- Fourier ---- */
        double Mn = NAN; int64_t xistar = 0;
        double complex *spec = NULL;
        if (n <= NFFT) {
            int64_t Nf = P3[n - 1];
            spec = calloc(Nf, sizeof(double complex));
            int64_t x = 1;
            for (int64_t l = 0; l < L; l++) {
                double ang = -2.0 * M_PI * ((double)x / (double)mod);
                spec[x % Nf] += P[l] * cexp(I * ang);
                x = (x * 2) % mod;
            }
            fft3(spec, n - 1);
            Mn = -1;
            for (int64_t e = 0; e < Nf; e++) { double a = cabs(spec[e]); if (a > Mn) { Mn = a; xistar = 1 + 3 * e; } }
            if (xistar > mod / 2) xistar -= mod;
            /* self-check 1: direct DFT for n <= 7 */
            if (n <= 7) {
                double maxd = 0;
                for (int64_t e = 0; e < Nf; e++) {
                    int64_t xi = 1 + 3 * e; double complex acc = 0; int64_t y = 1;
                    for (int64_t l = 0; l < L; l++) { acc += P[l] * cexp(-2.0 * M_PI * I * (double)((xi * y) % mod) / (double)mod); y = (y * 2) % mod; }
                    double d = cabs(acc - spec[e]); if (d > maxd) maxd = d;
                }
                fprintf(stderr, "n=%d direct-DFT vs FFT max|diff| = %.3e\n", n, maxd);
            }
            /* self-check 2: recursion phi_n(xi) = sum_a 2^-a e(-xi 2^-a/3^n) phi_{n-1}(xi 2^-a mod 3^(n-1)) */
            if (n >= 3 && specPrev) {
                int64_t inv2 = (mod + 1) / 2; int64_t modp = P3[n - 1], Nfp = P3[n - 2];
                double maxd = 0;
                for (int t = 0; t < 12; t++) {
                    int64_t xi = (t == 0) ? ((xistar % mod) + mod) % mod : (1 + 3 * ((int64_t)(t * 7919 * 104729LL) % Nf)) % mod;
                    if (xi % 3 == 0) xi += 1;
                    double complex acc = 0; int64_t xa = xi; double wa = 1.0;
                    for (int a = 1; a <= 70; a++) {
                        xa = (xa * inv2) % mod; wa *= 0.5;
                        int64_t r = xa % modp; double complex ph;
                        if (r % 3 == 1) ph = specPrev[(r - 1) / 3 % Nfp];
                        else ph = conj(specPrev[((modp - r) - 1) / 3 % Nfp]);
                        acc += wa * cexp(-2.0 * M_PI * I * ((double)xa / (double)mod)) * ph;
                    }
                    double complex direct = (xi % 3 == 1) ? spec[(xi - 1) / 3] : conj(spec[((mod - xi) - 1) / 3]);
                    double d = cabs(acc - direct); if (d > maxd) maxd = d;
                }
                fprintf(stderr, "n=%d recursion-identity check (12 xi) max|diff| = %.3e\n", n, maxd);
            }
        }
        printf("%2d %10lld %.17g %.10f %.10f %.2e %.12e %lld %.10f  argmin_unit=%lld\n", n, (long long)L, mn, mn * (double)L,
               mx * (double)L, (double)(sum - 1.0L), Mn, (long long)xistar, -log(mn) / log(3.0), (long long)argu);
        fflush(stdout);
        free(Pprev); Pprev = P;
        free(specPrev); specPrev = spec;
    }
    return 0;
}
