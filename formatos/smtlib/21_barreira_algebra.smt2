; Barreira: a = b + t  (a = beta^2+gamma^2, b = (1-beta)^2+gamma^2, t = 2 beta - 1), e
; numerador da derivada em beta: d/dbeta [t b] = 2b + 2t(beta-1)  (ATK.BarreiraModelos.deriv_beta)
(set-logic QF_NRA)
(declare-const be Real) (declare-const ga Real)
(define-fun a () Real (+ (* be be) (* ga ga)))
(define-fun b () Real (+ (* (- 1.0 be) (- 1.0 be)) (* ga ga)))
(define-fun t () Real (- (* 2.0 be) 1.0))
(assert (not (= a (+ b t))))
(check-sat)
