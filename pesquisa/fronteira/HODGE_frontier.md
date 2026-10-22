# HODGE: fronteira de pesquisa (estado em 2026-10-21)

Base no corpus (dossier `HODGE_summary.md`): **P0 = P1 = 0**. O que é genuíno é só álgebra linear sobre `ATK.L3Base.HodgeStructure` (HodgeFiltracao: Hdg = V_ℚ ∩ F^p, F^p ∩ F̄^p = H^{p,p}, `hodgeClasses_eq_top`) e o exemplo HodgeToro. `ATK.HodgeOficial` enuncia HC com objetos da Mathlib (Scheme, `SmoothOfRelativeDimension`, `AlgebraicCycle X ℚ`, `singularHomologyFunctor`), mas analitificação, decomposição de Hodge e `cl` entram como **dados** (`ConstrucoesHodge`). O próprio kernel prova que com `cl = 0` o enunciado degenera (`hodge_cl_zero_iff`, `zero_coerente`).

## 1. Estado da arte (out/2026)
**Clássico (enunciado oficial do Clay, por Deligne).** Toda classe em H^{2p}(X,ℚ) ∩ H^{p,p} é ℚ-combinação de cl(Z).
- **Casos conhecidos.** O caso H² sai da sequência exponencial (Lefschetz 1924, completado por Kodaira–Spencer). Por Lefschetz difícil vale também em grau 2n−2, e logo em dim X ≤ 3.
- **Primeiro caso aberto (Totaro, 2026).** Codimensão 2 em dimensão 4.
- **Questões laterais abertas.** Não se sabe se o locus de Hodge é definido sobre ℚ̄. Não há algoritmo conhecido para detectar classes de Hodge numa família. Até as classes "triviais" (a diagonal, as inversas de Lefschetz) estão em aberto.

**4-folds conhecidos.**
- Cúbicas (Zucker 1977).
- Unirracionais (Murre 1977) e unirregradas (Conte–Murre 1978): quárticas e quínticas.
- CH₀ suportado em dimensão ≤ 3 (Bloch–Srinivas 1983): várias interseções completas de gênero geométrico 0. Survey: da Silva, arXiv 2105.04695.

**Abelianas: avanço maior do período.**
- **Antes de 2025.** E^n (Murasaki 1969); simples de dimensão prima (Tankeev 1982); o tipo Weil só em casos parciais (Schoen, van Geemen).
- **Markman, arXiv 2502.03415 (fev/2025, v2 jun/2025).** Thm 1.5.1: as classes de Weil são algébricas em 6-folds abelianos polarizados de tipo Weil com discriminante −1, para todo K = ℚ(√−d). O método usa feixes "secantes" semirregulares (Buchweitz–Flenner) e a transformada de Orlov. Cor. 1.6.1: **HC para todos os 4-folds abelianos**, via a degeneração de Schoen e as reduções de Moonen–Zarhin.
- **Dimensão ≤ 5.** HC para abelianas de dimensão ≤ 5 segue disso, segundo Markman 2509.23403 e o post de Totaro no blog de Tao (11/09/2026).
- **Confirmação independente parcial.** Floccari–Fu, 2504.13607 (v2 em 10/02/2026), reprovam o caso de discriminante 1 via variedades OG6 singulares.
- **Ressalva interna.** A versão torcida da semirregularidade (Conj. 7.3.9) está provada só para famílias de abelianas (§7.4).
- **Ainda aberto.** 6-folds de Weil com disc ≠ −1 ("completamente aberto", segundo Mostaed, 2603.20268, que propõe um "caminho decidível" via a curva de McMullen, não uma prova) e abelianas de dimensão ≥ 6 em geral. Markman 2509.23079 dá um critério para multiplicação real, mas sem a semirregularidade provada.
- **Potências de 4-folds CM.** Li, 2609.27916 (set/2026): HC para potências de 4-folds abelianos CM e Tate para potências de abelianas de dimensão ≤ 4 sobre 𝔽_q, via Markman e o critério de Milne.

**IA (2026): a notícia mais importante para este tópico.**
- **O preprint.** "The rational Hodge conjecture for CM abelian varieties", datado de 30/09/2026 e publicado em 06–07/10/2026 em github.com/openai/math (família 032). Afirma HC racional para **toda** abeliana CM, suas potências e seus produtos. Corolários declarados: Tate para abelianas sobre 𝔽_q (via Milne) e a conjectura padrão de Hodge para abelianas em qualquer característica.
- **Status.**
  - Sem revisão por pares.
  - Sem escopo Lean documentado para a família 032.
  - O campo de revisão do catálogo diz "unchecked" (Pebblous, 13/10).
  - Em 07/10 foram retirados os manuscritos-irmãos (Kuga–Satake para K3, HC para produtos de K3, classes de Weil em 8-folds split) por um erro de sinal num argumento de "stabilization-trace cancellation". O manuscrito CM foi mantido e a família, renomeada.
  - Só há reações preliminares (Saha, Lozano-Robledo, Buzzard: "We do not yet even know what is true").
- **Outros posts e boatos.** Voisin (post convidado no blog de Tao, 12/09) chama Markman de "big recent progress" e acha improvável que a semirregularidade baste para a HC variacional. Nos comentários, R. Thomas relata um boato de prova, feita por IA, da HC tropical para abelianas tropicais (não checada).
- **Inferência nossa, a verificar.** Pela estrutura indutiva de Shioda–Katsura, X_m^n é dominada racionalmente por (X_m^1)^n, e J(X_m^1) é de tipo CM. Logo o resultado 032, se correto, implicaria HC para **todas** as variedades de Fermat. Isso faz do teste T1 um teste de consistência concreto para o 032.

**Fermat X_m^n.**
- **Casos resolvidos.**
  - Shioda 1979: m ≤ 20, m primo, m = 4.
  - Aoki: m = p².
  - da Silva, 2101.04739: X_m^4 com mdc(m,6) = 1; X_21^n e X_27^n. Mostra também que a condição (P_33) falha.
  - **Jumagulov, 2608.18134 (jul–ago/2026):** X_m^4 para todo m ímpar ≤ 199, com prova assistida por computador e **por IA** e certificados por órbita. O censo dá 13 órbitas "excepcionais" além das decomponíveis, quase-decomponíveis e de Aoki. Há trechos de prova truncados.
  - **Favero–Kelly, 2609.12759 (set/2026):** X_33^4, com ciclos novos (scrolls racionais da cúbica de Billi–Grossi–Marquand, puxados por um mapa de Shioda). Usam uma fórmula de ch_k de fatorações de matrizes no anel Jacobiano.
- **Até onde vimos nas fontes lidas, ninguém cobre X_m^4 com m par ≥ 22.**
- **Integral.** Aljovin–Movasati–Villaflor (1711.02628, J. Symb. Comp. 2019) verificam HC integral para X_4^4 e X_5^4. Em (4,6) o cálculo é inconclusivo: mais de 2 dias de Singular e 56 GB de swap.

**Loci de Hodge.**
- Cattani–Deligne–Kaplan 1995: o locus de Hodge é uma união enumerável de subvariedades algébricas. Bakker–Klingler–Tsimerman (JAMS 33, 2020) reprovam isso por o-minimalidade.
- Baldi–Klingler–Ullmo (2107.08838): em nível ≥ 3 o locus de período positivo é união finita de subvariedades especiais. Exemplo: hipersuperfícies, sob condições sobre (n,d).
- Voisin (math/0605766): componentes definidas sobre corpos de números sob hipóteses; HC para classes absolutamente de Hodge se reduz ao caso de corpos de números.
- Deligne: classes de Hodge em abelianas são absolutamente de Hodge (Charles–Schnell 1101.3647). HC = (Hodge ⇒ absolutamente Hodge) + (absolutamente Hodge ⇒ algébrica).
- Movasati–Villaflor (1705.00084): fórmula fechada dos períodos de ciclos lineares em Fermat. O locus de [P1]+[P2] (P1 ∩ P2 = P^m) é liso, reduzido e igual ao locus das hipersuperfícies que contêm P1 ∪ P2 **só para uma lista finita** de (n,d,m), verificada em Singular. O caso geral depende da sua Conj. 1, um problema de posto "elementar" ainda em aberto.
- Duque–Villaflor (2112.14818): **ciclos lineares falsos** existem para d = 3, 4, 6, o que refuta a Conj. 18.8 de Movasati. Para d ≥ 2 + 6/n e d ∉ {3,4,6} não existem.

## 2. Barreiras e resultados no-go
1. **Kähler.** A HC é falsa para Kähler não projetivas: toros de Zucker; Voisin, math/0112247, mostra que nem classes de Chern de feixes coerentes bastam. Toda prova tem de usar a projetividade de forma essencial, e informação puramente de Hodge ou Kähler não basta.
2. **Integral.**
   - Torção: Atiyah–Hirzebruch 1962.
   - Não-torção: Kollár (hipersuperfícies em ℙ⁴).
   - Enriques × curva (Benoist–Ottem, CMH).
   - **ppav muito gerais de g ≥ 4:** toda curva é múltiplo **par** da classe mínima, e para g = 4, 5 a imagem é 2ℤ·Θ^c/c! (Engel–de Gaay Fortman–Schreieder, 2507.15704).
   Só ℚ é viável.
3. **Método indutivo de Griffiths.** Bloqueado pelo grupo de Griffiths de posto infinito (Voisin; enunciado do Clay).
4. **Semirregularidade.** É provavelmente insuficiente para a HC variacional em geral (Voisin 2026).
5. **Via tropical de Kontsevich (Zharkov 2002.02347).** Brosnan (2609.14169) mostra que degenerações maximais de 2n-folds de Weil exigem disc = (−1)^n, e isso Markman já cobre para n = 2, 3. A via não dá contraexemplo nessas dimensões; restam as degenerações "uma a menos que maximal".
6. **Primeira ordem não determina ciclos.** Os ciclos lineares falsos mostram que o espaço tangente do locus de Hodge, sozinho, não certifica algebricidade. Todo teste infinitesimal precisa de uma confirmação de segunda ordem.
7. **CDK, BKT e BKU.** Os loci de Hodge já se comportam "como se HC valesse", então um contraexemplo não aparecerá como locus não algébrico.

**Rotas do corpus já excluídas.**
- **(i) Teoremas sobre `HodgeStructure` abstrata** (HodgeFiltracao, HodgeToro, L3Base). Nunca implicam HC: a barreira 1 dá estruturas de Hodge de toros não algébricos com classes de Hodge e sem ciclos, e o próprio `hodge_cl_zero_iff` diz o mesmo.
- **(ii) A rota métrica de Kähler** (`KahlerLocal`). Barreira 1.
- **(iii) Qualquer enunciado com coeficientes ℤ.** Barreira 2.
- **(iv) `KnownCases ∧ MiddleCodimension`.** É logicamente correto, mas `MiddleCodimension` *é* a HC para 2 ≤ p ≤ n−2, então não há redução alguma.
- **(v) "Casos conhecidos" com `isAlgebraic := ∃ Z, True`.** São vácuos.

## 3. Questões atacáveis, ordenadas por valor × tratabilidade
- **Q1 (a, nova matemática, computacional; alta × alta). HC para X_m^4 com m par, 22 ≤ m ≤ 64.**
  - *Enunciado.* B_m^4 é o conjunto de caracteres a ∈ (ℤ/m∖0)^6 com Σa ≡ 0 tais que Σ_i⟨t·a_i⟩ = 3m para todo t ∈ (ℤ/m)^×. A pergunta é se toda órbita de B_m^4 é decomponível ou quase-decomponível (a condição (P_m^4) de Shioda/da Silva). Para cada órbita residual, achar Z ⊂ X_m^4 com projeção de cl(Z) ≠ 0 em V(α): ciclos padrão de Aoki, scrolls de Favero–Kelly, ou ch₂ de fatorações de matrizes.
  - *Por que importa.* É o primeiro caso aberto (codim 2, dim 4) numa família CM concreta e serve de teste de consistência para o OpenAI-032 e para o censo de Jumagulov (assistido por IA).
  - *Progresso.* Lista exata de R_m (T1) e, para cada órbita residual, um ciclo com certificado exato de período.
- **Q2 (a; alta × média). Conj. 1 de Movasati–Villaflor e o locus de [P1] + r[P2].**
  - *Enunciado.* Para n par, d ≥ 3, −1 ≤ m ≤ n/2 − 2 e r ∈ ℚ^×, vale codim T_0V_λ = codim do locus das hipersuperfícies que contêm deformações de P1 ∪ P2? (Assim V_λ é liso e reduzido, e a HC variacional vale localmente.)
  - *Forma algébrica.* Com sistemas inversos de Macaulay e f_i = P_{P_i}, vale Ann(f_1 + r f_2)_d = (Ann f_1 ∩ Ann f_2)_d + J_d no anel de Fermat? É um problema de "soma conexa" de álgebras de Gorenstein, possivelmente provável em geral.
  - *Progresso.* Uma prova, ou um contraexemplo, isto é, uma componente nova ou não reduzida (T2).
- **Q3 (b, formalização do conhecido; média × alta). D^p = B^p para E^n.** O anel de Hodge de E^n é gerado por classes de grau 2 (Murasaki/Tate), e as classes de Weil existem num 4-fold de tipo Weil e não estão em D² (Weil 1977). Tudo como teoremas sobre estruturas de Hodge em ∧^k(H¹)^{⊕n}, generalizando HodgeToro. *Por que importa.* Seria o primeiro teorema estrutural não vácuo: HC(E^n) fica reduzida a **um único** insumo geométrico, Lefschetz (1,1), que vira ponte honesta com status PUBLICADA_NAO_FORMALIZADA.
- **Q4 (b; média × média). Lefschetz (1,1) para toros ℂ^g/Λ na forma Appell–Humbert.**
  - Toda E ∈ ∧²Hom(Λ,ℤ) com E(ix,iy) = E(x,y) é c₁ de um fator de automorfia (H = E(i·,·) + iE).
  - E > 0 ⟺ polarização (relações de Riemann), logo NS ⊗ ℚ = Hdg¹.
  - Não precisa de cohomologia de feixes; a identificação com o c₁ da sequência exponencial fica como ponte nomeada.
- **Q5 (a, computacional; média × média). HC integral para X_6^4 e X_7^4.** AMV param em d = 5. A pergunta é se o reticulado L dos ciclos lineares é saturado em H⁴(X,ℤ) ∩ H^{2,2} (T4).
- **Q6 (a; muito alta × baixa). Classes de Weil em 6-folds de Weil com disc ≠ −1.** Inclui os pontos CM do locus de Weil de Mostaed e as degenerações parciais sugeridas por Brosnan. É o próximo passo além da dimensão 5.
- **Q7 (b, infraestrutura; muito alta × baixa). Uma `ConstrucoesHodge` genuína, ao menos o pedaço c₁.** X(ℂ) com a topologia clássica, a cohomologia singular com cup product, e c₁: Pic(X) → H²(X(ℂ),ℤ) pela sequência exponencial com a comparação de feixes com a cohomologia singular. Com isso, Lefschetz (1,1) vira um enunciado da Mathlib não paramétrico.

## 4. O que precisa ser criado
- **C1 — `HodgeStructure` completa.** Morfismos, ⊗, dual, ∧^k, twist de Tate, polarização (Hodge–Riemann), operador de Weil e a ação h: U(1) → GL(V_ℝ). Com isso "Hodge = invariante de h(U(1))" e o fechamento de Hdg sob ⊗ e ∧ viram teoremas (base para Q3).
- **C2 — `ComplexTorus Λ J` em dimensão g.** H¹ := Hom(Λ,ℚ) com a estrutura de Hodge induzida por J e H^k := ∧^k H¹, rotulado como **modelo**: verdadeiro para toros, mas definicional aqui. Mais as relações de Riemann e Appell–Humbert (Q4).
- **C3 — Biblioteca de Fermat e CM.**
  - Caracteres de Shioda, tipo de Hodge por |tα| e o semigrupo M_m.
  - Decomponível e quase-decomponível.
  - Períodos de ciclos lineares (Movasati–Villaflor Thm 1) em ℚ(ζ_{2d}).
  - Somas de Jacobi (verificar o que já existe em `Mathlib.NumberTheory`).
- **C4 — Formato de certificado de algebricidade para classes CM.** Uma tupla (órbita α, ciclo Z, tipo de construção, identidade exata em ℚ(ζ) mostrando ⟨cl(Z), V(α)⟩ ≠ 0), verificável no kernel por `decide` ou `norm_num` sobre ciclotômicos.
- **C5 — Condicional honesto `TeoremasClassicos`.** Uma estrutura cujos campos são **teoremas publicados** (isomorfismo do resíduo de Griffiths, fórmula de períodos de Carlson–Griffiths, estrutura indutiva de Shioda, critério (P_m^n)), com referências, para provar dela "HC(X_m^4) para m ∈ S". As hipóteses são teoremas, não a conclusão; é o oposto de `HodgeBridge`.
- **C6 — Infraestrutura Mathlib (longo prazo).** Inventário verificado:
  - **Existe:** `AlgebraicCycle`, `singularHomologyFunctor` (usados no kernel); cohomologia de feixes como Ext (`Sheaf.H`, ainda com TODOs de comparação); `extDerivWithin` só em espaços normados.
  - **Não existe:** formas diferenciais em variedades ("in progress, help welcome", Rothgang, dez/2025), variedades complexas como feature, analitificação, de Rham, Dolbeault, teorema de Hodge e Poincaré dualidade/classe fundamental (não encontrados).
  - **Ordem mínima para Q7:** topologia em X(ℂ) via imersão em ℙ^N(ℂ), independente da imersão → anel de cohomologia singular → exponencial e c₁ → comparação feixe–singular.

## 5. Testes baratos (especificados, não executados)
**T1 — Censo de caracteres de Hodge em X_m^4, 3 ≤ m ≤ 64.** Python + numpy, ~5–10 min.
- *Entrada.* m.
- *Cálculo.*
  1. Enumerar 6-uplas não decrescentes a ∈ {1..m−1}^6 com Σa ≡ 0 (mod m): ~1,6·10⁶ para m = 64.
  2. Testar Hodge: ∀t ∈ (ℤ/m)^×, Σ⟨t a_i⟩ = 3m. A dimensão de Hdg²_prim é a soma das multiplicidades por permutação.
  3. M_m(c): ∀t, 2Σ⟨t c_i⟩ = |c|·m (comprimento par, y constante). Note que M_m(1) = pares {β, m−β}.
  4. Decomponível: ∃ c ⊊ a com |c| ∈ {2,4} e c ∈ M_m.
  5. Quase-decomponível: ∃β, a ⊎ {β, m−β} = c ⊎ d com c, d ∈ M_m não vazios e c, d ≠ a.
  6. R_m := órbitas sob (ℤ/m)^× que não são nem uma coisa nem outra.
- *Saída.* dim Hdg²_prim, o número de órbitas, |R_m| e os representantes.
- *Validação.*
  - m = 3 → 20; m = 4 → 141 (AMV dá posto 142 com h²).
  - mdc(m,6) = 1 → R_m = ∅ (da Silva, Prop. 3.1); m = 21, 27 → ∅; m = 33 → ≠ ∅.
  - Para m ímpar, comparar com o censo de Jumagulov.
- *Hipótese H1.* Para m par em [22,64], R_m ≠ ∅ só se 3 | m.
- *O que é informativo.*
  - Cada m par com R_m = ∅ é um **novo caso** de HC (computacional) via (P_m^4).
  - Cada órbita residual vira alvo para Q1 e uma pergunta concreta ao manuscrito 032.
  - Uma divergência do censo de Jumagulov aponta um erro nele.

**T2 — Loci de Hodge de λ = [P1] + r[P2] no Fermat X_d^n.** Python + python-flint (`nmod_mat`), ≤ 20 min.
- *Ciclos.* P_{a,b} = {x_{b_{2e}} = ζ_{2d}^{1+2a_{2e+1}} x_{b_{2e+1}}}. P2 usa o mesmo b e coincide com P1 em k pares, de modo que m = k − 1.
- *Funcional (Movasati–Villaflor, Thm 1).* Para |i| = D := (n/2+1)d − n − 2: ℓ_P(x^i) = sgn(b)·ζ_{2d}^{Σ_e (i_{b_{2e}}+1)(1+2a_{2e+1})} se i_{b_{2e}} + i_{b_{2e+1}} = d − 2 para todo e, e 0 caso contrário. A constante comum é omitida.
- *Matrizes.* A[F,G] = ℓ_λ(x^{F+G}) com F ∈ Mon_d e G ∈ Mon_{D−d}. Então rank A = codim T_0V_λ.
- *Comparação.* c_alg = dim ℂ[x]_d − dim((I_{P1} ∩ I_{P2})_d + J_d), com J_d = ⟨x_j x_i^{d−1}⟩.
- *Corpos.* Trabalhar em 𝔽_p com p ≡ 1 (mod 2d), usando dois primos.
- *Faixa.* n = 4: d = 3..10, m ∈ {−1, 0}; n = 6: d = 3..6, m ≤ 1; n = 8: d = 3, 4, m ≤ 2; r ∈ {1, −1, 2}. As matrizes vão até ~3000 × 19000.
- *Validação.*
  - Ciclo único: rank = C(n/2+d, d) − (n/2+1)².
  - Reproduzir as triplas da lista de Movasati–Villaflor.
  - rank A > c_alg indica bug.
- *Hipótese H2.* rank A = c_alg em toda a faixa.
- *O que é informativo.* Cada caso com rank A < c_alg é um candidato a componente falsa ou não reduzida (e então se faz o teste de segunda ordem). A igualdade estende o Thm 2 deles.

**T3 — Certificado Lean do censo para m pequeno.** Lean 4.34.1 + Mathlib, sem `native_decide`, ≤ 20 min.
- *Definições (sobre `List ℕ`).* `IsHodge6 m a`, `InM m c`, `Dec`, `QDec`.
- *Certificados.* O T1 exporta, por órbita, uma testemunha (c) ou (β, c, d).
- *Teorema.* `∀ a, a ∈ sortedZeroSum6 m → IsHodge6 m a → Dec m a ∨ QDec m a`, por `decide`. A completude é checada sobre todas as 6-uplas ordenadas, sem precisar da ação de grupo.
- *Medida.* Tempo de kernel para m = 5..16 e o expoente de escala.
- *Hipótese H3.* `decide` é viável até m ≈ 12–16.
- *O que é informativo.* Decide se certificar o censo até m = 64 ou 199 exige um verificador refletido próprio. O lema resultante é combinatório honesto (classe V, explicitamente sem variedade) e entra em C5.

**T4 — Reticulado integral dos ciclos lineares em X_d^4, d = 4..7.** Python + flint, ≤ 20 min para d = 7.
- *Dados.* N = 15d³ planos (5145 para d = 7) mais Z_∞.
- *Gram.* P_i·P_j = (1 − (1−d)^{m_ij+1})/d (AMV), P·Z_∞ = 1 e Z_∞² = d. O valor m_ij + 1 é o número de componentes "consistentes" do grafo união dos dois emparelhamentos: produto das razões ao longo do ciclo = 1.
- *Cálculo.*
  - Posto sobre ℚ, com um primo grande.
  - Déficits k_p = r − rank_{𝔽_p} G para p ≤ 100.
  - det do Gram de um subconjunto independente, fatorado.
- *Validação.* Postos 21 (d = 3), 142 (d = 4) e 1002 (d = 6) da AMV. Para d = 6, comparar r com dim Hdg² do T1: o déficit é o que falta aos ciclos lineares.
- *Hipótese H4.* Para d = 7, k_p = 0 para todo p ≠ 7.
- *O que é informativo.* Um p ∤ d com k_p > 0 diz que L não é p-saturado ou que o reticulado de Hodge tem p no discriminante. As duas coisas são dados novos sobre a HC integral em Fermat.

## Fontes (abertas nesta pesquisa)
- Clay/Deligne: https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf
- Markman: https://arxiv.org/abs/2502.03415 · https://arxiv.org/html/2502.03415v2 · https://www.arxiv.org/abs/2509.23403 · https://arxiv.org/html/2509.23403v2 · https://arxiv.org/html/2509.23079v1 · https://www.bimsa.cn/talk/25067.html · https://math.bgu.ac.il/en/research/fall2026/seminars/agnt/meetings/2025-11-05
- Floccari–Fu https://arxiv.org/abs/2504.13607 · Mostaed https://arxiv.org/html/2603.20268v1 · Li https://arxiv.org/abs/2609.27916
- Totaro (blog de Tao) https://terrytao.wordpress.com/2026/09/11/on-the-hodge-conjecture/ · Voisin (blog de Tao) https://terrytao.wordpress.com/2026/09/12/the-status-of-the-hodge-conjecture/
- OpenAI 032: https://github.com/openai/math/blob/main/history.md · https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-September-30-2026/paper.pdf (só metadados carregados) · https://kingy.ai/blog/openai-math-722-manuscripts-results-proofs-compute-costs/ · https://aicoder.com/news/news-20261007-openai-math-722-manuscripts-internal-frontier-model · https://officechai.com/ai/hodge-conjecture-abelian-varieties/ · https://www.kucoin.com/news/flash/openai-retracts-3-ai-math-papers-due-to-sign-error-in-key-proof · https://blog.pebblous.ai/report/openai-math-722-verification-ledger/en/ · https://www.emergentmind.com/openai-math-explorer · https://hub.valency.io/collections/openai-math · https://hraness.com/reading/mathematician-reactions-to-openais-372-math-results · https://proofsandprompts.com/2026/10/08/100-reactions-to-100-solutions/ · https://en.wikipedia.org/wiki/OpenAI_bulk_release_of_mathematical_papers · https://cryptobriefing.com/openai-hodge-conjecture-math-pushback/
- Integral e Kähler: https://arxiv.org/abs/math/0112247 · https://arxiv.org/abs/1802.01845v2 · https://arxiv.org/pdf/1907.08670 · https://arxiv.org/html/2507.15704v3 · https://www.ms.u-tokyo.ac.jp/~toshi/jjm/JJM_HP/contents/abstract/2-2/JJM0639.html
- Loci e Hodge absoluto: https://www.ams.org/jams/2020-33-04/S0894-0347-2020-00952-3/ · https://arxiv.org/abs/2107.08838v4 · https://arxiv.org/abs/math/0605766 · https://arxiv.org/pdf/1101.3647
- Tropical: https://arxiv.org/pdf/2609.14169 · https://arxiv.org/abs/2002.02347
- Fermat e ciclos lineares: https://arxiv.org/pdf/2101.04739 · https://arxiv.org/pdf/2105.04695 · https://arxiv.org/abs/2608.18134 · https://arxiv.org/abs/2609.12759 · https://arxiv.org/pdf/2609.12759 · https://arxiv.org/abs/1711.02628 · https://ar5iv.arxiv.org/html/1711.02628 · https://arxiv.org/pdf/1705.00084 · https://arxiv.org/pdf/2112.14818
- Lean/Mathlib: https://www.math.uni-bonn.de/people/rothgang/slides_Italean2025_diffgeo.pdf · https://math.iisc.ac.in/~gadgil/PfsProgs25doc/Mathlib/CategoryTheory/Sites/SheafCohomology/Basic.html · https://www.emergentmind.com/papers/2605.01028 · https://github.com/google-deepmind/formal-conjectures (o README não menciona Hodge)
- **Bloqueadas (permissão expirou, não lidas):** arxiv.org/abs/2609.12759v1 · arxiv.org/abs/2608.18134v1 · arxiv.org/abs/2507.15704
