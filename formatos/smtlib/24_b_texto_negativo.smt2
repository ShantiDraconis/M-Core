; Formula do texto para b_k (ATK.ErrosGram.bTexto_neg): b~_{n+1} = (1 - gamma - (H_n - log(n+1)))/(n+1)
; e H_n - log(n+1) >= H_3 - log 4 = 11/6 - 2 log 2 para n >= 3. Com gamma > 0,5772156 e
; log 2 < 0,6931471808: 1 - gamma - (11/6 - 2 log 2) < 0, logo b~_k < 0 para todo k >= 4.
(set-logic QF_LRA)
(declare-const g Real) (declare-const l2 Real) (declare-const s Real)
(assert (< 0.5772156 g)) (assert (< l2 0.6931471808))
(assert (<= (- (/ 11.0 6.0) (* 2.0 l2)) s))
(assert (not (< (- (- 1.0 g) s) 0.0)))
(check-sat)
