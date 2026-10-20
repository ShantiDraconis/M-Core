import ATK.Conditional.YangMills
import ATK.YMOficial

/-!
# F.1/O8: `ConstructiveYM4D` é paramétrica

`ConstructiveYM4D M` só fala de campos abstratos de `M : YMModel` (`OSAxioms`, `ClusterRate`), sem
nenhum dos axiomas de Osterwalder–Schrader escrito. O kernel mostra que ela **não tem conteúdo
fixo**: num modelo ela vale (junto com `ClayYM`), noutro ela falha. Ela só passa a ser sobre
Yang–Mills quando o modelo é fixado, e o kernel não fixa nenhum.

A obrigação O8 contada por `OPEN_MATH` não é esta, é `ATK.YMOficial.YMNucleo`.

Ponto (iii) da auditoria de `YMNucleo`: a fórmula `ATK.YMOficial.wick` coincide com a de
Wick/Isserlis ordenada (pares na ordem original): `wick_dois`, `wick_tres` (ímpar ⇒ 0),
`wick_quatro` (os três emparelhamentos).
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

section Wick

open ATK.YMOficial

variable {S : Type*} (w : S → S → ℂ) (a b c d : S)

theorem wick_dois : wick w [a, b] = w a b := by simp [wick]

theorem wick_tres : wick w [a, b, c] = 0 := by simp [wick, Fin.sum_univ_succ]

theorem wick_quatro : wick w [a, b, c, d] = w a b * w c d + w a c * w b d + w a d * w b c := by
  simp only [wick, List.length_cons, List.length_nil, Fin.sum_univ_succ, Fin.sum_univ_zero]
  simp
  rw [wick_dois w c d, wick_dois w b d, wick_dois w b c]
  ring

end Wick

end ATK.F1YM

#print axioms ATK.F1YM.vale_no_vacuo
#print axioms ATK.F1YM.falha_no_vazio
#print axioms ATK.F1YM.parametrica
#print axioms ATK.F1YM.wick_dois
#print axioms ATK.F1YM.wick_tres
#print axioms ATK.F1YM.wick_quatro
