; Xi(t) = 2 int_0^inf Phi(u) cos(tu) du (ATK.XiPhi.constante_zero): com 4T = psi(1) + 1/2
; (equacao funcional de theta derivada em x = 1) e S = sum h'(0) = psi(1)/2 - 2T,
; a constante 1/2 + 2S e zero.
(set-logic QF_LRA)
(declare-const P Real) (declare-const T Real) (declare-const S Real)
(assert (= (* 4.0 T) (+ P 0.5)))
(assert (= S (- (* 0.5 P) (* 2.0 T))))
(assert (not (= (+ 0.5 (* 2.0 S)) 0.0)))
(check-sat)
