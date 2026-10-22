% ATK-Closed Math: os quatro estados pontuais sao exaustivos e mutuamente exclusivos,
% e "ambos" num mesmo ponto e contraditorio.
fof(def_c, axiom, ![S]: (c(S) <=> (zero(S) & linha(S)))).
fof(def_e, axiom, ![S]: (e(S) <=> (zero(S) & ~linha(S)))).
fof(def_nc, axiom, ![S]: (nc(S) <=> (~zero(S) & linha(S)))).
fof(def_ne, axiom, ![S]: (ne(S) <=> (~zero(S) & ~linha(S)))).
fof(completude, conjecture,
  ![S]: ( (c(S) | e(S) | nc(S) | ne(S))
        & ~(c(S) & e(S)) & ~(c(S) & nc(S)) & ~(c(S) & ne(S))
        & ~(e(S) & nc(S)) & ~(e(S) & ne(S)) & ~(nc(S) & ne(S)) )).
