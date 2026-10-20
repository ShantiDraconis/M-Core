import ATK.Conditional.YangMills

/-!
# F.1/O8: `ConstructiveYM4D` é paramétrica

`ConstructiveYM4D M` só fala de campos abstratos de `M : YMModel` (`OSAxioms`, `ClusterRate`), sem
nenhum dos axiomas de Osterwalder–Schrader escrito. O kernel mostra que ela **não tem conteúdo
fixo**: num modelo ela vale (junto com `ClayYM`), noutro ela falha. Ela só passa a ser sobre
Yang–Mills quando o modelo é fixado, e o kernel não fixa nenhum.

A obrigação O8 contada por `OPEN_MATH` não é esta, é `ATK.YMOficial.YMNucleo`.
-/

namespace ATK.F1YM

open ATK.Conditional.YangMills

/-- Modelo com `OSAxioms` e `ClusterRate` sempre verdadeiros. -/
def modeloVacuo : YMModel.{0, 0, 0} where
  Group := Unit
  CompactSimple := fun _ => True
  Euclidean := Unit
  OSAxioms := fun _ _ => True
  ClusterRate := fun _ _ => True
  Quantum := Unit
  reconstruct := fun _ => ()
  IsQuantumYM := fun _ _ => True
  GapAtLeast := fun _ _ => True

/-- Modelo com `OSAxioms` sempre falso. -/
def modeloVazio : YMModel.{0, 0, 0} :=
  { modeloVacuo with OSAxioms := fun _ _ => False }

/-- **Num modelo, `ConstructiveYM4D`, a ponte e o enunciado "Clay" valem trivialmente.** -/
theorem vale_no_vacuo :
    ConstructiveYM4D modeloVacuo ∧ OSReconstruction modeloVacuo ∧ ClayYM modeloVacuo :=
  ⟨fun _ _ => ⟨(), trivial, 1, one_pos, trivial⟩,
   fun _ _ _ => ⟨trivial, fun _ _ => trivial⟩,
   fun _ _ => ⟨(), trivial, 1, one_pos, trivial⟩⟩

/-- **Noutro, falha.** -/
theorem falha_no_vazio : ¬ ConstructiveYM4D modeloVazio := fun h => by
  obtain ⟨_, hOS, _⟩ := h () trivial
  exact hOS

/-- **Veredito**: o valor de `ConstructiveYM4D` depende só do modelo; sem fixar o modelo ela não é
um enunciado sobre Yang–Mills. -/
theorem parametrica :
    (∃ M : YMModel.{0, 0, 0}, ConstructiveYM4D M) ∧ (∃ M : YMModel.{0, 0, 0}, ¬ ConstructiveYM4D M) :=
  ⟨⟨_, vale_no_vacuo.1⟩, ⟨_, falha_no_vazio⟩⟩

end ATK.F1YM

#print axioms ATK.F1YM.vale_no_vacuo
#print axioms ATK.F1YM.falha_no_vazio
#print axioms ATK.F1YM.parametrica
