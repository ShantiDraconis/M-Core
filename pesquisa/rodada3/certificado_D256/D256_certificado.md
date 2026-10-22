# D_256 de Báez-Duarte: certificado intervalar (2026-10-22)

**Resultado.** Em mpmath.iv (dps 60), com extremos arredondados para fora:
D_256 ∈ [0,00823371627726102144159803810263543453410462; 0,00823371627726102144159803810263543453410463].
A largura é 5,7e−47. Em particular, **D_256 ≤ 0,00823372**, com folga rigorosa de **3,7227e−9**.
Só com coeficientes de 4 casas decimais a folga já é 1,91e−9. Isso descarrega a hipótese numérica de
`ATK.ContracaoDN.cert_Dinf_numerico`, `DN 256 ≤ 823372/10^8`, *módulo* a fórmula de Vasyunin (ver "Do que depende").

## Objeto
- H = L²(0,∞), χ = 1_(0,1], ρ_k(x) = {1/(kx)} e D_N = min_c ‖χ − Σ_{k≤N} c_k ρ_k‖² = 1 − bᵀG⁻¹b.
- O `DN 256` do Lean usa ρ₁..ρ₂₅₆, como aqui. D_255 = 0,0082338714 já fica acima de 0,00823372.
- **Dados.** ‖χ‖² = 1, b_k = (log k + 1 − γ)/k (elementar) e G_ij pela fórmula de Vasyunin.
  - Referências: Vasyunin 1995; Landreau–Richard 2002, Thm 2.1; Bettin–Conrey 2013, eq. 13.
  - No código uso a forma pareada exata V(h,k) = (1/k) Σ_{m<k/2} (2·(mh mod k) − k)·cot(πm/k), com pesos inteiros.

## Método (`gram_iv.py`, `cert_D256.py`)
1. **Entradas intervalares.** π, γ, log k e cot(πm/k) = cos/sin (16 256 valores, uma vez por k) são inflados por ±1e−50 relativo.
   - V é memoizado nos 19 947 pares coprimos. As 32 896 entradas de G e b saem por +, −, ×, ÷ em iv.
   - Larguras máximas: G 2,2e−49 e b 1,3e−50.
2. **Cota superior.** Para qualquer c, D_N ≤ Q(c) = 1 − 2bᵀc + cᵀGc.
   - Tomo c_k = n_k/10^d, com n_k inteiros: c* (solução não rigorosa em mp) arredondado. Q(c) vai em intervalos.
   - A cota não depende de como c foi escolhido.
3. **Cota inferior.** Q(c) − D_N = (c−c*)ᵀG(c−c*) = rᵀG⁻¹r ≤ ‖r‖²/λ_min(G), com r = Gc − b.
   - Com c = c* em 30 casas (`coef_d30.txt`), ‖r‖² ≤ 1,42e−60 (intervalar).
   - **λ_min(G) ≥ μ = 1,93e−5** (estimado: 1,9454e−5), certificado de dois modos independentes:
     - (a) **Resíduo de Rump.** R = inteiros/2^219 ≈ Cholesky de mid(G) − μI. RRᵀ é calculado **exatamente** em inteiros.
       E = G − μI − RRᵀ vai em iv, com ‖E‖_F ≤ 2,6e−48. Como RRᵀ ⪰ 0, vale λ_min ≥ μ − ‖E‖_F.
     - (b) **Cholesky intervalar de G − μI.** Pivôs com extremo inferior > 0 dão G − μI ≻ 0, pela isotonia de inclusão.
       - Em dps 60 **falha** na coluna 115, por efeito de embrulho: a largura do pivô cresce ≈ ×2,9 por coluna.
       - Em dps 170 **passa**: as larguras vão de 7e−160 a 1,7e−41, e o menor pivô tem extremo inferior 5,96e−6.
   - Daí D_256 ≥ inf Q(c₃₀) − 7,4e−56.

## Cotas superiores com coeficientes curtos (`coef_*.txt`, linhas `k n_k`, c_k = n_k/10^d)
| escolha de c | sup Q(c) (rigoroso) | Q − D | folga a 0,00823372 |
|---|---|---|---|
| 4 casas, arredondamento ao mais próximo | 0,0082337180854519 | 1,81e−9 | **1,9145e−9** |
| 4 casas, plano mais próximo de Babai | 0,0082337167529579 | 4,76e−10 | 3,2470e−9 |
| 5 casas | 0,0082337163051655 | 2,79e−11 | 3,6948e−9 |
| 6 casas | 0,0082337162774353 | 1,74e−13 | 3,7226e−9 |
| 30 casas (envelope) | 0,00823371627726102144… | < 1e−55 | 3,7227389785e−9 |

- `verifica_coef.py` relê os arquivos de 4–6 casas e refaz a soma dupla noutra ordem; confere.
- Para uma prova formal só da cota superior com `coef_d4.txt`: Σ|c_k| = 62,52 e (Σ|c_k|)² = 3909.
  - Basta conhecer cada G_ij com erro ≤ 4e−13 e cada b_k com erro ≤ 1e−11; não é preciso λ_min nem c*.

## Do que depende o rigor
1. **A fórmula de Vasyunin** para G_ij é teorema publicado, não formalizado no kernel. b_k e G_ii são cálculo elementar.
2. **mpmath.iv arredonda para fora** em +, −, ×, ÷, √ e nas conversões de inteiro e decimal (`mpf_*` com arredondamento dirigido).
3. **Rotinas transcendentes de mpmath** (π, γ, log, cos, sin a 203 bits): só precisam acertar **50 dígitos relativos**, graças à inflação.
4. **Aritmética inteira exata do Python** no passo de Rump.
5. O rigor **não** depende de c*, da estimativa de λ_min, do arredondamento de Babai nem dos controles.

## Controles (`controls_D256.py`, `controls_D256.out`; todos passaram)
- **G₁₁:** [G₁₁] contém log 2π − γ (mp com 100 dígitos), com largura 6,8e−50; [G_ii] contém (log 2π − γ)/i para todo i.
- **V:** a definição completa (soma em m < k, em iv) contra a forma pareada, em 10 pares até (255,256): os intervalos se intersectam.
- **Double independente:** as 32 896 entradas, com a definição completa de V, diferem ≤ 2,4e−14.
- **Código C da wave2 (`RH_Gram_dn`, DUMPG):** em 2940 entradas, |dif|/|G| ≤ 1,2e−31 (binary128) e ≤ 5,5e−29 (dd).
  - Isso é o erro do próprio C, já que [G] tem largura ~1e−49.
- **Integração direta (mp.quad, dps 40, não rigorosa):** G em (1,1), (1,2), (2,3), (3,5), (5,7), (4,6), (7,10), (6,9) e b₁, b₃, b₁₀ diferem ≤ 4,9e−42.
- **D_256 do C:** o dd fica a 1,2e−30 do envelope (1,5e−28 relativo) e o binary128 a 2,1e−33 (2,5e−31).
  - A referência 0,0082337162772610214415980381 é o envelope arredondado.

**Tempos** (nice 10, 1 núcleo, Python puro):
- `cert_D256.py 256 60 rump`: 27 s no total (entradas 15 s, c* 3 s, cada Q(c) 0,5 s, Rump 5 s).
- `cert_D256.py 256 170 both`: 57 s (Cholesky intervalar: 24 s). Controles: 98 s. `verifica_coef.py`: ~16 s por arquivo.

**Arquivos (nesta pasta):**
- Código: `gram_iv.py`, `cert_D256.py` (`N dps rump|ivchol|both`), `verifica_coef.py`, `controls_D256.py`.
- Saídas: `cert_D256_dps60.out`, `cert_D256_dps170_both.out`, `cert_D256_result_*.json`, `controls_D256.out`, `verifica_coef.out`.
- Coeficientes: `coef_d{4,4_babai,5,6,8,30}.txt`. O cabeçalho diz dps 170 (última escrita); os n_k são os mesmos em dps 60.
