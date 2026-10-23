; Ajuste de dois pontos (ATK.BarreiraModelos.produto_decresce / ajuste_negativo):
; com 0,6931471803 < log 2 < 0,6931471808 e 0,2231435 < log 5 - log 4 < 0,2231436,
; D8000 (6 log 2 + 3 log 5) < D256 * 8 log 2, e o intercepto a = (D8000 L1 - D256 L0)/(L1 - L0) < -2,90e-5.
(set-logic QF_LRA)
(declare-const l2 Real) (declare-const l5 Real)
(assert (< 0.6931471803 l2)) (assert (< l2 0.6931471808))
(assert (< 0.2231435 (- l5 (* 2.0 l2)))) (assert (< (- l5 (* 2.0 l2)) 0.2231436))
(define-fun L0 () Real (* 8.0 l2))
(define-fun L1 () Real (+ (* 6.0 l2) (* 3.0 l5)))
(define-fun P0 () Real (* 0.0082337162772 L0))
(define-fun P1 () Real (* 0.0050691202 L1))
; a < -2.90e-5  <=>  P1 - P0 < -2.90e-5 (L1 - L0)   (L1 > L0)
(assert (not (and (< P1 P0) (< (- P1 P0) (* (- 0.0000290) (- L1 L0))))))
(check-sat)
