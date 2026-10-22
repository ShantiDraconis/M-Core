% Tempos verbais: perfeito exige o enunciado, negado exige a negacao.
fof(perfeito, axiom, ![A]: ((tempo_perfeito(A) & valida(A)) => verdadeiro(A))).
fof(negado, axiom, ![A]: ((tempo_negado(A) & valida(A)) => ~verdadeiro(A))).
fof(exclusivos, axiom, ![A]: ~(tempo_perfeito(A) & tempo_negado(A))).
fof(t, conjecture, ![A,B]: ((tempo_perfeito(A) & valida(A) & tempo_negado(B) & valida(B)
                              & (verdadeiro(A) <=> verdadeiro(B))) => $false)).
