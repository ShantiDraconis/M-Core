; Curvatura do toro: K = c/(r(R + r c)) >= -1/(r(R - r)) para -1 <= c <= 1, 0 < r < R.
(set-logic QF_NRA)
(declare-const R Real) (declare-const r Real) (declare-const c Real)
(declare-const K Real) (declare-const m Real)
(assert (< 0.0 r)) (assert (< r R)) (assert (<= -1.0 c)) (assert (<= c 1.0))
(assert (= (* K (* r (+ R (* r c)))) c))
(assert (= (* m (* r (- R r))) -1.0))
(assert (< K m))
(check-sat)
