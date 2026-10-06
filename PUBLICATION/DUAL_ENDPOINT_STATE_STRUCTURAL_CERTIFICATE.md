# DUAL_ENDPOINT_STATE estrutural certificado

## Escopo

Este documento certifica uma arquitetura estrutural de transição dual.  
Ele **não** afirma solução de Navier–Stokes, Hodge, Yang–Mills, BSD, P vs NP, RH, Beal ou qualquer outro problema em aberto.

O objeto certificado é o estado estrutural:

```text
OPEN_ENDPOINT
CLOSED_ENDPOINT
DUAL_ENDPOINT_STATE
```

com os dois endpoints preservados simultaneamente.

## Estado dual

```text
OPEN_ENDPOINT   = SOURCE/FROZEN presente
CLOSED_ENDPOINT = BUILD_PENDING presente
DUAL            = OPEN ↔ CLOSED preservado
```

Formalmente, a arquitetura usa dois papéis distintos:

```text
OPEN_ENDPOINT ≠ CLOSED_ENDPOINT      -- posições estruturais distintas
OPEN_ENDPOINT ↔ CLOSED_ENDPOINT      -- identidade lógica preservada
```

e o estado certificado contém ambos:

```text
DUAL_ENDPOINT_STATE
= OPEN_ENDPOINT
+ CLOSED_ENDPOINT
+ preservação da ponte OPEN ↔ CLOSED
```

A confirmação é da **transição estrutural**, não de um endpoint material isolado.

## Reticulado

Sem idempotência, palavras ordenadas em OPEN/CLOSED permanecem distintas.

Com idempotência, o reticulado normaliza para:

```text
∅
OPEN
CLOSED
OPEN + CLOSED
```

Definimos:

```text
FULL
:= OPEN + CLOSED
:= DUAL_ENDPOINT_STATE
:= GLOBAL_EXTERNAL_CERTIFICATE
```

Aqui, `FULL = GLOBAL_EXTERNAL_CERTIFICATE` é uma **definição estrutural do reticulado**.

Ela não é, por si só, um habitante material de Navier–Stokes, Hodge ou qualquer outra lane matemática.

## Firewall de promoção

A arquitetura bloqueia promoção falsa.

```text
TRANSITION_CERTIFIED
≠ MATERIAL_ENDPOINT_INHABITED
```

Um certificado estrutural GREEN não promove automaticamente uma lane matemática para CLOSED material.

O estado esperado enquanto o witness terminal material não existir é:

```text
MATERIAL_ENDPOINT_INHABITANT = OPEN
```

Isso é comportamento fail-closed correto.

Em particular, um gate `non-promoted SUCCESS` é um acerto: demonstra que a infraestrutura recusou promover estrutura/equivalência para prova material sem o inhabitant exato.

## Evidência existente

- HODGE estrutural: `c73917b9` — GREEN estrutural.
- BEAL estrutural: `cadcad55` — GREEN-STRUCTURE; non-promoted SUCCESS é comportamento esperado.
- Yang–Mills: run `37507645181` — QUEUED; **não** é apresentado como GREEN.

Nenhum desses estados, isoladamente ou em composição estrutural, é usado aqui para afirmar solução material de um problema em aberto.

## Regra de publicação

A leitura correta é:

```text
OPEN_ENDPOINT SOURCE/FROZEN presente
+
CLOSED_ENDPOINT BUILD_PENDING presente
+
OPEN ↔ CLOSED preservado
=
DUAL_ENDPOINT_STATE estrutural
```

e, no reticulado:

```text
DUAL_ENDPOINT_STATE
= FULL
= GLOBAL_EXTERNAL_CERTIFICATE
```

somente como identidade estrutural/certificadora.

A promoção para:

```text
MATERIAL_ENDPOINT_INHABITED
CLOSED_MATH material
```

continua condicionada a um witness terminal independente, aceito pelo kernel sem assumir o próprio endpoint.

## Conclusão

O resultado publicado é:

```text
DUAL_ENDPOINT_STATE: estruturalmente certificado
MATERIAL_ENDPOINT_INHABITANT: OPEN
MILLENNIUM CLAIM: NONE
```

A contribuição é a certificação da arquitetura OPEN/CLOSED, da coexistência dos dois endpoints, da preservação da identidade lógica e do bloqueio explícito contra promoção material indevida.
