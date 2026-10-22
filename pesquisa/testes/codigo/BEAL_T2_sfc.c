/* BEAL T2: busca de contraexemplos para a "Strong Fermat-Catalan" (Mihailescu, arXiv 2509.18275):
   F_p(x,y) = (x^p + y^p)/(x + y) = p^e z^q,  e = v_p(F) in {0,1}, z >= 2, q primo.
   modos:
     box p N       : pares coprimos 2 <= x <= N, -x < y < x, y != 0
     slice p X     : y = -1 (Nagell-Ljunggren) e y = 1 - x, 2 <= x <= X
   Saida: cada acerto "HIT p x y e q z" (q=2 e q=p marcados), contagens por q, e v_p(F) >= 2.
   Aritmetica exata em __int128; a raiz q-esima e estimada em ponto flutuante e conferida exatamente (z-1,z,z+1). */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

typedef unsigned __int128 u128;
typedef __int128 i128;

static const int QS[] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127};
#define NQ (int)(sizeof QS / sizeof QS[0])


static void u128str(u128 v, char *buf) {
    char t[64]; int n = 0;
    if (v == 0) { strcpy(buf, "0"); return; }
    while (v) { t[n++] = '0' + (int)(v % 10); v /= 10; }
    for (int i = 0; i < n; i++) buf[i] = t[n - 1 - i];
    buf[n] = 0;
}

static long hits[128], hits_e1[128], vp2 = 0, npairs = 0;

/* compara z^q com G: -1 (<), 0 (=), 1 (>, inclusive overflow) */
static int cmp_pow(uint64_t z, int q, u128 G) {
    u128 r = 1, b = z;
    for (int i = 0; i < q; i++) {
        u128 t;
        if (__builtin_mul_overflow(r, b, &t)) return 1;
        r = t;
        if (r > G) return 1;
    }
    return r == G ? 0 : -1;
}
/* raiz q-esima: estimativa em ponto flutuante (double se F < 2^100, senao long double), depois
   ajuste inteiro exato ate z = floor(F^(1/q)); devolve z se z^q == F, senao 0 */
static uint64_t qroot(u128 F, int q, long double lg, int small) {
    long double zf = small ? (long double)exp((double)lg / q) : expl(lg / q);
    uint64_t z0 = (uint64_t)(zf + 0.5L);
    if (z0 < 1) z0 = 1;
    while (z0 > 1 && cmp_pow(z0, q, F) > 0) z0--;
    while (cmp_pow(z0 + 1, q, F) <= 0) z0++;
    return (z0 >= 2 && cmp_pow(z0, q, F) == 0) ? z0 : 0;
}
static long double lgof(u128 F, int *small) {
    *small = (F >> 100) == 0;
    return *small ? (long double)log((double)F) : logl((long double)F);
}

/* testa G = F/p^e; usa long double se G for grande */
static void test(int p, long x, long y, i128 Fs) {
    u128 F = (u128)Fs;
    int e = 0;
    while (F % (u128)p == 0) { F /= (u128)p; e++; }
    if (e >= 2) {
        vp2++;
        if (vp2 <= 20) printf("VP2 p=%d x=%ld y=%ld e=%d\n", p, x, y, e);
    }
    if (F < 4) return;
    int small;
    long double lg = lgof(F, &small);
    for (int k = 0; k < NQ; k++) {
        int q = QS[k];
        if ((long double)q * 0.6931471805599453L > lg + 1e-9L) break; /* z >= 2 impossivel */
        uint64_t z = qroot(F, q, lg, small);
        {
            if (z) {
                char b[64]; u128str((u128)Fs, b);
                hits[q]++;
                if (e) hits_e1[q]++;
                if (hits[q] <= 40 || (q != 2 && q != p))
                    printf("HIT p=%d x=%ld y=%ld F=%s e=%d q=%d z=%llu%s\n", p, x, y, b, e, q,
                           (unsigned long long)z, q == 2 ? " [q=2]" : (q == p ? " [q=p]" : (p == 3 ? " [p=3 controle]" : " ***CONTRAEXEMPLO***")));
                /* sem break: F = w^6 conta para q=2 e q=3 */
            }
        }
    }
}

static i128 Fp(int p, long x, long y) {
    /* F = sum_{i=0}^{p-1} x^{p-1-i} (-y)^i */
    i128 t = -(i128)y, acc = 0, X = x;
    i128 tp = 1;
    i128 xp[32]; xp[0] = 1;
    for (int i = 1; i < p; i++) xp[i] = xp[i - 1] * X;
    for (int i = 0; i < p; i++) { acc += xp[p - 1 - i] * tp; tp *= t; }
    return acc;
}

static long g(long a, long b) { if (a < 0) a = -a; if (b < 0) b = -b; while (b) { long t = a % b; a = b; b = t; } return a; }

int main(int argc, char **argv) {
    long ntest = 0;
    /* autoteste: potencias sinteticas tem de ser achadas; vizinhas nao */
    for (int k = 0; k < NQ; k++) {
        int q = QS[k];
        for (uint64_t z = 2; z < 4000000000000000000ULL; z = z * 3 + 1) {
            u128 G = 1; int ok = 1;
            for (int i = 0; i < q; i++) { u128 t; if (__builtin_mul_overflow(G, (u128)z, &t)) { ok = 0; break; } G = t; }
            if (!ok || G >> 126) break;
            int sm; long double lg = lgof(G, &sm);
            uint64_t z0 = qroot(G, q, lg, sm);
            int found = (z0 == z);
            if (!found) { printf("AUTOTESTE FALHOU q=%d z=%llu small=%d\n", q, (unsigned long long)z, sm); return 2; }
            { int s1; long double l1 = lgof(G + 1, &s1); if (qroot(G + 1, q, l1, s1)) { printf("AUTOTESTE falso positivo\n"); return 2; } }
            ntest++;
        }
    }
    printf("autoteste ok (%ld potencias sinteticas, caminhos double e long double)\n", ntest);
    if (argc < 4) return 0;
    int p = atoi(argv[2]);
    long N = atol(argv[3]);
    if (!strcmp(argv[1], "box")) {
        for (long x = 2; x <= N; x++)
            for (long y = -x + 1; y < x; y++) {
                if (y == 0 || g(x, y) != 1) continue;
                npairs++;
                test(p, x, y, Fp(p, x, y));
            }
    } else {
        for (long x = 2; x <= N; x++) {
            npairs += 2;
            test(p, x, -1, Fp(p, x, -1));
            if (x >= 3) test(p, x, 1 - x, Fp(p, x, 1 - x));
        }
    }
    printf("RESUMO modo=%s p=%d N=%ld pares=%ld vp>=2:%ld\n", argv[1], p, N, npairs, vp2);
    for (int k = 0; k < NQ; k++)
        if (hits[QS[k]]) printf("  q=%d acertos=%ld (com e=1: %ld)\n", QS[k], hits[QS[k]], hits_e1[QS[k]]);
    return 0;
}
