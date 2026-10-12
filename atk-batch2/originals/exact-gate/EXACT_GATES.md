# ATK — portas de fechamento auditáveis (12 outubro 2026)

## Critério operacional
Para cada uma das 7 lanes, definir `Target` concretamente e fornecer `material : Material` e `sound : Material → Target` com tipos vinculados às semânticas originais. O kernel precisa compilar os sete termos e `#print axioms` precisa revelar apenas fundamentos permitidos, não conjecturas como axiomas. A auditoria externa precisa verificar que o alvo corresponde ao enunciado matemático pretendido.

## 24 obrigações materiais de trabalho (não equivalentes automaticamente a 24 provas independentes)
RH (3): K_star, Schur_completeness, uniform_log_rate.
NS (4): cB_star, cT_star, C_min, bulk_tail_budget.
YM (4): toPhysical, surjectivePhysical, continuumControl, spectralGap_proof.
BSD (3): rankResidual_proof, torsionPositive_proof, quotientIdentity_proof.
Hodge (3): realize, algebraicity_proof, gluing_proof.
Beal (4): measure, transform, strictDecrease, primitivePreserved.
PNP (3): exactSemantics_proof, SAT_superpoly_lower_bound, lowerBound_proof.
Total 3+4+4+3+3+4+3 = 24.

## Fontes consultadas diretamente no GitHub
RH `lean/MCore/Material/Closure.lean` blob 197dd3d32059a231188eea65e61f517005f40493: `ConcreteUniformLogDNBound DN := Nonempty (RHClosure DN)`; `DN` é argumento arbitrário. Necessário amarrar `DN` ao residual real de Báez-Duarte, e demonstrar limite universal K.
PNP `lean/MCore/Material/Closure.lean` blob 9176280b73be8ff0107de822ee91f955b0492fdc: `polyHalts`, `exactSemantics`, `lowerBound` são campos `Prop` livres. Instanciar com `True` não prova SAT∉P. Necessário fixar a semântica concreta de SAT, de máquina e limite inferior.
YM `lean/MCore/Material/Closure.lean` blob fa9645e0d2bab5c2601fdca00a86a37d2f7a0972: `spectralGap`, `surjectivePhysical`, `continuumControl` são campos `Prop` livres. Necessário conectá-los ao modelo 4D construído.
Hodge `open_math/P05_HODGE_GAP_ConcreteAlgebraicityPayload.issue.md` blob f5793d3122a54a5f3a6351b48c7c7b3cf16093b9: requisito universal explícito `ConcreteAlgebraicityPayload M`, com p≥2 ainda aberto.

## Quantificação do progresso
Fechamento universal certificado: 0/7. Portanto 7/7 = 100% dos alvos universais permanecem sem certificado terminal conhecido. Das 24 obrigações de trabalho, não há auditoria de compilação e dependências suficiente nesta execução para declarar uma contagem exata das resolvidas. Uma fração de itens não equivale a uma porcentagem de dificuldade matemática restante.

## Testes obrigatórios
1. Verificar identidade entre `Target` e enunciado original (quantificadores, hipóteses e semântica).
2. Substituir `Prop` livre por predicado concretamente definido.
3. Exibir `witness` e `sound`, sem assumir `Target` nem equivalente.
4. `lake env lean ATKExactGate.lean` e `#print axioms ATK.seven_close`.
5. Compilar módulo root com todas as dependências reais.
6. Registrar commit SHA, run ID, axiomas, toolchain, hash de artefato.

## Status
SOURCE_LOCAL; BUILD_NOT_RUN; OPEN_MATH=true; CLOSED_MATH=false; TERMINAL_CERTIFIED=0/7.
