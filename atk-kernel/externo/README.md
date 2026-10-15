# atk-kernel/externo

Pacote Lake que compila **junto com o atk-kernel** (mesma Mathlib, `d13f23b` = tag `v4.34.1`)
teoremas externos já provados em Lean, e os usa como teoremas do ATK.

- `ATKExterno/RiemannQuasi.lean`: a quasi-hipótese de Riemann da OpenAI
  (`openai/math` `1581d4c`, `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re`: `ζ(s) ≠ 0` para
  `Re s > 7/8`) descarrega a hipótese de `ATK.QuasiRiemann`, e fica provado
  `RiemannHypothesis ↔ FaixaLivre (1/2) (7/8)` sem hipóteses.

O lakefile da OpenAI aplica patches de compatibilidade às dependências dela só quando ela é o pacote
raiz; o workflow aplica os mesmos patches (`lean/patches/*-lean4341.patch`, do commit fixado) antes de
compilar.

O workflow `atk-externo.yml` compila tudo do código-fonte (≈ 2 960 módulos além da Mathlib) e
audita os axiomas. Se o build passar do limite de uma execução do GitHub, o que já foi compilado
fica num cache do próprio repositório e a execução seguinte continua.

Nada aqui prova RH: o resíduo é a faixa `1/2 < Re s ≤ 7/8`.
