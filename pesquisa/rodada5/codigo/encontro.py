#!/usr/bin/env python3
"""Companheiro numérico de ATK/ZeroClasses/Encontro (rodada 21): matrizes, composições, colisão, varredura.

Só biblioteca padrão. **Nada aqui é certificado**: são as contas finitas que o kernel não faz.

* conferência dos números enviados: |ζ(σ + iγₖ)| em 5 × 3 pontos, det A = |ζ|², ζ(s₁) + ζ(s₂), o peso
  w = −ζ(s₁)/ζ(s₂), ζ(−½) = −ζ(3/2)/(4π);
* ξ(s) = ½s(s−1)π^{−s/2}Γ(s/2)ζ(s) com Γ de Lanczos; identidade (|S|² + |D|²)/4 = |ξ(s₊)|² = det A;
* estabilização |ξ(ρ₁+u)|²/u² → |ξ′(ρ₁)|² ≈ 1,9119·10⁻⁶ (e |ζ(ρ₁+u)|²/u² → |ζ′(ρ₁)|² ≈ 0,6291);
* colisão F_δ(s) = (s − c)² − δ²: zeros c ± δ, F′/F = 1/(s−ρ₊) + 1/(s−ρ₋) → 2/(s − c);
* **varredura** de |ζ| fora da linha (0,05 ≤ σ ≤ 0,45 e 0,55 ≤ σ ≤ 0,95, 10 ≤ t ≤ 100): mínimo positivo
  (heurístico, não certificado); margem de exclusão heurística min|ζ| − M·h/√2;
* certificado de contração (numérico) nos zeros 2–5 da linha;
* escala do candidato gigante ρ = ½ + 1/(2·10¹⁰⁰⁰+1) + i·10¹⁰⁰: Riemann–Siegel com ≈ 3,99·10⁴⁹ termos,
  T·δ < 5·10⁻⁹⁰¹ (conta inteira exata), janela de 2026 em T = 10¹⁰⁰.
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zeroclasses as zc  # noqa: E402

GAMMAS = [14.134725141734693, 21.022039638771555, 25.010857580145688, 30.424876125859513,
          32.935061587739189]
SIGMAS = [0.2, 0.35, 0.65, 0.8, 0.985]

_LG = 7
_LC = [0.99999999999980993, 676.5203681218851, -1259.1392167224028, 771.32342877765313,
       -176.61502916214059, 12.507343278686905, -0.13857109526572012, 9.9843695780195716e-6,
       1.5056327351493116e-7]


def gamma(z):
    """Γ complexa (Lanczos g = 7, n = 9; reflexão para Re z < 1/2)."""
    z = complex(z)
    if z.real < 0.5:
        return math.pi / (cmath.sin(math.pi * z) * gamma(1 - z))
    z -= 1
    x = _LC[0]
    for i in range(1, _LG + 2):
        x += _LC[i] / (z + i)
    t = z + _LG + 0.5
    return math.sqrt(2 * math.pi) * t ** (z + 0.5) * cmath.exp(-t) * x


def xi(s):
    s = complex(s)
    return 0.5 * s * (s - 1) * math.pi ** (-s / 2) * gamma(s / 2) * zc.zeta(s)


def det_A(w):
    return w.real * w.real + w.imag * w.imag


def deriv(f, s, h=1e-5):
    return (f(s + h) - f(s - h)) / (2 * h)


def SD(s):
    a, b = xi(s), xi(1 - s.conjugate())
    S, D = a + b, a - b
    return a, b, S, D


def Fcol(d, c, s):
    return (s - c) ** 2 - d * d


def bloco(s0, s1, t, hs, ht, folga=1.25):
    """min|ζ| e margem heurística min − folga·M·(diagonal/2) na malha de [s0, s1] × [t, t+1]."""
    ns, nt = int(round((s1 - s0) / hs)), int(round(1 / ht))
    mn, M, arg = float("inf"), 0.0, None
    for i in range(ns + 1):
        for k in range(nt + 1):
            z = complex(s0 + hs * i, t + ht * k)
            v = abs(zc.zeta(z))
            if v < mn:
                mn, arg = v, (z.real, z.imag)
            if i % 5 == 0 and k % 10 == 0:
                M = max(M, abs(deriv(zc.zeta, z)))
    return mn, arg, mn - folga * M * math.hypot(hs, ht) / 2


def varredura(t0=10, t1=100, hs=0.01, ht=0.02, niveis=3):
    """Varredura fora da linha por blocos [t, t+1) × faixa, com refinamento (passos/2) nos blocos de margem ≤ 0.

    Margem > 0 seria uma exclusão (`certificado_exclusao`) **se** M fosse uma cota rigorosa de |ζ′| no bloco —
    aqui M é só amostrado (com folga 1,25). Heurístico.
    """
    faixas = {"esquerda": (0.05, 0.45), "direita": (0.55, 0.95)}
    melhor = (float("inf"), None)
    blocos, positivos, refinados, pior = 0, 0, 0, float("inf")
    por_faixa = {}
    for nome, (s0, s1) in faixas.items():
        mf = float("inf")
        for t in range(t0, t1):
            h1, h2 = hs, ht
            for nivel in range(niveis):
                mn, arg, margem = bloco(s0, s1, t, h1, h2)
                if margem > 0:
                    break
                h1, h2 = h1 / 2, h2 / 2
                refinados += nivel == 0
            blocos += 1
            positivos += margem > 0
            pior = min(pior, margem)
            mf = min(mf, mn)
            if mn < melhor[0]:
                melhor = (mn, arg)
        por_faixa[nome] = mf
    return melhor, por_faixa, (hs, ht), (blocos, positivos, refinados, pior)


def main(saida=None):
    res = {}
    # 1. conferência dos números enviados
    tab = {}
    for s in SIGMAS:
        tab[format(s, ".3f")] = [format(abs(zc.zeta(complex(s, g))), ".6f") for g in GAMMAS[:3]]
    res["modulos_zeta_5x3"] = tab
    res["detA_gamma1"] = {format(s, ".3f"): format(det_A(zc.zeta(complex(s, GAMMAS[0]))), ".8f") for s in SIGMAS}
    z1, z2 = zc.zeta(complex(0.2, 14.134725)), zc.zeta(complex(0.8, 14.134725))
    w = -z1 / z2
    res["dois_pontos"] = {"zeta_s1": [z1.real, z1.imag], "zeta_s2": [z2.real, z2.imag],
                          "soma": [(z1 + z2).real, (z1 + z2).imag], "modulo_soma": abs(z1 + z2),
                          "w": [w.real, w.imag], "residuo_com_w": abs(z1 + w * z2)}
    zm = zc.zeta(-0.5)
    res["zeta_menos_meio"] = {"zeta(-1/2)": zm.real, "-zeta(3/2)/(4pi)": -zc.zeta(1.5).real / (4 * math.pi)}
    a = [zc.zeta(k).real for k in (2, 3, 4)]
    res["zero_coletivo_2_3_4"] = (a[1] - a[2]) * a[0] + (a[2] - a[0]) * a[1] + (a[0] - a[1]) * a[2]
    # 2. ξ, S, D
    rho = zc.zero_newton(complex(0.5, 14.13))
    dxi, dz = deriv(xi, rho), deriv(zc.zeta, rho)
    res["primeiro_zero"] = {"rho": [rho.real, rho.imag], "|zeta'(rho)|": abs(dz), "|zeta'|^2": abs(dz) ** 2,
                            "|xi'(rho)|": abs(dxi), "|xi'|^2": abs(dxi) ** 2}
    est = []
    for u in (1e-1, 1e-2, 1e-3, 1e-4):
        Dv = abs(xi(rho + u)) ** 2
        est.append({"u": u, "D": format(Dv, ".6e"), "D/u^2": format(Dv / u ** 2, ".10e"),
                    "erro_rel": format(abs(Dv / u ** 2 - abs(dxi) ** 2) / abs(dxi) ** 2, ".3e"),
                    "|xi(rho-u)|-|xi(rho+u)|": format(abs(xi(rho - u)) - abs(xi(rho + u)), ".1e")})
    res["estabilizacao_xi"] = est
    sp = complex(0.5 + 0.1, 14.0)
    a_, b_, S, D = SD(sp)
    res["cruzamento_em_0.6+14i"] = {"(|S|^2+|D|^2)/4": (abs(S) ** 2 + abs(D) ** 2) / 4, "|xi|^2": abs(a_) ** 2,
                                     "detA": det_A(a_), "xi(s+)xi(s-)": [(a_ * b_).real, (a_ * b_).imag],
                                     "|xi(s-) - conj xi(s+)|": abs(b_ - a_.conjugate())}
    # 3. colisão
    c = complex(0.5, 14.0)
    col = []
    for n in (1, 10, 100, 1000):
        d = 1 / (2 * n + 1)
        s = complex(0.3, 13.0)
        lhs = 2 * (s - c) / Fcol(d, c, s)
        rhs = 1 / (s - (c + d)) + 1 / (s - (c - d))
        col.append({"n": n, "delta": d, "F(c+d)": abs(Fcol(d, c, c + d)), "logderiv_erro": abs(lhs - rhs),
                    "dist_ao_limite_2/(s-c)": abs(rhs - 2 / (s - c))})
    res["colisao"] = col
    # 4. varredura fora da linha
    melhor, faixa, (hs, ht), (nb, npos, nref, pior) = varredura()
    res["varredura"] = {"regiao": "0,05≤σ≤0,45 e 0,55≤σ≤0,95, 10≤t≤100", "passo_sigma": hs, "passo_t": ht,
                        "min_|zeta|": melhor[0], "onde": melhor[1], "min_por_faixa": faixa,
                        "blocos": nb, "blocos_margem_positiva": npos, "blocos_refinados": nref,
                        "menor_margem_final": pior,
                        "aviso": "não certificado: M é amostrado, não uma cota rigorosa de |ζ′|"}
    # 5. certificados de contração numéricos nos zeros 2–5 (todos na linha)
    cert = []
    for g in GAMMAS[1:]:
        r0 = zc.zero_newton(complex(0.5, g))
        cc = deriv(zc.zeta, r0)
        r = 1e-6
        sup = max(abs(1 - deriv(zc.zeta, r0 + r * cmath.exp(2j * math.pi * k / 16)) / cc) for k in range(16))
        cert.append({"gamma": r0.imag, "re": r0.real, "sup|1-zeta'/c|": sup, "|zeta(z0)/c|": abs(zc.zeta(r0) / cc),
                     "r/2": r / 2, "valido(heuristico)": sup <= 0.5 and abs(zc.zeta(r0) / cc) <= r / 2})
    res["certificados_linha"] = cert
    # 6. escala gigante
    T, N = 10 ** 100, 10 ** 1000
    K = math.sqrt(T / (2 * math.pi))
    lt = 100 * math.log(10)
    res["gigante"] = {"RS_termos": format(K, ".9e"), "log10_RS_termos": math.log10(K),
                      "T*delta<5e-901": 10 ** 100 * 10 ** 901 < 5 * (2 * N + 1),
                      "delta_aprox": "5e-1001", "borda_janela_2026": 1 / (4.896 * lt),
                      "candidato_na_janela": 1 / (4.896 * lt) < 0.5 < 1 - 1 / (4.896 * lt)}
    res["aviso"] = ("contas em ponto flutuante; o kernel prova as identidades, o critério e os certificados "
                    "(Encontro.lean), não estes números")
    if saida:
        json.dump(res, open(saida, "w"), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return res


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
