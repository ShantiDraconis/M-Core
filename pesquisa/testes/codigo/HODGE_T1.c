/* HODGE T1 — censo de caracteres de Hodge (2,2) em Fermat X_m^4 (grau m em P^5).
 *
 * Caracter: multiconjunto a = {a_0..a_5}, a_i em {1..m-1}, sum a_i == 0 (mod m).
 * Hodge (2,2): para todo t em (Z/m)^*, sum <t a_i> = 3m  (|t a| = 3).
 * M_m(y): multiconjuntos c de comprimento 2y com sum <t c_i> = y m para todo t.
 * dec   : a = c + d com c,d em M_m  <=> a contem um par {b, m-b}   (c em M_m(1)).
 * qdec  : a + {b,-b} = c + d, c,d em M_m, c,d != a; modulo dec isso equivale a
 *         uma particao 3+3 de a com s = soma da tripla != 0 e (tripla, -s) em M_m(2).
 * tsplit: a se parte em duas triplas de soma 0 (mod m) -> vem de X^1 x X^1
 *         (estrutura indutiva de Shioda + Lefschetz (1,1) na superficie C x C').
 *         NAO faz parte de (P_m^4); e o "criterio (1)" de Jumagulov. Reportado a parte.
 * R_m   : orbitas sob (Z/m)^* de caracteres Hodge nem dec nem qdec (spec do frontier).
 * R'_m  : R_m menos tsplit.
 *
 * Uso: HODGE_T1 mmin mmax [maxreps]
 * Saida: uma linha "SUM" por m e linhas "REP" com representantes de R_m.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int m, nunits, units[256], nhalf, half[128];

static int gcd(int a, int b) { while (b) { int t = a % b; a = b; b = t; } return a; }

static int hodge_quad(int x0, int x1, int x2, int x3) {
    /* (x0..x3) em M_m(2)?  t=1 e t em half (t e -t complementares) */
    if (x0 + x1 + x2 + x3 != 2 * m) return 0;
    for (int j = 0; j < nhalf; j++) {
        int t = half[j];
        int s = (t * x0) % m + (t * x1) % m + (t * x2) % m + (t * x3) % m;
        if (s != 2 * m) return 0;
    }
    return 1;
}

static int cmpint(const void *p, const void *q) { return (*(const int *)p) - (*(const int *)q); }

/* representante canonico da orbita: min lexicografico de sort(t a) sobre todo t unidade */
static void canon(const int *a, int *best, int *orbsize) {
    int imgs[256][6];
    int nimg = 0;
    for (int j = 0; j < nunits; j++) {
        int t = units[j], b[6];
        for (int i = 0; i < 6; i++) b[i] = (t * a[i]) % m;
        qsort(b, 6, sizeof(int), cmpint);
        int dup = 0;
        for (int k = 0; k < nimg && !dup; k++) if (memcmp(imgs[k], b, sizeof b) == 0) dup = 1;
        if (!dup) { memcpy(imgs[nimg], b, sizeof b); nimg++; }
    }
    int bi = 0; /* comparacao lexicografica numerica feita a mao */
    for (int k = 1; k < nimg; k++) {
        for (int i = 0; i < 6; i++) {
            if (imgs[k][i] < imgs[bi][i]) { bi = k; break; }
            if (imgs[k][i] > imgs[bi][i]) break;
        }
    }
    memcpy(best, imgs[bi], 6 * sizeof(int));
    *orbsize = nimg;
}

static long long fact[7] = {1, 1, 2, 6, 24, 120, 720};

int main(int argc, char **argv) {
    int mmin = atoi(argv[1]), mmax = atoi(argv[2]);
    int maxreps = argc > 3 ? atoi(argv[3]) : 50;
    static const int tri[10][3] = {{0,1,2},{0,1,3},{0,1,4},{0,1,5},{0,2,3},{0,2,4},{0,2,5},{0,3,4},{0,3,5},{0,4,5}};
    for (m = mmin; m <= mmax; m++) {
        nunits = 0; nhalf = 0;
        for (int t = 1; t < m; t++) if (gcd(t, m) == 1) { units[nunits++] = t; if (t > 1 && 2 * t < m) half[nhalf++] = t; }
        long long dimH = 0, nms = 0, norb = 0;
        long long orb_dec = 0, orb_qdec = 0, orb_R = 0, orb_Rts = 0, orb_Rp = 0;
        long long dim_R = 0, dim_Rp = 0, ms_indec = 0, orb_indec = 0, orb_ts = 0;
        int nrep = 0;
        int a[6];
        for (a[0] = 1; 6 * a[0] <= 3 * m; a[0]++)
        for (a[1] = a[0]; a[0] + 5 * a[1] <= 3 * m; a[1]++)
        for (a[2] = a[1]; a[0] + a[1] + 4 * a[2] <= 3 * m; a[2]++)
        for (a[3] = a[2]; a[0] + a[1] + a[2] + 3 * a[3] <= 3 * m; a[3]++)
        for (a[4] = a[3]; a[0] + a[1] + a[2] + a[3] + 2 * a[4] <= 3 * m; a[4]++) {
            a[5] = 3 * m - (a[0] + a[1] + a[2] + a[3] + a[4]);
            if (a[5] < a[4] || a[5] > m - 1) continue;
            int ok = 1;
            for (int j = 0; j < nhalf && ok; j++) {
                int t = half[j], s = 0;
                for (int i = 0; i < 6; i++) s += (t * a[i]) % m;
                if (s != 3 * m) ok = 0;
            }
            if (!ok) continue;
            /* caracter de Hodge */
            nms++;
            long long mult = 720;
            { int i = 0; while (i < 6) { int j = i; while (j < 6 && a[j] == a[i]) j++; mult /= fact[j - i]; i = j; } }
            dimH += mult;
            int dec = 0, qdec = 0, ts = 0;
            for (int i = 0; i < 6 && !dec; i++) for (int j = i + 1; j < 6; j++) if (a[i] + a[j] == m) { dec = 1; break; }
            for (int k = 0; k < 10; k++) {
                int x = a[tri[k][0]], y = a[tri[k][1]], z = a[tri[k][2]];
                int s = (x + y + z) % m;
                if (s == 0) { ts = 1; continue; }
                if (!qdec && hodge_quad(x, y, z, m - s)) qdec = 1;
            }
            int canonrep[6], osz;
            canon(a, canonrep, &osz);
            int isrep = memcmp(canonrep, a, sizeof a) == 0;
            if (!dec) ms_indec++;
            if (isrep) {
                norb++;
                if (dec) orb_dec++;
                else { orb_indec++; if (qdec) orb_qdec++; }
                if (ts) orb_ts++;
            }
            if (!dec && !qdec) {
                dim_R += mult;
                if (!ts) dim_Rp += mult;
                if (isrep) {
                    orb_R++;
                    if (ts) orb_Rts++; else orb_Rp++;
                    if (nrep < maxreps) {
                        printf("REP m=%d a=(%d,%d,%d,%d,%d,%d) orbsize=%d tsplit=%d\n", m, a[0], a[1], a[2], a[3], a[4], a[5], osz, ts);
                        nrep++;
                    }
                }
            }
        }
        printf("SUM m=%d phi=%d dimHdgPrim=%lld multisets=%lld orbits=%lld orb_dec=%lld orb_indec=%lld orb_indec_qdec=%lld "
               "orb_tsplit_any=%lld R_orbits=%lld R_dim=%lld R_tsplit_orbits=%lld Rprime_orbits=%lld Rprime_dim=%lld\n",
               m, nunits, dimH, nms, norb, orb_dec, orb_indec, orb_qdec, orb_ts, orb_R, dim_R, orb_Rts, orb_Rp, dim_Rp);
        fflush(stdout);
    }
    return 0;
}
