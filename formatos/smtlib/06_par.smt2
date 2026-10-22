; T4/T5/T6: centro 1/2 + it, separação^2 = 4 d^2, coincidência sse d = 0.
(set-logic QF_NRA)
(declare-const d Real) (declare-const t Real)
(assert (not (and (= (/ (+ (+ 0.5 d) (- 0.5 d)) 2.0) 0.5)
                  (= (* (- (+ 0.5 d) (- 0.5 d)) (- (+ 0.5 d) (- 0.5 d))) (* 4.0 d d))
                  (= (= (+ 0.5 d) (- 0.5 d)) (= d 0.0)))))
(check-sat)
