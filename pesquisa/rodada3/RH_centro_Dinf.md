# RH — D_∞: centro, tolerância, precisão e cauda (rodada 3, 22/10/2026)

**Resposta curta.** O valor exato de D_∞ é 0 se RH vale e é positivo se RH falha (B1 e `rh_iff_DN` no kernel); nenhuma conta finita
decide entre os dois. O que os dados de N ≤ 8000 forçam:

* **cerco** (numérico, ~24 dígitos, ainda sem aritmética intervalar): 0 ≤ D_∞ < D_8000 = 0,00506912020009596;
* **centro extrapolado**: D̂_∞ = 0 ± 1·10⁻³, isto é ±20% de D_8000. O modelo com D_∞ = 0 forçado ajusta tão bem quanto os modelos com D_∞ livre;
* **resolução**: abaixo de ~10⁻⁴ os dados não enxergam nada. Um zero fora da linha acima da altura verificada (3·10¹²) só garante
  D_∞ ≥ m(ρ)², e esse piso é no máximo 5,1·10⁻²⁷, cerca de 22 ordens de grandeza abaixo do que a extrapolação resolve (~10⁻⁴).

Código: `codigo/RH_centro_dn.cpp` (Cholesky incremental em float / double / double-double / binary128, Gram exata de Vasyunin,
tabela de arredondamento dos coeficientes) e `codigo/RH_centro_fit.py` (ajustes, cauda, piso). Dados em `dados/`.
A referência de alta precisão é `../rodada2/dados/RH_Gram_DN.tsv` (dd, N ≤ 8000).

## 1. Três réguas para D_∞

| régua | o que diz sobre D_∞ | centro | tolerância | base |
| --- | --- | --- | --- | --- |
| rigorosa | [0; D_8000] = [0; 0,0050691202] | 0,0025345601 | ±100% do centro | D_∞ ≤ D_N (monotonia) e D_∞ ≥ 0 |
| extrapolação | 0 ± ~1·10⁻³ | ≈ 0 | ±20% de D_8000 | modelos com D_∞ livre, janelas a partir de N ≤ 400 (§2) |
| zero fora da linha | se existir, D_∞ ≥ m(ρ)², com m(ρ)² ≤ 5,1·10⁻²⁷ | — | — | `ForaDaLinha.piso_DN` + Platt–Trudgian 2021 (RH até 3,0002·10¹²) |

O piso é m(ρ) = 1/(|ρ|(1/√(2σ−1) + 1/(1−σ))). O fator entre parênteses é mínimo (4,6636) em σ = 0,6319, logo m(ρ)² ≤ 1/(4,6636·3,0002·10¹²)².
Mais perto da linha o piso cai ainda mais: σ = 0,51 dá 1,3·10⁻²⁷; σ = 0,5001 dá 2,1·10⁻²⁹.

## 2. O centro forçado pelos dados (ajustes com D_∞ livre)

Amostra de 300 N log-uniformes por janela. Modelos: **A** D = D_∞ + A/(log N + a); **B** D = D_∞ + A/log N + B/log²N;
**C** D = D_∞ + C₀/(log N + a), com C₀ = 2 + γ − log 4π = 0,0461914 fixo; **0** D_∞ = 0 forçado.

| janela | A | B | C | rms relativo: A / 0 |
| --- | --- | --- | --- | --- |
| [50, 8000] | −4,1·10⁻⁵ (−0,8%) | +8,8·10⁻⁶ (+0,2%) | −2,4·10⁻⁴ (−4,7%) | 1,40% / 1,40% |
| [100, 8000] | +6,8·10⁻⁴ (+13,5%) | +8,8·10⁻⁴ (+17,4%) | −2,3·10⁻⁴ (−4,5%) | 1,25% / 1,31% |
| [200, 8000] | +2,4·10⁻⁴ (+4,8%) | +2,6·10⁻⁴ (+5,1%) | −1,1·10⁻⁴ (−2,1%) | 1,18% / 1,18% |
| [400, 8000] | +2,9·10⁻⁴ (+5,7%) | +2,8·10⁻⁴ (+5,5%) | −8,1·10⁻⁵ (−1,6%) | 1,27% / 1,28% |
| [800, 8000] | −1,3·10⁻² (−258%) | −4,6·10⁻³ (−91%) | −5,3·10⁻⁵ (−1,0%) | 1,06% / 1,17% |
| [1600, 8000] | +2,4·10⁻³ (+47%) | +1,0·10⁻² (+202%) | −4,1·10⁻⁴ (−8,0%) | 1,01% / 1,10% |

(Percentuais em relação a D_8000.)

* **O erro padrão ingênuo engana.** Ele fica entre 4·10⁻⁶ e 4·10⁻⁴, e mesmo corrigido pela autocorrelação dos resíduos (n_eff ≈ 8–27) é bem menor que a dispersão entre
  modelos e janelas. A tolerância é sistemática: vem da oscilação lenta de ±1,3% em D_N·log N (período ≈ 2,6 em log N), não de ruído.
* **O modelo C dá sempre D_∞ < 0**, o que é impossível. A forma C₀/(log N + a) com C₀ fixo não descreve a segunda ordem.
* **O modelo nulo D_∞ = 0 ajusta tão bem quanto os livres** (diferença de rms ≤ 0,1 ponto percentual nas janelas longas).
  Conclusão: centro 0, tolerância ~1·10⁻³, e nada abaixo de ~10⁻⁴ é visível.
* **Convergência com N_max** (janela [100, N_max]): o centro do modelo A oscila entre −1,4·10⁻³ (N_max = 1000) e +1,4·10⁻³ (N_max = 3000) e não se estabiliza.

## 3. Menor precisão com a menor tolerância

### 3a. Aritmética (precisão com que D_N é calculado)

| aritmética | unidade u | desvio relativo de D_N contra dd | primeiro N com desvio > 0,1% |
| --- | --- | --- | --- |
| float (24 bits) | 6,0·10⁻⁸ | N = 256: 0,022%; 1000: −4,1%; 2000: −73%; **D_N = 0 em N = 2112**, depois negativo; pivô ≤ 0 em N = 4995 | 500 |
| double | 1,1·10⁻¹⁶ | máximo 3,8·10⁻⁹ % em N ≤ 8000 (≈ 10 dígitos corretos) | — |
| double-double | ≈ 10⁻³² | ≤ 2,6·10⁻²⁴ % contra binary128 até N = 3000 (≈ 24 dígitos) | — |

* **Em float, o resultado finge que D_∞ = 0.** D_N chega a zero em N = 2112 e fica negativo. A menor precisão produz exatamente o "zero" procurado, e é um artefato.
* **Lei da quebra.** O pivô de Schur é s_N ≈ 4/N² (2,9·10⁻⁴ em N = 100; 7,8·10⁻⁸ em 8000). A aritmética quebra quando s_N cai abaixo de ≈ N·u,
  ou seja em N* ≈ (4/u)^{1/3}: float ≈ 400–500 (observado: 0,1% em N = 500), double ≈ 3·10⁵, dd ≈ 7·10¹⁰.
* **Derivada da precisão.** Em double os dígitos perdidos crescem ≈ 1,25 por década de N: 3,2 em N ≤ 100; 4,6 em ≤ 1000; 5,5 em ≤ 8000.
* **Integral da precisão.** O erro de D_N é a soma dos erros dos ganhos g_n. Em double eles se cancelam: metade dos passos para cada lado, |Σ| / Σ|·| ≈ 0.
  Em float, passada a quebra, viram deriva de um lado só: 81% dos passos superestimam o ganho em [1000, 2112), |Σ| / Σ|·| = 0,96. É essa
  deriva acumulada que fabrica o zero falso.

### 3b. Dígitos de D_N necessários para o centro

Arredondando D_N a k algarismos significativos e refazendo os ajustes (janela [100, 8000]), o centro muda:
k = 2: ~1·10⁻⁴ (2% de D_8000); k = 3: ~2·10⁻⁵; **k = 4: < 1·10⁻⁶ (0,02%)**; k ≥ 5: < 6·10⁻⁸.
Os dados em double reproduzem o centro do dd em todos os dígitos impressos. Os dados em float empurram o centro para −4,6·10⁻² (janela [100, 2000]), um valor impossível.
**Quatro algarismos de D_N já dão a menor tolerância alcançável;** a precisão não é o gargalo, o tamanho de N é.

### 3c. Dígitos dos coeficientes para um certificado (cota superior rigorosa via `DN_le`)

Arredondando c* a d casas decimais, Q(c_d) − D_N = δᵀGδ exatamente, com δ = c_d − c*.
O valor esperado é tr(G_N)·10^{−2d}/12, com tr(G_N) = (log 2π − γ)·H_N (7,7 em N = 256; 12,1 em 8000).

| d (casas) | N = 256 | N = 1000 | N = 8000 (double) |
| --- | --- | --- | --- |
| 2 | 8,2·10⁻⁵ (0,99%) | 1,8·10⁻⁵ (0,28%) | 5,5·10⁻⁵ (1,09%) |
| 3 | 1,6·10⁻⁷ (1,9·10⁻³ %) | 1,1·10⁻⁷ (1,7·10⁻³ %) | 5,9·10⁻⁷ (1,2·10⁻² %) |
| **4** | **1,8·10⁻⁹ (2,2·10⁻⁵ %)** | 6,4·10⁻⁹ (9,7·10⁻⁵ %) | 1,3·10⁻⁸ (2,6·10⁻⁴ %) |
| 5 | 2,8·10⁻¹¹ | 4,2·10⁻¹¹ | 5,9·10⁻¹¹ |
| 6 | 1,7·10⁻¹³ | 9,2·10⁻¹³ | 8,2·10⁻¹³ |

* **Derivada:** cada casa decimal a mais reduz o desvio em duas ordens de grandeza (inclinação −2, lei quadrática).
* **Dependência em N:** o desvio relativo cresce só como (log N)², então a precisão dos coeficientes custa quase nada.
* **Certificado da hipótese numérica do kernel** (`ContracaoDN.cert_Dinf_numerico`: D_256 ≤ 0,00823372, folga 3,72·10⁻⁹): **bastam 4 casas decimais**
  (desvio 1,8·10⁻⁹). Com 3 casas falha (1,6·10⁻⁷). Falta avaliar b e G com aritmética intervalar e formalizar a fórmula de Vasyunin.

## 4. A cauda: derivada e integral da tolerância

* **Derivada (exata):** D_{N+1} − D_N = −g_N. Modelo sob RH: dD/dN ≈ −C₀/(N log²N). As médias de g_N·N·log²N/C₀ por bloco diádico
  de [64, 128) a [2048, 4096) dão 1,11; 1,26; 0,93; 1,09; 0,67; 1,36 (média 1,07). Em escala logarítmica, d log D / d log N ≈ −1/log N:
  em N = 8000 a tolerância cai 11% a cada fator e em N, e essa taxa também tende a zero.
* **Integral (exata):** Σ_{n<N} g_n = D_1 − D_N (telescópio). O desconhecido é o resto Σ_{n≥N} g_n = D_N − D_∞, ou seja a própria cauda.
* **Integral relativa:** Σ_{1≤n<8000} η_n = 3,965 e cresce como log log N. Sua forma exata é a O1 (`CapturaIncondicional.captura_log_iff_incondicional`).
* **Integral da tolerância em escala log:** Σ D_n/n cresce como C₀·log log N. Os incrementos conferem: de 100 a 1000, 0,018772 contra 0,018729 previsto;
  de 1000 a 8000, 0,012006 contra 0,012155. Essa integral diverge, mesmo com D_N → 0.

## 5. Quanto N para cada tolerância (sob RH, D_N ≈ C₀/(log N + a), a = −0,17)

| tolerância τ | log N | N |
| --- | --- | --- |
| 5·10⁻³ | 9,4 | ≈ 1,2·10⁴ |
| 2,5·10⁻³ (metade de D_8000) | 18,6 | ≈ 1,3·10⁸ |
| 1·10⁻³ | 46 | ≈ 10²⁰ |
| 1·10⁻⁴ | 462 | ≈ 10²⁰⁰ |
| 1·10⁻⁶ | 4,6·10⁴ | ≈ 10^(2·10⁴) |
| 5·10⁻²⁷ (piso de um zero fora da linha) | 9·10²⁴ | ≈ 10^(3,9·10²⁴) |

Derivada: dN/dτ = −N·C₀/τ². Cada redução da tolerância custa um fator exponencial em N.
Escalas físicas encaminhadas: N = R_universo/a_Bohr (log N = 85,0) dá C₀/log N = 5,4·10⁻⁴ (10,7% de D_8000); N = R_universo/ℓ_Planck (141,5) dá 3,3·10⁻⁴ (6,4%).
Nem a razão universo/Planck leva a tolerância abaixo de 6% de D_8000. A escala "log N = c (velocidade da luz)" é uma escolha arbitrária, sem ligação demonstrada com a sequência.

## 6. Conferência dos textos encaminhados

* 25345601/5·10⁹ = 0,0050691202 está correto como fração do decimal, mas o decimal está truncado: D_8000 = 0,0050691202000959571…
  4423/872538 erra 1,3·10⁻¹² do D_8000 verdadeiro. Nenhuma fração é D_∞, e D_∞ < D_8000 estritamente, porque cada ganho g_N é positivo.
* Q_8000 = 1 − D_8000/D_1 = 0,99409339 está correto.
* D_∞ = sup_{h ⊥ W, h ≠ 0} |⟨h,χ⟩|²/‖h‖² está correto (distância a um subespaço fechado), mas não dá um valor numérico.
* A cauda 1/T do candidato (−0,83; 1,90) está correta: por paridade de m, |r| ≤ 1 em t ≥ 1. O valor médio é 0,44305/T. Para esse candidato,
  porém, não é preciso truncar: E(c) = 1 − 2bᵀc + cᵀGc tem forma fechada com log 2π, γ e log 2, e vale **0,2899675923375918…**
  O excesso sobre D_2 = 0,2899645737422027… é **3,02·10⁻⁶**; o número 1,7·10⁻⁵ que dei antes estava errado.
  Esse candidato é exatamente c* arredondado a 2 casas (§3c).

## 7. Interpretação honesta

* **Mostra:** o cerco [0; 0,0050691202]; que o centro que os dados forçam é 0 com tolerância ~10⁻³; que 4 algarismos de D_N e 4 casas nos
  coeficientes já atingem a menor tolerância alcançável; e que a precisão baixa (float) fabrica um falso D_∞ = 0.
* **Não mostra:** nada sobre RH. A tolerância cai como 1/log N, e a diferença entre "D_∞ = 0" e "D_∞ = piso de um zero acima de 3·10¹²"
  só apareceria em N ≈ 10^(10²⁴).
* **Próximo passo útil:** o certificado intervalar de D_256 com 4 casas decimais (§3c), que tira a única hipótese numérica do kernel de RH.
