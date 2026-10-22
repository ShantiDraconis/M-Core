; P1: G_{d,g}(1/2 + d + i g) = 0 (componentes). s - 1/2 - d = (x, y); com x = 0, y = g.
(set-logic QF_NRA)
(declare-const d Real)
(declare-const g Real)
(define-fun ux () Real 0.0)
(define-fun uy () Real g)
; fator 1: u^2 + g^2  (u complexo): re = ux^2 - uy^2 + g^2, im = 2 ux uy
(define-fun f1r () Real (+ (- (* ux ux) (* uy uy)) (* g g)))
(define-fun f1i () Real (* 2.0 ux uy))
(assert (not (and (= f1r 0.0) (= f1i 0.0))))
(check-sat)
