; Menor 3x3 contiguo de Toeplitz (ATK.TruncToep.menor3): det [[a1,a0,0],[a2,a1,a0],[a3,a2,a1]]
; (cofatores na 1a linha) = a1^3 - 2 a0 a1 a2 + a0^2 a3. Nega-se a identidade: espera-se unsat.
(set-logic QF_NRA)
(declare-const a0 Real) (declare-const a1 Real) (declare-const a2 Real) (declare-const a3 Real)
(assert (not (= (- (* a1 (- (* a1 a1) (* a0 a2))) (* a0 (- (* a2 a1) (* a0 a3))))
                (+ (- (* a1 a1 a1) (* 2.0 a0 a1 a2)) (* a0 a0 a3)))))
(check-sat)
