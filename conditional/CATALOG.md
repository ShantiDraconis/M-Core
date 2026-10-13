# Catálogo dos repositórios

251 repositórios da conta `ShantiDraconis`, agrupados por função. Gerado por `scripts/build_catalog.py` a partir de `catalog/repos.txt` (lista obtida por buscas em 2026-10-13; algum repositório antigo pode faltar).

Nada aqui altera os repositórios originais.

| Grupo | Repositórios |
|---|---|
| A. Núcleo canônico (M-Core + 7 lanes) | 11 |
| B. Espelhos públicos ATK | 8 |
| C. Millennium por problema (histórico/exploratório) | 42 |
| D. Programas Millennium unificados e meta | 20 |
| E. Lean, verificação formal e ferramentas | 19 |
| F. Fundações próprias (indeterminação, 0-0, I, identidade emergente) | 37 |
| G. Ciência simbólica (série -00) | 27 |
| H. Linguagem, história e textos | 19 |
| I. Arte, espetáculo e portfólio | 30 |
| J. Engenharia, sistemas e laboratórios | 27 |
| K. Jurídico, negócios e arquivos pessoais | 11 |

## Por problema

| Problema | Repositórios |
|---|---|
| riemann | `atk-riemann-public`, `m-core-riemann`, `millennium-riemann-I`, `riemann-offcritical-zero-certifier`, `zeta-i-formal.lean`, `lc-rh-coercivity`, `riemann-transverse-stability-program`, `Riemann-multistate-program`, `riemann-indeterminacy`, `Riemann-unity-zero`, `Riemann-energy-proofline`, `millennium-riemann-classical`, `riemann-transverse-signature`, `emergent-identity-rh`, `riemann-coercivity-program`, `Millennium-rh-energy-torus-quantum`, `hawking-rh`, `collapse-lemma-rh.lean` |
| navier-stokes | `atk-navier-stokes-public`, `navier-stokes-critical-barrier-audit`, `millennium-navier-stokes-I`, `M-Navier-Stokes`, `millennium-regularity-I`, `navier-stokes-noncircular`, `navier-stokes-critical-L3`, `hawking-ns`, `millennium-navier-stokes-classical` |
| p-vs-np | `atk-p-vs-np-public`, `m-core-p-vs-np`, `millennium-p-vs-np-I`, `millennium-p-vs-np-classical`, `complexity-collapse-pnp`, `emergent-complexity-N-NP`, `hawking-pnp` |
| hodge | `atk-hodge-public`, `m-core-hodge`, `millennium-hodge`, `-millennium-bsd-hodge-yangmills-I`, `millennium-hodge-classical`, `hawking-hodge` |
| bsd | `atk-bsd-public`, `m-core-bsd`, `millennium-bsd`, `-millennium-bsd-hodge-yangmills-I`, `millennium-birch-swinnerton-dyer-classical`, `hawking-bsd` |
| yang-mills | `atk-yang-mills-public`, `m-core-yang-mills`, `millennium-yang-mills`, `-millennium-bsd-hodge-yangmills-I`, `millennium-mass-gap-I`, `millennium-yang-mills-classical`, `hawking-ym` |
| poincare | `millennium-poincare-classical`, `millennium-poincare-symbolic` |
| beal | `atk-beal-public`, `m-core-beal` |
| collatz | `collatz_reverse-tree` |

## A. Núcleo canônico (M-Core + 7 lanes) (11)

| Repositório | Papel |
|---|---|
| [`M-Core`](https://github.com/ShantiDraconis/M-Core) | Registro central: FinalProofRegistry (7 lanes, todos openMath) + atk-kernel com 19 lemas auxiliares. |
| [`m-core-riemann`](https://github.com/ShantiDraconis/m-core-riemann) | Lane RH (Nyman–Beurling/Báez-Duarte). Terminal: FiniteSpanApproximatesChi / majorante de D_N. |
| [`m-core-beal`](https://github.com/ShantiDraconis/m-core-beal) | Lane Beal. Terminal: GCDLowerBoundProducer. |
| [`navier-stokes-critical-barrier-audit`](https://github.com/ShantiDraconis/navier-stokes-critical-barrier-audit) | Lane NS. Terminal: ActualNSToSignedGainCore em EnstrophyData genuína. |
| [`m-core-hodge`](https://github.com/ShantiDraconis/m-core-hodge) | Lane Hodge. Terminal: ConcreteAlgebraicityPayload. |
| [`m-core-p-vs-np`](https://github.com/ShantiDraconis/m-core-p-vs-np) | Lane P vs NP. Terminal: P01MachineConstruction ∧ G21Pointwise. |
| [`m-core-bsd`](https://github.com/ShantiDraconis/m-core-bsd) | Lane BSD. Terminal: domínio realizável + igualdade de posto + fórmula refinada. |
| [`m-core-yang-mills`](https://github.com/ShantiDraconis/m-core-yang-mills) | Lane Yang–Mills. Terminal: B60ConcretePhysicalAdapter. |
| [`m-core-openai-ns-audit`](https://github.com/ShantiDraconis/m-core-openai-ns-audit) | Kernel NS no formato atk-kernel + CI de axiomas (modelo deste monorepo). |
| [`axiomatic-millenium`](https://github.com/ShantiDraconis/axiomatic-millenium) | GlobalOpenMathCut (importado no atk-math-core-public). |
| [`atk-certified-priority-record`](https://github.com/ShantiDraconis/atk-certified-priority-record) | Registro de prioridade/autoria. |

## B. Espelhos públicos ATK (8)

| Repositório | Visibilidade | Problema |
|---|---|---|
| [`atk-beal-public`](https://github.com/ShantiDraconis/atk-beal-public) | public | beal |
| [`atk-bsd-public`](https://github.com/ShantiDraconis/atk-bsd-public) | public | bsd |
| [`atk-hodge-public`](https://github.com/ShantiDraconis/atk-hodge-public) | public | hodge |
| [`atk-math-core-public`](https://github.com/ShantiDraconis/atk-math-core-public) | public | — |
| [`atk-navier-stokes-public`](https://github.com/ShantiDraconis/atk-navier-stokes-public) | public | navier-stokes |
| [`atk-p-vs-np-public`](https://github.com/ShantiDraconis/atk-p-vs-np-public) | public | p-vs-np |
| [`atk-riemann-public`](https://github.com/ShantiDraconis/atk-riemann-public) | public | riemann |
| [`atk-yang-mills-public`](https://github.com/ShantiDraconis/atk-yang-mills-public) | public | yang-mills |

## C. Millennium por problema (histórico/exploratório) (42)

| Repositório | Visibilidade | Problema |
|---|---|---|
| [`-millennium-bsd-hodge-yangmills-I`](https://github.com/ShantiDraconis/-millennium-bsd-hodge-yangmills-I) | private | hodge, bsd, yang-mills |
| [`collapse-lemma-rh.lean`](https://github.com/ShantiDraconis/collapse-lemma-rh.lean) | private | riemann |
| [`collatz_reverse-tree`](https://github.com/ShantiDraconis/collatz_reverse-tree) | private | collatz |
| [`complexity-collapse-pnp`](https://github.com/ShantiDraconis/complexity-collapse-pnp) | private | p-vs-np |
| [`emergent-complexity-N-NP`](https://github.com/ShantiDraconis/emergent-complexity-N-NP) | private | p-vs-np |
| [`emergent-identity-rh`](https://github.com/ShantiDraconis/emergent-identity-rh) | private | riemann |
| [`hawking-bsd`](https://github.com/ShantiDraconis/hawking-bsd) | private | bsd |
| [`hawking-hodge`](https://github.com/ShantiDraconis/hawking-hodge) | private | hodge |
| [`hawking-ns`](https://github.com/ShantiDraconis/hawking-ns) | private | navier-stokes |
| [`hawking-pnp`](https://github.com/ShantiDraconis/hawking-pnp) | private | p-vs-np |
| [`hawking-rh`](https://github.com/ShantiDraconis/hawking-rh) | private | riemann |
| [`hawking-ym`](https://github.com/ShantiDraconis/hawking-ym) | private | yang-mills |
| [`lc-rh-coercivity`](https://github.com/ShantiDraconis/lc-rh-coercivity) | private | riemann |
| [`M-Navier-Stokes`](https://github.com/ShantiDraconis/M-Navier-Stokes) | private | navier-stokes |
| [`millennium-birch-swinnerton-dyer-classical`](https://github.com/ShantiDraconis/millennium-birch-swinnerton-dyer-classical) | private | bsd |
| [`millennium-bsd`](https://github.com/ShantiDraconis/millennium-bsd) | private | bsd |
| [`millennium-hodge`](https://github.com/ShantiDraconis/millennium-hodge) | private | hodge |
| [`millennium-hodge-classical`](https://github.com/ShantiDraconis/millennium-hodge-classical) | private | hodge |
| [`millennium-mass-gap-I`](https://github.com/ShantiDraconis/millennium-mass-gap-I) | private | yang-mills |
| [`millennium-navier-stokes-classical`](https://github.com/ShantiDraconis/millennium-navier-stokes-classical) | private | navier-stokes |
| [`millennium-navier-stokes-I`](https://github.com/ShantiDraconis/millennium-navier-stokes-I) | private | navier-stokes |
| [`millennium-p-vs-np-classical`](https://github.com/ShantiDraconis/millennium-p-vs-np-classical) | private | p-vs-np |
| [`millennium-p-vs-np-I`](https://github.com/ShantiDraconis/millennium-p-vs-np-I) | private | p-vs-np |
| [`millennium-poincare-classical`](https://github.com/ShantiDraconis/millennium-poincare-classical) | private | poincare |
| [`millennium-poincare-symbolic`](https://github.com/ShantiDraconis/millennium-poincare-symbolic) | private | poincare |
| [`millennium-regularity-I`](https://github.com/ShantiDraconis/millennium-regularity-I) | private | navier-stokes |
| [`Millennium-rh-energy-torus-quantum`](https://github.com/ShantiDraconis/Millennium-rh-energy-torus-quantum) | private | riemann |
| [`millennium-riemann-classical`](https://github.com/ShantiDraconis/millennium-riemann-classical) | private | riemann |
| [`millennium-riemann-I`](https://github.com/ShantiDraconis/millennium-riemann-I) | private | riemann |
| [`millennium-yang-mills`](https://github.com/ShantiDraconis/millennium-yang-mills) | private | yang-mills |
| [`millennium-yang-mills-classical`](https://github.com/ShantiDraconis/millennium-yang-mills-classical) | private | yang-mills |
| [`navier-stokes-critical-L3`](https://github.com/ShantiDraconis/navier-stokes-critical-L3) | private | navier-stokes |
| [`navier-stokes-noncircular`](https://github.com/ShantiDraconis/navier-stokes-noncircular) | private | navier-stokes |
| [`riemann-coercivity-program`](https://github.com/ShantiDraconis/riemann-coercivity-program) | private | riemann |
| [`Riemann-energy-proofline`](https://github.com/ShantiDraconis/Riemann-energy-proofline) | private | riemann |
| [`riemann-indeterminacy`](https://github.com/ShantiDraconis/riemann-indeterminacy) | private | riemann |
| [`Riemann-multistate-program`](https://github.com/ShantiDraconis/Riemann-multistate-program) | private | riemann |
| [`riemann-offcritical-zero-certifier`](https://github.com/ShantiDraconis/riemann-offcritical-zero-certifier) | private | riemann |
| [`riemann-transverse-signature`](https://github.com/ShantiDraconis/riemann-transverse-signature) | private | riemann |
| [`riemann-transverse-stability-program`](https://github.com/ShantiDraconis/riemann-transverse-stability-program) | private | riemann |
| [`Riemann-unity-zero`](https://github.com/ShantiDraconis/Riemann-unity-zero) | private | riemann |
| [`zeta-i-formal.lean`](https://github.com/ShantiDraconis/zeta-i-formal.lean) | private | riemann |

## D. Programas Millennium unificados e meta (20)

| Repositório | Visibilidade | Problema |
|---|---|---|
| [`equations-of-unsolved-problems-book`](https://github.com/ShantiDraconis/equations-of-unsolved-problems-book) | private | — |
| [`hawking-framework`](https://github.com/ShantiDraconis/hawking-framework) | private | — |
| [`hawking-lean`](https://github.com/ShantiDraconis/hawking-lean) | private | — |
| [`hawking-numerics`](https://github.com/ShantiDraconis/hawking-numerics) | private | — |
| [`hawking-singularities-millennium-problems`](https://github.com/ShantiDraconis/hawking-singularities-millennium-problems) | private | — |
| [`Meta-mathematical-foundation-00`](https://github.com/ShantiDraconis/Meta-mathematical-foundation-00) | private | — |
| [`meta-mathematics-indeterminate-I`](https://github.com/ShantiDraconis/meta-mathematics-indeterminate-I) | private | — |
| [`Meta-millenium-independence-00`](https://github.com/ShantiDraconis/Meta-millenium-independence-00) | private | — |
| [`Millenium--core`](https://github.com/ShantiDraconis/Millenium--core) | private | — |
| [`Millenium-delta-unified-frame`](https://github.com/ShantiDraconis/Millenium-delta-unified-frame) | public | — |
| [`Millennium`](https://github.com/ShantiDraconis/Millennium) | private | — |
| [`millennium-classical-parameters`](https://github.com/ShantiDraconis/millennium-classical-parameters) | private | — |
| [`millennium-engineering-00`](https://github.com/ShantiDraconis/millennium-engineering-00) | private | — |
| [`millennium-hypothesi`](https://github.com/ShantiDraconis/millennium-hypothesi) | private | — |
| [`millennium-limit-unification`](https://github.com/ShantiDraconis/millennium-limit-unification) | private | — |
| [`millennium-research-os`](https://github.com/ShantiDraconis/millennium-research-os) | private | — |
| [`millennium-symbolic-program`](https://github.com/ShantiDraconis/millennium-symbolic-program) | private | — |
| [`open-math-scoped-final`](https://github.com/ShantiDraconis/open-math-scoped-final) | private | — |
| [`unified-millennium-invariant`](https://github.com/ShantiDraconis/unified-millennium-invariant) | private | — |
| [`ussf-millennium-locks`](https://github.com/ShantiDraconis/ussf-millennium-locks) | private | — |

## E. Lean, verificação formal e ferramentas (19)

| Repositório | Visibilidade | Problema |
|---|---|---|
| [`0-0-FORMAL-SUITE`](https://github.com/ShantiDraconis/0-0-FORMAL-SUITE) | private | — |
| [`copilot-cli`](https://github.com/ShantiDraconis/copilot-cli) | public-fork | — |
| [`critical-bridge-formalization-private`](https://github.com/ShantiDraconis/critical-bridge-formalization-private) | private | — |
| [`Elyon-Public-Proof`](https://github.com/ShantiDraconis/Elyon-Public-Proof) | public | — |
| [`i-foundations.lean`](https://github.com/ShantiDraconis/i-foundations.lean) | private | — |
| [`latex-library-global`](https://github.com/ShantiDraconis/latex-library-global) | private | — |
| [`lean-audit-kit`](https://github.com/ShantiDraconis/lean-audit-kit) | private | — |
| [`lean-cursor-shuttle`](https://github.com/ShantiDraconis/lean-cursor-shuttle) | private | — |
| [`lean-fin-composition`](https://github.com/ShantiDraconis/lean-fin-composition) | private | — |
| [`lean-preserving-read`](https://github.com/ShantiDraconis/lean-preserving-read) | private | — |
| [`lean-refinement-bridge`](https://github.com/ShantiDraconis/lean-refinement-bridge) | public | — |
| [`lean-uniform-bounds`](https://github.com/ShantiDraconis/lean-uniform-bounds) | public | — |
| [`lean-winwin-logic`](https://github.com/ShantiDraconis/lean-winwin-logic) | private | — |
| [`proof-engineering-00`](https://github.com/ShantiDraconis/proof-engineering-00) | private | — |
| [`proofs-multiprover`](https://github.com/ShantiDraconis/proofs-multiprover) | private | — |
| [`sfh-formalization-lab`](https://github.com/ShantiDraconis/sfh-formalization-lab) | private | — |
| [`The-Proof-Log`](https://github.com/ShantiDraconis/The-Proof-Log) | private | — |
| [`universal-proof-hub`](https://github.com/ShantiDraconis/universal-proof-hub) | private | — |
| [`universe-00-ci-templates`](https://github.com/ShantiDraconis/universe-00-ci-templates) | private | — |

## F. Fundações próprias (indeterminação, 0-0, I, identidade emergente) (37)

| Repositório | Visibilidade | Problema |
|---|---|---|
| [`0-0`](https://github.com/ShantiDraconis/0-0) | private | — |
| [`00-limit-foundation`](https://github.com/ShantiDraconis/00-limit-foundation) | private | — |
| [`cardinality-and-infinity`](https://github.com/ShantiDraconis/cardinality-and-infinity) | private | — |
| [`Codex_Indeterminancy`](https://github.com/ShantiDraconis/Codex_Indeterminancy) | private | — |
| [`continuum-fields-indeterminacy`](https://github.com/ShantiDraconis/continuum-fields-indeterminacy) | private | — |
| [`cryptographic-logic-foundations`](https://github.com/ShantiDraconis/cryptographic-logic-foundations) | private | — |
| [`discrete-dynamics-indeterminacy`](https://github.com/ShantiDraconis/discrete-dynamics-indeterminacy) | private | — |
| [`emergent-identity-framework`](https://github.com/ShantiDraconis/emergent-identity-framework) | private | — |
| [`federated-trivalent-manifold`](https://github.com/ShantiDraconis/federated-trivalent-manifold) | private | — |
| [`Heu-7-universal-framework`](https://github.com/ShantiDraconis/Heu-7-universal-framework) | private | — |
| [`horizon-prime---framework`](https://github.com/ShantiDraconis/horizon-prime---framework) | private | — |
| [`Horizon_Prime_-framework`](https://github.com/ShantiDraconis/Horizon_Prime_-framework) | private | — |
| [`i-constant-core`](https://github.com/ShantiDraconis/i-constant-core) | private | — |
| [`I-Framework-Nexus`](https://github.com/ShantiDraconis/I-Framework-Nexus) | private | — |
| [`i-theology-unified`](https://github.com/ShantiDraconis/i-theology-unified) | private | — |
| [`indeterminate-collapse-core`](https://github.com/ShantiDraconis/indeterminate-collapse-core) | private | — |
| [`invariance-signature-framework`](https://github.com/ShantiDraconis/invariance-signature-framework) | private | — |
| [`metalogic-infinity-00`](https://github.com/ShantiDraconis/metalogic-infinity-00) | private | — |
| [`Omega-completa`](https://github.com/ShantiDraconis/Omega-completa) | private | — |
| [`orion`](https://github.com/ShantiDraconis/orion) | private | — |
| [`pi-border-primes`](https://github.com/ShantiDraconis/pi-border-primes) | private | — |
| [`Singulariity`](https://github.com/ShantiDraconis/Singulariity) | private | — |
| [`Spectrally-Guided`](https://github.com/ShantiDraconis/Spectrally-Guided) | private | — |
| [`structural-signature-calculus`](https://github.com/ShantiDraconis/structural-signature-calculus) | private | — |
| [`TABP-weighted-irregular-sampling`](https://github.com/ShantiDraconis/TABP-weighted-irregular-sampling) | private | — |
| [`The-Algebra-of-Ideterminate-I`](https://github.com/ShantiDraconis/The-Algebra-of-Ideterminate-I) | private | — |
| [`Trans`](https://github.com/ShantiDraconis/Trans) | private | — |
| [`UMA`](https://github.com/ShantiDraconis/UMA) | private | — |
| [`umi-core-axioms`](https://github.com/ShantiDraconis/umi-core-axioms) | private | — |
| [`umi-master`](https://github.com/ShantiDraconis/umi-master) | private | — |
| [`unified-classical-foundations`](https://github.com/ShantiDraconis/unified-classical-foundations) | private | — |
| [`universal-0-5-emergent-identity`](https://github.com/ShantiDraconis/universal-0-5-emergent-identity) | private | — |
| [`universal-arithmetic-stability`](https://github.com/ShantiDraconis/universal-arithmetic-stability) | private | — |
| [`universal-emergent-logic-`](https://github.com/ShantiDraconis/universal-emergent-logic-) | private | — |
| [`universal-indeterminate-constant-I`](https://github.com/ShantiDraconis/universal-indeterminate-constant-I) | private | — |
| [`zero-codex-archive-00`](https://github.com/ShantiDraconis/zero-codex-archive-00) | private | — |
| [`zero-game-00`](https://github.com/ShantiDraconis/zero-game-00) | private | — |

## G. Ciência simbólica (série -00) (27)

| Repositório | Visibilidade | Problema |
|---|---|---|
| [`-sbfe-physics-unified`](https://github.com/ShantiDraconis/-sbfe-physics-unified) | private | — |
| [`consciousness-symbolic-model-00`](https://github.com/ShantiDraconis/consciousness-symbolic-model-00) | private | — |
| [`cosmic-geometry-00`](https://github.com/ShantiDraconis/cosmic-geometry-00) | private | — |
| [`dmt-timelines-00`](https://github.com/ShantiDraconis/dmt-timelines-00) | private | — |
| [`identity-fields-00`](https://github.com/ShantiDraconis/identity-fields-00) | private | — |
| [`olympic-symbolic-00`](https://github.com/ShantiDraconis/olympic-symbolic-00) | private | — |
| [`psychology-symbolic-00`](https://github.com/ShantiDraconis/psychology-symbolic-00) | private | — |
| [`quantum-axioms-lab`](https://github.com/ShantiDraconis/quantum-axioms-lab) | private | — |
| [`quantum-field-symbolic-00`](https://github.com/ShantiDraconis/quantum-field-symbolic-00) | private | — |
| [`quantum-spacetime-00`](https://github.com/ShantiDraconis/quantum-spacetime-00) | private | — |
| [`siamese-consciousness-00`](https://github.com/ShantiDraconis/siamese-consciousness-00) | private | — |
| [`stationary-photon-moving-geometry`](https://github.com/ShantiDraconis/stationary-photon-moving-geometry) | private | — |
| [`symbolic-analysis-00`](https://github.com/ShantiDraconis/symbolic-analysis-00) | private | — |
| [`symbolic-arithmetic-00`](https://github.com/ShantiDraconis/symbolic-arithmetic-00) | private | — |
| [`symbolic-automata-00`](https://github.com/ShantiDraconis/symbolic-automata-00) | private | — |
| [`symbolic-balance-field-equation`](https://github.com/ShantiDraconis/symbolic-balance-field-equation) | private | — |
| [`symbolic-biology-00`](https://github.com/ShantiDraconis/symbolic-biology-00) | private | — |
| [`symbolic-chemistry-00`](https://github.com/ShantiDraconis/symbolic-chemistry-00) | private | — |
| [`symbolic-collapse-00`](https://github.com/ShantiDraconis/symbolic-collapse-00) | private | — |
| [`symbolic-complexity-00`](https://github.com/ShantiDraconis/symbolic-complexity-00) | private | — |
| [`symbolic-cosmology-00`](https://github.com/ShantiDraconis/symbolic-cosmology-00) | private | — |
| [`symbolic-grammar-00`](https://github.com/ShantiDraconis/symbolic-grammar-00) | private | — |
| [`symbolic-gravitational-collapse-00`](https://github.com/ShantiDraconis/symbolic-gravitational-collapse-00) | private | — |
| [`symbolic-linguistics-00`](https://github.com/ShantiDraconis/symbolic-linguistics-00) | private | — |
| [`symbolic-metamathematics-00`](https://github.com/ShantiDraconis/symbolic-metamathematics-00) | private | — |
| [`symbolic-quantum-computing`](https://github.com/ShantiDraconis/symbolic-quantum-computing) | private | — |
| [`symbolic-topology-00`](https://github.com/ShantiDraconis/symbolic-topology-00) | private | — |

## H. Linguagem, história e textos (19)

| Repositório | Visibilidade | Problema |
|---|---|---|
| [`archetypes-humanity`](https://github.com/ShantiDraconis/archetypes-humanity) | private | — |
| [`Beit-Hamikdash-iii`](https://github.com/ShantiDraconis/Beit-Hamikdash-iii) | public | — |
| [`Genesis_Elyon`](https://github.com/ShantiDraconis/Genesis_Elyon) | private | — |
| [`harappan-00-universal`](https://github.com/ShantiDraconis/harappan-00-universal) | private | — |
| [`Harappan-guilds-0-0`](https://github.com/ShantiDraconis/Harappan-guilds-0-0) | private | — |
| [`harappan-unified-audit-`](https://github.com/ShantiDraconis/harappan-unified-audit-) | private | — |
| [`harappan-universal-dictionary`](https://github.com/ShantiDraconis/harappan-universal-dictionary) | private | — |
| [`indus-operational-mathematics`](https://github.com/ShantiDraconis/indus-operational-mathematics) | private | — |
| [`Indus-System`](https://github.com/ShantiDraconis/Indus-System) | private | — |
| [`linguistic-universal-00`](https://github.com/ShantiDraconis/linguistic-universal-00) | private | — |
| [`mishkan-iii-core`](https://github.com/ShantiDraconis/mishkan-iii-core) | private | — |
| [`Oral-substrate-br`](https://github.com/ShantiDraconis/Oral-substrate-br) | private | — |
| [`phonology-ancestral-00`](https://github.com/ShantiDraconis/phonology-ancestral-00) | private | — |
| [`primordial-language-00`](https://github.com/ShantiDraconis/primordial-language-00) | private | — |
| [`sacred-texts-mirror`](https://github.com/ShantiDraconis/sacred-texts-mirror) | private | — |
| [`tanakh-mirror-00`](https://github.com/ShantiDraconis/tanakh-mirror-00) | private | — |
| [`tupi-hebrew-bridge-00`](https://github.com/ShantiDraconis/tupi-hebrew-bridge-00) | private | — |
| [`universal-education-00`](https://github.com/ShantiDraconis/universal-education-00) | private | — |
| [`Universal-translation-0-0`](https://github.com/ShantiDraconis/Universal-translation-0-0) | private | — |

## I. Arte, espetáculo e portfólio (30)

| Repositório | Visibilidade | Problema |
|---|---|---|
| [`art-00-vision`](https://github.com/ShantiDraconis/art-00-vision) | private | — |
| [`Ceremony-OS`](https://github.com/ShantiDraconis/Ceremony-OS) | private | — |
| [`creative-direction-portfolio-00`](https://github.com/ShantiDraconis/creative-direction-portfolio-00) | private | — |
| [`digital-fire-la28`](https://github.com/ShantiDraconis/digital-fire-la28) | private | — |
| [`installations-design-00`](https://github.com/ShantiDraconis/installations-design-00) | private | — |
| [`LA-2008-R-`](https://github.com/ShantiDraconis/LA-2008-R-) | private | — |
| [`lighting-narrative-lab`](https://github.com/ShantiDraconis/lighting-narrative-lab) | private | — |
| [`lighting-tech-portfolio-00`](https://github.com/ShantiDraconis/lighting-tech-portfolio-00) | private | — |
| [`Lunar-Hive`](https://github.com/ShantiDraconis/Lunar-Hive) | public | — |
| [`Lunar-Hive-00`](https://github.com/ShantiDraconis/Lunar-Hive-00) | public | — |
| [`music-harmonic-00`](https://github.com/ShantiDraconis/music-harmonic-00) | private | — |
| [`olympic-00-chama`](https://github.com/ShantiDraconis/olympic-00-chama) | private | — |
| [`olympic-00-core`](https://github.com/ShantiDraconis/olympic-00-core) | private | — |
| [`olympic-architecture-00`](https://github.com/ShantiDraconis/olympic-architecture-00) | private | — |
| [`olympic-choreography-00`](https://github.com/ShantiDraconis/olympic-choreography-00) | private | — |
| [`olympic-costumes-00`](https://github.com/ShantiDraconis/olympic-costumes-00) | private | — |
| [`olympic-dramaturgy-00`](https://github.com/ShantiDraconis/olympic-dramaturgy-00) | private | — |
| [`olympic-lighting-00`](https://github.com/ShantiDraconis/olympic-lighting-00) | private | — |
| [`olympic-livebook-00`](https://github.com/ShantiDraconis/olympic-livebook-00) | private | — |
| [`olympic-operations-00`](https://github.com/ShantiDraconis/olympic-operations-00) | private | — |
| [`olympic-rituals-00`](https://github.com/ShantiDraconis/olympic-rituals-00) | private | — |
| [`olympic-score-00`](https://github.com/ShantiDraconis/olympic-score-00) | private | — |
| [`olympic-show-prototype-00`](https://github.com/ShantiDraconis/olympic-show-prototype-00) | private | — |
| [`olympic-video-00`](https://github.com/ShantiDraconis/olympic-video-00) | private | — |
| [`Parque-do-Bixiga-00`](https://github.com/ShantiDraconis/Parque-do-Bixiga-00) | private | — |
| [`sound-tech-portfolio-00`](https://github.com/ShantiDraconis/sound-tech-portfolio-00) | private | — |
| [`stage-management-portfolio-00`](https://github.com/ShantiDraconis/stage-management-portfolio-00) | private | — |
| [`The-America-Call-LA2028-Master`](https://github.com/ShantiDraconis/The-America-Call-LA2028-Master) | private | — |
| [`tiago-fagliari-creative-technical-portfolio`](https://github.com/ShantiDraconis/tiago-fagliari-creative-technical-portfolio) | public | — |
| [`urban-lighting-00`](https://github.com/ShantiDraconis/urban-lighting-00) | private | — |

## J. Engenharia, sistemas e laboratórios (27)

| Repositório | Visibilidade | Problema |
|---|---|---|
| [`closed-loop-engineering-00`](https://github.com/ShantiDraconis/closed-loop-engineering-00) | private | — |
| [`Eclectic_S`](https://github.com/ShantiDraconis/Eclectic_S) | private | — |
| [`global-systems-lab`](https://github.com/ShantiDraconis/global-systems-lab) | private | — |
| [`hotel-lunar-00`](https://github.com/ShantiDraconis/hotel-lunar-00) | private | — |
| [`hotel-terra-00`](https://github.com/ShantiDraconis/hotel-terra-00) | private | — |
| [`infinite-energy-reactor-00`](https://github.com/ShantiDraconis/infinite-energy-reactor-00) | private | — |
| [`M-private`](https://github.com/ShantiDraconis/M-private) | private | — |
| [`maritimo-delta-estrela-k13`](https://github.com/ShantiDraconis/maritimo-delta-estrela-k13) | private | — |
| [`metaos-operational-system`](https://github.com/ShantiDraconis/metaos-operational-system) | private | — |
| [`NIPAH-research-HUB`](https://github.com/ShantiDraconis/NIPAH-research-HUB) | private | — |
| [`projeto-0-0`](https://github.com/ShantiDraconis/projeto-0-0) | private | — |
| [`S5-BIO-SHIELD-`](https://github.com/ShantiDraconis/S5-BIO-SHIELD-) | private | — |
| [`S5-Core-Private`](https://github.com/ShantiDraconis/S5-Core-Private) | private | — |
| [`seet-r-off-lab-`](https://github.com/ShantiDraconis/seet-r-off-lab-) | private | — |
| [`ship-zero-waste-00`](https://github.com/ShantiDraconis/ship-zero-waste-00) | private | — |
| [`tiefc-audit-lab`](https://github.com/ShantiDraconis/tiefc-audit-lab) | private | — |
| [`universal`](https://github.com/ShantiDraconis/universal) | private | — |
| [`universal-archive`](https://github.com/ShantiDraconis/universal-archive) | private | — |
| [`universal-sustainable-engineering`](https://github.com/ShantiDraconis/universal-sustainable-engineering) | private | — |
| [`Universe-0-0`](https://github.com/ShantiDraconis/Universe-0-0) | private | — |
| [`universe-archives-00`](https://github.com/ShantiDraconis/universe-archives-00) | private | — |
| [`universe-archives-00-`](https://github.com/ShantiDraconis/universe-archives-00-) | private | — |
| [`urban-future-architecture-00`](https://github.com/ShantiDraconis/urban-future-architecture-00) | private | — |
| [`water-cycles-00`](https://github.com/ShantiDraconis/water-cycles-00) | private | — |
| [`Zero--OS`](https://github.com/ShantiDraconis/Zero--OS) | private | — |
| [`zero-ai-00`](https://github.com/ShantiDraconis/zero-ai-00) | private | — |
| [`zero-engine-00`](https://github.com/ShantiDraconis/zero-engine-00) | private | — |

## K. Jurídico, negócios e arquivos pessoais (11)

| Repositório | Visibilidade | Problema |
|---|---|---|
| [`Archive-Mystic-Silence`](https://github.com/ShantiDraconis/Archive-Mystic-Silence) | private | — |
| [`Archive-Royal-Blue`](https://github.com/ShantiDraconis/Archive-Royal-Blue) | private | — |
| [`Marella-RWS-Evidence-Repository`](https://github.com/ShantiDraconis/Marella-RWS-Evidence-Repository) | private | — |
| [`Network-Investment-Fund`](https://github.com/ShantiDraconis/Network-Investment-Fund) | private | — |
| [`Protocol-Vessel-Control`](https://github.com/ShantiDraconis/Protocol-Vessel-Control) | private | — |
| [`Psychological-Warfare-Vault`](https://github.com/ShantiDraconis/Psychological-Warfare-Vault) | private | — |
| [`System-Integrity-Audit`](https://github.com/ShantiDraconis/System-Integrity-Audit) | private | — |
| [`The-Consortium-of-Redemption`](https://github.com/ShantiDraconis/The-Consortium-of-Redemption) | private | — |
| [`The-Crew-Voice-Archive-`](https://github.com/ShantiDraconis/The-Crew-Voice-Archive-) | private | — |
| [`The-Legal-Playbook-Script`](https://github.com/ShantiDraconis/The-Legal-Playbook-Script) | private | — |
| [`The-Vessel-Logos-Admin`](https://github.com/ShantiDraconis/The-Vessel-Logos-Admin) | private | — |
