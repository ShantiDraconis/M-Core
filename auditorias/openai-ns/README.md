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
  Execução [40131056493](https://github.com/ShantiDraconis/M-Core/actions/runs/40131056493) (commit `ba0f178`,
  24/10/2026, 1 h 23 min): **sucesso**.
* Por que o sucesso é evidência: o passo de axiomas sai com erro se **qualquer** um dos seis teoremas não imprimir
  exatamente `[propext, Classical.choice, Quot.sound]`, ou se a saída contiver `error`. `lake env lean` não compila
  dependências; ele só importa `.olean` prontos. Então a importação de `NavierStokes.ComparatorSolution` em
  `Auditoria.lean` só funciona se o cone inteiro tiver sido compilado, ou seja, verificado pelo kernel. Na primeira
  execução, o passo de compilação passava por `| tail -40` sem `pipefail`, então o código de saída dele não contava
  sozinho. O workflow agora usa `shell: bash` (`-eo pipefail`) e publica anotações (`::notice`) com o tempo e a
  memória da compilação e cada teorema certificado. Uma execução de confirmação roda junto com este veredito.

## 4. Veredito

| Item | Estado | Evidência |
| --- | --- | --- |
| `navier_stokes_breakdown_R3` (alternativa (C), ℝ³) | **CERTIFIED** (kernel do Lean, axiomas padrão) | CI 40131056493 |
| `navier_stokes_breakdown_periodic` (alternativa (D), ℝ³/ℤ³) | **CERTIFIED** (kernel do Lean, axiomas padrão) | CI 40131056493 |
| O tipo provado **é** o enunciado do desafio (mini-comparador `enunciado_C`, `enunciado_D`) | **CERTIFIED** | CI 40131056493 |
| Enunciado do desafio = Formal Conjectures (DeepMind) a menos de mudanças cosméticas | conferido (texto) | `compara_enunciados.py` |
| Enunciado ↔ texto oficial do Clay (C)/(D), item por item | conferido (leitura) | seção 1 |
| Não-vacuidade: o dado nulo é admissível e tem solução | **CERTIFIED** | `NaoVacuidade.lean`, CI 40131056493 |
| Fonte sem `sorry`/`axiom`/`native_decide`/metaprogramação | conferido (estático) | `varredura.py`, 2655 arquivos |
| Segundo kernel independente (`lean4export` + `nanoda`, o `comparator` oficial) | não executado | — |
| (A): regularidade global sem força | OPEN_MATH (esta prova não decide) | seção 1 |

**Conclusão.** Os teoremas da OpenAI para as alternativas (C) e (D) são aceitos pelo kernel do Lean, com o
toolchain e o Mathlib exatos do projeto e só os três axiomas padrão. O que eles provam é literalmente o enunciado
do desafio, e esse enunciado traduz fielmente (C) e (D) do texto oficial. Não achamos falha.

Esta auditoria **não declara** o problema do milênio resolvido. Isso depende do processo do Clay Institute
(publicação, prazo, comitê), do segundo kernel ainda não executado aqui e das questões de texto e procedência da
seção 5. A alternativa (A), que é a linha NS do ATK (`ATK.LigacaoNS.clayA_iff`), continua OPEN_MATH: o portão
terminal do ATK não muda.

## 5. O que esta auditoria não cobre

* A correspondência entre a prova em Lean e o texto em linguagem natural (Bastounis–Circelli–Hansen,
  arXiv:2610.08144, apontam pelo menos uma divergência, `m + 5` contra `m + 4` derivadas): isso afeta o artigo, não a
  validade do teorema em Lean.
* Crédito e procedência (a disputa com Buckmaster–Alpöge): fora do escopo de um kernel.
* A comparação com o `comparator` oficial (com `lean4export` + `nanoda`, um segundo kernel independente): não
  executada aqui.
