; Hadamard de genero 0 (ATK.Edrei.prodCoef, ATK.Hadamard.coef_eq_lim): coeficientes de a0*prod(1 + alpha_j z) pela
; recursao do Lean, com a0 = 1, alpha = (1/2, 1/3): depois de dois fatores, 1 + (5/6)z + (1/6)z^2. Os coeficientes
; crescem com o numero de fatores (prodCoef_mono) e ficam <= a0*(soma alpha)^n (prodCoef_le: 1/6 <= 25/36).
; Nega-se a conjuncao: espera-se unsat.
(set-logic QF_LRA)
(declare-const p10 Real) (declare-const p11 Real) (declare-const p12 Real)
(declare-const p20 Real) (declare-const p21 Real) (declare-const p22 Real)
(assert (= p10 1.0)) (assert (= (* 2.0 p11) 1.0)) (assert (= p12 0.0))
(assert (= p20 p10)) (assert (= (* 3.0 p21) (+ (* 3.0 p11) p10))) (assert (= (* 3.0 p22) (+ (* 3.0 p12) p11)))
(assert (not (and (= (* 6.0 p21) 5.0) (= (* 6.0 p22) 1.0) (<= p11 p21) (<= p12 p22) (<= (* 36.0 p22) 25.0))))
(check-sat)
