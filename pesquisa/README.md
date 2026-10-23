# Programa de pesquisa ATK — mapas de fronteira e testes (22/10/2026)

Esta pasta **não é importada pelo kernel** (`atk-kernel/`). Ela guarda a pesquisa que alimenta os produtores:
mapas do que é conhecido e do que falta, testes numéricos e combinatórios baratos, e revisões independentes
dos achados que pareciam novos. Nada aqui prova uma conjectura; números finitos não decidem enunciados assintóticos.

* `fronteira/<TÓPICO>_frontier.md` — estado da arte (out/2026), perguntas atacáveis, o que precisa ser criado, testes propostos.
* `testes/` — 1ª rodada: um relatório por teste (`<TÓPICO>_T<n>.md`), código em `testes/codigo/`, saídas em `testes/saidas/`.
* `rodada2/` — 2ª rodada: revisões independentes (NS, Hodge) e o cálculo exato de D_N (RH); dados em `rodada2/dados/`.
* `rodada3/` — RH: centro, tolerância, precisão e cauda de D_∞ (`RH_centro_Dinf.md`); certificado intervalar de D_256 (`certificado_D256/`).
* `rodada4/` — RH: lado material da prova formal de Bohr–Landau (`RH_BohrLandau_material.md`): média quadrática de ζ, contagem de Jensen e a constante efetiva; 1/2 como incógnita (`RH_zero_incognito.md`): o sistema Re ζ = Im ζ = 0 resolvido sem fixar 1/2; truncamento inexato e limite exato, sistema (k, d, y) (`RH_truncamento_zero.md`); o sistema paramétrico e a zeta trocada, provados e certificados (`RH_texto_parametrico_certificado.md`).
* `rodada5/` — Closed Math completo (modelo, toro, tempos verbais, redução terminal de HR a somas finitas): `RH_closed_math.md`; espelhos em `formatos/` (Coq, Isabelle, SMT-LIB, TPTP).

Os caminhos absolutos dentro dos scripts são os do ambiente onde rodaram (máquina de 2 núcleos, sem numpy/PyPI;
mpmath/sympy/networkx puros, CaDiCaL e gcc).

## Resultados

Em cada linha, o controle (resultado conhecido reproduzido) vem antes do que é novo.

| Tópico | Teste | Controle | Resultado |
| --- | --- | --- | --- |
| NS | T2 + revisão | Lei–Lin κ* ≥ 1 recuperado; derivada temporal conferida | **Limiar de Lei–Lin melhorado de ν para 3ν/2** (argumento angular + lema de Björck); √2·ν conferido passo a passo. Não achado na literatura (pode ser folclore). Teto do método ≈ 3,5ν. |
| NS | T1 | — | Expoentes da explosão forçada (OpenAI, caso C) não violam Leray/Serrin/BKM/CKN; duas correções ao mapa (CKN, barreira B4). Só consistência dimensional. |
| RH | rodada 2 | Fórmula de Vasyunin = integração direta (4e−44) | **D_N para todo N ≤ 8000** (~24 dígitos): D_8000 = 0,0050691202; D_256 = 0,0082337162773 (confirma a hipótese numérica do kernel, folga 3,7e−9). D_N·log N ∈ [0,96; 1,01]·(2+γ−log 4π). Lei por passo η_N ≥ c/(N+1) é falsa (Burnol); por passo η_N ≥ c/(N log N) só com c ≤ 6e−8 nos dados. As três leis estão decididas no kernel em `ATK.LeisDeGanho` (PR #60). |
| RH | rodada 5 | contornos 3 e 6, Gauss–Bonnet, corda e cilindro dos anexos (10⁻¹⁵); 22 testes pytest | **Closed Math fechado no escopo modelo** (`UGModelo` provado, ~165 teoremas novos): toro (HR ⟺ zeros no equador interno; curvatura mínima −1/(r(R−r)) na linha), princípio do argumento para multiconjuntos, ordem 3 no encontro de `H`; **`rh_iff_criterioEM`: HR ⟺ desigualdade de somas finitas de Euler–Maclaurin em todo K_n** — a redução não prova HR. **Fase 3: primeiro zero certificado no kernel** (`zero_na_linha`: Re ρ = ½, |ρ − (½+14,1347251417i)| ≤ 10⁻⁶, único no disco) ⇒ `Z` não vazio, incondicional; Jensen/Turán formalizado, com a correção TP∞(aₙ) e não TP∞(γₙ); **`δ₅ > 0` certificado** (`|ζ| ≥ 1/10` em K₅, 450 discos no kernel). |
| RH | rodada 6 | G₁₂ pela forma fechada = soma de degraus (3·10⁻⁵⁹); D₁, D₂, C₀, zeros 2 e 3 numéricos; 10 testes | **319 teoremas novos** (`RH_closed_math.md` §4j–4l): **G₁₁ = log 2π − γ, G₁₂ = ¾(log 2π−γ) − ¼ log 2, γ ∈ (0,5772156; 0,5772163) certificado, D₂ ∈ (0,2899; 0,2900) ⇒ D_∞ < 0,29** (primeira cota numérica incondicional); **2º e 3º zeros certificados na linha** (21,0220396388 e 25,0108575801, ±10⁻⁶); zeros triviais simples; ξ′/ξ com digama; teste do disco de Jensen; critério de sinal (direção suficiente); critério de somas parciais de η; barreira, modelo log e ajuste de dois pontos (intercepto < 0); K₆, métricas, Hodge/Bogomolny, coeficiente líder de BSD ≠ 0; 13 erros dos textos registrados (vários com contraexemplo formal). Nada disso prova HR. |
| RH | rodada 4d | 18/18 valores do modelo em racional exato; \|ζ(Tρₙ)\| do texto a 5·10⁻¹², dentro do envelope provado | **Sistema paramétrico provado** (47 teoremas): troca, centro, k_N, derivadas, integrais, semântica; \|ζ(s) − 1\| ≤ 2^{−σ} + 2^{1−σ}/(σ−1); `exato_de_toda_tolerancia`: um número fixo aproximado em toda tolerância é exato. |
| RH | rodada 4c | \|ρ_N − ρ\| = N^{−1/2}/(2\|ζ′(ρ)\|) previsto e medido (1–3%) | **Truncamento inexato, limite exato**: zeros de ζ_N têm ε_N ≠ 0, oscilando nos dois lados, e o limite é zero exato de ζ (`ATK.TruncamentoZero.limite_de_zeros_truncados`). Eixo de simetria único sem supor zeros na reta (`eixo_unico`); RH ⟺ o sistema (k, d, y) sem solução (`rh_iff_sem_solucao`). |
| RH | rodada 4b | Argumento = trocas de sinal de Z(t) (29 até 100, 138 até 300) | **1/2 como incógnita**: Σ(β − κ) = 0 ⟺ κ = 1/2, provado sem RH (`ATK.ZeroIncognito.incognita_resolvida`); dispersão Σ(β − 1/2)² ≤ δ²N(T) + C_δT; RH ⟺ dispersão nula. Busca livre (β, γ incógnitos): 138 soluções até γ = 300, todas com \|β − 1/2\| < 10⁻¹². |
| RH | rodada 4 | ζ(2), 1º zero, ζ(1/2+10i) a 10⁻¹⁵ | **Bohr–Landau provado no kernel** (`ATK.BLProva.bohrLandau`, PR #67). A média quadrática bate com os dois termos clássicos (~1%). A constante da prova para δ = 1/4 é C ≈ 734 com M numérico; a densidade só morde a partir de T ≈ 10²⁰⁰⁵ (teorema qualitativo). |
| RH | T1, T2 | Inclinação clássica −(2σ−1) recuperada | O desenho F = ζ·R do mapa é mal posto (piso positivo provado); substituído por F = ζ(1 − 2^{β₀−s}), em que o ótimo segue −2(σ−β₀). |
| Hodge | T1 + revisão | dim Hdg para m = 3..6; R_33 = 1 órbita | (P_m⁴) vale para m par ∈ {22,24,26,28,30,34,38,46,58,74,82,86,94,98} — confirmado por reimplementação, **mas todos já conhecidos** (Aoki). Hipótese H1 do mapa refutada. Possível novidade: família m = 4q com certificado de 2 pares (m ∈ {44,52,66,68,76,78,88,92}); m = 70 segue aberto. |
| BSD | T4 | L(E,1) = ϖ/4 (35 dígitos); c₂ = 2 por Tate | `formula_E32_iff` é numericamente verdadeira (o período do kernel é 2ϖ); sem erro de fator 2. |
| Beal | T1 | 11,43% e 16,79% do kernel reproduzidos | Cobertura em {3..200}³: 27,17% (Darmon–Merel sobre ℤ) → 66,00% (literatura) → 71,17% (com Fermat–Catalan forte). Assinaturas abertas mais valiosas: (2,5,11), (2,3,11), (2,5,7). |
| Beal | T2 | p = 3 acha soluções (como deve) | Nenhum contraexemplo à Fermat–Catalan forte para p = 5 (|x|,|y| ≤ 8000) e p = 7 (≤ 5000). Evidência fraca. |
| P vs NP | T1 | Tabelas de Knuth (B2) e 3(n−1) para XOR (U2) | No modelo ATK: XOR_n = 4(n−1) para n = 2,3,4 (n = 4 com uma restrição deduzida, não formal); MAJ₃ = 4, MAJ₅ = 10. |
| YM | T1 | ℤ₂: ½·artanh(1/(3(d−1))) com 12 dígitos | Limiares exatos de Dobrushin para ℤ₃, ℤ₄, S₃, Q₈, SU(2); SU(2) em forma fechada c(β) = L₁(2β)/I₁(2β). A cota do projeto `lgt` fica 5–14× abaixo. |
| YM | T3 | Acoplamento forte: gap → −4 log tanh β | ℤ₂ em 2+1D, L = 2,3,4: o gap **não** é uniforme em L além de β ≈ 0,21. |
| Collatz | T1 | c₁ = 1/3, c₂ = 2/63, c₃ exatos | Lei exata de Syrac(ℤ/3ⁿ) até n = 16; o máximo de Fourier cai como ~n^{−2,1}, sem decaimento exponencial visível (não contradiz Tao). |
| Poincaré | T2 | — | Leitura estática parcial de duas formalizações externas: enunciados usam a topologia real da Mathlib; nenhuma ocorrência de axiom/sorry nos ~430 arquivos lidos; build e Comparator não executados aqui. |

## Correções a textos de terceiros (registradas para não se repetirem)

* b_k = ⟨χ, ρ_k⟩ = (log k + 1 − γ)/k (certificado em `ATK.BaezDuarteVetorB.b_formula`); a versão com −log k está errada.
* ‖ρ₁‖² = log 2π − γ; a versão "log 2π − γ − 1" omite ∫₁^∞.
* D₁ = 0,858212051396, ⟨ρ₁,ρ₂⟩ = ¾(log 2π − γ) − ¼ log 2 = 0,772209255991, D₂ = 0,289964573742.
* O candidato (−0,83; 1,90) tem erro exato E = 0,289967592338 (forma fechada), 3,02·10⁻⁶ acima de D₂ (não 1,7·10⁻⁵).
* Identidades de Gram, independência dos ρ_k, D_N = 1 − bᵀG⁻¹b e a lei D_{N+1} = (1−η_N)D_N **já estão no kernel**
  (`GramBaezDuarte`, `CapturaRH`); "a soma dos ganhos esgota D₁" é a própria O1 (`CapturaRH.captura_log_iff`).
