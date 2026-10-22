# POINCARÉ — fronteira de pesquisa (estado em 2026-10-21)

**Resumo.** A conjectura é teorema (Perelman 2002–03). A novidade decisiva de 2026 é que **ela já está formalizada em Lean 4/Mathlib, por dois projetos independentes**,
e a geometrização também foi anunciada. Os dois projetos são assistidos por IA, têm kernel e axiomas padrão e não foram arbitrados.
Com isso o rótulo do ATK `LEAN_KERNEL_FINAL_PROOF: EXTERNAL_CLASSICAL_PENDING` / `FORMAL_IMPORT_GAPS: 1` (M-Core `atk-poincare-f8-f7`, 0ab76790) ficou desatualizado.
A lacuna deixou de ser a existência de uma prova formal; agora é **verificação, importação (toolchain e tamanho) e redução**.
"Matemática nova" perto de Poincaré só existe na dimensão 4: SPC4, Schoenflies suave e Andrews–Curtis.
O corpus do ATK não tem enunciado fiel (o arquivo usa `constant` de Lean 3 e não faz parse), mas tem 2 axiomas inconsistentes em `Millennium/main` e transportes F7/F8 tautológicos.
O único conteúdo real é cálculo na S³ redonda (`K1Geometry.lean`, `ATK/Geometry.lean: round_sphere_scalar_integral`).

## 1. Estado da arte

### 1.1 Matemática (caminhos formalizáveis)
- **Perelman / Morgan–Tian** (arXiv math/0607607, v2 de 21/03/2007; monografia Clay). Fluxo de Ricci com cirurgia, κ-não-colapso, vizinhanças canônicas e extinção em tempo finito para π₁ = 1.
  Para Poincaré basta a extinção finita; a análise de tempo longo e a decomposição grossa-fina só são necessárias para a geometrização.
- **Colding–Minicozzi** (math/0308090, 2003/2006) dão a extinção finita por largura min-max de superfícies mínimas, como alternativa ao argumento de Perelman com encurtamento de curvas.
- **Kleiner–Lott + Bamler–Kleiner** (1709.04122, 2017/18) constroem o fluxo canônico através de singularidades, único, estável e limite de fluxos com cirurgia.
  Essa rota é conceitualmente mais limpa (dispensa a contabilidade de parâmetros de cirurgia), mas não tem precedente formal.

### 1.2 Formalização (cronologia verificada)
- **Mathlib (Rothgang, ItaLean, 11/12/2025).**
  - Já tem: variedades suaves, fibrados (tangente, hom, soma direta), colchete de Lie, métricas de fibrado e "basic Riemannian manifolds", curvas integrais e fluxos locais.
  - Em progresso: Levi-Civita, imersões e subvariedades, orientação, formas diferenciais.
  - Ausente: classificação de 1- e 2-variedades, Sard, existência de métrica riemanniana, TFI/TFImp em variedades, quocientes e colagem.
  - Fluxos em variedades de Banach: Yin–Kudryashov, arXiv 2602.13247 (02/2026).
- **Hamilton 1982 em Lean** (Chow–Liao–Qin, arXiv 2608.21502, 25/08/2026).
  - Enunciado: Ric > 0 em M³ fechada implica forma espacial esférica.
  - Rota de blow-up, com existência curta via DeTurck e teoria espectral (sem Schauder).
  - 1.945.081 linhas, Lean/Mathlib v4.29.0, axiomas {propext, Classical.choice, Quot.sound}.
- **Poincaré, projeto A** (Qin–Liao–Khaitan–Chow, arXiv 2609.33842, 27/09/2026; repo `qinz1yang/differential-geometry`, v0.1.3 = 7a48598d, Lean/Mathlib v4.33.1).
  - Endpoints: `DifferentialGeometry.Topology.poincare_conjecture` (M T2, compacta, simplesmente conexa, `ChartedSpace (EuclideanSpace ℝ (Fin 3))` ⇒ M ≃ₜ S³ ⊂ ℝ⁴), `smoothPoincareConjecture_holds`, e `exists_isManifold_three` (Moise).
  - Rota: cirurgia de Perelman e extinção por "least-area width" (Hamilton/Perelman); Moise com aproximação PL leva ao enunciado topológico.
  - `#print axioms` dá os 3 axiomas padrão nos 4 endpoints.
  - Ressalva do próprio artigo: as interfaces de compacidade de κ-soluções e de vizinhança canônica são "apresentadas como resultados citados", e o relato completo "aparecerá em outro lugar".
  - Imprensa secundária: ≈4,0 M linhas no cone, 14.197 arquivos, cadeia de 353, ~2,7 M linhas escritas em 2 semanas.
- **Poincaré, projeto B, independente** (Zhang, Delaval, …, Bin Dong; arXiv 2610.08329, 06/10/2026; `frenzymath/PoincareConjecture`, toolchain v4.33.1).
  - Rota Morgan–Tian, ≈3,2 M linhas (≈2,8 M após extrair o cone), ~90 marcos, custo ≈ US$ 25 mil.
  - Verificação: Comparator com o kernel Lean e o Nanoda; só os 3 axiomas padrão são permitidos.
  - O artigo afirma que o projeto A também passa Comparator contra enunciados só-Mathlib.
  - Enunciado-alvo (`Comparator/Challenge.lean`, lido no repo):
    `∀ (M : Type u) [TopologicalSpace M] [T2Space M] [SecondCountableTopology M] [ChartedSpace (EuclideanSpace ℝ (Fin 3)) M] [IsManifold (𝓡 3) ∞ M] [CompactSpace M] [SimplyConnectedSpace M], Nonempty (Diffeomorph (𝓡 3) (𝓡 3) M ThreeSphere ∞)`.
    A versão topológica omite `IsManifold` e conclui `Nonempty (M ≃ₜ ThreeSphere)`.
- **Geometrização** (Liao, Qin, …, Peng Lu, Chow; arXiv 2610.13897; v0.1.5 = bafefb7, Lean v4.35.0-rc3).
  - Endpoint `GC.Endpoint.geometrization`.
  - Ressalvas: os cortes são só por toros, sem unicidade JSJ, e um caso de curvatura ≥ 0 não é mostrado ser variedade gráfica.
- **No HEAD fd2f07f do repo A (10/10/2026) há também** `poincare_high_dim_topological` (n ≥ 5, engulfing de Newman) e `poincare_smooth_ge6` (h-cobordismo).
  Vi o código-fonte, mas não compilei. Não há arquivos de Freedman / 4D topológico.
- **Confiança no kernel.** O bug de soundness #14576 (tipos indutivos aninhados) foi explorado em 07/2026 por uma "refutação" de Collatz feita por IA e corrigido no Lean 4.32.2 (28/07/2026).
  A e B usam 4.33.1, posterior à correção. Ainda não há arbitragem humana independente: a única reação de especialista na imprensa é elogiosa (Lichtman), e Agol apenas repostou.

### 1.3 Vizinhos genuinamente abertos (dimensão 4)
- **SPC4 (suave): aberta.**
  - Akbulut (arXiv 2209.09968) afirma um "outline" de prova, sem publicação revisada encontrada.
  - Estratégia s-invariante: FGMW 2010 obteve s(K₂) = 0 após 766 h de CPU; as esferas de Cappell–Shaneson foram mostradas padrão (Akbulut, Gompf).
  - Manolescu–Piccirillo (2102.04391, v3 2023) acharam 5 candidatos via 0-cirurgia, todos eliminados (Nakamura: não H-fatiáveis em #ⁿCP²).
  - Manolescu–Marengon–Sarkar–Willis mostraram que a estratégia falha para twists de Gluck.
  - Ren–Willis (2402.10452, 2024) fizeram a primeira detecção de exótica sem análise, com skein lasagna de Khovanov (traços de nós). Nahm (2510.10809, 2025) obteve o mesmo para variedades de Mazur exóticas.
    Esses resultados são em variedades compactas **com bordo**; nada ainda para esferas de homotopia fechadas.
- **Schoenflies suave em S⁴: aberta.** Scharlemann (math/0603511) provou os casos de gênero 2 e 3 via "Property R generalizada".
  Gabai (2212.02004, v0.695 de 05/2024) reformula SS4 em termos de pseudo-isotopias de S¹×S³ e prova que todo difeo de S¹×S³ isotópico à identidade é *estavelmente* isotópico.
- **Andrews–Curtis.** Shehper et al. (2408.15332, NeurIPS 2025) provaram AK(3) *estavelmente* AC-trivial, resolveram 3 subfamílias infinitas de Miller–Schupp e encurtaram AK(n) para comprimento n+11.
  Lisitsa (2501.18601, 2025) deu uma prova alternativa por Prover9, com sequências de 53/57 passos.
  AK(3) (não estável) continua aberto. Fagan et al. (2606.21611, ICML 2026) reduziram 550 apresentações MS não resolvidas a 261 classes.

## 2. Barreiras e o que elas já excluem
1. **Transportes por certificado** (F7/F8, `promote_to_kernel_endpoint`, `CertificadoPoincare`) colocam a conclusão num campo da hipótese e têm conteúdo zero. Toda a linha "CLOSED_UNCONDITIONAL" do corpus cai aqui.
2. **O fluxo de Ricci prova o enunciado suave.** O topológico (`≃ₜ`, `ChartedSpace` sem `IsManifold`) exige Moise (triangulação e suavização em dim 3), que custou ≈460–650 mil linhas em A e B.
   Qualquer enunciado topológico no ATK herda esse custo, ou então deve ser **suave**.
3. **Tamanho e toolchain.** Os cones têm 2,8–4,0 M linhas, em Lean 4.33.1 (A, B) ou 4.35-rc3 (geometrização). O ATK está em 4.34.1 + Mathlib d13f23b.
   Lake exige um único toolchain, então "importar" significa portar milhões de linhas ou manter um workspace de verificação separado.
4. **Confiança.** Há risco de enunciado infiel (mitigado pelo Comparator com enunciado só-Mathlib) e de kernel/checker (bug #14576 e bug de projeção do Nanoda antigo).
   Código gerado por IA também dificulta manutenção e revisão humana.
5. **SPC4.** O s-invariante falha para twists de Gluck, os candidatos CS e MP caíram, e invariantes de gauge clássicos não enxergam esferas de homotopia (b₂ = 0; fato clássico).
   Programas puramente computacionais de busca de nós têm histórico negativo.
6. **AC.** Há a dureza "two-hump" (Fagan et al.) e o limite prático de comprimento de relator ~20 nas buscas publicadas.
   Uma prova de AC-*não*-trivialidade de AK(3) exigiria invariante novo, que hoje não existe.

## 3. Questões atacáveis (ordenadas por valor × tratabilidade)
**Q1 [F, formalização de matemática conhecida] — Certificado externo auditável e equivalência de enunciados.**
- Enunciado: replicar `lake build` + Comparator (kernel ≥ 4.32.2 + Nanoda atual) de A@7a48598d e B@62db01a.
  Depois, provar em Lean que `DifferentialGeometry.Topology.poincare_conjecture` ⇔ `PoincareConjecture.TopologicalPoincare` (e o mesmo para as versões suaves).
- Por que importa: transforma o "PROVEN" do ATK em afirmação checável, sem confiar em release notes.
- Progresso: um relatório Comparator reprodutível com hashes, mais o lema de equivalência compilado.
- Conhecido: o artigo B diz que A passa Comparator, mas não há relatório público independente.

**Q2 [F] — π₁(Sⁿ) = 1 para n ≥ 2 e satisfatibilidade da hipótese.**
- Enunciado: `SimplyConnectedSpace (Metric.sphere (0 : EuclideanSpace ℝ (Fin (n+2))) 1)`.
- Sem isso a Mathlib não certifica que S³ satisfaz as hipóteses do próprio enunciado (risco de vacuidade parcial).
- Progresso: PR na Mathlib. Q2 é menor e mais "Mathlib-izável" que Q1.

**Q3 [F/meta] — Prova formal mínima.**
- Medir o cone por família (Moise/PL, análise parabólica, κ-soluções, cirurgia, extinção) e testar se a rota de extinção de Colding–Minicozzi ou o fluxo canônico de Bamler–Kleiner reduz ≥ 2× o núcleo analítico.
- Progresso: uma métrica de tamanho por módulo e um protótipo de rota alternativa para o passo de extinção.

**Q4 [F] — Subir para a Mathlib os blocos reutilizáveis vendorizados em `External/`:**
- invariância de domínio, Jordan/Schoenflies 2D, classificação de superfícies (Moise), cobrimentos;
- Levi-Civita, Ricci e escalar;
- existência curta via DeTurck.
- Progresso: PRs aceitos. O valor está em remover a dependência de repositórios de 4 M linhas.

**Q5 [N, matemática nova] — Andrews–Curtis para AK(3) e para as 261 classes MS.**
- Qualquer AC-trivialização é resultado novo. Uma obstrução computável a AC-equivalência sob cota de comprimento seria uma ferramenta nova.
- Conhecido: trivialidade estável de AK(3) e as classes de Fagan et al.
- Ligação com SPC4: indireta, via decomposições em alças de bolas de homotopia.

**Q6 [N] — SS4 na formulação de Gabai.**
- Para difeos explícitos de S¹×S³ (por exemplo os de "barbell"), decidir se são S-equivalentes à identidade. O gênero 4 do Schoenflies (além de Scharlemann) é o primeiro caso aberto concreto.
- Valor muito alto; tratabilidade baixa.

**Q7 [F, longo prazo] — Poincaré topológico em dim 4 (Freedman), ausente de A e B.**
- Seria o primeiro passo formal em topologia 4D genuína. Tamanho estimado: maior que o Poincaré 3D. Não recomendado como meta de curto prazo.

## 4. O que precisa ser criado
- **No ATK:**
  - `ATK/Poincare/Statement.lean` com o enunciado de B copiado verbatim, nas versões suave e topológica.
  - Um portão `ATK/Terminal/Poincare.lean` cujo status é `EXTERNAL_VERIFIED(commit, toolchain, comparator-hash)`, nunca `CLOSED_MATH` dentro do kernel do ATK.
  - Apagar o `Poincare.lean` com `constant` de Lean 3, a constante `MATERIAL_PRODUCER_GAPS := 0` e o claim CLOSED_UNCONDITIONAL.
  - Isolar e marcar os 2 axiomas inconsistentes do repo Millennium.
- **Infraestrutura:**
  - um workspace de verificação pinado em v4.33.1 com Comparator, `lean4export` e Nanoda;
  - um script de cone de dependência e varredura de metaprogramação (§5 T2);
  - um lema de equivalência entre enunciados;
  - π₁(Sⁿ).
- **Para vizinhos 4D:** apresentações balanceadas e movimentos AC em Lean (`FreeGroup` existe na Mathlib), com verificador de certificados de sequência AC (Lean `decide` sobre palavras reduzidas).
  Khovanov / s-invariante não existem em Lean: projeto grande, sem prioridade.

## 5. Testes baratos (≤ 20 min, 2 núcleos). Especificados, não executados.
**T1 — Enunciado fiel + censo de instâncias na Mathlib local (≤ 10 min).**
- Entrada: um arquivo novo com `ThreeSphere := Metric.sphere (0 : EuclideanSpace ℝ (Fin 4)) 1` e `SmoothPoincare`/`TopologicalPoincare` verbatim de B; compilar em Lean 4.34.1 + Mathlib d13f23b.
- Depois, `example : <Classe> ThreeSphere := inferInstance` para `T2Space`, `SecondCountableTopology`, `CompactSpace`, `ChartedSpace (EuclideanSpace ℝ (Fin 3))`, `IsManifold (𝓡 3) ∞` e `SimplyConnectedSpace`.
  Para as duas instâncias de carta (`ChartedSpace`/`IsManifold`), tentar também com `haveI : Fact (finrank ℝ (EuclideanSpace ℝ (Fin 4)) = 3 + 1)`.
- Hipótese: tudo é sintetizado exceto `SimplyConnectedSpace`.
- Saída informativa: a lista exata de faltas, que dimensiona Q2. Se `SimplyConnectedSpace` existir, Q2 está fechado. Se falhar a sintaxe, há deriva de API entre 4.33.1 e 4.34.1, o que mede o custo de porte.

**T2 — Auditoria estática dos cones de A e B, sem compilar (≤ 15 min).**
- Clone blobless de `qinz1yang/differential-geometry@7a48598d` e de `frenzymath/PoincareConjecture@62db01a`.
- Script Python com `-I`, fora do diretório clonado:
  1. Localiza o endpoint (`grep "theorem poincare_conjecture"` / `Proofs/Main.lean`).
  2. Resolve o fecho de `import` do endpoint.
  3. Conta módulos e linhas por diretório de topo (Moise/PL, RicciFlow, Analysis, External).
  4. Varre o fecho por `axiom`, `sorry`, `admit`, `native_decide`, `implemented_by`, `@[extern`, `unsafe`, `addDecl`, `Environment.add`, `Kernel.`, `skipKernelTC`, `ofReduceBool`, `run_cmd`, `run_elab`, `elab_rules`.
  5. Extrai a assinatura do endpoint e verifica que não há parâmetros-estrutura do tipo `*Interface/*Contract/*Certificate`. O repo A tem cerca de 396 arquivos com Frontier/Contract/Interface no nome.
- Hipótese: o cone não tem metaprogramação capaz de injetar declarações no kernel e o endpoint não tem hipóteses.
- Saída: tabela de tamanhos (confirma ou refuta "≈4,0 M linhas", que vem de fonte secundária) e qualquer ocorrência suspeita com arquivo:linha.

**T3 — Extração e porte do lema π₁(Sⁿ) = 1 (≤ 20 min).**
- Procurar em A e B uma declaração com conclusão `SimplyConnectedSpace (… sphere …)`. Em A, candidatos são `Topology/Covering/SimplyConnected.lean` e `External/CanonicalTopology/Topology/LoopSpace/SimplyConnectedTarget.lean`.
- Calcular o fecho de imports. Se tiver ≤ 60 arquivos e depender só da Mathlib, copiar para um projeto de rascunho em 4.34.1/d13f23b, compilar e registrar cada erro de porte.
- Hipótese: existe uma prova autocontida e portável, ou seja, um candidato direto a PR na Mathlib que fecha a última falta de T1.
- Se nenhum dos dois repos tiver o lema, isso também é informativo: nenhum dos projetos certifica que S³ satisfaz a hipótese de π₁.

## 6. Marcos realistas para o ATK
- **M0 (dias):** T1 + T2, enunciado fiel no ATK, remoção dos claims falsos.
- **M1 (1–2 semanas):** Q1, com relatório Comparator reprodutível de A e B e o lema de equivalência.
- **M2 (semanas):** Q2, com PR de π₁(Sⁿ).
- **M3 (meses):** porte seletivo ou dependência pinada; Q3 e Q4.
- **Pesquisa nova:** Q5 (computacional), depois Q6.

## Fontes (abertas nesta sessão)
- https://arxiv.org/abs/2608.21502 ; https://arxiv.org/pdf/2608.21502
- https://github.com/qinz1yang/differential-geometry (README; código lido via `git` no HEAD fd2f07f e tags)
- https://arxiv.org/abs/2609.33842 ; https://arxiv.org/pdf/2609.33842v1
- https://arxiv.org/html/2610.08329 ; https://github.com/frenzymath/PoincareConjecture (README; `Comparator/Challenge.lean` lido via `git`)
- https://arxiv.org/html/2610.13897
- https://www.kucoin.com/news/flash/poincar-conjecture-proof-fully-verified-by-ai-in-4-7-million-lines-of-code (secundária)
- https://eu.36kr.com/en/p/4022237394309254 (secundária) ; https://mathstodon.xyz/@Ianagol/117361769275765173
- https://www.math.uni-bonn.de/people/rothgang/slides_Italean2025_diffgeo.pdf ; https://arxiv.org/abs/2602.13247
- https://arxiv.org/abs/math/0607607 ; https://arxiv.org/abs/1709.04122 ; https://arxiv.org/abs/math/0308090v3
- https://arxiv.org/abs/2102.04391 ; https://math.princeton.edu/node/17113 ; https://tqft.net/papers/SPC4.pdf ; https://arxiv.org/abs/2209.09968
- https://arxiv.org/abs/2402.10452v1 ; https://arxiv.org/abs/2510.10809
- https://arxiv.org/abs/2212.02004 ; https://arxiv.org/abs/math/0603511
- https://arxiv.org/abs/2408.15332 ; https://arxiv.org/html/2408.15332v2 ; https://arxiv.org/abs/2501.18601 ; https://arxiv.org/abs/2606.21611
- https://gigazine.net/gsc_news/en/20260803-collatz-lean-kernel-bug (bug #14576 e correção no 4.32.2)
- Bloqueados (sem permissão, não usados): leanprover.github.io/lean-eval-leaderboard/problems/poincare_3d_topological ; raw.githubusercontent.com/frenzymath/… (obtido via git) ; leodemoura.github.io postmortem #14576
