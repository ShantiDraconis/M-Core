# POINCARÉ P-T2 — auditoria estática (sem build) das duas formalizações externas

**Hipótese.** O cone não tem metaprogramação capaz de injetar declarações no kernel; o endpoint não tem hipóteses extras e usa a topologia da Mathlib.

## Material disponível (nada novo foi clonado)
- Os clones rasos *blobless* em `ext/` só têm árvores, sem conteúdo:
  - `fz` = frenzymath/PoincareConjecture @62db01a: o B do mapa, com checkout esparso de 4 arquivos.
  - `qz` = qinz1yang/differential-geometry @fd2f07f (HEAD): o A, mas **não** a v0.1.3 = 7a48598d do mapa, que não está no clone.
- Busquei por blob, em lote, ~430 arquivos pequenos (~10 MB): raízes, lakefiles, manifests, CI, Comparator, endpoints e importações diretas; 264 arquivos de A com SimplyConnected/Sphere/ChartedSpace/IsManifold no nome; AxiomAudit e GrushkoUnsafe; e 200 `.lean` aleatórios por repo (semente 20261022). Código: `tests/code/POINCARE_T2_fetch.sh`, `POINCARE_T2_scan.py`.
- A API do GitHub foi negada pela política (403); não tentei de novo.
- A varredura completa exigiria ~400 MB (A) + ~160 MB (B) de texto, com 0,6 GB livres e o brief vedando clones grandes: **não foi feita**.

## Tamanho e toolchain

| | A (qinz1yang @fd2f07f, v0.1.5) | B (frenzymath @62db01a) |
|---|---|---|
| arquivos `.lean` | 28.771 (a raiz importa 28.750) | 23.560 (23.554 em PoincareLib) |
| linhas (amostra, IC 95%) | 7,5 ± 1,3 M (repo inteiro: Poincaré + geometrização + dim ≥ 5) | 3,3 ± 0,7 M (mapa: ≈ 3,2 M) |
| Lean / Mathlib | v4.35.0-rc3 / v4.35.0-rc3 (c55e6e78) | v4.33.1 / 0df444a3 |
| verificação prevista | CI só roda `lake --no-cache build` (self-hosted); `#print axioms` manual pelo README; sem Comparator | Comparator 3927ad38, lean4export 15f6055e, Nanoda 0.4.18; axiomas {propext, Classical.choice, Quot.sound}; `enable_nanoda: true` |

O "≈ 4,0 M linhas no cone" de A não é verificável sem o fecho de imports.

## Enunciado final exato
**B** (`Comparator/Challenge.lean` = `PoincareConjecture/Statement.lean`, só `import Mathlib`):
```
ThreeSphere := Metric.sphere (0 : EuclideanSpace ℝ (Fin 4)) 1
SmoothPoincare := ∀ (M : Type u) [TopologicalSpace M] [T2Space M] [SecondCountableTopology M]
  [ChartedSpace (EuclideanSpace ℝ (Fin 3)) M] [IsManifold (𝓡 3) ∞ M] [CompactSpace M] [SimplyConnectedSpace M],
  Nonempty (Diffeomorph (𝓡 3) (𝓡 3) M ThreeSphere ∞)
TopologicalPoincare: idem sem IsManifold, conclusão Nonempty (M ≃ₜ ThreeSphere)
```
**A** (`DifferentialGeometry/Topology/ThreeManifold/Poincare.lean`):
```
theorem poincare_conjecture (M : Type u) [TopologicalSpace M] [ChartedSpace (EuclideanSpace ℝ (Fin 3)) M]
  [T2Space M] [CompactSpace M] [SimplyConnectedSpace M] : Nonempty (M ≃ₜ Metric.sphere (0 : EuclideanSpace ℝ (Fin 4)) 1)
smooth_poincare_conjecture: + [IsManifold (𝓡 3) ∞ M], conclusão Nonempty (M ≃ₘ⟮𝓡 3, 𝓡 3⟯ Metric.sphere 0 1)
```
Os dois usam só classes da Mathlib e não têm parâmetros do tipo Interface/Contract/Certificate. A omite SecondCountableTopology, o que é inócuo: variedade compacta e localmente euclidiana é segundo-enumerável.

## Varredura (após remover comentários e strings)
Padrões: `axiom`, `sorry`, `admit`, `native_decide`, `implemented_by`, `@[extern]`, `unsafe`, `addDecl`/`Environment.add`, `skipKernelTC`, `ofReduceBool`, `run_cmd`/`#eval`, `elab`/`macro`/`initialize`, `import Lean`.
- **A, endpoint + 5 importações diretas:** 0.
- **A, amostra de 200 (52 mil linhas):** 0 (1 falso positivo de `Kernel.`: heat kernel).
- **A, `Geometrization/Checks/AxiomAudit.lean`:** 1 `run_cmd` com `import Lean`, que só lê `getEnv` e confere axiomas (auditoria, não injeção).
- **A, `GrushkoUnsafe.lean`:** 0; "Unsafe" só no nome.
- **B, Challenge/Solution/Statement/Main, `PoincareLib/Topology/Manifold/Poincare.lean` e `Final/Main.lean`:** só os 2 `sorry` de Challenge.lean, esperados (alvos do Comparator).
- **B, amostra de 200 (28 mil linhas):** 0.
- **Sombreamento:** nenhuma redefinição de SimplyConnectedSpace, ChartedSpace, IsManifold, EuclideanSpace, T2Space, CompactSpace, Diffeomorph ou sphere nos 264 + 5 arquivos de A checados.

## Achados
1. **B @62db01a não tem verificação própria.** O README do Comparator diz "The import PR has not run a Lean build or Comparator; verification is left to the reviewer". Segundo MODIFICATIONS.md, o PoincareLib é cópia byte a byte de frenzymath/Poincare-Conjecture @432c38f2, verificado lá com um Comparator com patch de ordem de execução. O script `scripts/check_poincare_endpoints.lean` citado no endpoint não existe neste repo.
2. **Em A, o enunciado não está isolado.** Ele é elaborado dentro de `namespace DifferentialGeometry.Topology` com o cone importado; excluir sombreamento em todo o cone exige um Comparator contra enunciado só-Mathlib, que A não traz. O mapa diz (via artigo B) que A passa o Comparator, mas não há artefato no repo.
3. **Nenhum padrão de injeção nos ~430 arquivos lidos** (~1,7% de A, ~0,9% de B). Pela amostra, a fração de arquivos com algum padrão é < 1,5% (IC 95%, regra 3/n). Isso **não certifica ausência**: um único `axiom` ou `sorry` basta.

## Interpretação
O que dá para verificar estaticamente está limpo, e os dois enunciados usam a topologia da Mathlib. "Sem injeção no cone" fica **sem decisão**, porque a varredura completa não coube no ambiente. O status certo no ATK continua `EXTERNAL_PENDING(commit)`; para B é pior do que o mapa supunha, pois o commit atual não foi verificado.

## Próximo
(1) Com ≥ 2 GB de disco, buscar todos os blobs e varrer o fecho de imports com os mesmos scripts. (2) Para B, conferir os hashes do PoincareLib contra @432c38f2. (3) Comparator nos dois projetos (Q1 do mapa).
