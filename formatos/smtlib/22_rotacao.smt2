; Rotacao preserva d^2 + t^2 (ATK.GeometriaExtra.rotacao), com c^2 + s^2 = 1
(set-logic QF_NRA)
(declare-const d Real) (declare-const t Real) (declare-const c Real) (declare-const s Real)
(assert (= (+ (* c c) (* s s)) 1.0))
(assert (not (= (+ (* (- (* d c) (* t s)) (- (* d c) (* t s))) (* (+ (* d s) (* t c)) (+ (* d s) (* t c))))
                (+ (* d d) (* t t)))))
(check-sat)
