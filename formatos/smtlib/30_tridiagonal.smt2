; Menores tridiagonais de 1 + x + x^2 (ATK.ToeplitzTN.um_x_x2): D_{r+2} = D_{r+1} - D_r,
; D_0 = D_1 = 1, logo D_3 = -1 < 0 e T(1,1,1) nao e totalmente nao negativa.
(set-logic QF_LRA)
(declare-const d0 Real) (declare-const d1 Real) (declare-const d2 Real) (declare-const d3 Real)
(assert (= d0 1.0)) (assert (= d1 1.0))
(assert (= d2 (- d1 d0))) (assert (= d3 (- d2 d1)))
(assert (not (< d3 0.0)))
(check-sat)
