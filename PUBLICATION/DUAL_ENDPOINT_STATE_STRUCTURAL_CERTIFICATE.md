# DUAL_ENDPOINT_STATE estrutural certificado

## Escopo

Este documento certifica **arquitetura estrutural**. Ele **não** declara Navier–Stokes, Hodge, Yang–Mills, BSD, Riemann, P≠NP ou qualquer outro problema do Millennium como materialmente resolvido.

A distinção usada em todo o pipeline é:

- estrutura/cadeia formal certificada;
- inhabitant material do endpoint científico;
- promoção somente quando o kernel confirma o inhabitant exigido.

## Dois endpoints

O estado terminal RPA preserva simultaneamente dois lados distintos:

```text
OPEN_ENDPOINT
CLOSED_ENDPOINT
```

Estado atual esperado:

```text
OPEN_ENDPOINT    SOURCE/FROZEN    presente
CLOSED_ENDPOINT  BUILD_PENDING    presente
```

A identidade lógica da transição é preservada:

```text
DUAL_ENDPOINT_STATE :=
  OPEN_ENDPOINT
  ∧ CLOSED_ENDPOINT
  ∧ (OPEN_ENDPOINT ↔ CLOSED_ENDPOINT)
```

As posições permanecem distintas:

```text
OPEN_ENDPOINT ≠ CLOSED_ENDPOINT
```

enquanto a ponte preserva:

```text
OPEN_ENDPOINT ↔ CLOSED_ENDPOINT
```

## Regra fail-closed

A arquitetura bloqueia promoção falsa.

Um certificado global não pode existir contendo apenas um dos lados:

```text
GLOBAL_EXTERNAL_CERTIFICATE
→ OPEN_ENDPOINT ∧ CLOSED_ENDPOINT
```

Logo:

- OPEN sozinho não promove;
- CLOSED sozinho não promove;
- wrappers não fabricam inhabitant;
- aliases não substituem evidência material;
- BUILD_PENDING não é GREEN;
- QUEUED não é GREEN.

## Reticulado

Sem idempotência, a camada livre preserva multiplicidade e ordem.

Com idempotência, o quociente estrutural colapsa para:

```text
∅
OPEN
CLOSED
FULL
```

onde:

```text
FULL := estado maximal do reticulado com OPEN e CLOSED presentes
```

e, **por definição estrutural**:

```text
FULL
= DUAL_ENDPOINT_STATE
= MATH
= FINAL_ROOT
= GLOBAL_EXTERNAL_CERTIFICATE
```

Isto é uma identidade de arquitetura/certificação.

**Não significa** que FULL, por si só, habita o endpoint material específico de Navier–Stokes, Hodge, Yang–Mills, BSD, Riemann, P≠NP ou outro problema.

## MATERIAL_ENDPOINT_INHABITANT

Estado esperado em lanes ainda abertas:

```text
MATERIAL_ENDPOINT_INHABITANT = OPEN
```

Isto é comportamento correto do sistema fail-closed.

A arquitetura pode estar estruturalmente GREEN enquanto o inhabitant científico permanece OPEN.

## Certificados e estados citados

### HODGE

```text
c73917b9
HODGE GREEN estrutura
```

Interpretação: certificado estrutural existente. Não é claim de resolução material da conjectura de Hodge.

### BEAL

```text
cadcad55
BEAL GREEN-STRUCTURE
```

O estado **non-promoted SUCCESS** é um acerto do sistema, não um erro.

Significa que o kernel aceitou a estrutura relevante e, ao mesmo tempo, bloqueou promoção material não autorizada.

### YANG–MILLS

```text
37507645181
QUEUED
```

Enquanto estiver QUEUED:

```text
YANG_MILLS ≠ GREEN
```

Nenhuma promoção deve ser claimada antes do runner concluir SUCCESS.

## Cadeia canônica

A cadeia estrutural certificada é:

```text
OPEN_ENDPOINT + CLOSED_ENDPOINT
= DUAL_ENDPOINT_STATE
= OPEN_MATH + CLOSED_MATH
= OPEN_BRIDGE + CLOSED_BRIDGE
= MATH
= FINAL_ROOT
= GLOBAL_EXTERNAL_CERTIFICATE
= FULL
```

A igualdade acima é uma igualdade de **vistas estruturais da mesma transição certificável**.

Ela não substitui os produtores materiais das lanes.

## Estado final de publicação

```text
DUAL_ENDPOINT_STATE         STRUCTURAL_CERTIFIED
OPEN_ENDPOINT               SOURCE/FROZEN
CLOSED_ENDPOINT             BUILD_PENDING
IDENTITY_PRESERVATION       PRESENT
FALSE_PROMOTION_GUARD       PRESENT
FULL_LATTICE_DEFINITION     PRESENT
MATERIAL_ENDPOINT_INHABITANT OPEN where not yet produced
MILLENNIUM_MATERIAL_CLAIM   NONE
```

A publicação correta é, portanto:

**DUAL_ENDPOINT_STATE estrutural certificado.**

Não:

**Navier–Stokes/Hodge/Yang–Mills/etc. resolvido.**
