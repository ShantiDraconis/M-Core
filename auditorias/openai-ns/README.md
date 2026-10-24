# Auditoria independente: a prova em Lean da explosão de Navier–Stokes (OpenAI, 8/9/2026)

Objeto: `openai/NavierStokesAndEuler`, commit `f9e8bc5b38b6e212696e8a30e3e91517af887bbd` (Apache-2.0).
Teoremas auditados: `NavierStokes.Comparator.navier_stokes_breakdown_R3` (alternativa (C) do Clay, ℝ³) e
`NavierStokes.Comparator.navier_stokes_breakdown_periodic` (alternativa (D), ℝ³/ℤ³).

## 1. O enunciado

* O desafio (`ComparatorChallenges/NavierStokes.lean`) é o enunciado da **Formal Conjectures** (Google DeepMind,
  commit `8bf45ed`) com mudanças só cosméticas: atributos `category`/`AMS` removidos, notações locais, namespace
  `NavierStokes.Comparator`, e os teoremas (A)/(B) retirados (`compara_enunciados.py`: 44 linhas de diff, todas
  dessas categorias).
* As definições usadas pela solução (`NavierStokes/ComparatorDefinitions.lean`) são **idênticas** às do desafio,
  exceto pela retirada dos dois teoremas com `sorry` (13 linhas de diff, só remoções).
* Leitura contra o texto oficial (Fefferman, 2000), alternativa (C): existem `u⁰` suave, de divergência nula, com
  decaimento (4), e `f` suave em `ℝ³ × [0, ∞)` com decaimento (5), para os quais **não** existe `(p, u)` com
  (1) equação, (2) divergência nula, (3) dado inicial, (6) `p, u ∈ C^∞(ℝ³ × [0, ∞))` e (7) energia limitada.
  A tradução confere item por item: (1) com `derivWithin` em `[0, ∞)`, termo convectivo `Dv(v)`, `Δ` e `gradient`
  da Mathlib; (4) e (5) com `iteratedFDeriv`/`iteratedFDerivWithin` e todo `m`, `K`; (6) com `ContDiffOn ℝ ∞`
  (`∞` = suave, não analítico); (7) com `MemLp 2` e `∃ E, ∀ t ≥ 0, ∫ ‖v‖² < E`. Vale para **todo** `ν > 0`, mais forte
  que o enunciado do Clay (um `ν` fixo). (D) é o análogo periódico, com a pressão periódica (errata do Clay).
* **Não-vacuidade, certificada** (`NaoVacuidade.lean`, axiomas padrão): o dado nulo `u⁰ = 0`, `f = 0` é admissível e
  tem solução global `v = 0`, `p = 0`. A classe de soluções não é vazia por construção; "não existe solução" é uma
  propriedade genuína de um dado específico.
* **Alcance.** O Clay aceita qualquer uma das quatro alternativas (A)–(D). Se a prova vale, ela resolve o problema
  do milênio pela alternativa (C) (e (D)): **existe** força suave que produz explosão. Ela **não** decide (A)
  (regularidade global sem força, `f ≡ 0`), que continua aberta. A linha NS do ATK (`ATK.LigacaoNS.clayA_iff`) é a
  (A); o seu portão terminal não muda.

## 2. A fonte

`varredura.py` em 2655 arquivos (640 857 linhas; 816 de Navier–Stokes): **nenhuma** ocorrência de `sorry`, `admit`,
`axiom`, `native_decide`, `implemented_by`, `@[extern]`, `unsafe`, `opaque`, `skipKernelTC`, `debug.*`, `addDecl`,
`Lean.Elab`, `#exit`, `elab`/`macro`/`syntax`, `run_cmd`/`run_elab`, `initialize`, `ofReduceBool`, `#eval` ou
`set_option`; nenhum import fora de `Mathlib`, `NavierStokes` e `Euler`. Não há caminho para burlar o kernel nem
para redefinir notação.

## 3. O kernel

* **Neste ambiente** (Lean 4.34.1, Mathlib v4.34.1; o projeto usa 4.34.0-rc2): do cone de 609 módulos de
  `ComparatorSolution`, 287 compilaram, 8 falharam e 314 ficaram bloqueados. As 8 falhas são **mudança de API do
  Mathlib** entre as versões (`MemLp` redefinida como `eLpNorm f p μ < ∞`, assinaturas de `eLpNorm_mono_ae`,
  `eLpNorm_add_le`, `Finset.prod_le_one`), não erro matemático. O cache do Mathlib rc2 não é acessível daqui.
* **No CI** (`.github/workflows/auditoria-openai-ns.yml`): toolchain e Mathlib exatos do projeto (`lake exe cache
  get`), compilação de `NavierStokes.ComparatorSolution`, `#print axioms`, o mini-comparador `Auditoria.lean` (que
  reescreve literalmente os enunciados (C) e (D) do desafio e os fecha com os teoremas da OpenAI) e `NaoVacuidade.lean`.
  Resultado: ver a execução do workflow e a seção 4.

## 4. Veredito

Preenchido após a execução do CI.

## 5. O que esta auditoria não cobre

* A correspondência entre a prova em Lean e o texto em linguagem natural (Bastounis–Circelli–Hansen,
  arXiv:2610.08144, apontam pelo menos uma divergência, `m + 5` contra `m + 4` derivadas): isso afeta o artigo, não a
  validade do teorema em Lean.
* Crédito e procedência (a disputa com Buckmaster–Alpöge): fora do escopo de um kernel.
* A comparação com o `comparator` oficial (com `lean4export` + `nanoda`, um segundo kernel independente): não
  executada aqui.
