#!/usr/bin/env python3
"""Confere, número a número, as tabelas do texto encaminhado (22/10, 13:41).

1. Modelo paramétrico (A7 e a regra consecutiva) em aritmética racional exata (fractions):
   cada decimal impresso no texto é comparado com o valor exato arredondado.
2. ζ nos zeros trocados T(ρ) = γ + i/2: valor numérico (Euler–Maclaurin, ponto flutuante) e envelope
   CERTIFICADO pela cota provada no kernel (ATK.ZetaTroca.norm_zeta_sub_one_le), avaliada em
   aritmética racional com σ ≥ ⌊γ⌋.
3. Zeros 100, 1000, 10000 citados no texto: resíduo, troca de sinal de Z(t) em ±10⁻⁶ e índice por
   θ(γ)/π + 1 (Riemann–von Mangoldt).
4. D_256 e D_8000 contra os dados das rodadas 2 e 3.
5. A lei real de truncamento (rodada 4c) contra a lei escolhida A7.
Uso: python3 certifica_texto.py <dir_saida>
"""
import json, math, os, sys
from fractions import Fraction as Fr
import numpy as np
from scipy.special import loggamma
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bohr_landau_material import zeta

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", ".."))


def arred(x: Fr, casas: int) -> str:
    q = Fr(10) ** casas
    n = (x * q).numerator * 2 + (x * q).denominator
    v = n // (2 * (x * q).denominator)  # arredondamento meio-para-cima
    s = str(v).rjust(casas + 1, "0")
    return s[:-casas] + "." + s[-casas:]


def confere(nome, exato: Fr, impresso: str):
    casas = len(impresso.split(".")[1])
    r = arred(exato, casas)
    return {"item": nome, "impresso": impresso, "exato_arredondado": r, "ok": r == impresso}


def modelo():
    linhas = []
    meio = Fr(1, 2)
    # regra consecutiva: v_N = 1/2 + 1/N, k_N = (v_N + v_{N+1})/2
    tabA = {10: ("0.600000000", "0.595454545"), 100: ("0.510000000", "0.509950495"),
            1000: ("0.501000000", "0.500999500"), 10000: ("0.500100000", "0.500099995"),
            10**6: ("0.500001000", "0.500001000"), 10**9: ("0.500000001", "0.500000001")}
    for N, (v, kk) in tabA.items():
        vN = meio + Fr(1, N)
        kN = (vN + meio + Fr(1, N + 1)) / 2
        linhas.append(confere(f"consecutiva v_{N}", vN, v))
        linhas.append(confere(f"consecutiva k_{N}", kN, kk))
        assert kN - meio == Fr(2 * N + 1, 2 * N * (N + 1))  # fórmula fechada do texto
    # A7: j_N = 1/2 + 1/(2N) + 1/(2(N+1)^2)
    tabB = {10: "0.554132231405", 100: "0.505049014802", 1000: "0.500500499001",
            10**6: "0.5000005000005", 10**12: "0.5000000000005"}
    for N, j in tabB.items():
        jN = meio + Fr(1, 2 * N) + Fr(1, 2 * (N + 1) ** 2)
        linhas.append(confere(f"A7 j_{N}", jN, j))
    # expansão assintótica: 1/(2(N+1)^2) = 1/(2N^2) − 1/N^3 + 3/(2N^4) − 2/N^5 + ...
    N = 10**4
    resto = Fr(1, 2 * (N + 1) ** 2) - (Fr(1, 2 * N**2) - Fr(1, N**3) + Fr(3, 2 * N**4))
    linhas.append({"item": "expansão até N^-4 em N = 10^4: resto·N^5", "valor": float(resto * N**5),
                   "ok": abs(float(resto * N**5) + 2) < 1e-3})
    return linhas


def b_cert(sigma_inf: int) -> Fr:
    """Cota provada 2^{−σ} + 2^{1−σ}/(σ−1), decrescente em σ, avaliada em σ = sigma_inf ≤ σ."""
    return Fr(1, 2**sigma_inf) + Fr(2, 2**sigma_inf) / (sigma_inf - 1)


def theta(t):
    return float(np.imag(loggamma(0.25 + 0.5j * t)) - 0.5 * t * math.log(math.pi))


def Zfun(t):
    return float(np.real(np.exp(1j * theta(t)) * zeta(np.array([0.5 + 1j * t]))[0]))


def zeros_trocados():
    d = json.load(open(os.path.join(RAIZ, "rodada4", "dados", "ate300", "zero_incognito.json")))
    gam = sorted(d["newton"]["gamma"])[:8]
    texto = {1: 1.00005244444, 2: 1.00000044177, 3: 1.00000002782, 4: 1.00000000065, 5: 1.00000000011}
    extra = {100: 236.524229665816, 1000: 1419.422480945996, 10000: 9877.782654005501}
    linhas = []
    for n, g in list(enumerate(gam, 1)) + list(extra.items()):
        w = complex(g, 0.5)
        z = zeta(np.array([w]))[0]
        s_inf = math.floor(g)
        b = b_cert(s_inf)
        lb = float(b) if b > Fr(1, 10**300) else None
        log10b = math.log10(b.numerator) - math.log10(b.denominator)
        linha = {"n": n, "gamma": g, "abs_zeta_Trho": abs(z), "abs_zeta_menos_1": abs(z - 1),
                 "cota_certificada_log10": log10b,
                 "dentro_da_cota": abs(z - 1) <= (lb if lb is not None else 0) or abs(z - 1) == 0.0}
        if n in texto:
            linha["texto"] = texto[n]
            linha["texto_dentro_do_envelope"] = abs(texto[n] - 1) <= float(b)
            linha["texto_menos_calculado"] = texto[n] - abs(z)
        if n in extra:
            r = abs(zeta(np.array([complex(0.5, g)]))[0])
            zl, zr = Zfun(g - 1e-6), Zfun(g + 1e-6)
            linha["residuo_na_reta"] = r
            linha["troca_de_sinal_Z"] = zl * zr < 0
            linha["theta_sobre_pi_mais_1"] = theta(g) / math.pi + 1
            linha["indice_menos_meio"] = n - 0.5
        linhas.append(linha)
    return linhas


def dados_D():
    D2 = {}
    for l in open(os.path.join(RAIZ, "rodada2", "dados", "RH_Gram_DN.tsv")):
        p = l.split("\t")
        if p[0] in ("256", "7999"):
            D2[int(p[0])] = p[1]
    D3 = {}
    for l in open(os.path.join(RAIZ, "rodada3", "dados", "DN_double.tsv")):
        p = l.split("\t")
        if p[0] in ("256", "8000"):
            D3[int(p[0])] = p[1].strip()
    return {"D_256 (rodada 2, ~24 dígitos)": D2.get(256), "D_7999 (rodada 2)": D2.get(7999),
            "D_8000 (rodada 3, double)": D3.get(8000), "texto D_256": "0.008233716277261",
            "texto D_8000": "0.0050691202",
            "D_256 certificado (rodada 3, intervalar)": "D_256 ≤ 0.00823372, folga 3.7227e-9"}


def lei_real():
    d = json.load(open(os.path.join(RAIZ, "rodada4", "dados", "truncamento_zero.json")))
    out = []
    for info in d["zeros"]:
        e = [l["eps"] for l in info["linhas"]]
        out.append({"gamma": info["rho"][1], "trocas_de_sinal": info["trocas_de_sinal_de_eps"],
                    "positivos": sum(1 for x in e if x > 0), "negativos": sum(1 for x in e if x < 0)})
    return {"lei_real": out, "lei_A7": "k_N − c > 0 e decrescente para todo N (provado: k_gt, k_anti)"}


def main():
    rel = {"modelo": modelo(), "zeros_trocados": zeros_trocados(), "D": dados_D(), "truncamento": lei_real()}
    json.dump(rel, open(os.path.join(OUT, "certifica_texto.json"), "w"), indent=1, default=str)
    ok = sum(1 for l in rel["modelo"] if l.get("ok"))
    print(f"modelo: {ok}/{len(rel['modelo'])} conferidos")
    for l in rel["modelo"]:
        if not l.get("ok"):
            print("  DIVERGE:", l)
    for l in rel["zeros_trocados"]:
        s = (f"n={l['n']:>5} γ={l['gamma']:.6f} |ζ(Tρ)|={l['abs_zeta_Trho']:.14f} |ζ−1|={l['abs_zeta_menos_1']:.3e} "
             f"cota log10={l['cota_certificada_log10']:.2f} dentro={l['dentro_da_cota']}")
        if "texto" in l:
            s += f" texto={l['texto']} (dif {l['texto_menos_calculado']:+.2e}, no envelope={l['texto_dentro_do_envelope']})"
        if "residuo_na_reta" in l:
            s += (f" | resíduo 1/2+iγ={l['residuo_na_reta']:.2e} sinal Z={l['troca_de_sinal_Z']} "
                  f"θ/π+1={l['theta_sobre_pi_mais_1']:.3f} (n−1/2={l['indice_menos_meio']})")
        print(s)
    print(json.dumps(rel["D"], ensure_ascii=False, indent=1))
    print(json.dumps(rel["truncamento"], ensure_ascii=False))


if __name__ == "__main__":
    main()
