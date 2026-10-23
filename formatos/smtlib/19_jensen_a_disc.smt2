; a = (1,2,2): J_{N,0} = 1 + 2N X + N(N-1) X^2 tem discriminante 4N > 0 para N >= 1
; (ATK.GeometriaExtra.jensen_a_hiperbolico)
(set-logic QF_NRA)
(declare-const N Real)
(assert (>= N 1.0))
(assert (not (and (= (- (* (* 2.0 N) (* 2.0 N)) (* 4.0 (* N (- N 1.0)))) (* 4.0 N))
                  (> (* 4.0 N) 0.0))))
(check-sat)
