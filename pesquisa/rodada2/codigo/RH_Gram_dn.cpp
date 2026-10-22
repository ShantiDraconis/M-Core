// RH_Gram_dn.cpp — D_N de Báez-Duarte por Cholesky incremental (uma linha por N), em
// double / long double / double-double (dd) / __float128 (q).
//   G_{ij} = <rho_i, rho_j> pela fórmula de Vasyunin (verificada em RH_Gram_verify.py contra integração
//   direta, |dif| <= 4e-44):  com d = gcd(i,j), h = i/d, k = j/d,
//   G_{ij} = (1/d) [ (log 2pi - g)/2 (1/h + 1/k) + (k-h)/(2hk) log(h/k) - pi/(2hk) (V(h,k) + V(k,h)) ],
//   V(h,k) = sum_{m=1}^{k-1} {mh/k} cot(pi m/k) = (1/k) sum_{m<k/2} (2 (mh mod k) - k) cot(pi m/k).
//   b_k = (log k + 1 - g)/k.  D_N = D_{N-1} - y_N^2, y = L^{-1} b,  G_N = L L^T.
// Uso: RH_Gram_dn <d|ld|dd|q> Nmax out.tsv [coef.tsv N1,N2,...]
// Compilar: g++ -O2 -mfma -ffp-contract=off -fopenmp -o RH_Gram_dn RH_Gram_dn.cpp -lquadmath
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <ctime>
extern "C" {
#include <quadmath.h>
}
typedef __float128 q;
static const q PIQ = M_PIq;
static const q GAMQ = 0.577215664901532860606512090082402431042159335939923598805767Q;

// ---------------- double-double ----------------
struct dd { double hi, lo; };
static inline dd two_sum(double a, double b) { double s = a + b, bb = s - a; return {s, (a - (s - bb)) + (b - bb)}; }
static inline dd qts(double a, double b) { double s = a + b; return {s, b - (s - a)}; }
static inline dd operator+(dd a, dd b) {
  dd s = two_sum(a.hi, b.hi), t = two_sum(a.lo, b.lo);
  s.lo += t.hi; s = qts(s.hi, s.lo); s.lo += t.lo; return qts(s.hi, s.lo);
}
static inline dd operator-(dd a) { return {-a.hi, -a.lo}; }
static inline dd operator-(dd a, dd b) { return a + (-b); }
static inline dd operator*(dd a, dd b) {
  double p = a.hi * b.hi, e = std::fma(a.hi, b.hi, -p);
  e += a.hi * b.lo + a.lo * b.hi; return qts(p, e);
}
static inline q toq(dd a) { return (q)a.hi + (q)a.lo; }
static inline q toq(double a) { return (q)a; }
static inline q toq(long double a) { return (q)a; }
static inline q toq(q a) { return a; }
template <class T> T fromq(q x);
template <> dd fromq<dd>(q x) { double h = (double)x; return {h, (double)(x - (q)h)}; }
template <> double fromq<double>(q x) { return (double)x; }
template <> long double fromq<long double>(q x) { return (long double)x; }
template <> q fromq<q>(q x) { return x; }
static inline dd operator/(dd a, dd b) { return fromq<dd>(toq(a) / toq(b)); }
static inline dd sqrtT(dd a) { return fromq<dd>(sqrtq(toq(a))); }
static inline double sqrtT(double a) { return std::sqrt(a); }
static inline long double sqrtT(long double a) { return sqrtl(a); }
static inline q sqrtT(q a) { return sqrtq(a); }

// produto interno de comprimento n
template <class T> static T dot(const T* a, const T* b, long n) {
  T s = fromq<T>(0); for (long i = 0; i < n; i++) s = s + a[i] * b[i]; return s;
}
// dd: Dot2 (Ogita–Rump–Oishi) com produtos dd (termo lo*lo desprezado, ~1e-48 relativo)
template <> dd dot<dd>(const dd* a, const dd* b, long n) {
  double sh = 0, sl = 0;
  for (long i = 0; i < n; i++) {
    double p = a[i].hi * b[i].hi, pe = std::fma(a[i].hi, b[i].hi, -p);
    double cr = a[i].hi * b[i].lo + a[i].lo * b[i].hi;
    double t = sh + p, bb = t - sh, se = (sh - (t - bb)) + (p - bb);
    sh = t; sl += se + pe + cr;
  }
  dd r = two_sum(sh, sl); return r;
}
// soma ponderada com pesos inteiros w[i] (exatos em double)
template <class T> static T wdot(const int* w, const T* c, long n) {
  T s = (T)0; for (long i = 0; i < n; i++) s = s + (T)w[i] * c[i]; return s;
}
template <> dd wdot<dd>(const int* w, const dd* c, long n) {
  double sh = 0, sl = 0;
  for (long i = 0; i < n; i++) {
    double wi = (double)w[i];
    double p = wi * c[i].hi, pe = std::fma(wi, c[i].hi, -p), cr = wi * c[i].lo;
    double t = sh + p, bb = t - sh, se = (sh - (t - bb)) + (p - bb);
    sh = t; sl += se + pe + cr;
  }
  return two_sum(sh, sl);
}

static inline long gcdl(long a, long b) { while (b) { long t = a % b; a = b; b = t; } return a; }
static inline long tri(long k, long h) { return k * (k - 1) / 2 + (h - 1); } // 1<=h<k

template <class T> int run(long N, const char* out, const char* coef, std::vector<long> cN) {
  clock_t t0 = clock();
  std::vector<q> logk(N + 1);
  for (long k = 1; k <= N; k++) logk[k] = logq((q)k);
  const q A = logq(2 * PIQ) - GAMQ;
  // tabela V(h,k), depois G0(h,k) no mesmo lugar
  std::vector<T> V((size_t)tri(N + 1, 1) + 1);
#pragma omp parallel for schedule(dynamic, 8)
  for (long k = N; k >= 2; k--) {
    std::vector<T> cot(k / 2 + 2);
    std::vector<int> w(k / 2 + 2);
    long M = (k - 1) / 2;
    for (long m = 1; m <= M; m++) { q x = PIQ * (q)m / (q)k; cot[m - 1] = fromq<T>(cosq(x) / sinq(x)); }
    for (long h = 1; h < k; h++) {
      if (gcdl(h, k) != 1) { V[tri(k, h)] = fromq<T>(0); continue; }
      long r = 0;
      for (long m = 1; m <= M; m++) { r += h; if (r >= k) r -= k; w[m - 1] = (int)(2 * r - k); }
      V[tri(k, h)] = fromq<T>(toq(wdot<T>(w.data(), cot.data(), M)) / (q)k);
    }
  }
  fprintf(stderr, "[%s] V pronto: %.1fs\n", out, (double)(clock() - t0) / CLOCKS_PER_SEC);
  for (long k = N; k >= 2; k--)
    for (long h = 1; h < k; h++) {
      if (gcdl(h, k) != 1) continue;
      q vhk = toq(V[tri(k, h)]);
      q vkh = (h == 1) ? (q)0 : toq(V[tri(h, k % h)]);
      q hk = (q)h * (q)k;
      q g = A / 2 * (1 / (q)h + 1 / (q)k) + (q)(k - h) / (2 * hk) * (logk[h] - logk[k]) - PIQ / (2 * hk) * (vhk + vkh);
      V[tri(k, h)] = fromq<T>(g);
    }
  auto G = [&](long i, long j) -> T {  // 1-indexado
    long d = gcdl(i, j), h = i / d, k = j / d;
    if (h > k) { long t = h; h = k; k = t; }
    if (k == 1) return fromq<T>(A / (q)d);
    T g = V[tri(k, h)];
    return d == 1 ? g : fromq<T>(toq(g) / (q)d);
  };
  if (const char* dg = getenv("DUMPG")) {  // controle: imprime G(i,j) pedidos, formato i:j,i:j
    char* s = strdup(dg);
    for (char* t = strtok(s, ","); t; t = strtok(nullptr, ",")) {
      long i, j; if (sscanf(t, "%ld:%ld", &i, &j) == 2 && i <= N && j <= N) {
        char bb[64]; quadmath_snprintf(bb, 64, "%.33Qe", toq(G(i, j))); fprintf(stderr, "G %ld %ld %s\n", i, j, bb); }
    }
    if (getenv("DUMPONLY")) return 0;
  }
  std::vector<T> L((size_t)N * (N + 1) / 2), inv(N), y(N), b(N);
  for (long k = 1; k <= N; k++) b[k - 1] = fromq<T>((logk[k] + 1 - GAMQ) / (q)k);
  FILE* f = fopen(out, "w");
  fprintf(f, "N\tD_N\ts_N\ty2_N\n");
  T D = fromq<T>(1);
  char b1[64], b2[64], b3[64];
  std::vector<T> grow(N);
  for (long n = 0; n < N; n++) {
    T* Ln = &L[(size_t)n * (n + 1) / 2];
    for (long j = 0; j <= n; j++) grow[j] = G(n + 1, j + 1);
    for (long j = 0; j < n; j++) {
      const T* Lj = &L[(size_t)j * (j + 1) / 2];
      Ln[j] = (grow[j] - dot<T>(Ln, Lj, j)) * inv[j];
    }
    T s = grow[n] - dot<T>(Ln, Ln, n);
    if (!(toq(s) > 0)) { fprintf(stderr, "pivô <= 0 em N=%ld\n", n + 1); fclose(f); return 1; }
    T piv = sqrtT(s);
    Ln[n] = piv; inv[n] = fromq<T>(1 / toq(piv));
    y[n] = (b[n] - dot<T>(Ln, y.data(), n)) * inv[n];
    T y2 = y[n] * y[n];
    D = D - y2;
    quadmath_snprintf(b1, 64, "%.33Qe", toq(D));
    quadmath_snprintf(b2, 64, "%.20Qe", toq(s));
    quadmath_snprintf(b3, 64, "%.33Qe", toq(y2));
    fprintf(f, "%ld\t%s\t%s\t%s\n", n + 1, b1, b2, b3);
    if ((n + 1) % 500 == 0) { fflush(f); fprintf(stderr, "[%s] N=%ld %.1fs\n", out, n + 1, (double)(clock() - t0) / CLOCKS_PER_SEC); }
  }
  fclose(f);
  if (coef) {  // coeficientes c* = L^{-T} y em N selecionados + recálculo direto do resíduo
    FILE* g = fopen(coef, "w");
    fprintf(g, "N\tnorm2_c\tmax_abs_c\tS=sum c_k/k\tD_N(Cholesky)\tD_N(1-2c.b+cGc)\tE_N(BCF)\tc_1..c_12\n");
    std::vector<int> mu(N + 1, 1), isc(N + 1, 0);
    for (long p = 2; p <= N; p++) if (!isc[p]) { for (long m = p; m <= N; m += p) { if (m > p) isc[m] = 1; mu[m] = -mu[m]; }
      for (long m = p * p; m <= N; m += p * p) mu[m] = 0; }
    for (long Nc : cN) {
      if (Nc > N) continue;
      std::vector<q> c(Nc);
      for (long i = Nc - 1; i >= 0; i--) {
        q s = toq(y[i]);
        for (long j = i + 1; j < Nc; j++) s -= toq(L[(size_t)j * (j + 1) / 2 + i]) * c[j];
        c[i] = s / toq(L[(size_t)i * (i + 1) / 2 + i]);
      }
      q n2 = 0, mx = 0, S = 0, cb = 0, cGc = 0, Dch = 1;
      for (long i = 0; i < Nc; i++) { n2 += c[i] * c[i]; if (fabsq(c[i]) > mx) mx = fabsq(c[i]); S += c[i] / (q)(i + 1); cb += c[i] * toq(b[i]); Dch -= toq(y[i]) * toq(y[i]); }
      for (long i = 0; i < Nc; i++) { q r = 0; for (long j = 0; j < Nc; j++) r += toq(G(i + 1, j + 1)) * c[j]; cGc += c[i] * r; }
      char s1[64], s2[64];
      quadmath_snprintf(s1, 64, "%.30Qe", Dch); quadmath_snprintf(s2, 64, "%.30Qe", 1 - 2 * cb + cGc);
      // E_N: polinômio de Bettin–Conrey–Farmer c_k = -mu(k)(1 - log k/log N)  (cota superior de D_N)
      q E = 1; std::vector<q> cb2(Nc + 1, 0); std::vector<long> sf;
      for (long k = 1; k <= Nc; k++) if (mu[k]) { cb2[k] = -(q)mu[k] * (1 - logq((q)k) / logq((q)Nc)); sf.push_back(k); E -= 2 * cb2[k] * toq(b[k - 1]); }
      for (long i : sf) for (long j : sf) E += cb2[i] * cb2[j] * toq(G(i, j));
      char s3[64]; quadmath_snprintf(s3, 64, "%.15Qe", E);
      fprintf(g, "%ld\t%.6e\t%.6e\t%.6e\t%s\t%s\t%s", Nc, (double)n2, (double)mx, (double)S, s1, s2, s3);
      for (long i = 0; i < 12 && i < Nc; i++) fprintf(g, "\t%.6f", (double)c[i]);
      fprintf(g, "\n"); fflush(g);
    }
    fclose(g);
  }
  fprintf(stderr, "[%s] fim %.1fs\n", out, (double)(clock() - t0) / CLOCKS_PER_SEC);
  return 0;
}

int main(int argc, char** argv) {
  if (argc < 4) { fprintf(stderr, "uso: %s <d|ld|dd|q> Nmax out.tsv [coef.tsv N1,N2,..]\n", argv[0]); return 2; }
  long N = atol(argv[2]);
  const char* coef = argc > 4 ? argv[4] : nullptr;
  std::vector<long> cN;
  if (argc > 5) { char* s = strdup(argv[5]); for (char* t = strtok(s, ","); t; t = strtok(nullptr, ",")) cN.push_back(atol(t)); }
  std::string ty = argv[1];
  if (ty == "d") return run<double>(N, argv[3], coef, cN);
  if (ty == "ld") return run<long double>(N, argv[3], coef, cN);
  if (ty == "dd") return run<dd>(N, argv[3], coef, cN);
  if (ty == "q") return run<q>(N, argv[3], coef, cN);
  return 2;
}
