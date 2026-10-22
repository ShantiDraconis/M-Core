; Superfície do toro: x = A cp, y = A sp, z = r st, A = R + r ct, cp^2+sp^2 = 1, ct^2+st^2 = 1,
; q >= 0, q^2 = x^2 + y^2  =>  (q - R)^2 + z^2 = r^2   (com 0 <= r < R).
(set-logic QF_NRA)
(declare-const R Real) (declare-const r Real) (declare-const ct Real) (declare-const st Real)
(declare-const cp Real) (declare-const sp Real) (declare-const q Real)
(assert (<= 0.0 r)) (assert (< r R))
(assert (= (+ (* cp cp) (* sp sp)) 1.0)) (assert (= (+ (* ct ct) (* st st)) 1.0))
(define-fun A () Real (+ R (* r ct)))
(assert (<= 0.0 q))
(assert (= (* q q) (+ (* (* A cp) (* A cp)) (* (* A sp) (* A sp)))))
(assert (not (= (+ (* (- q R) (- q R)) (* (* r st) (* r st))) (* r r))))
(check-sat)
