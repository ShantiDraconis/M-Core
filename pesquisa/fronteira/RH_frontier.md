# RH: fronteira de pesquisa para o programa ATK/M-Core (2026-10-21)

Base: `audit/dossier/RH_summary.md` (P0 = 0; P1 = B1 Báez-Duarte ⇒ RH, `rh_iff_DN` só no ramo `atk/rh-rho-independent`, regiões livres `faixa_estreitada`/`faixa_log` com (log t)^-9, piso `piso_DN`, `DN_espectral`, Bagchi) e `obligations.json` (O1 = `UniformLogBound`, ∃K ∀N D_N ≤ K/log(N+2)).
Em uma linha: o fato novo que muda o mapa é a quasi-RH (zero-free Re s > 7/8, com prova em Lean). A rota D_N → 0 em σ = 1/2 é equivalente a RH, e numericamente ela não falsifica nada. O ganho realista está em (i) consequências formais da quasi-RH, (ii) uma versão ponderada σ > 1/2 do critério com taxa de potência, e (iii) a infraestrutura clássica (região c/log t, produto de Hadamard) que falta na Mathlib.

## 1. Estado da arte (out/2026)

**1.1 Quasi-RH (OpenAI, família 003).**
- Manuscrito de 30/09/2026, com 199 pp. Afirma que ζ, todas as L de Dirichlet e as L de Hecke de ordem finita sobre Q(√−3) não têm zeros em Re s > 7/8. Há um companheiro de 05/10, com 49 pp e 11/12, que não está formalizado, e um texto de 9 pp sobre zeros de Landau–Siegel com c não explícito. Publicado em 06/10 junto com 719 manuscritos (372 famílias).
- Lean: o desafio `ComparatorChallenges/QuasiRiemannHypothesis.lean` é só o enunciado `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re {s} (hs : 7/8 < s.re) : riemannZeta s ≠ 0` com `sorry`. A prova está no módulo-solução `OAI.NumberTheory.DirichletL.Nonvanishing`. O JSON do comparator permite só `propext`, `Quot.sound` e `Classical.choice` (`enable_nanoda: false`).
- Imprensa: cerca de 486 mil linhas em 2.924 módulos. Uma única reexecução independente (D. Goldblatt, dois kernels, 63 min) aceitou a prova.
- **ATK** (`atk/reducoes-externas-20261015`): importa o módulo-solução, não o desafio. Ainda assim falta re-checar localmente.
- Revisão humana: nenhuma concluída. A Quanta (19/10) diz que os especialistas "largely agree" que o resultado está correto (Radziwiłł: "staggering"; Lichtman: maior feito de IA em matemática). Sarnak não o trata como teorema antes da checagem humana. Sawin acha provável que RH continue tão longe quanto antes.
- Ingredientes: β* = sup das partes reais dos zeros da família de Hecke sobre Q(√−3), soma de teta cúbica completada com reflexão (expansões de Dunn–Radziwiłł), Poisson, detector de zeros por polinômios de Dirichlet, grande crivo sêxtico e momentos de ordem 4 e inversos. A parte I dá 11/12 e a parte II dá 7/8. A contradição vem da continuação de Mellin de 1/L além de β*.
- Melhorias:
  - Liu (arXiv 2610.12234, 08/10): B(ℓ) = 11/12 − ℓ/4 e B ≈ 0,874957, que ele chama de ótimo "para as estimativas direta e de contagem de caracteres usadas".
  - LW56e2/quasi-riemann-improved: B = 0,8749570698 em Lean 4.34.1 (a mesma versão do ATK), axiomas padrão, sem revisão. Traz uma "two-bin obstruction": retunar dois parâmetros não baixa o limite em 10⁻¹².
  - Sang 0,8748867 e Cureton–Thorner (Dedekind, 31/32): só relatados (postcutoff), não verifiquei.
  - Kintali (07/10): versão curta derivada, com 47/48.
- Barreira relatada em 3/4 ("needs a nice new idea", emergentmind). É coerente com o limite Z^{1/4+ε} do sinal de prova.

**1.2 Regiões livres clássicas.**
- de la Vallée Poussin explícita: σ ≥ 1 − 1/(4,896 log t), t ≥ 3 (Bellotti–Trudgian–Yang, arXiv 2603.21490, mar/2026). A anterior era 5,558691 (Mossinghoff–Trudgian–Yang 2022).
- Korobov–Vinogradov explícita: σ ≥ 1 − 1/(55,241 (log t)^{2/3}(log log t)^{1/3}), |t| ≥ 3 (MTY).
- Todas encolhem até σ = 1 quando t → ∞. Só a quasi-RH dá um semiplano fixo.

**1.3 Densidade de zeros.**
- Guth–Maynard (Annals 203(2) 2026, pp. 623–675): N(σ,T) ≤ T^{30(1−σ)/13+o(1)}, e primos em intervalos de comprimento x^{17/30+o(1)}. O limiar crítico é o de valores perto de N^{3/4}.
- Tao–Trudgian–Yang (arXiv 2501.16779): otimização sistemática via ANTEDB (`teorth/expdb`, Python com blueprint).
- A Hipótese de Densidade segue aberta, e mesmo ela não implica RH.

**1.4 Verificação numérica, de Bruijn–Newman e Li.**
- RH vale até altura 3·10¹² (Platt–Trudgian, aritmética intervalar, BLMS 2021).
- Λ ≥ 0 (Rodgers–Tao 2018/2020), Λ ≤ 0,22 (Polymath15) e Λ ≤ 0,2 (Platt–Trudgian). RH ⟺ Λ = 0. Melhorar o limite superior exige verificar RH a alturas maiores.
- Li/Keiper: λ_n ≥ 0 conhecido até n ≈ 2550–4000 (McPhedran 2024). Uma violação vinda de um zero de altura > 3·10¹² só apareceria em n ~ 10²⁵.

**1.5 Nyman–Beurling–Báez-Duarte.**
- RH ⟺ d_N → 0 (Báez-Duarte 2003).
- Piso incondicional: liminf d_N² log N ≥ Σ m_ρ²/|ρ|² (BBLS 2000; Burnol, Adv. Math. 2002).
- Sob RH, só se sabe d_N² ≪ (log log N)^{5/2+ε}/√log N (Balazard–de Roton).
- Sob RH + zeros simples + Σ_{|γ|≤T} 1/|ζ'(ρ)|² ≪ T^{3/2−δ}, o polinômio Σ μ(n)(1 − log n/log N)n^{−s} atinge (2+γ−log 4π)/log N (Bettin–Conrey–Farmer 2012). Portanto O1 é mais do que se sabe deduzir de RH.
- Numérica: Landreau–Richard (Exp. Math. 2002) foram até **N = 20.000**, com d_N ≈ 0,21377/√log N contra √C = 0,21492. Os dados do ATK (N ≤ 1500, D_N·log(N+2) = 0,04567 = 0,9888·C) não são novos.
- Variantes em L^p e ponderadas:
  - Beurling 1955: ζ ≠ 0 em Re s > 1/p ⟺ χ está no fecho em L^p(0,1).
  - Nikolski.
  - Ghosh–Kremnizer–Noor–Santos (arXiv 2206.00434) e arXiv 2206.02654 (espaços de Dirichlet ponderados). Ambos dão critérios de semiplano, e **nenhum relaciona taxa de decaimento com sup Re ρ**.
  - Darses–Hillion (dilatações aleatórias, piso ≫ 1/log n).
  - Pyvovarov (2607.12084, redução a cancelamento bilinear sem d_N).

**1.6 Formalização.**
- Mathlib `d13f23b` tem:
  - ζ, equação funcional, ζ ≠ 0 em Re ≥ 1;
  - zeros discretos (`ZetaZeros`, 2026);
  - FE de ζ'/ζ (`logDeriv_riemannZeta_one_sub`, Tao 2026);
  - **Borel–Carathéodory** (Radziwiłł 2026), Jensen, decomposição canônica (Kebekus 2026), três retas;
  - ψ e θ de Chebyshev.
- Mathlib **não** tem: TNP, produto de Hadamard de ξ, N(T), fórmula explícita, nem região livre além de Re s ≥ 1.
- TNP forte em Lean: PNT+ (Kontorovich–Tao) concluído com o agente Gauss (cerca de 25 mil linhas, ~set/2025). Não pude abrir o blueprint para ver qual região livre está lá.
- Isabelle AFP (Song–Yao, mai/2024): região livre 1 − 1/(952320 log(|γ|+2)) e π(x) = Li(x) + O(x e^{−√log x/3653}).
- ATK (rodadas 37 e 52–54, out/2026): região livre `1 − c/log|γ|`, `ζ′/ζ = O(log² t)` nela, `ψ(x) = x + O(x e^{−b√log x})` e `π(x) ~ x/log x` (`ATK.ZeroClasses.PNT.tendsto_primeCounting`), com constantes não explícitas. Rodada 81: `θ(x) = x + O(x e^{−b√log x})` e `π(x) = Li(x) + O(x e^{−b′√log x})` (`ATK.ZeroClasses.TNPPi.theta_tnp`, `pi_tnp`). Rodada 86: a cota de convexidade `ζ(σ + it) ≪ |t|^{(1−σ)/2+ε}`, incondicional (`ATK.ZeroClasses.Convexidade.convexidade`). Rodada 87: o teorema de Landau para transformadas de Mellin de `f ≥ 0` (`ATK.ZeroClasses.Unilateral.landau`). Rodada 88: `ψ(x) − x = Ω±(√x)`, `M(x) = Ω±(√x)` com constante, e `M(x) ≤ A√x + K` ⟹ RH e zeros simples (`ATK.ZeroClasses.OmegaRaiz`).

## 2. Barreiras e no-go (o que já cai)
- **B1 (piso de Burnol/BBLS).** D_N ≥ (C − o(1))/log N, então a taxa 1/log N de O1 é a melhor possível. (ATK, rodada 80: provado na classe `‖c‖₁ ≤ N^A`, `D_N^{(N^A)} ≥ C/(A log N + B)`, `BDBurnolL1.burnol_L1`. Rodada 84, para `c` arbitrário: nenhuma lei de potência, `D_N ≠ O(N^{−δ})`, e a contração diádica é impossível sem o piso citado (`BDSemPotencia.DN_sem_potencia`, `contracao_impossivel_incond`); o `1/log N` de Burnol segue citado.) Isso refuta contração geométrica e qualquer lei de potência em σ = 1/2 (o ATK já registra `sem_contracao_de_piso_log`). Além disso, O1 ⇐ RH **não** é conhecido (BCF precisa de hipóteses extras). Atacar O1 é pelo menos tão difícil quanto RH somado ao controle de 1/ζ'(ρ).
- **B2 (cegueira numérica, cálculo meu).** O piso de um zero fora da linha é ≤ (2β−1)/|ρ|² ≤ 1/γ² ≤ 1,1·10⁻²⁵ para γ ≥ 3·10¹². Com D_N ≈ C/log N, ele só aparece com log N ≳ 4·10²³. Para Li, n ~ 10²⁵. Nenhuma amostra de D_N, λ_n ou Λ pode falsificar RH além de Platt–Trudgian. Isso confirma `amostra_finita_nao_decide`: a numérica de D_N serve só para calibrar constantes.
- **B3 (armadilha de equivalência).** `IsEmpty ZeroFora`, D_N → 0, `FaixaLivre (1/2) (7/8)`, Λ = 0 e λ_n ≥ 0 ∀n são todos ⟺ RH. Progresso parcial precisa de um parâmetro monotônico com sentido conhecido: θ do semiplano, κ(σ) (§3, Q2), A(σ).
- **B4.** Métodos de função única (3–4–1, Hadamard–dlVP, Vinogradov–Korobov) dão regiões que tendem a 1. A rota `ZetaLog`/`ValleePoussin` do ATK nunca dá semiplano. O semiplano fixo exigiu média sobre família (metapléticas, Q(√−3)).
- **B5 (quasi-RH).** Barreira relatada em 3/4. Otimização paramétrica esgotada perto de 0,87496 (Liu; obstrução de LW56e2). Especialistas duvidam que o método alcance 1/2.
- **B6.** Rodgers–Tao (Λ ≥ 0) mostra que RH vale "no limite", sem folga. Argumentos perturbativos com folga ε (fluxo de calor, t > 0) não chegam a t = 0.

## 3. Questões atacáveis (ordem: valor × tratabilidade)

**Q1 [(b) formalização + (a) leve]. Quasi-RH dentro do kernel e suas consequências.**
- Enunciado: com `hθ : ∀ s, θ < s.re → riemannZeta s ≠ 0`, provar
  1. M(x) = Σ_{n≤x} μ(n) ≪_ε x^{θ+ε};
  2. ψ(x) = x + O_ε(x^{θ+ε});
  3. instanciar θ = 7/8 (OpenAI) ou θ = 0,8749570698 (LW56e2) por import.
- Por que importa: seria o primeiro TNP com economia de potência verificado por kernel (Isabelle e PNT+ têm só e^{−c√log x}). Também troca o meta-teorema `rh_iff_faixa` por teoremas de conteúdo.
- O que se sabe: é a dedução clássica (Perron truncado + 1/ζ ≪ t^ε e ζ'/ζ ≪ (log t)^A em σ ≥ θ + δ, via Borel–Carathéodory/três círculos, análogo a Titchmarsh §14.2). O ATK já tem `PerronSuave` (ramo lateral). A Mathlib tem Borel–Carathéodory.
- Progresso: (i) re-checagem local do módulo-solução (lean4checker/comparator); (ii) M(x) ≪ x^{θ+ε} com θ paramétrico, sem `sorry`.
- ATK (rodadas 51 e 55, out/2026): a recíproca está certificada com θ livre — `|M(N)| ≤ C(N+1)^θ` ou `|ψ(N) − N| ≤ C(N+1)^θ` ⟹ `ζ ≠ 0` em `Re s > θ` (`ATK.ZeroClasses.VonKoch.zeroFree_of_mertens`, `zeroFree_of_psi`). A direção desta questão está certificada com θ = 1/2: para `M` (`ATK.ZeroClasses.Mertens.mertens_of_RH`, rodada 51) e para ψ (`ATK.ZeroClasses.VonKochRH.psi_of_RH`, rodada 56, via um Littlewood geral `cota_gen`). Rodada 57: θ geral certificado — `ATK.ZeroClasses.QuasiRH.semZeros_iff_psi` e `semZeros_iff_mertens` (`ζ ≠ 0` em `Re s > θ` ⟺ `ψ(x) = x + O(x^{θ+ε})` ⟺ `M(x) = O(x^{θ+ε})`, ½ ≤ θ < 1). Os itens 1–2 desta questão estão feitos; o item 3 depende de importar um semiplano externo. Rodada 87: **um lado basta** — `ψ(x) − x ≤ A x^θ + K` (ou `≥ −…`, ou o mesmo para `M`) já implica `ζ ≠ 0` em `Re s > θ` (`ATK.ZeroClasses.Unilateral.semZeros_of_psi_le` e variantes, pelo teorema de Landau); `Θ` e RH se leem por um lado (`Teta_le_iff_psi_le`, `rh_iff_psi_le`), e `ψ(x) − x`, `M(x)` são `Ω±(x^θ)` para todo `θ < Θ`. Rodada 92: incondicionalmente, `ψ(x) − x = Ω±(√x log log log x)` (Littlewood, `LittlewoodMontagem.littlewood`). Rodada 97: o mesmo para `θ(x) − x` e `π(x) − Li(x)` — `Θ ≤ θ` ⟺ uma cota de um lado com expoente `θ + ε` (`PiUnilateral.Teta_le_iff_theta_le`, `_theta_ge`, `_pi_le`, `_pi_ge`), e RH ⟺ `π(x) ≤ Li(x) + O(x^{½+ε})` (`rh_iff_pi_le`), ou o lado de baixo (`rh_iff_pi_ge`). Rodada 98: **`Θ` é o expoente exato de cada uma, de cada lado** — `Θ = inf{θ : E(N) ≤ N^θ para N grande}` para `E = ±(ψ − N)`, `±(θ − N)`, `±(π − Li)`, `±M` e os valores absolutos (`TetaExpoente.Teta_eq_psi_cima`, …, `Teta_eq_mertens`); para os lados de cima de `θ − N` e `π − Li` abaixo de `½` entra Littlewood. Rodada 99: a função de Liouville — `Σ λ(n)n^{−s} = ζ(2s)/ζ(s)` (produtos de Euler), RH ⟺ `L(x) = O(x^{½+ε})` e o mesmo de um lado só (`LiouvilleRH.rh_iff_liouville`, `_le`, `_ge`), **a conjectura de Pólya implica RH** (`rh_of_polya`), `L(x) ≠ O(x^θ)` para `θ < ½` sem hipóteses (o polo de `ζ(2s)` em `s = ½`) e `Θ = inf{θ : |L(N)| ≤ N^θ}` (`Teta_eq_liouville`). Rodada 100: **a conjectura de Turán implica RH** (`TuranLiouville.rh_of_turan`: `Σ_{n ≤ N} λ(n)/n ≥ 0` para todo `N` ⟹ RH), por Landau abaixo de `Re s = 0`, no disco `|s − 2| < 5/2`. Rodada 101: primos em intervalos curtos — para `θ > Θ` há primo em `(x, x + x^θ]` (`PrimosCurtos.primo_curto_Teta`); sob RH, em `(x, x + C√x log³ x]` (`primo_curto_RH`); e sem hipóteses em `(x, x + x e^{−c√log x}]` (`primo_curto_tnp`). Rodada 102: a abscissa sem zeros `c := inf{θ : ζ ≠ 0 em Re s > θ}`, definida sem `½`, satisfaz `½ ≤ c ≤ 1`, `c = sup Re ρ` e `RH ⟺ c = ½` (`PontesRH.rh_iff_c`); para `½ ≤ θ < 1`, `c ≤ θ` ⟺ `Σ μ(n)n^{−s}` converge em `Re s > θ` (`PontesRHAbscissa.c_le_iff_mu`); o passo de indução em altura é equivalente a RH (`passo_iff_rh`).

**Q2 [(a) nova + (b)]. Báez-Duarte ponderado: um critério com taxa de potência.**
- Definições, para σ ∈ (1/2,1):
  - D_N(σ) := inf_{c∈ℝ^N} ∫_0^∞ (χ − Σ_{k≤N} c_k ρ_k)² t^{2σ−1} dt = inf (1/2π)∫ |1 + ζ(s)Σc_k k^{−s}|²/|s|² dτ, com s = σ+iτ, ‖χ‖² = 1/(2σ). Converge em 0 < σ < 1.
  - κ(σ) := liminf −log D_N(σ)/log N e Θ := sup Re ρ.
- (i) Suficiência: D_N(σ) → 0 ⇒ ζ ≠ 0 em Re s > σ. É uma cópia de B1/`piso_DN` com o núcleo de H² do semiplano σ.
- (ii) Necessidade com taxa: Θ ≤ θ < σ ⇒ κ(σ) ≥ 2(σ−θ). A prova usa mollificador μ(k)g(k/N) com g ∈ C_c^∞ e g = 1 perto de 0, desloca o contorno até θ + ε e usa ∫|ζ(σ+iτ)|²/|s|^{2−ε} < ∞. Com a quasi-RH isso dá um resultado **incondicional**: D_N(σ) ≪ N^{−2(σ−0,875)+ε}, o primeiro critério tipo Nyman–Beurling efetivamente convergente; não conheço precedente.
- (iii) **Resolvida na rodada 109** (era aberta): κ(σ) ≤ 2(σ−Θ), um piso de Burnol ponderado. Se valer para um único σ_0, então RH ⟺ κ(σ_0) ≥ 2σ_0 − 1. É o análogo L² de "Θ = inf{θ : M(x) ≪ x^{θ+ε}}". Pela minha leitura das fontes, a literatura de semiplanos não tem taxa. Fácil: piso polinomial se ‖c‖₁ ≤ N^A (cortar t < N^{−B}). Difícil: c arbitrário. **Checagem de literatura (parcial, 27/10/2026, só resumos e descrições públicas):** critérios qualitativos de semiplano do tipo Q2(i) já existem — Beurling (1955, versão `L^p`), de Roton (Trans. AMS 359, 2007, classe de séries de Dirichlet), Delaunay–Fricain–Mosaki–Robert (Trans. AMS 365, 2013, discos e semiplanos), Ghosh–Kremnizer–Noor–Santos (Adv. Math. 2024, `H^p` e `ℓ²` ponderados, arXiv 2206.00434) e o trabalho em espaços de Dirichlet ponderados (arXiv 2206.02654). Nessas fontes não encontrei taxas `N^{−κ}` ligadas a `Θ`. Ghosh et al. e 2206.02654 declaram-se qualitativos. Nikolski (AIF 45, 1995), lido no texto completo, dá discos livres de zeros e a equivalência qualitativa, sem taxa em `N`. De Roton (Bull. SMF 134, 2006) estende o piso de Burnol/BBLS à classe de Selberg, na reta crítica. Não li o texto completo de de Roton (Trans. AMS 2007). Portanto Q2(i) **não é nova**, e Q2(ii)/(iii) (rodadas 75, 83) só podem ser chamadas de novas depois dessa leitura e de uma busca mais ampla.
- Progresso: (i) e (ii) em Lean, adaptando `NecessidadeRH`, que hoje usa RH apenas como zero-freeness em Re s > 1/2 (verificar com T4). Para (iii), o caso de c com suporte diádico, ou um contraexemplo (T2).
- ATK (rodada 59, out/2026): (i) certificado — `ATK.ZeroClasses.BDPonderado.semZeros_of_DNσ` (`inf_N D_N(σ) = 0` ⟹ `ζ ≠ 0` em `Re s > σ`, 0 < σ < 1), e `piso_DNσ`: `inf_N D_N(σ) > 0` para `σ < ½`, incondicional (Hardy). (ii) e (iii) seguem abertos. Rodada 73: a forma espectral `D_N(σ) ≤ (1/2π)∫|1 + ζP_c|²/|s|²` (Plancherel ponderado) e o molificador de Riesz `A_N = Σ μ(k)(1 − k/N)² k^{−s}` com a representação `(1/2π)∫ W(c+iy)N^{c+iy}/ζ(s+c+iy) dy` (`ATK.ZeroClasses.BDEspectral`) — primeira peça de (ii). Rodada 74: sob `SemZeros θ`, `|A_N(σ+iτ) − 1/ζ(σ+iτ)| ≤ K N^{−δ}(1+|τ|)^η` (`ATK.ZeroClasses.BDDesloc.molif_cota`, deslocando a integral de `A_N` para `Re z = −δ`). **Rodada 75: (ii) certificado** — sob `SemZeros θ`, `D_N(σ) ≤ K N^{−2δ}` para todo `δ < σ − θ`, isto é, `κ(σ) ≥ 2(σ − θ)` (`ATK.ZeroClasses.BDTaxa.DNσ_taxa`); daí `SemZeros θ ⟺ ∀ σ ∈ (θ,1), inf_N D_N(σ) = 0` (`semZeros_iff_DNσ`) e RH ⟺ `inf_N D_N(σ) = 0` em `(½,1)` (`rh_iff_DNσ`). A versão incondicional depende de importar um semiplano sem zeros; (iii) segue aberto. Rodada 76: `Θ` definido (`ATK.ZeroClasses.BDTheta.Teta`), RH ⟺ `Θ = ½`, os três instrumentos (`ψ`, `M`, `D_N(σ)`) medem o mesmo `Θ`, e (iii) está enunciada como `BDTheta.PisoPonderado` (OPEN_MATH), com `rh_iff_taxa_de_piso`: se o piso valer, RH se decide num único `σ₀`. Rodada 79: (iii) na classe `‖c‖₁ ≤ N^A` — `κ_A(σ) ≤ 2A(σ − Θ)/Θ` (`ATK.ZeroClasses.BDPisoL1.taxaL_Teta`, pelo piso `‖res‖²_σ ≥ C_ρ(1 + ‖c‖₁)^{−2(σ−β)/β}`), e como o molificador de Riesz tem `‖c_N‖₁ ≤ N`, `2(σ − Θ) ≤ κ₁(σ) ≤ 2(σ − Θ)/Θ` (`taxaL_sanduiche`). Falta (iii) para `c` arbitrário e o fator `1/Θ`. Rodada 80: uma taxa `ℓ¹` positiva num único `σ` certifica `Θ ≤ 2Aσ/(κ + 2A)` (`ATK.ZeroClasses.BDBurnolL1.taxaL_pos`), e `TaxaL σ₀ 1 (4σ₀ − 2)` num só `σ₀ ∈ (½,1)` implica RH (`rh_of_taxaL`); sob RH o molificador dá `2σ₀ − 1`, e a lacuna é o fator `1/Θ`. Rodada 82: sob `SemZeros θ`, `θ < σ`, todo `c` com `‖res_c‖²_σ ≤ 1` tem `‖c‖₁ ≤ K N^{σ+3/2+2η}` (`ATK.ZeroClasses.BDNormaL1.norma_l1_le`, valor médio + `1/ζ ≪ τ^η` + Plancherel). **Rodada 83: (iii) a menos de constante, para `c` arbitrário** — `κ(σ) ≤ (2σ + 3)(σ − Θ)/Θ` (`ATK.ZeroClasses.BDTaxaPiso.taxaDN_teto`), logo `2(σ − Θ) ≤ κ(σ) ≤ (2σ + 3)(σ − Θ)/Θ`; uma taxa positiva num só `σ` certifica `Θ ≤ (2σ + 3)σ/(κ + 2σ + 3)`, e `TaxaDN σ₀ ((2σ₀ + 3)(2σ₀ − 1))` ⟹ RH (`rh_of_taxaDN`). Falta o fator exato (`(2σ + 3)/(2Θ) → 1`). **Rodada 109: (iii) exata** — `TaxaDN σ κ ⟹ κ ≤ 2(σ − Θ)` em `(Θ, 1)` (`ATK.ZeroClasses.BDPisoExato.taxa_le_Teta`), logo `κ(σ) = 2(σ − Θ)` (`kappa_exato`); `PisoPonderado` é teorema (`pisoPonderado`) e RH ⟺ `TaxaDN σ₀ (2σ₀ − 1)` num único `σ₀ ∈ (½, 1)` (`rh_iff_taxa_um`). A prova pareia o resíduo com `sK(s)x^s/ζ(s)`: para todo `c`, `D_N(σ) ≫ x^{−2σ}|G(x)|²` com a Mertens suavizada `G(x) = Σ μ(n)ψ(n/x)`, e `|G(x)| ≪ x^θ` estende `1/ζ` a `Re s > θ` pela transformada de Mellin `K(s)/ζ(s)` (§4de).

**Q3 [(b)]. Região clássica c/log t no ATK.**
- Enunciado: ∃ c > 0 explícito tal que ζ(β+iγ) = 0 e |γ| ≥ 2 ⇒ β ≤ 1 − c/log|γ|.
- Substitui (log t)^{-9} (`faixa_log_simples`).
- Faltam: o lema de Landau (−Re ζ'/ζ(s) ≤ −Σ_{|γ−t|≤1} Re 1/(s−ρ) + O(log t)) via Borel–Carathéodory/Jensen e a desigualdade 3–4–1, que já está no ATK.
- Primeiro verificar e reutilizar o PNT+. Meta mínima: c = 1/952320 (paridade com Isabelle). Meta ambiciosa: c ≈ 1/5,56 com Stechkin, que é mais difícil.

**Q4 [(b) infraestrutura]. Produto de Hadamard de ξ, N(T), fórmula explícita e critério de Li.**
- Enunciados:
  - ξ(s) = e^{A+Bs}∏(1−s/ρ)e^{s/ρ};
  - N(T) = (T/2π)log(T/2πe) + 7/8 + O(log T);
  - RH ⟺ λ_n ≥ 0 ∀n, com λ_n = Σ_ρ[1−(1−1/ρ)^n].
- Por que importa: habilita o piso de Burnol formal (hoje um teorema citado no ATK), as somas Σ1/|ρ|² = 2+γ−log 4π, e as rotas de Li e Weil. Médio valor, média tratabilidade (Jensen e decomposição canônica já existem).
- ATK (rodadas 33, 42, 63–68, out/2026): Hadamard (`hadamardXi`), N(T) (`riemannVonMangoldt`), as peças da fórmula explícita (`ExplicitaPecas`: princípio do argumento ponderado, resíduo `x − Σ x^ρ/ρ`, alturas boas), von Koch clássico (`Koch.rh_iff_psiLog2`, `rh_iff_piLog`) e **o critério de Li completo** (`LiCompleto.rh_iff_li`) estão certificados. Rodada 69: `λ₁ = 1 + γ/2 − ½ log 4π` e RH ⟺ `Σ 1/|ρ|² = 2 + γ − log 4π` (`LiUm`). Rodada 70: a identidade de resíduos da fórmula explícita no retângulo largo `[−(2K + ½), c] × [−T, T]`, com os zeros triviais simples e o resíduo `−log 2π` em `0` (`FormulaExplicita.bordo_largo`). Rodada 71: **a fórmula explícita de Riemann–von Mangoldt sem hipóteses** (`ExplicitaLimite.formula_explicita`: `Σ_{|γ|≤T_k} x^ρ/ρ → x − ψ(N) − log 2π − ½ log(1 − x^{−2})`, `x = N + ½`, alturas boas); rodada 72: o limite com `T → ∞` qualquer (`ExplicitaT.formula_explicita_T`); rodada 77: `x > 1` real não inteiro (`ExplicitaReal.formula_explicita_T_x`); rodada 78: `x` inteiro com `ψ₀`, e daí **a fórmula explícita para todo `x > 1`** (`ExplicitaInteira.formula_explicita_T_real`). Rodada 89: **a fórmula explícita com peso gaussiano** `W(s) = e^{(s−½)u + τ(s−½)²}`, soma em `ρ` absolutamente convergente (`ATK.ZeroClasses.ExplicitaGauss.formula_gauss`) — a ferramenta das provas de oscilação (Littlewood segue BUILD_PENDING). Rodada 90: o lado aritmético dessa fórmula é `ψ` suavizado, `A_τ(u) − e^{u/2+τ/4} = ∫ k_τ(v)F(u − v) dv` com `F(y) = (ψ(e^y) − e^y)e^{−y/2}` (`LittlewoodBase.A_sub_eq`, `formula_psi`), e sob RH uma média gaussiana grande de `F` força `F` grande em `[u − 1, u + 1]` (`localiza_menos`/`localiza_mais`); para Littlewood faltam as estimativas da soma sobre zeros e o alinhamento de Dirichlet com cota explícita. Rodada 91: essas estimativas estão certificadas sob RH (`LittlewoodSoma.soma_forcada`: com `τ = A₀/T²` e `n` que alinha os zeros de `|γ| ≤ 3T`, a soma em `u = n ± 1/T` vale `±c log T` a menos de `C₁ + ε Σ m_ρ/|ρ|`), junto com Dirichlet simultâneo com cota `n ≤ n₀Q^K` (`dirichlet_Q`, `alinha`); falta só a montagem. Rodada 92: **o teorema de Littlewood está certificado sem hipóteses** (`ATK.ZeroClasses.LittlewoodMontagem.littlewood`: `ψ(x) − x = Ω±(√x log log log x)`), por casos — sob RH pela montagem gaussiana (`F_grande`, `F_omega_RH`), e sem RH por `Θ > ½` e a rodada 87 (`littlewood_nao_RH`). Rodada 93: o mesmo para `θ` (`LittlewoodTeta.theta_littlewood`) e as trocas de sinal infinitas de `ψ(x) − x` e `θ(x) − x`; para `π(x) − Li(x)` falta a fórmula explícita integrada (`∫ (ψ(t) − t) dt = O(x^{3/2})` sob RH). Rodada 94: o substituto está certificado — sob RH, `|∫ₐᵇ F| ≤ C(1 + log b)` (`LittlewoodMedia.integral_F_log`), integrando a fórmula gaussiana em `u`. Rodada 95: **sob RH, `π(x) − Li(x) = Ω±(√x log log log x/log x)`** e troca de sinal infinitas vezes (`LittlewoodPi.pi_littlewood_RH`); a versão sem hipóteses precisa ainda do caso `¬RH` (Landau para `log ζ`). Rodada 96: **Littlewood para `π` está certificado sem hipóteses** (`LittlewoodPiIncond.pi_littlewood`, `pi_troca_sinal`): o caso `¬RH` sai de Landau para `log ζ` (`semZeros_of_aPi_le`/`_ge`) e de `a(N) = π(N) − Li(N) + O(√N)`, que dão `π − Li = Ω±(x^θ)` para `½ ≤ θ < Θ`. Rodada 80: o piso de Burnol na classe `‖c‖₁ ≤ N^A` (`ATK.ZeroClasses.BDBurnolL1.burnol_L1`: `D_N^{(N^A)} ≥ C/(A log N + B)`). Falta Burnol para `c` arbitrário.

**Q5 [(a) alto valor, baixa tratabilidade]. Baixar o expoente da quasi-RH.**
- Enunciado: provar ζ ≠ 0 em Re s > B' com B' < 0,8748867, ou provar que o método da sonda não passa de 3/4 (um no-go também é publicável).
- Alavanca: Liu mostra que B é ótimo **para as estimativas de contagem de caracteres atuais**. Uma estimativa de grandes valores tipo Guth–Maynard para polinômios de Dirichlet torcidos pela família sêxtica/cúbica sobre Q(√−3), ou um quarto momento melhor, mexe em B diretamente.
- Progresso: qualquer B' < 0,87488 com entrada nova verificável, mesmo condicional a uma conjectura de grandes valores explicitada.

**Q6 [(a) baixo valor]. Segunda ordem de D_N.**
- Testar d_N² log N = C − c₁/log N + o(1/log N). Os dados ficam abaixo de C, coerente com convergência lenta por baixo. Útil só para calibrar heurísticas, sem impacto em RH.

## 4. O que precisa ser criado
1. `ATK.QuasiRH (θ)` paramétrico, com o import fixado de `openai/math` (módulo-solução) e o de LW56e2. Re-checagem com lean4checker/nanoda no CI, e checagem de não-sombreamento de `riemannZeta`, que o comparator garante.
2. `ATK.BaezDuartePonderado`:
   - `DNσ σ N`;
   - Mellin–Plancherel em L²(t^{2σ−1}dt) ↔ L²(Re s = σ), generalizando `MellinPlancherel`;
   - suficiência (i);
   - necessidade com taxa (ii);
   - o invariante κ(σ) e o perfil σ ↦ κ(σ).
3. Merge de `rh_iff_DN`, `PerronSuave`, `RHLogZeta` e `RazaoZeta` em `main`, para a obligations.json deixar de dizer "não formalizada".
4. Mathlib/upstream: lema de Landau para ζ'/ζ, região dlVP, Perron truncado, produto de Hadamard (ordem 1), N(T), fórmula explícita, coeficientes de Li, ψ − x ≪ x^{θ+ε} a partir de semiplano livre.
5. Numérica rigorosa: D_N e D_N(σ) com aritmética intervalar (python-flint/arb). O `nb_gram.py` usa `Decimal` sem cota de erro, então o "certificado (A)" não é certificado.

## 5. Testes baratos (≤ 20 min, 2 núcleos; não executados)

**T1. Expoente ponderado κ(σ).** Testa Q2(ii) e mede uma quantidade que não encontrei na literatura.
- Entradas: σ ∈ {0,60, 0,70, 0,80, 0,90}; N ∈ {25, 50, 100, 200, 400, 800}.
- g(x) = 1 para x ≤ 1/2; g(x) = S(2−2x) em (1/2,1), com S(u) = e^{−1/u}/(e^{−1/u}+e^{−1/(1−u)}); g(x) = 0 para x ≥ 1.
- a_k = μ(k)g(k/N) e P_N(s) = Σ_{k≤N} a_k k^{−s}.
- Calcular E_N(σ) = (1/π)∫_0^T |1 − ζ(s)P_N(s)|²/|s|² dτ + cauda, com:
  - s = σ+iτ, T = 16000, Simpson com Δτ = 0,05;
  - ζ por Euler–Maclaurin vetorizado (numpy, ⌈τ/2⌉+50 termos, 6 correções de Bernoulli; conferir 200 pontos com `mpmath.zeta`, erro relativo < 1e−9);
  - cauda = (1/(πT))·(ζ(2σ)·Σ_{j,k} a_j a_k lcm(j,k)^{−2σ} − 1), pelo valor médio com T ≥ 20N.
- Para N ≤ 200, calcular também o ótimo D_N(σ) = 1/(2σ) − bᵀG⁻¹b em `mpmath` com dps 40:
  - G_{jk} = (1/π)∫_0^T Re(j^{−s}·conj(k^{−s}))|ζ|²/|s|² dτ + ζ(2σ)lcm(j,k)^{−2σ}/(πT);
  - b_k = (1/π)∫_0^T Re(ζ(s)k^{−s})/|s|² dτ + [k=1]/(πT).
- Sanidade: para N ≤ 5, comparar com a integral direta ∫(χ − Σc_kρ_k)² t^{2σ−1} dt.
- Hipótese: a inclinação de log E_N contra log N em [100,800] é −(2σ−1) ± 0,1 (−0,2, −0,4, −0,6, −0,8), com oscilação quase periódica em log N (frequências γ_j).
- Resultado informativo:
  - inclinações batem → κ é observável em N ~ 10³, ao contrário de 1/log N;
  - D_N/E_N → 0 polinomialmente → o ótimo vence Möbius suave, o que refuta a heurística "Möbius é ótimo";
  - inclinação rasa em σ = 0,6 → regime pré-assintótico, a quantificar.
- Tempo: cerca de 10–15 min.

**T2. Zero plantado.** Tenta falsificar a conjectura Q2(iii).
- F(s) = ζ(s)(s−ρ₀)(s−ρ̄₀)/((s−ρ₁)(s−ρ̄₁)), com ρ₁ = 1/2 + 14,134725141734693i e ρ₀ = β₀ + 14,134725141734693i, β₀ ∈ {0,65, 0,75}. Linha de base: β₀ = 1/2, isto é, F = ζ.
- σ ∈ {0,80, 0,90}; N ∈ {10, 20, 40, 80, 160, 240}.
- Mesmo pipeline do ótimo de T1, com |F|² no lugar de |ζ|² e F em b. Reutilizar a grade de ζ; R → 1 na cauda.
- Hipótese (conjectura): D_N^F(σ) ≍ N^{−2(σ−β₀)}. Exemplo: σ = 0,9, β₀ = 0,75 dá inclinação −0,30, contra −0,80 sem o zero plantado.
- Resultado informativo:
  - se o caso plantado ainda decai a cerca de −(2σ−1), polinômios de Dirichlet contornam o polo de 1/F e κ não lê Θ, então abandonar Q2(iii);
  - se a inclinação ≈ −2(σ−β₀), investir na prova do piso.
- Controle: com σ = 0,6 < β₀ = 0,65, D_N^F deve estacionar acima de (2β₀−1)/|ρ₀|²-ish. Tempo: menos de 5 min.

**T3. Quasi-RH dentro do ANTEDB.**
- Clonar `github.com/teorth/expdb` (Python em `blueprint/src/python`).
- Adicionar `Hypothesis` "ζ(s) ≠ 0 para Re s > 0,8749570698", na forma A(σ) = 0 em [B,1], ao lado de `literature`.
- Rerodar os otimizadores e comparar com a linha de base:
  1. melhor A(σ) em σ ∈ [1/2,1], passo 0,005;
  2. a faixa onde A(σ) ≤ 2 (Hipótese de Densidade);
  3. os expoentes de primos em intervalos curtos, se implementados.
- Hipótese: o ganho fica restrito a [B,1] (a quasi-RH seria "ortogonal" a grandes valores), ou o ganho vaza para σ < B via regras de interpolação.
- Resultado informativo: qualquer melhora fora de [B,1] é um corolário novo, condicional à quasi-RH. Nenhuma melhora diz que Q5 precisa de entradas novas, não de combinatória do banco.
- Tempo: alguns minutos. Se o banco não aceitar N(σ,T) = 0, codificar como um limite de A(σ) por partes.

**T4. Sonda Lean da generalização (prepara Q2 e Q1).**
- Copiar para o scratch `NecessidadeRH`, `PerronSuave`, `RHLogZeta`, `RazaoZeta` e `NecessidadeBD` de `atk/rh-rho-independent`.
- Trocar a hipótese `RiemannHypothesis` por `∀ s, θ < s.re → riemannZeta s ≠ 0` (θ ∈ [1/2,1)) em `RHLogZeta.norm_zeta_le_RH` e a jusante, com a faixa θ+δ ≤ Re s.
- `lake env lean` arquivo por arquivo (Lean 4.34.1, Mathlib d13f23b) e anotar quais lemas quebram.
- Hipótese: RH entra só como zero-freeness à direita de 1/2 mais constantes numéricas. A lista de quebras é o plano de trabalho de Q2(ii). Tempo: cerca de 10–20 min.
- Não é barato: `lake build` de `OAI.NumberTheory.DirichletL.Nonvanishing` e comparator, cerca de 1h ou mais (a reexecução de Goldblatt levou 63 min). É prioridade de auditoria, mas fica fora do orçamento.

## 6. Riscos e notas
- A quasi-RH ainda não tem revisão humana publicada: tratar como teorema Lean (kernel), não como teorema publicado. Os textos de 11/12 e de Siegel não estão formalizados. O LW56e2 exige 2 patches de compatibilidade e não tem revisão.
- Bloqueados nesta sessão (sem consentimento): o blueprint do PNT+ (alexkontorovich.github.io) e math.inc/gauss.

## Fontes (abertas)
- Quasi-RH: https://github.com/openai/math · https://github.com/openai/math/blob/main/lean/docs/003.md · https://github.com/openai/math/blob/main/lean/ComparatorChallenges/QuasiRiemannHypothesis.lean · https://github.com/openai/math/blob/main/lean/ComparatorChallenges/QuasiRiemannHypothesis.json · https://github.com/openai/math/blob/main/lean/ComparatorChallenges/README.md · https://quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019 · https://postcutoff.com/e/2026-10-06-quasi-riemann-hypothesis-openai/ · https://orply.com/articles/perplexity/the-quasi-riemann-hypothesis-explained-1e6b84d5 · https://www.emergentmind.com/openai-math-explorer/results/003 · https://www.emergentmind.com/openai-math-explorer/papers/5.pdf · https://arxiv.org/html/2610.12234v1 · https://github.com/LW56e2/quasi-riemann-improved · https://shivakintali.github.io/papers/QRH.pdf
- Densidade, regiões, verificação: https://annals.math.princeton.edu/2026/203-2/p06 · https://arxiv.org/abs/2501.16779v1 · https://github.com/teorth/expdb · https://reservoir.lean-lang.org/@teorth/expdb · https://arxiv.org/abs/2212.06867 · https://arxiv.org/html/2603.21490v1 · https://arxiv.org/abs/2004.09765v1 · https://www.arxiv.org/abs/1904.12438 · https://en.wikipedia.org/wiki/De_Bruijn%E2%80%93Newman_constant · https://arxiv.org/html/2311.06294v3
- Nyman–Beurling: https://arxiv.org/abs/math/0103058 · https://arxiv.org/abs/1211.5191 · https://emis.univie.ac.at/journals/EM/expmath/volumes/11/11.3/Landreau349_360.pdf · https://arxiv.org/abs/1805.06733v1 · https://pith.science/paper/2607.12084 · https://ar5iv.labs.arxiv.org/html/1101.1199 · https://arxiv.org/abs/2206.00434 · https://arxiv.org/abs/2206.02654
- Formalização: https://isa-afp.org/entries/PNT_with_Remainder.html · https://github.com/AlexKontorovich/PrimeNumberTheoremAnd · https://www1.fields.utoronto.ca/talks/Gauss-agentic-formalization-Prime-Number-Theorem · https://tildes.net/~science/1qid/introducing_gauss_an_agent_for_autoformalization · local: Mathlib `d13f23b` (ZetaZeros, RiemannZetaLogDeriv, BorelCaratheodory, Chebyshev); M-Core `ccr-46709b88-u9mbgb`, `atk/reducoes-externas-20261015`.
