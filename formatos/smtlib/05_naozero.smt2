; P5: g != 0  =>  G(2) = ((3/2-d)^2+g^2)((3/2+d)^2+g^2) > 0 e G(1/2) = (d^2+g^2)^2 > 0.
(set-logic QF_NRA)
(declare-const d Real) (declare-const g Real)
(assert (not (= g 0.0)))
(assert (not (and (> (* (+ (* (- 1.5 d) (- 1.5 d)) (* g g)) (+ (* (+ 1.5 d) (+ 1.5 d)) (* g g))) 0.0)
                  (> (* (+ (* d d) (* g g)) (+ (* d d) (* g g))) 0.0))))
(check-sat)
