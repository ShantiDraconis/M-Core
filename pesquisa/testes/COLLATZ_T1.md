# COLLATZ T1 — lei exata de Syrac(ℤ/3ⁿ): decaimento de Fourier M_n e mínimos c_n, n ≤ 16

**Hipóteses.**
- H1 (observação de Tao): log M_n é linear em n, com M_n := max_{3∤ξ} |E e(−ξ·Syrac/3ⁿ)|.
- H2 (Tao 2020): ρ_n := c_n·φ(3ⁿ) é limitado inferiormente (κ = 1), com c_n = min_b P(Syrac = b).

## Método
- C em `tests/code/COLLATZ_T1_syrac.c`; saídas em `tests/work/collatz/`. n = 1..16 em 20 s, pico ~0,6 GB.
- **Recursão:** 2 é raiz primitiva mod 3ⁿ; indexo as unidades por log discreto e uso P_n(ℓ) = ½Q_n(ℓ+1) + ½P_n(ℓ+1), cíclica, in place, com aquecimento exato (2^{−280}).
- **Erro:** só somas de não negativos e multiplicações por ½ (exatas), então o erro relativo fica ≲ L_n·ε ≤ 3e−9 no pior caso.
- **Fourier:** basta ξ ≡ 1 mod 3 (ξ ≡ 2 é conjugado); FFT radix-3 de comprimento 3^{n−1} (14,3 M pontos em n = 16).

## Controles (todos passaram)
1. **Valores do mapa:** c₁ = 1/3, c₂ = 2/63, c₃ = 1598/262143, recuperados em racionais exatos.
2. **Força bruta A** (`COLLATZ_T1_exact.py`): DP em racionais sobre a definição, estado (S mod L_n, X mod 3ⁿ), n ≤ 5. A lei inteira coincide (erro relativo ≤ 2,2e−16), soma 1, suporte = todas as unidades.
3. **Força bruta B** (`COLLATZ_T1_brute.c`): enumeração direta das tuplas com a_i ≤ 30 (n ≤ 5) e ≤ 24 (n = 6). Em todo ponto, algoritmo ≥ bruta e |algoritmo − bruta| ≤ massa truncada (n = 5: 1,3e−10 ≤ 4,7e−9).
4. **Fourier:** FFT contra DFT direta (n ≤ 7), ≤ 2,6e−16. Identidade φ_n(ξ) = Σ_a 2^{−a} e(−ξ2^{−a}/3ⁿ) φ_{n−1}(ξ2^{−a}) em 12 ξ (incluindo ξ*) para cada n = 3..16: ≤ 3,4e−16.

## Resultados
δ_n := −log₃c_n − n, ou seja, c_n = 3^{−n−δ_n}.

| n | c_n | ρ_n | δ_n | M_n | ξ* | M_n^{1/n} |
|---|---|---|---|---|---|---|
| 1 | 0,33333 | 0,667 | 0,000 | 0,5774 | +1 | 0,577 |
| 2 | 3,1746e−2 | 0,190 | 1,140 | 0,3779 | +2² | 0,615 |
| 3 | 6,0959e−3 | 0,110 | 1,642 | 0,2522 | −2³ | 0,632 |
| 4 | 1,7891e−3 | 0,097 | 1,758 | 0,1770 | +2⁴ | 0,649 |
| 6 | 1,2400e−4 | 0,060 | 2,188 | 0,09611 | +2⁶ | 0,677 |
| 8 | 1,1441e−5 | 0,0500 | 2,357 | 0,06089 | −2⁹ | 0,705 |
| 10 | 1,0309e−6 | 0,0406 | 2,548 | 0,03828 | +2¹² | 0,722 |
| 12 | 9,9569e−8 | 0,0353 | 2,675 | 0,02646 | +2¹⁴ | 0,739 |
| 13 | 3,1424e−8 | 0,0334 | 2,725 | 0,02205 | +2¹⁶ | 0,746 |
| 14 | 9,8092e−9 | 0,0313 | 2,785 | 0,01913 | −2¹⁷ | 0,754 |
| 15 | 3,0743e−9 | 0,0294 | 2,841 | 0,01628 | +2¹⁸ | 0,760 |
| 16 | 9,9726e−10 | 0,0286 | 2,866 | 0,01441 | +2²⁰ | 0,767 |

- **Ajustes de log M_n, n ≥ 9:** exponencial e^{−αn} com α = 0,172 (rms 0,036); potência n^{−A} com A = 2,10 (rms 0,0086); misto a = 0,010, A = 1,99. Para n ≥ 6: rms 0,063 (exponencial) e 0,036 (potência).
- **Taxa local** −log(M_{n+1}/M_n), n = 6 a 16: 0,24 → 0,22 → 0,24 → 0,23 → 0,18 → 0,19 → 0,18 → 0,14 → 0,16 → 0,12.
- **κ:** κ ≤ min_m e_m/m = e₁₅/15 = **1,258**, cota rigorosa por subaditividade (Fekete) usando c₁₆.
- **ρ_n, n ≥ 8:** potência n^{−0,80} (rms 0,020) contra geometria 0,934ⁿ, isto é, κ ≈ 1,062 (rms 0,037).

## Interpretação
- **Mostra:** em 1 ≤ n ≤ 16, M_n cai de 0,58 para 0,0144, mas a taxa exponencial local cai de 0,24 para 0,12 e M_n^{1/n} sobe monotonamente até 0,767. Na faixa, n^{−2,1} descreve os dados 4× melhor (rms) do que e^{−αn}.
- **Não contradiz Tao** (M_n ≪_A n^{−A} para todo A): a cota é assintótica, com constantes não explícitas, então o regime ~n^{−2} tem de ser pré-assintótico.
- **Para Q2:** uma cota explícita C·ρⁿ válida para todo n precisa de ρ ≥ 0,767 com C = 1. Até n = 16 não há decaimento exponencial visível.
- **Novo (não encontrei publicado):** o maximizador é sempre ξ* = ±2^j, com |ξ*|/3ⁿ ∈ [0,018; 0,044] para n ≥ 9. O pior caractere é de "baixa frequência real" na órbita de 2: a obstrução parece estar na escala grande (Syrac/3ⁿ como real), e Q2 pode focar em ξ ∈ ⟨2⟩·{pequenos}.
- **c_n:** ρ_n ainda decresce em n = 16 (0,0286). Potência ajusta um pouco melhor (compatível com κ = 1, a conjectura de Tao) do que geometria (κ ≈ 1,06), mas a diferença é pequena; a cota rigorosa é só κ ≤ 1,258.

## Limites
- Parei em n ≤ 16: n = 17 exigiria ~1,8 GB, com memória e disco escassos.
- Sem arb/python-flint (indisponível): substituí por análise de erro e controles exatos.
- A oscilação O(m,n) de Tao não foi calculada; os ajustes usam 8–11 pontos, com ruído de paridade.

## Próximo
- φ_n só em ξ ∈ ±2^j·{1..K}, por somas diretas em O(L_n·K) e sem FFT: permite n ≈ 20 e testar se a taxa local continua caindo.
- c_n em float32 para n = 17–18.
