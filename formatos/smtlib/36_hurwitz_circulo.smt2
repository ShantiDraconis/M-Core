; Hurwitz (ATK.Hurwitz.hurwitz_local), o passo do circulo: se |g| >= delta na circunferencia e |g - F| < delta/2,
; entao |F| >= |g| - |g - F| > delta/2; e no centro |F(z0)| = |F(z0) - g(z0)| < delta/2 (g(z0) = 0). O modulo maximo
; para 1/F exige |F(z0)| >= min_circ |F| > delta/2 — contradicao. Variaveis = normas. Espera-se unsat.
(set-logic QF_LRA)
(declare-const delta Real) (declare-const g Real) (declare-const e Real) (declare-const F Real)
(declare-const F0 Real) (declare-const e0 Real)
(assert (> delta 0.0)) (assert (>= g delta)) (assert (< e (* 0.5 delta))) (assert (>= F (- g e)))
(assert (< e0 (* 0.5 delta))) (assert (= F0 e0))
(assert (>= F0 F))
(check-sat)
