% ATK-RHTerminal (forma logica): cobertura de S+ pelos K_n, criterio em cada K_n
% e simetria R  =>  HR. (Nao prova o criterio: ele e hipotese, equivalente a HR.)
fof(cobertura, axiom, ![S]: (splus(S) => ?[N]: (n5(N) & k(N,S)))).
fof(criterio, axiom, ![N,S]: ((n5(N) & k(N,S)) => ~zero(S))).
fof(faixa_divide, axiom, ![S]: ((faixa(S) & ~linha(S)) => (splus(S) | splus(r(S))))).
fof(simetria, axiom, ![S]: ((zero(S) & faixa(S)) => (zero(r(S)) & faixa(r(S))))).
fof(rh_def, axiom, (rh <=> ![S]: ((zero(S) & faixa(S)) => linha(S)))).
fof(t31, conjecture, rh).
