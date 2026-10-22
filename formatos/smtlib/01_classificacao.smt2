; Exaustividade e exclusividade dos quatro estados (lógica proposicional).
(set-logic QF_UF)
(declare-const zero Bool)
(declare-const linha Bool)
(define-fun C () Bool (and zero linha))
(define-fun E () Bool (and zero (not linha)))
(define-fun NC () Bool (and (not zero) linha))
(define-fun NE () Bool (and (not zero) (not linha)))
; negação de: exatamente um estado vale
(assert (not (and (or C E NC NE)
                  (not (and C E)) (not (and C NC)) (not (and C NE))
                  (not (and E NC)) (not (and E NE)) (not (and NC NE)))))
(check-sat)
