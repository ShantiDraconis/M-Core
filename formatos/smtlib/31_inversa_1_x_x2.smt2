; Coeficientes de B = 1/(1 - x + x^2) (ATK.ASWReciproca: p(-x)·B = 1 com p = 1 + x + x^2):
; b0 = 1, b1 - b0 = 0, b2 - b1 + b0 = 0, b3 - b2 + b1 = 0, logo b3 = -1 < 0: um menor 1x1 de T(b)
; com coluna inicial e negativo, entao T(1,1,1) nao e totalmente nao negativa (cc_de_tn, contrapositiva).
(set-logic QF_LRA)
(declare-const b0 Real) (declare-const b1 Real) (declare-const b2 Real) (declare-const b3 Real)
(assert (= b0 1.0))
(assert (= (- b1 b0) 0.0))
(assert (= (+ (- b2 b1) b0) 0.0))
(assert (= (+ (- b3 b2) b1) 0.0))
(assert (not (< b3 0.0)))
(check-sat)
