/* BEAL T1: marca a cobertura de {3..200}^3 por padroes de divisibilidade e ranqueia assinaturas candidatas.
   uso: BEAL_T1_mark pats.txt cands.txt ncands level_out.bin rank_out.txt
   pats.txt: "cenario dx dy dz"; cands.txt: "id dx dy dz".
   level_out.bin: 198^3 bytes, menor cenario que cobre a celula (255 = descoberta). */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define LO 3
#define HI 200
#define W (HI - LO + 1)
#define NC (W * W * W)
#define IDX(x, y, z) ((((x) - LO) * W + ((y) - LO)) * W + ((z) - LO))

static unsigned char level[NC];
static unsigned char cov[NC];
static int32_t stamp[NC];

typedef struct { int id, dx, dy, dz; } Pat;

static int first(int d) { return ((LO + d - 1) / d) * d; }

static long count_cand(Pat *p, int np, int tag) {
    long c = 0;
    for (int k = 0; k < np; k++)
        for (int x = first(p[k].dx); x <= HI; x += p[k].dx)
            for (int y = first(p[k].dy); y <= HI; y += p[k].dy)
                for (int z = first(p[k].dz); z <= HI; z += p[k].dz) {
                    int i = IDX(x, y, z);
                    if (!cov[i] && stamp[i] != tag) { stamp[i] = tag; c++; }
                }
    return c;
}
static void apply_cand(Pat *p, int np) {
    for (int k = 0; k < np; k++)
        for (int x = first(p[k].dx); x <= HI; x += p[k].dx)
            for (int y = first(p[k].dy); y <= HI; y += p[k].dy)
                for (int z = first(p[k].dz); z <= HI; z += p[k].dz) cov[IDX(x, y, z)] = 1;
}

int main(int argc, char **argv) {
    if (argc < 6) { fprintf(stderr, "uso\n"); return 1; }
    memset(level, 255, sizeof level);
    FILE *f = fopen(argv[1], "r");
    int s, dx, dy, dz;
    while (fscanf(f, "%d %d %d %d", &s, &dx, &dy, &dz) == 4)
        for (int x = first(dx); x <= HI; x += dx)
            for (int y = first(dy); y <= HI; y += dy)
                for (int z = first(dz); z <= HI; z += dz) {
                    int i = IDX(x, y, z);
                    if (level[i] > s) level[i] = (unsigned char)s;
                }
    fclose(f);
    FILE *o = fopen(argv[4], "wb"); fwrite(level, 1, NC, o); fclose(o);
    long cnt[256] = {0};
    for (int i = 0; i < NC; i++) cnt[level[i]]++;
    long cum = 0;
    for (int sc = 0; sc < 16; sc++) { cum += cnt[sc]; printf("S%d cumulativo %ld (%.4f%%)\n", sc, cum, 100.0 * cum / NC); }
    printf("descobertas %ld total %d\n", cnt[255], NC);

    /* candidatas */
    int ncand = atoi(argv[3]);
    Pat *all = malloc(sizeof(Pat) * 200000); int na = 0;
    f = fopen(argv[2], "r");
    while (na < 200000 && fscanf(f, "%d %d %d %d", &all[na].id, &all[na].dx, &all[na].dy, &all[na].dz) == 4) na++;
    fclose(f);
    int *st = calloc(ncand + 1, sizeof(int));
    for (int k = na - 1; k >= 0; k--) st[all[k].id] = k;
    int *np = calloc(ncand, sizeof(int));
    for (int k = 0; k < na; k++) np[all[k].id]++;
    FILE *r = fopen(argv[5], "w");
    int bases[2] = {4, 6};
    for (int b = 0; b < 2; b++) {
        for (int i = 0; i < NC; i++) cov[i] = level[i] <= bases[b];
        memset(stamp, 0xff, sizeof stamp);
        for (int c = 0; c < ncand; c++) {
            long v = count_cand(all + st[c], np[c], c);
            fprintf(r, "raw S%d %d %ld\n", bases[b], c, v);
        }
    }
    /* guloso sobre S4: 25 escolhas sequenciais pelo ganho marginal */
    for (int i = 0; i < NC; i++) cov[i] = level[i] <= 4;
    int tag = 0;
    for (int it = 0; it < 25; it++) {
        long best = -1; int bc = -1;
        memset(stamp, 0xff, sizeof stamp); tag = 0;
        for (int c = 0; c < ncand; c++) {
            long v = count_cand(all + st[c], np[c], c);
            if (v > best) { best = v; bc = c; }
        }
        apply_cand(all + st[bc], np[bc]);
        fprintf(r, "greedy %d %d %ld\n", it + 1, bc, best);
        fflush(r);
    }
    fclose(r);
    return 0;
}
