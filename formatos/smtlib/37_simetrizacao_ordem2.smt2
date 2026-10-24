; Identidade de dispersao de ordem 2 (ATK.TuranDisp.turan_disp): o integrando simetrizado
; K(t)K(s)(ts)^{2m+2}(t^2 - s^2)(psi(t) - psi(s)) e >= 0 quando psi e crescente; o nucleo do argumento e
; (t^2 - s^2)(psi t - psi s) >= 0 para t, s > 0 com (t <= s => psi t <= psi s) e (s <= t => psi s <= psi t).
; Nega-se: espera-se unsat.
(set-logic QF_NRA)
(declare-const t Real) (declare-const s Real) (declare-const pt Real) (declare-const ps Real)
(assert (> t 0.0)) (assert (> s 0.0))
(assert (=> (<= t s) (<= pt ps))) (assert (=> (<= s t) (<= ps pt)))
(assert (< (* (- (* t t) (* s s)) (- pt ps)) 0.0))
(check-sat)
