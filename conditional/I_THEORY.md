# A teoria de `I` — levantamento completo, formalização e veredito do kernel

`I` = conjunto dos números indeterminados. Este documento reúne **tudo o que o acervo propõe** sobre
`I` (leis, fundamentação, álgebra, geometria, estados, operações, operadores) e diz, item por item,
o que o kernel do Lean **certificou**, o que ele **refutou** e o que **não é formalizável** como está.
Nada aqui fecha uma obrigação O1–O8: `CLOSED_MATH` continua `false`.

## 1. Levantamento

* Varredura de todos os branches dos 224 repositórios com commits (`scripts/i_scan.py`): **4.922
  arquivos distintos** em **79 repositórios** tratam de `I` (3.179 Markdown, 717 Python, 527 Lean,
  306 LaTeX, 77 Coq, 52 Isabelle, 29 Agda, 35 texto). Os núcleos: `the-algebra-of-ideterminate-i`,
  `indeterminate-collapse-core`, `meta-mathematics-indeterminate-i`, `i-constant-core` (T-State),
  `riemann-indeterminacy`, `universe-0-0` (torque/neon), `millennium` (lei do zero harappiana).
* Catálogo deduplicado em `catalog/ilaws/` — **586 leis/hipóteses/teoremas**, cada um com fonte
  (repositório · branch:caminho · blob) e veredito:

| catálogo | linhas | conteúdo |
|---|---|---|
| `A_algebra_of_I.md` | 220 | sistema cardinal I1–I7, `K_I` com 15 postulados, PAX, meadow absorvente, NexusField, AEI "I = 1/0", IEA, multiestado, rodas, lógica, ultrapotências |
| `B_collapse_meta.md` | 164 | axiomas de colapso/propagação/estabilidade, ExtendedReal, Phi3, pontes "IReformulation/MainBridge" dos 7 problemas |
| `C_constant_tstate_logic.md` | 150 | constante `I`, Δ = 0.∞19, T-State e tabelas de limites, lógicas de 3/6 estados, enunciados sobre a reta crítica |
| `D_geometry.md` | 52 | geometria: extremos fechados → meio, neutro, tensão/compressão/torção, torque `𝕋`, ampulheta, operador zero |

Achados estruturais do levantamento:

1. **Não existe uma definição única de `I`**: há pelo menos nove portadores incompatíveis entre si
   (`0·I` vale `0`, `I`, `1` ou um elemento novo conforme o arquivo; `I − I` vale `I` ou `0`).
2. **Vários conjuntos de axiomas são inconsistentes** — o arquivo que os declara prova `False`:
   os 15 postulados PAX/`K_I`, o axioma P1 "toda transformação fixa `I`" (importado por todos os
   `*Core/MainBridge.lean`), `I_invariant` (`IConstant.lean`), os axiomas de Δ em Isabelle, a equação
   funcional "total" em Isabelle (falha em `s = 0`), `discrete_geometric_correction`
   (`HarappanGeometry/Core.lean`) e mais 14 listados em `A_algebra_of_I.md` §4.
3. **Nenhuma ponte para os problemas do milênio tem conteúdo**: as seis `MainBridge` só provam que
   um construtor difere de outro; o lado clássico é `True` ou `sorry`.
4. A frase "início fechado tendendo a meio fechado e fim fechado tendendo ao mesmo meio, o neutro
   tensionado, comprimido, torcido" **não aparece literalmente**; a figura aparece em ~8 formas
   (ampulheta do neon com cintura em 1/2, torque `𝕋` = 1 nos extremos e 0 em 1/2, "forças dos dois
   lados se cancelam em σ = 1/2", partição meio-aberta com célula central, inversão dual
   `x ↦ 2c − x`, tração/retração/torção, neutro de Kleene). Todas são conjugadas a **um** modelo,
   formalizado abaixo.

## 2. O que o kernel certificou — 186 teoremas novos, 4 módulos

Todos compilam sem `sorry`, sem axiomas novos; `#print axioms` só mostra `propext`,
`Classical.choice`, `Quot.sound` (ou nenhum).

### `ATK/IFormas.lean` (53) — `I` materializado: as sete formas e seus conjuntos de valores

O "valor" de uma forma é o conjunto dos limites atingíveis em `[−∞, +∞]` quando `t → 0⁺`:

| forma | conjunto de valores | teorema |
|---|---|---|
| `0/0`, `0·∞`, `∞ − ∞` | `[−∞, +∞]` inteiro | `div00_eq`, `mul0Inf_eq`, `subInf_eq` |
| `∞/∞`, `1^∞`, `0^0`, `∞^0` | `[0, +∞]` | `divInf_eq`, `pow1Inf_eq`, `pow00_eq`, `powInf0_eq` |

As sete realizam também o estado `oscila` (`*_oscila`), são **indeterminadas** (conjunto com mais
de um ponto: `sete_indeterminadas`) e as de potência nunca valem `−∞` (`sem_menosInf`). Contraste —
formas **determinadas** (conjunto unitário, fora de `I`): `a + b`, `∞ + ∞ = ∞`, `∞·∞ = ∞`, `a/∞ = 0`,
`0^∞ = 0` (`determinadas`). Refutação: "`lim x/x = I`" é falso, `x/x → 1` e `x²/x → 0`
(`x_div_x`, `x2_div_x`) — o mesmo `0/0` com germes diferentes dá valores diferentes.

### `ATK/IAlgebra.lean` (34) — a álgebra: consistente × inconsistente

* **Impossibilidades** (cada uma refuta axiomas do acervo): absorvente único
  (`absorvente_unico`); absorvente = neutro ⇒ estrutura trivial (`absorvente_zero_trivial`);
  `I + I = I` com `I − I = 0` ⇒ `I = 0` (`idempotente_inverso`, `pax_inconsistente`); absorvente com
  inverso ⇒ trivial (`absorvente_inverso_trivial`); `x·I = I ∀x` ⇒ `I = 0` (`mul_absorvente_zero`);
  **triângulo** `I + x = I`, `I·0 = 0`, `I·1 = I`, distributividade ⇒ `I = 0` (`triangulo`); `I² = I`
  num domínio ⇒ `I ∈ {0,1}` (`idempotente_dominio`); P1 e `I_invariant` falsos
  (`propagacao_universal_falsa`, `invariancia_falsa`); transformações estáveis = `Option.map f`
  (`estavel_iff_map`).
* **Modelos consistentes**: `Option ℝ` com `I` absorvente — monoides comutativos, **distributividade
  total**, `0·I = I`, `I` sem inverso (`addI_*`, `mulI_*`, `mulI_addI`, `I_sem_inverso`,
  `zero_mulI_I`); modelo multiestado `I := ℝ` — `{x}+I = I`, `{x}·I = I` (x ≠ 0), `{0}·I = {0}`,
  `I+I = I·I = I−I = I`, só subdistributividade, e a distributividade **falha**
  (`distributiva_falha`); testemunha `(1,0) ∈ ℝ²` (`testemunha_idempotente`).
* **Δ infinitesimal**: existe nos hiper-reais (`delta_hiperreal`), não em `ℝ`
  (`delta_real_nao_existe`) — única leitura consistente de "Δ = 0.∞19".

### `ATK/IGeometria.lean` (56) — a geometria do neutro

* Tensão `ρ(x) = 1 − x`: involução, único fixo `1/2`, troca `[0,1/2)` ↔ `(1/2,1]`, fechos só se tocam
  no neutro (`rho_*`, `fechos_metades`, `metades_*`).
* Compressão `D_λ`: fixa o neutro, compõe, comuta com a tensão; iterada converge ao neutro
  (`compressao_converge`), tração diverge (`tracao_diverge`); rigidez — quem comuta com a tensão fixa
  `1/2` (`rigidez_neutro`).
* **O processo**: `⋂ [1/2 − 1/(n+1), 1/2] = {1/2}` (`inicio_fechado_meio`),
  `⋂ [1/2, 1/2 + 1/(n+1)] = {1/2}` (`fim_fechado_meio`) — **o mesmo meio**; os meio-abertos convergem
  ao vazio (`meio_aberto_esquerda`, `meio_aberto_direita`).
* Torção no plano `R_θ`: fixa o neutro, compõe, `R_π` = tensão (`R_*`).
* Torque do acervo `𝕋(x) = |x − 1/2|/|x + 1/2|`: `𝕋(0) = 1`, `𝕋 → 1` no infinito, `𝕋 = 0` só em
  `1/2`, `𝕋 < 1` em `(0,∞)`, simetria `𝕋(1/(4x)) = 𝕋(x)`; no plano, `𝕋 < 1 ⟺ Re z > 0`
  (`T_*`, `torcao_plano`); refutação da faixa alegada: `𝕋(−1) = 3`.
* Conjugações `x ↦ 1−x` ≅ `u ↦ −u` ≅ `y ↦ 1/y` (`conj_afim`, `conj_log`, `inv_fixo_iff`).
* Lógica K3 com neutro `N`: único fixo da negação, De Morgan, Kleene, terceiro excluído falha só em
  `N`, LP não explode, `K3 ↪ [0,1]` com `N ↦ 1/2` e negação ↦ tensão (`K3.*`).

### `ATK/ZetaSimetria.lean` (43) — a geometria aplicada aos zeros de ζ (Mathlib)

* **Extremos fechados**: `Re s ≥ 1` sem zeros (Mathlib) e `Re s ≤ 0` só com zeros triviais
  (`zero_trivial_de_re_nao_pos`); todo zero não trivial está em `0 < Re s < 1` (`zero_na_faixa`).
* **O eixo neutro**: `ζ(σ)` é real e **negativo** em `(0,1)` (`zeta_real_neg`), em particular
  `ζ(1/2) < 0` (`zeta_meio_neg`); nenhum zero não trivial é real (`im_ne_zero_of_mem_Z`).
* **Simetrias**: zeros invariantes pela tensão `s ↦ 1−s`, pelo espelho `s ↦ s̄` e pela torção
  `s ↦ 1−s̄` (`*_mem_Z`); a reta crítica é exatamente o conjunto fixo da torção
  (`torcao_fixo_iff`); **quartetos**: zero fora da reta tem órbita de 4 pontos distintos, na reta de 2
  (`quarteto`).
* **Os dois processos são um só**: "`[a, ∞)` sem zeros" ⟺ "`(−∞, 1−a]` sem zeros não triviais"
  (`fim_iff_inicio`). **RH ⟺** o fim chega ao meio (`riemann_iff_fim`) ⟺ o início chega ao meio
  (`riemann_iff_inicio`) ⟺ todo zero é fixo pela torção (`riemann_iff_torcao`) ⟺ toda compressão
  preserva as partes reais dos zeros (`riemann_iff_compressao`) ⟺ colares arbitrariamente finos
  (`riemann_iff_colares`). Os extremos certificados são `a = 1` e `b = 0`; o limite `a ↓ 1/2` **é**
  RH (obrigação O1) e continua aberto.

## 3. O que não é teorema

* **Equivalente a RH ou circular** (não demonstrável aqui): o "Teorema da Estabilidade de Fase", o
  teorema do desvio 0,70, a ponte energia–zeros, a "prisão geométrica", o colapso Δ com `I ≠ 1`, a
  unicidade vale/parede — ver `C_constant_tstate_logic.md` §4 e `D_geometry.md` §2. O kernel prova
  só as **equivalências** acima, não o limite.
* **Falso** (contraexemplo no catálogo): 64 itens em A, dezenas em B, C e D — p.ex. De Morgan da
  lógica LS6, "razões de Fibonacci oscilam em torno de 0,5", "x/x → I", o limite
  `sin(πs/2)/Γ(1−s)⁻¹ → π/2` (tende a 0), "rodas são modelos" da álgebra do colapso.
* **Vago** (sem conteúdo matemático preciso): 18 itens em A e os axiomas em prosa de B e C.

## 4. Reprodução

`scripts/i_scan.py <repo> <corpus>` refaz a coleta; os catálogos estão em `catalog/ilaws/`; os
quatro módulos estão em `atk-kernel/ATK/` e entram no CI (`scripts/expected_theorems.txt`, 442
teoremas esperados).
