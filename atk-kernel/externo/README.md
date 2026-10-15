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

## Resultado

Execução 38735388197 (commit `54cef29`, 15/10/2026): **ATK-EXTERNO CERTIFIED 4/4**. O `lake build`
saiu com 0; 2 692 módulos da OpenAI foram compilados nessa execução, e o restante veio do cache da
execução 38711103232, também compilado por este workflow. Os quatro teoremas de
`ATKExterno/RiemannQuasi.lean` (`OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re`, `quasiRH`,
`rh_iff_faixa`, `rh_de_faixa`) dependem só de `propext`, `Classical.choice` e `Quot.sound`, e a fonte
não tem `sorry`, `admit` nem `axiom`.

Isso confirma que o enunciado da OpenAI passa no kernel do Lean junto com o atk-kernel. Não substitui
a revisão da prova: o texto de 199 páginas ainda não foi revisado por pares, e a configuração oficial
da OpenAI não usa um segundo kernel.

Nada aqui prova RH: o resíduo é a faixa `1/2 < Re s ≤ 7/8`.
