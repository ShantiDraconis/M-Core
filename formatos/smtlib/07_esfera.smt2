; Projeção estereográfica cai na esfera: com D (1 + a^2 + b^2) = 1.
(set-logic QF_NRA)
(declare-const a Real) (declare-const b Real) (declare-const D Real)
(assert (= (* D (+ 1.0 (* a a) (* b b))) 1.0))
(define-fun X () Real (* 2.0 a D))
(define-fun Y () Real (* 2.0 b D))
(define-fun Z () Real (* (- (+ (* a a) (* b b)) 1.0) D))
(assert (not (= (+ (* X X) (* Y Y) (* Z Z)) 1.0)))
(check-sat)
