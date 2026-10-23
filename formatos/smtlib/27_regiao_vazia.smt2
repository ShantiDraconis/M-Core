; Regiao 1/2 + 1/T <= sigma <= 1 - 1/T vazia para 0 < T < 4 (ATK.ErrosAnaliticos.R_vazio):
; com u = 1/T > 1/4, nao existe sigma.
(set-logic QF_LRA)
(declare-const u Real) (declare-const s Real)
(assert (< 0.25 u))
(assert (and (<= (+ 0.5 u) s) (<= s (- 1.0 u))))
(check-sat)
