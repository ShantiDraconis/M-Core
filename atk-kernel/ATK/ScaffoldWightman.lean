import Mathlib
import ATK.SpectralBridge

/-!
# ATK — ScaffoldWightman (andaime mínimo dos axiomas de Wightman)

ANDAIME SIMPLIFICADO, não os axiomas de Wightman completos e tecnicamente
precisos exigidos pela literatura física padrão (Streater–Wightman, "PCT,
Spin and Statistics, and All That"; estrutura confirmada via busca web,
outubro de 2026: espaço de Hilbert com representação unitária do grupo de
Poincaré; vácuo único invariante; condição espectral — momento no cone de
luz futuro; campos como distribuições operator-valued num domínio denso
comum; covariância de Poincaré; localidade/microcausalidade; ciclicidade do
vácuo — ver https://en.wikipedia.org/wiki/Wightman_axioms e a literatura lá
citada). Mathlib não tem: grupo de Poincaré, grupo de Lorentz, distribuições
operator-valued, nem teoria de espectro para operadores não-limitados (esta
última já contornada pelo stub `ATK.SpectralBridge.UnboundedOp`).

Simplificações explícitas, cada uma documentada no campo correspondente da
structure abaixo:

1. `G` é um grupo abstrato qualquer no lugar do grupo de Poincaré.
2. Campos são operadores LIMITADOS (`E →L[ℂ] E`), não distribuições
   operator-valued testadas contra funções de Schwartz.
3. Localidade usa uma relação "tipo-espaço" abstrata dada como parâmetro
   externo, não derivada de uma métrica de Minkowski real.
4. A condição espectral reusa o stub local `ATK.SpectralBridge.LocalSpectrum`
   (autovalores, não espectro geral) em vez do teorema espectral geral para
   operadores não-limitados, que não existe no Mathlib.

Isso serve só para que uma afirmação de existência de uma QFT (em
particular, de Yang-Mills com mass gap) seja enunciável como `Prop`
não-vazia — nada é provado aqui, não há habitante, não há `sorry`, não há
`axiom` novo.
-/

namespace ATK.ScaffoldWightman

open ATK.SpectralBridge

/-- Andaime mínimo dos axiomas de Wightman. Ver aviso de simplificação no
    comentário do arquivo. -/
structure WightmanAxioms (E : Type) [NormedAddCommGroup E] [InnerProductSpace ℂ E]
    [CompleteSpace E] (G : Type) [Group G] (ι : Type) where
  /-- SIMPLIFICAÇÃO 1: representação unitária de um grupo abstrato `G`, no
      lugar do grupo de Poincaré (que o Mathlib não formaliza). -/
  rep : G →* (E ≃ₗᵢ[ℂ] E)
  vacuum : E
  vacuum_unit : ‖vacuum‖ = 1
  vacuum_invariant : ∀ g : G, rep g vacuum = vacuum
  /-- SIMPLIFICAÇÃO 2: campos como operadores LIMITADOS indexados por `ι`,
      não distribuições operator-valued (Mathlib não tem essa teoria). -/
  fields : ι → E →L[ℂ] E
  /-- SIMPLIFICAÇÃO 3: relação "tipo-espaço" dada como parâmetro externo,
      não derivada de uma métrica de Minkowski. -/
  spacelike : ι → ι → Prop
  locality : ∀ i j, spacelike i j → fields i * fields j = fields j * fields i
  cyclicity :
    Dense (↑(Submodule.span ℂ (Set.range (fun i => fields i vacuum))) : Set E)
  /-- SIMPLIFICAÇÃO 4: condição espectral via o stub local
      `ATK.SpectralBridge.UnboundedOp`/`LocalSpectrum`, não o teorema
      espectral geral para operadores não-limitados. -/
  energy : UnboundedOp E
  energy_selfadjoint : LocalSelfAdjoint energy
  spectrum_condition : ∀ lam ∈ LocalSpectrum energy, 0 ≤ lam.re

/-- Obrigação aberta: existe uma QFT (neste sentido simplificado) com mass
    gap estrito — isto é, o espectro pontual de energia tem ínfimo positivo
    acima de zero. Nenhum habitante é fornecido; isto NÃO decide a
    existência de Yang-Mills em 4D nem o mass gap — é só a declaração do
    tipo da obrigação, usando o andaime simplificado acima. -/
def MassGapObligation (E : Type) [NormedAddCommGroup E] [InnerProductSpace ℂ E]
    [CompleteSpace E] (G : Type) [Group G] (ι : Type) : Prop :=
  ∃ W : WightmanAxioms E G ι, ∃ Δ : ℝ, 0 < Δ ∧
    ∀ lam ∈ LocalSpectrum W.energy, lam ≠ 0 → Δ ≤ lam.re

end ATK.ScaffoldWightman
