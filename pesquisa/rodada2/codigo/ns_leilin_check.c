/* Referee numerico da melhoria da constante de Lei–Lin (wave2).
 *
 * u(x) = sum_k v_k e^{ik.x} em T^3=[0,2pi]^3, k em Z^3\0, k.v_k=0, v_{-k}=conj(v_k).
 * d/dt v_k = -nu|k|^2 v_k + W_k,  W_k = -i P_k G_k,  G_k = sum_{p+q=k} (k.v_p) v_q.
 * A_s = sum |k|^s |v_k|.  Cadeia verificada:
 *   Nder := sum_{k in S}|k|^-1 Re<v_k/|v_k|,W_k> + sum_{k notin S}|k|^-1|W_k|   (d+/dt A_{-1}, parte NL)
 *   N1   := sum_k |k|^-1 |W_k|
 *   N2   := sum_k |k|^-1 sum_{p+q=k} |k.v_p||v_q|          (passo 1)
 *   Nt   := sum_{p+q!=0} sin<(p+q,p) a_p a_q               (passo 2)
 *   Q/4  := (1/4) sum_{p,q} T(p,q) a_p a_q  (=Nt, passo 3) ;  T<=|p^-q^|+|p^+q^| (projecao radial)
 *   Bj/4 := (1/4) sum_{p,q} (|p^-q^|+|p^+q^|) a_p a_q <= (2/3) A_0^2  (Bjorck)
 *   A_0^2/sqrt2 (afirmacao) ; (2/3)A_0^2 (melhor) ; A_0^2 <= A_{-1}A_1.
 * Controles: energia sum Re<v_k,W_k> = 0, helicidade sum Re<i k x v_k, W_k> = 0, Nt = Q/4.
 *
 * Uso: ns_leilin_check rand  ntrials seed     (suportes aleatorios, varios tipos)
 *      ns_leilin_check shell R0 R1 seed       (cascas finas de raio R, amplitude uniforme)
 *      ns_leilin_check repl  R  iters seed    (maximiza a^T T a/(sum a)^2 por replicador na bola |k|<=R)
 *      ns_leilin_check pair                   (casos exatos: par ortogonal, 3 eixos)
 *      ns_leilin_check climb nclass M iters ntries seed (subida de encosta em Nder/(A-1 A1))
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <complex.h>

typedef double complex cplx;

static unsigned long long rng = 88172645463325252ULL;
static double urand(void) { rng ^= rng << 13; rng ^= rng >> 7; rng ^= rng << 17; return (rng >> 11) * (1.0 / 9007199254740992.0); }
static double grand(void) { double u = urand() + 1e-300, v = urand(); return sqrt(-2 * log(u)) * cos(2 * M_PI * v); }

#define MAXM 8192
static int nm;                 /* numero de modos (com sinal) */
static int K[MAXM][3];
static cplx V[MAXM][3];
static int Mbox;               /* |k_i| <= Mbox */

static int ispos(const int *k) { if (k[0]) return k[0] > 0; if (k[1]) return k[1] > 0; return k[2] > 0; }
static double nrm(const int *k) { return sqrt((double)k[0]*k[0] + (double)k[1]*k[1] + (double)k[2]*k[2]); }

/* adiciona o par (k,-k) com v ortogonal a k (projeta) */
static void addmode(const int *k, cplx v[3]) {
    double kk = (double)k[0]*k[0] + (double)k[1]*k[1] + (double)k[2]*k[2];
    cplx kv = k[0]*v[0] + k[1]*v[1] + k[2]*v[2];
    int i, j;
    for (i = 0; i < 3; i++) v[i] -= kv * k[i] / kk;
    for (j = 0; j < 2; j++) {
        int s = j ? -1 : 1;
        for (i = 0; i < 3; i++) { K[nm][i] = s * k[i]; V[nm][i] = j ? conj(v[i]) : v[i]; }
        nm++;
    }
}

typedef struct { double Nder, N1, N2, Nt, Q4, Bj4, A_1, A0, A1, en, hel, enscale; } Res;

static int L, OFF;
static cplx (*G)[3];
static int *inS;

static int bidx(int a, int b, int c) { return ((a + OFF) * L + (b + OFF)) * L + (c + OFF); }

static Res evaluate(void) {
    Res r; memset(&r, 0, sizeof r);
    int i, j, d;
    L = 4 * Mbox + 1; OFF = 2 * Mbox;
    size_t NB = (size_t)L * L * L;
    G = calloc(NB, sizeof *G); inS = malloc(NB * sizeof(int));
    for (size_t t = 0; t < NB; t++) inS[t] = -1;
    double *a = malloc(nm * sizeof(double)), *kn = malloc(nm * sizeof(double));
    for (i = 0; i < nm; i++) {
        double s = 0; for (d = 0; d < 3; d++) s += creal(V[i][d] * conj(V[i][d]));
        a[i] = sqrt(s); kn[i] = nrm(K[i]);
        r.A_1 += a[i] / kn[i]; r.A0 += a[i]; r.A1 += a[i] * kn[i];
        inS[bidx(K[i][0], K[i][1], K[i][2])] = i;
    }
    for (i = 0; i < nm; i++) for (j = 0; j < nm; j++) {
        int k[3] = {K[i][0] + K[j][0], K[i][1] + K[j][1], K[i][2] + K[j][2]};
        double cr[3] = {(double)K[i][1]*K[j][2] - (double)K[i][2]*K[j][1],
                        (double)K[i][2]*K[j][0] - (double)K[i][0]*K[j][2],
                        (double)K[i][0]*K[j][1] - (double)K[i][1]*K[j][0]};
        double pxq = sqrt(cr[0]*cr[0] + cr[1]*cr[1] + cr[2]*cr[2]);
        /* T(p,q) e kernel de Bjorck (para todos os pares, T=0 se p=+-q) */
        if (pxq > 0) {
            int km[3] = {K[i][0] - K[j][0], K[i][1] - K[j][1], K[i][2] - K[j][2]};
            double T = pxq * (kn[i] + kn[j]) / (kn[i] * kn[j]) * (1.0 / nrm(k) + 1.0 / nrm(km));
            r.Q4 += 0.25 * T * a[i] * a[j];
        }
        { double dot = 0; for (d = 0; d < 3; d++) dot += K[i][d] * K[j][d];
          double c = dot / (kn[i] * kn[j]); if (c > 1) c = 1; if (c < -1) c = -1;
          double bj = sqrt(2 - 2 * c) + sqrt(2 + 2 * c);
          if (i == j || (K[i][0] == -K[j][0] && K[i][1] == -K[j][1] && K[i][2] == -K[j][2])) bj = 2; /* diagonal: |x-x|+|x+x| = 2 */
          r.Bj4 += 0.25 * bj * a[i] * a[j]; }
        if (k[0] == 0 && k[1] == 0 && k[2] == 0) continue;
        double kk = nrm(k);
        cplx kv = k[0]*V[i][0] + k[1]*V[i][1] + k[2]*V[i][2];
        int b = bidx(k[0], k[1], k[2]);
        for (d = 0; d < 3; d++) G[b][d] += kv * V[j][d];
        r.N2 += cabs(kv) * a[j] / kk;
        r.Nt += pxq / (kn[i] * kk) * a[i] * a[j];
    }
    /* W = -i P_k G */
    int x, y, z;
    for (x = -2 * Mbox; x <= 2 * Mbox; x++) for (y = -2 * Mbox; y <= 2 * Mbox; y++) for (z = -2 * Mbox; z <= 2 * Mbox; z++) {
        if (!x && !y && !z) continue;
        int b = bidx(x, y, z); int k[3] = {x, y, z};
        double kk2 = (double)x*x + (double)y*y + (double)z*z, kk = sqrt(kk2);
        cplx kg = x*G[b][0] + y*G[b][1] + z*G[b][2];
        cplx W[3]; double w2 = 0;
        for (d = 0; d < 3; d++) { W[d] = -I * (G[b][d] - kg * k[d] / kk2); w2 += creal(W[d] * conj(W[d])); }
        if (w2 == 0) continue;
        r.N1 += sqrt(w2) / kk;
        int m = inS[b];
        if (m >= 0) {
            double am = a[m]; cplx ip = 0, ih = 0;
            for (d = 0; d < 3; d++) ip += conj(V[m][d]) * W[d];
            /* vorticidade i k x v */
            cplx om[3] = {I * (k[1]*V[m][2] - k[2]*V[m][1]), I * (k[2]*V[m][0] - k[0]*V[m][2]), I * (k[0]*V[m][1] - k[1]*V[m][0])};
            for (d = 0; d < 3; d++) ih += conj(om[d]) * W[d];
            r.en += creal(ip); r.hel += creal(ih);
            r.enscale += am * sqrt(w2) * (1 + kk);
            if (am > 0) r.Nder += creal(ip) / am / kk; else r.Nder += sqrt(w2) / kk;
        } else r.Nder += sqrt(w2) / kk;
    }
    free(G); free(inS); free(a); free(kn);
    return r;
}

static void randvec(cplx v[3]) { for (int d = 0; d < 3; d++) v[d] = grand() + I * grand(); }

static int have(const int *k) {
    for (int i = 0; i < nm; i++) if (K[i][0] == k[0] && K[i][1] == k[1] && K[i][2] == k[2]) return 1;
    return 0;
}

static void report(const char *tag, Res r, double *mx) {
    double A02 = r.A0 * r.A0;
    double q[7] = { r.Nder / r.N1, r.N1 / r.N2, r.N2 / r.Nt, r.Nt / A02, r.Bj4 / A02, A02 / (r.A_1 * r.A1), r.Nder / (r.A_1 * r.A1) };
    if (tag) printf("%-10s nm=%5d Nder/N1=%.4f N1/N2=%.4f N2/Nt=%.4f Nt/A0^2=%.5f Bj/A0^2=%.5f A0^2/(A-1A1)=%.4f Nder/(A-1A1)=%.5f |Nt-Q/4|=%.1e en=%.1e hel=%.1e\n",
                    tag, nm, q[0], q[1], q[2], q[3], q[4], q[5], q[6], fabs(r.Nt - r.Q4) / r.Nt, fabs(r.en) / (r.enscale + 1e-300), fabs(r.hel) / (r.enscale + 1e-300));
    if (mx) for (int t = 0; t < 7; t++) if (q[t] > mx[t]) mx[t] = q[t];
}

int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "uso\n"); return 1; }
    if (!strcmp(argv[1], "pair")) {
        /* par ortogonal: p=e1 (v ~ e2 + i e3), q=e2 ... varre polarizacoes */
        int p[3] = {1, 0, 0}, q[3] = {0, 1, 0}; cplx v[3];
        nm = 0; Mbox = 1; v[0] = 0; v[1] = 1; v[2] = 0; addmode(p, v); v[0] = 1; v[1] = 0; v[2] = 0; addmode(q, v);
        report("par(e2,e1)", evaluate(), NULL);
        nm = 0; v[0] = 0; v[1] = 0; v[2] = 1; addmode(p, v); v[0] = 0; v[1] = 0; v[2] = 1; addmode(q, v);
        report("par(e3,e3)", evaluate(), NULL);
        nm = 0; v[0] = 0; v[1] = 1; v[2] = I; addmode(p, v); v[0] = 1; v[1] = 0; v[2] = I; addmode(q, v);
        report("par(circ)", evaluate(), NULL);
        int r3[3] = {0, 0, 1};
        nm = 0; v[0] = 0; v[1] = 1; v[2] = 0; addmode(p, v); v[0] = 0; v[1] = 0; v[2] = 1; addmode(q, v); v[0] = 1; v[1] = 0; v[2] = 0; addmode(r3, v);
        report("3eixos", evaluate(), NULL);
        return 0;
    }
    if (!strcmp(argv[1], "rand")) {
        int ntr = atoi(argv[2]); rng ^= (unsigned long long)atoll(argv[3]) * 0x9E3779B97F4A7C15ULL;
        double mx[7] = {-1e9, -1e9, -1e9, -1e9, -1e9, -1e9, -1e9};
        for (int t = 0; t < ntr; t++) {
            int type = t % 4; nm = 0;
            int M = 2 + (int)(urand() * 9);           /* caixa 2..10 */
            int target = 2 + (int)(urand() * (type == 3 ? 2000 : 1200));
            Mbox = M;
            int tries = 0;
            while (nm < 2 * target && tries < 200000) {
                tries++;
                int k[3] = {(int)floor(urand() * (2 * M + 1)) - M, (int)floor(urand() * (2 * M + 1)) - M, (int)floor(urand() * (2 * M + 1)) - M};
                if (!k[0] && !k[1] && !k[2]) continue;
                if (!ispos(k)) { k[0] = -k[0]; k[1] = -k[1]; k[2] = -k[2]; }
                double kn = nrm(k);
                if (type == 1 && fabs(kn - 0.7 * M) > 0.6) continue;            /* casca fina */
                if (have(k)) continue;
                cplx v[3]; randvec(v);
                double amp = 1;
                if (type == 0) amp = exp(3 * grand());                         /* amplitudes log-normais */
                if (type == 2) amp = pow(kn, -2.0 - 2 * urand());               /* lei de potencia */
                if (type == 3) { v[0] = grand(); v[1] = grand(); v[2] = grand(); } /* polarizacao linear real */
                for (int d = 0; d < 3; d++) v[d] *= amp;
                addmode(k, v);
            }
            Res r = evaluate();
            char tag[32]; snprintf(tag, sizeof tag, "t%d/M%d", type, M);
            report(t < 8 ? tag : NULL, r, mx);
        }
        printf("MAX sobre %d campos: Nder/N1=%.5f N1/N2=%.5f N2/Nt=%.5f Nt/A0^2=%.5f Bj/A0^2=%.5f A0^2/(A-1A1)=%.5f Nder/(A-1A1)=%.5f\n",
               ntr, mx[0], mx[1], mx[2], mx[3], mx[4], mx[5], mx[6]);
        printf("referencias: 1/sqrt2=%.5f  2/3=%.5f\n", 1 / sqrt(2.0), 2.0 / 3);
        return 0;
    }
    if (!strcmp(argv[1], "shell")) {
        int R0 = atoi(argv[2]), R1 = atoi(argv[3]); rng ^= (unsigned long long)atoll(argv[4]);
        for (int R = R0; R <= R1; R++) {
            nm = 0; Mbox = R + 1;
            for (int x = -R - 1; x <= R + 1; x++) for (int y = -R - 1; y <= R + 1; y++) for (int z = -R - 1; z <= R + 1; z++) {
                int k[3] = {x, y, z};
                if ((!x && !y && !z) || !ispos(k)) continue;
                double kn = nrm(k); if (fabs(kn - R) > 0.5) continue;
                cplx v[3]; randvec(v);
                /* normaliza |v|=1 apos projecao */
                double kk = kn * kn; cplx kv = x*v[0] + y*v[1] + z*v[2]; double s = 0;
                for (int d = 0; d < 3; d++) { v[d] -= kv * k[d] / kk; s += creal(v[d] * conj(v[d])); }
                for (int d = 0; d < 3; d++) v[d] /= sqrt(s);
                addmode(k, v);
            }
            char tag[32]; snprintf(tag, sizeof tag, "casca R=%d", R);
            report(tag, evaluate(), NULL);
        }
        return 0;
    }
    if (!strcmp(argv[1], "repl")) {
        /* maximiza a^T T a / (sum a)^2 (= 4 Nt / A0^2) sobre a>=0 na bola |k|<=R, replicador (Baum-Eagon) */
        int R = atoi(argv[2]), iters = atoi(argv[3]); rng ^= (unsigned long long)atoll(argv[4]);
        static int P[MAXM][3]; int n = 0;
        for (int x = -R; x <= R; x++) for (int y = -R; y <= R; y++) for (int z = -R; z <= R; z++) {
            if ((!x && !y && !z) || x*x + y*y + z*z > R*R) continue;
            if (n >= MAXM) break;
            P[n][0] = x; P[n][1] = y; P[n][2] = z; n++;
        }
        float *T = malloc((size_t)n * n * sizeof(float));
        double *a = malloc(n * sizeof(double)), *Ta = malloc(n * sizeof(double));
        for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) {
            double cr[3] = {(double)P[i][1]*P[j][2] - (double)P[i][2]*P[j][1], (double)P[i][2]*P[j][0] - (double)P[i][0]*P[j][2], (double)P[i][0]*P[j][1] - (double)P[i][1]*P[j][0]};
            double pxq = sqrt(cr[0]*cr[0] + cr[1]*cr[1] + cr[2]*cr[2]);
            double t = 0;
            if (pxq > 0) {
                int s[3] = {P[i][0]+P[j][0], P[i][1]+P[j][1], P[i][2]+P[j][2]}, m[3] = {P[i][0]-P[j][0], P[i][1]-P[j][1], P[i][2]-P[j][2]};
                double pi = nrm(P[i]), pj = nrm(P[j]);
                t = pxq * (pi + pj) / (pi * pj) * (1 / nrm(s) + 1 / nrm(m));
            }
            T[(size_t)i * n + j] = (float)t;
        }
        double best = 0;
        for (int start = 0; start < 3; start++) {
            for (int i = 0; i < n; i++) a[i] = 0.5 + urand();
            /* simetriza a_{-p}=a_p: P e simetrico, o indice de -p e n-1-i pela ordem do laco */
            for (int i = 0; i < n; i++) { double m = 0.5 * (a[i] + a[n - 1 - i]); a[i] = a[n - 1 - i] = m; }
            double val = 0;
            for (int it = 0; it < iters; it++) {
                double s = 0, q = 0;
                for (int i = 0; i < n; i++) s += a[i];
                for (int i = 0; i < n; i++) a[i] /= s;
                for (int i = 0; i < n; i++) { double acc = 0; const float *row = T + (size_t)i * n; for (int j = 0; j < n; j++) acc += row[j] * a[j]; Ta[i] = acc; q += a[i] * acc; }
                val = q;
                for (int i = 0; i < n; i++) a[i] *= Ta[i] / q;
            }
            /* estrutura: massa por casca */
            double rmin = 1e9, rmax = 0, mass = 0;
            for (int i = 0; i < n; i++) if (a[i] > 1e-4 / n) { double kn = nrm(P[i]); if (kn < rmin) rmin = kn; if (kn > rmax) rmax = kn; mass += a[i]; }
            printf("repl R=%d n=%d inicio %d: max a^T T a/(sum a)^2 = %.6f (4*2/3=%.6f, 2sqrt2=%.6f) suporte |k| em [%.2f,%.2f]\n",
                   R, n, start, val, 8.0 / 3, 2 * sqrt(2.0), rmin, rmax);
            if (val > best) best = val;
        }
        printf("repl R=%d: melhor Nt/A0^2 = %.6f  (2/3=%.6f, 1/sqrt2=%.6f)\n", R, best / 4, 2.0 / 3, 1 / sqrt(2.0));
        return 0;
    }
    if (!strcmp(argv[1], "climb")) {
        /* subida de encosta em rho^{-1} = Nder/(A_{-1}A_1) com suportes pequenos aleatorios */
        int ncl = atoi(argv[2]), M = atoi(argv[3]), iters = atoi(argv[4]), ntries = atoi(argv[5]);
        rng ^= (unsigned long long)atoll(argv[6]) * 0x9E3779B97F4A7C15ULL;
        double gbest = 0;
        for (int tr = 0; tr < ntries; tr++) {
            static int KK[64][3]; static cplx VV[64][3]; int nc = 0;
            while (nc < ncl) {
                int k[3] = {(int)floor(urand() * (2 * M + 1)) - M, (int)floor(urand() * (2 * M + 1)) - M, (int)floor(urand() * (2 * M + 1)) - M};
                if ((!k[0] && !k[1] && !k[2])) continue;
                if (!ispos(k)) { k[0] = -k[0]; k[1] = -k[1]; k[2] = -k[2]; }
                int dup = 0; for (int c = 0; c < nc; c++) if (KK[c][0] == k[0] && KK[c][1] == k[1] && KK[c][2] == k[2]) dup = 1;
                if (dup) continue;
                memcpy(KK[nc], k, sizeof k); randvec(VV[nc]); nc++;
            }
            Mbox = M;
            nm = 0; for (int c = 0; c < nc; c++) { cplx v[3]; memcpy(v, VV[c], sizeof v); addmode(KK[c], v); }
            Res r = evaluate(); double cur = r.Nder / (r.A_1 * r.A1); double step = 0.3;
            for (int it = 0; it < iters; it++) {
                static cplx save[64][3]; memcpy(save, VV, sizeof(cplx) * 3 * nc);
                int c = (int)(urand() * nc);
                for (int d = 0; d < 3; d++) VV[c][d] += step * (grand() + I * grand()) * (sqrt(creal(VV[c][0]*conj(VV[c][0]) + VV[c][1]*conj(VV[c][1]) + VV[c][2]*conj(VV[c][2]))) + 0.05);
                nm = 0; for (int cc = 0; cc < nc; cc++) { cplx v[3]; memcpy(v, VV[cc], sizeof v); addmode(KK[cc], v); memcpy(VV[cc], v, sizeof v); }
                r = evaluate(); double val = r.Nder / (r.A_1 * r.A1);
                if (val > cur) cur = val; else { memcpy(VV, save, sizeof(cplx) * 3 * nc); step *= 0.999; }
                if (step < 0.01) step = 0.3;
            }
            if (cur > gbest) gbest = cur;
        }
        printf("climb ncl=%d M=%d: max Nder/(A-1A1) = %.5f  => rho_min <= %.4f  (limiar do metodo <= %.4f nu)\n", ncl, M, gbest, 1 / gbest, 1 / gbest);
        return 0;
    }
    return 1;
}
