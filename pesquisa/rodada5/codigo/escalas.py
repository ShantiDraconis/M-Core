#!/usr/bin/env python3
"""Companheiro numérico de ATK/ZeroClasses/Escalas (rodada 20): onde um zero fora da linha ainda pode estar.

Só biblioteca padrão. Nada aqui é certificado; as constantes da literatura entram como dados:

* H = 3 000 175 332 800 — Platt–Trudgian (2021): todos os zeros até essa altura estão na linha e são simples;
* R = 4,896, t ≥ 3 — Bellotti–Trudgian–Yang (2026): ζ ≠ 0 em σ ≥ 1 − 1/(R log t);
* Littlewood explícito (Trudgian): σ ≥ 1 − log log t/(21,233 log t);
* Korobov–Vinogradov explícito (Bellotti): σ ≥ 1 − 1/(53,989 (log t)^{2/3}(log log t)^{1/3}), t ≥ 3;
* densidade (Guth–Maynard, Annals 2026): N(σ, T) ≤ T^{30(1−σ)/13 + o(1)}.

Saídas: a janela [δ(t), 1 − δ(t)] por altura (com a melhor das três regiões), as retas ATK σₙ = ½ + 1/(2n+3) dentro
dela, o expoente de densidade em cada reta ATK, a escala de Selberg 1/log t, e a lei da cauda perto do 1º zero
(R/d → |ζ′(ρ₁)| ≈ 0,79316, entre os limites certificados |c|/2 e 3|c|/2, |c| ≈ 0,7932).
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zeroclasses as zc  # noqa: E402

H = 3000175332800
R_CLASSICA = 4.896
R_LITTLEWOOD = 21.233
R_KV = 53.989
C_CERT = complex(0.78330, 0.12470)  # c do certificado de §4f (`ATK.ZeroCert.cC`, arredondado)


def delta_classica(logt):
    return 1 / (R_CLASSICA * logt)


def delta_littlewood(logt):
    return math.log(logt) / (R_LITTLEWOOD * logt)


def delta_kv(logt):
    return 1 / (R_KV * logt ** (2 / 3) * math.log(logt) ** (1 / 3))


def delta_melhor(logt):
    """Largura excluída junto às bordas: a maior das três regiões (todas válidas para t ≥ 3)."""
    return max(delta_classica(logt), delta_littlewood(logt), delta_kv(logt))


def expoente_gm(sigma):
    """Expoente de T na cota de Guth–Maynard; ≥ 1 significa que não melhora a contagem trivial N(T) ~ T log T."""
    return 30 * (1 - sigma) / 13


def sigma_atk(n):
    return 0.5 + 1 / (2 * n + 3)


def main(saida=None):
    alturas = {"3e12 (H)": math.log(H), "1e15": 15 * math.log(10), "1e20": 20 * math.log(10),
               "1e50": 50 * math.log(10), "1e100": 100 * math.log(10), "1e1000": 1000 * math.log(10),
               "e^100": 100.0, "e^10^6": 1e6}
    janela = {}
    for nome, lt in alturas.items():
        d = delta_melhor(lt)
        janela[nome] = {"delta_borda": format(d, ".6g"), "janela": [format(d, ".6g"), format(1 - d, ".6g")],
                        "regiao": max((("classica", delta_classica(lt)), ("littlewood", delta_littlewood(lt)),
                                       ("kv", delta_kv(lt))), key=lambda x: x[1])[0],
                        "escala_selberg_1/log_t": format(1 / lt, ".4g")}
    # cruzamentos: Littlewood passa a clássica quando log log t > 21.233/4.896; KV passa Littlewood muito depois
    cruz_lw = math.exp(R_LITTLEWOOD / R_CLASSICA)
    atk = {}
    for n in range(0, 8):
        s = sigma_atk(n)
        dH = delta_melhor(math.log(H))
        atk[str(n)] = {"sigma": format(s, ".6f"), "dentro_da_janela_em_H": dH < s < 1 - dH,
                       "expoente_GM": format(expoente_gm(s), ".4f"), "GM_nao_trivial": expoente_gm(s) < 1}
    # lei da cauda perto do 1º zero
    rho = zc.zero_newton(complex(0.5, 14.13))
    cauda = []
    for d in (1e-2, 1e-3, 1e-4, 1e-5):
        r = abs(zc.zeta(rho + d))
        cauda.append({"d": d, "R": format(r, ".6g"), "R/d": format(r / d, ".6f")})
    res = {
        "H_Platt_Trudgian": H,
        "janela_por_altura": janela,
        "log_log_t_cruzamento_classica_littlewood": format(R_LITTLEWOOD / R_CLASSICA, ".4f"),
        "log_t_cruzamento_classica_littlewood": format(cruz_lw, ".4f"),
        "retas_ATK": atk,
        "sigma_onde_GM_deixa_de_ajudar": format(17 / 30, ".6f"),
        "cauda_primeiro_zero": cauda,
        "limites_certificados_R/d": [format(abs(C_CERT) / 2, ".5f"), format(3 * abs(C_CERT) / 2, ".5f")],
        "aviso": "dados da literatura como entrada; o kernel prova a janela a partir deles (`janela`), não os dados",
    }
    if saida:
        json.dump(res, open(saida, "w"), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return res


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
