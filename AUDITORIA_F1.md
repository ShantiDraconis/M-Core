# M-Core: Auditoria F.1 — Fidelidade dos Enunciados

F.1 audita fidelidade dos enunciados do kernel aos problemas Millennium. Não formaliza, não
fecha obrigação. O entregável de cada seção é uma classificação — `fiel | sombra | tautologia |
mais forte | mais fraco` — não um teorema. Quando a classificação exige um contraexemplo e Lean
seria caro demais para justificar nesta auditoria, o contraexemplo vai em prosa. Evidência
`by-source` (leitura direta do kernel) é aceitável aqui; `by-build` só quando a seção
efetivamente produz um teorema.

## O8 — Yang–Mills (`ConstructiveYM4D`)

**1. `def` verbatim do kernel** (`ATK/Conditional/YangMills.lean`):

```lean
structure YMModel where
  Group : Type u
  CompactSimple : Group → Prop
  Euclidean : Type v
  OSAxioms : Group → Euclidean → Prop        -- comentário: "axiomas OS + é o limite
                                              -- contínuo de Yang–Mills com grupo G"
  ClusterRate : Euclidean → ℝ → Prop          -- comentário: "correlações decaem como e^{-m|x|}"
  Quantum : Type w
  reconstruct : Euclidean → Quantum
  IsQuantumYM : Group → Quantum → Prop
  GapAtLeast : Quantum → ℝ → Prop

def ConstructiveYM4D (M : YMModel.{u,v,w}) : Prop :=
  ∀ G, M.CompactSimple G → ∃ μ, M.OSAxioms G μ ∧ ∃ m : ℝ, 0 < m ∧ M.ClusterRate μ m
```

O docstring do arquivo declara a fidelidade explicitamente: **"fidelidade: PARAMÉTRICA"**.

**2. Axiomas de Osterwalder–Schrader**, com fonte (Osterwalder–Schrader, *Axioms for
Euclidean Green's Functions*, Comm. Math. Phys. 31, 1973; *...II*, Comm. Math. Phys. 42, 1975),
para funções de Schwinger $S_n(x_1,\dots,x_n)$:

1. **OS0** (temperância/regularidade) — $S_n$ são distribuições temperadas, analíticas num
   domínio apropriado.
2. **OS1** (covariância euclidiana) — invariância sob o grupo euclidiano $E(d)$ (translações +
   rotações).
3. **OS2** (positividade de reflexão) — $\sum_{i,j} \overline{S(\theta f_i, f_j)} \ge 0$ para
   funções-teste suportadas em tempo euclidiano positivo; é o axioma que permite a reconstrução
   euclidiana → Minkowski (rotação de Wick).
4. **OS3** (simetria) — $S_n$ simétricas sob permutação dos pontos (caso bosônico).
5. **OS4** (ergodicidade/clustering) — correlações decaem conforme os pontos se separam; dá
   vácuo único e é o axioma ligado ao gap de massa via decaimento exponencial.

**3. Classificação: `mais fraco`.** `M.OSAxioms : Group → Euclidean → Prop` é um campo
**não interpretado** da estrutura abstrata `YMModel`. Nada no tipo Lean força esse campo a
codificar OS0–OS4; é um parâmetro livre, satisfazível por qualquer predicado, inclusive um
vazio. `ConstructiveYM4D M` não formaliza "OS0–OS4 valem para uma medida euclidiana 4D
não-abeliana real" — formaliza "algum predicado que o modelo chama de `OSAxioms` vale", o que é
estritamente mais fraco. Isso não é um defeito escondido: o arquivo declara `PARAMÉTRICA`
abertamente. É a mesma classe de risco já documentada no kernel para NS/P vs NP (L1/L2) via
`ns_toy_model_vacuous`/`pnp_toy_model_vacuous`.

**4. Contraexemplo** (prosa — Lean seria caro demais para esta auditoria, e não é exigido):
instanciar `Euclidean := Unit`, `OSAxioms := fun _ _ => True`, `ClusterRate := fun _ _ => True`.
`ConstructiveYM4D` para esse `M` é provável em uma linha — não porque Yang–Mills contínuo 4D foi
construído, mas porque a interface admite uma testemunha vazia. **Diferença em relação a
NS/P vs NP:** aqueles dois já têm um lema committed e nomeado documentando exatamente esse
risco (`ns_toy_model_vacuous`, `pnp_toy_model_vacuous`). **Não existe ainda um
`ym_toy_model_vacuous`** para O8 — a mesma vulnerabilidade estrutural está presente e
não-documentada aqui. Este é um achado concreto desta auditoria, independente de qualquer
tentativa futura de formalizar os axiomas OS reais.

**5. N/A.** Não classificado `fiel`, então a pergunta "o `Iff` é `rfl` ou conteúdo" não se
aplica neste nível. Voltaria a ser relevante na obrigação de ligação (L5, já marcada
`NAO_EXISTE_NA_MATHLIB` em `scripts/obligations.json`), se/quando `OSAxioms` ganhar conteúdo
real.

**6. Nível de evidência: `by-source`.** `OSAxioms` não formalizado; classificação por inspeção
direta do tipo Lean, sem necessidade de build — formalizar os axiomas OS reais custaria muito
mais do que esta classificação justifica.
