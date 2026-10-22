/* Control B for COLLATZ T1: truncated direct enumeration of Syrac(Z/3^n) = sum_k 3^(k-1) 2^-(a1+..+ak) mod 3^n,
 * a_i ~ Geom(1/2) on {1,2,...}, all tuples with a_i <= A. Compares with the dump of the recursion algorithm.
 * Usage: brute n A dumpfile
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>

static int n, A; static int64_t mod, inv2; static double *law; static int64_t p3[20];
static int64_t ip[4096]; /* inv2^s mod 3^n for s up to n*A */

static void rec(int k, int S, int64_t X, double pr) {
    if (k > n) { law[X] += pr; return; }
    for (int a = 1; a <= A; a++) {
        int S2 = S + a;
        rec(k + 1, S2, (X + p3[k - 1] * ip[S2]) % mod, pr * ldexp(1.0, -a));
    }
}

int main(int argc, char **argv) {
    n = atoi(argv[1]); A = atoi(argv[2]);
    p3[0] = 1; for (int i = 1; i < 20; i++) p3[i] = p3[i - 1] * 3;
    mod = p3[n]; inv2 = (mod + 1) / 2;
    ip[0] = 1; for (int s = 1; s < 4096; s++) ip[s] = ip[s - 1] * inv2 % mod;
    law = calloc(mod, sizeof(double));
    rec(1, 0, 0, 1.0);
    double missing = 1.0 - pow(1.0 - ldexp(1.0, -A), n);
    FILE *f = fopen(argv[3], "r"); long long x; double p; double maxdiff = 0, maxneg = 0; int cnt = 0;
    double minb = 2;
    while (fscanf(f, "%lld %lf", &x, &p) == 2) {
        double d = p - law[x]; if (fabs(d) > maxdiff) maxdiff = fabs(d); if (-d > maxneg) maxneg = -d; cnt++;
        if (law[x] < minb) minb = law[x];
    }
    fclose(f);
    double tot = 0; int nz = 0; for (int64_t i = 0; i < mod; i++) { tot += law[i]; if (law[i] > 0 && i % 3 == 0) nz++; }
    printf("n=%d A=%d units=%d brute_mass=%.15f missing_bound=%.3e max|alg-brute|=%.3e max(brute-alg)=%.3e min_brute=%.15g mass_on_3Z=%d\n",
           n, A, cnt, tot, missing, maxdiff, maxneg, minb, nz);
    return 0;
}
