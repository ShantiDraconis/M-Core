; G12 = 3/4 (log 2 + log pi - gamma) - 1/4 log 2 (ATK.ErrosGram.G12_cotas): com as cotas certificadas,
; G12 > 0,7722084, acima do valor tabelado 0,7722083.
(set-logic QF_LRA)
(declare-const g Real) (declare-const l2 Real) (declare-const lp Real)
(assert (< g 0.5772163)) (assert (< 0.6931471803 l2)) (assert (< l2 0.6931471808)) (assert (< 1.1447295 lp))
(assert (not (< 0.7722084 (- (* 0.75 (- (+ l2 lp) g)) (* 0.25 l2)))))
(check-sat)
