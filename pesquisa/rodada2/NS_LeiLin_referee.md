# NS: parecer sobre "limiar de Lei–Lin melhorado para √2·ν" (wave2)

## Veredito: CORRETO, com precisões técnicas menores. Além disso, não é ótimo: o mesmo método dá **3ν/2**.
- O argumento de 4 passos está certo, e o teorema global de Lei–Lin passa intacto com ‖u₀‖_{χ⁻¹} < √2·ν.
- Uma única troca no passo 4 (lema de Björck/Legendre, §3) dá ‖u₀‖_{χ⁻¹} < **3ν/2**.
- 3/2 é o **ótimo** para qualquer argumento que passe por Ñ.
- Literatura: não achei nenhuma melhoria da constante; o estado é **aparentemente novo** (§4).

## 1. Normalização e o que Lei–Lin fazem de fato
- **Em T³ = [0,2π]³**, u = Σ û_k e^{ik·x}, com û₀ = 0. Ambrose–Lopes Filho–Nussenzveig Lopes usam essa normalização [ALN].
- **Em ℝ³**, u = ∫e^{ix·ξ}û dξ, isto é, û = (2π)⁻³∫e^{−ix·ξ}u. É a convenção em que (uv)^ = û∗v̂ sem constante.
- Lei–Lin nunca definem 𝓕 [LL, arXiv:1203.2699], mas escrevem a convolução com coeficiente 1, e a constante deles só vale nessa convenção.
  - Com 𝓕 = ∫e^{−ixξ}, como em Benameur [Be], o limiar vira (2π)³ vezes maior.
  - Na normalização ATK (e^{−2πixξ}) os limiares ficam: 2πν (Lei–Lin), 2√2πν (√2) e **3πν** (3/2).
- **A prova de Lei–Lin confere com a descrição.**
  - Tomam dados mollificados e a solução suave local, e estimam d/dt∫|ξ|⁻¹|v̂| + μ∫|ξ||v̂| ≤ ∫∫|v̂(η)||v̂(ξ−η)|dηdξ.
  - Esse passo descarta o fator unitário ξ/|ξ|, ou seja, **não usa** v̂(η) ⊥ η.
  - Em seguida, por AM-GM, (2.5) dá ≤ ½∫∫(|η|⁻¹|ξ−η| + |η||ξ−η|⁻¹)|v̂||v̂| = ‖v‖_{X⁻¹}‖v‖_{X¹}.
  - Daí a constante 1 e o limiar μ (Thm 1.1), e (2.7) dá sup‖v‖_{X⁻¹} + (μ−‖v₀‖)∫‖v‖_{X¹} ≤ ‖v₀‖.
  - A constante só entra em (2.6)–(2.7).
  - A unicidade/Cauchy entre soluções usa Gronwall com ∫‖v‖²_{X⁰} ≤ ∫‖v‖_{X⁻¹}‖v‖_{X¹} < ∞ e não depende do limiar. Com a constante nova, o teorema inteiro se transfere linha a linha.

## 2. Checagem passo a passo
Notação: a_p = |û_p|, W_k = −iP_kG_k e G_k = Σ_{p+q=k}(k·û_p)û_q, de modo que ∂_t û_k = −ν|k|²û_k + W_k.

**P1 (ok).**
- *Zeros de û_k.* Se f é C¹ com f(t) = 0, então D⁺|f|(t) = |f′(t)|; logo D⁺|û_k| ≤ −ν|k|²|û_k| + |W_k| vale também nos zeros (o termo viscoso se anula).
- *Rigor sem Dini de séries infinitas.* û_k é absolutamente contínua (|G_k| ≤ |k|A₀², com A₀ ∈ L²_t). Então |û_k| é AC, com d|û_k|/dt ≤ −ν|k|²|û_k| + |W_k| q.t.p. (num zero onde existe derivada, ela vale 0).
  - Integrando e somando com peso |k|⁻¹ (Tonelli, termos ≥ 0): A₋₁(t) + ν∫₀ᵗA₁ ≤ A₋₁(0) + ∫₀ᵗN, com N = Σ_k|k|⁻¹|W_k|.
  - Também se pode fazer em Galerkin, onde tudo é finito.
- |P_kG| ≤ |G| ≤ Σ|k·û_p||û_q|.
- *k = 0 e média.* W₀ = 0. Em T³ é preciso **û₀ = 0**, ou remover a média U.
  - A média é conservada. O termo p = 0 dá −i(k·U)û_k, que é fase pura e some em Re⟨û_k, ·⟩. O termo q = 0 dá (k·û_k)U = 0.
  - Logo as somas valem só com p, q ≠ 0, e A₀ não inclui |U|. A troca galileana não muda |û_k|.

**P2 (ok).**
- p·û_p = 0, logo k·û_p = k_⊥·û_p, com k_⊥ ⊥ p real.
- Por Cauchy–Schwarz em ℂ³, |k·û_p| ≤ |k_⊥|a_p, com |k_⊥| = |k| sin∠(k,p) = |p×q|/|p|.
- Os termos p = 0 ou q = 0 já foram tratados (a₀ = 0).

**P3 (ok, e de fato vale com igualdade).**
- Ñ = Σ_{p,q≠0, p+q≠0} w(p,q)a_pa_q, com w = |p×q|/(|p||p+q|).
- (p,q) ↦ (q,p) é bijeção do mesmo conjunto de índices. q ↦ −q leva {p+q ≠ 0} em {p ≠ q} e usa a_{−q} = a_q, que **exige u real**.
- Todos os termos são ≥ 0, então rearranjar é lícito.
- As exclusões caem justamente em p = ±q, onde |p×q| = 0. Pondo T(p,±p) := 0, vale **4Ñ = Σ_{p,q}T(p,q)a_pa_q**.

**P4 (ok).**
- Mudança de variável: (1+r)² = (1+r²)(1+x) e 1+r² ± 2r cosθ = (1+r²)(1 ± x cosθ).
- Monotonia em x: g(x) = h(xc) + h(−xc), com h(y) = (1+y)^{−1/2} convexa, cresce em |xc|, e √(1+x) também cresce. Logo **T(r,θ) ≤ T(1,θ) = 2sin(θ/2) + 2cos(θ/2) = |p̂−q̂| + |p̂+q̂| ≤ 2√2**.
- Numericamente, numa grade de 2·10⁶ pontos (r ∈ [10⁻³, 10³]), o máx é 2.8284269 em (1, π/2). Há zero violações genuínas: 4 sinalizações em r = 1 exato são arredondamento de 10⁻¹¹.

**Conclusão (ok).**
- N ≤ Ñ ≤ A₀²/√2 ≤ A₋₁A₁/√2, por Cauchy–Schwarz (A₀² ≤ A₋₁A₁).
- Daí A₋₁(t) + (ν − A₋₁(0)/√2)∫A₁ ≤ A₋₁(0), por continuidade enquanto A₋₁ ≤ A₋₁(0).
- **ℝ³:** idêntico com integrais. O conjunto p+q = 0 tem medida nula, e |û(−ξ)| = |û(ξ)| pois u é real.

## 3. Prova limpa do limiar 3ν/2 (substitui P4)
**Lema (Björck 1956, via Legendre).** Para toda medida finita μ ≥ 0 em S², ∬(|x−y| + |x+y|)dμ(x)dμ(y) ≤ (8/3)μ(S²)².
- *Prova.* Seja K(t) = √(2−2t) + √(2+2t) = 8/3 − 8Σ_{n par≥2} P_n(t)/((2n−1)(2n+3)).
  - A expansão vem de √(1−t) = (2√2/3)[1 − 3Σ_{n≥1}P_n/((2n−1)(2n+3))]. Converge uniformemente porque |P_n| ≤ 1 e Σn⁻² < ∞.
  - Pelo teorema de adição, ∬P_n(x·y)dμdμ = (4π/(2n+1))Σ_m|∫Y_{nm}dμ|² ≥ 0, e o resultado segue.
  - Conferido com mpmath: k₀ = 8/3; k_n = −8/((2n−1)(2n+3)) para n par e 0 para n ímpar, n ≤ 12, com 12 dígitos.

**Proposição.** Ñ ≤ (2/3)A₀² ≤ (2/3)A₋₁A₁.
- *Prova.* 4Ñ = ΣT(p,q)a_pa_q ≤ ΣK(p̂·q̂)a_pa_q. Fora da diagonal isso é P4; em p = ±q, T = 0 ≤ K = 2.
- O lado direito é ∬K dμdμ ≤ (8/3)A₀², com μ = Σa_pδ_{p̂}; em ℝ³, μ é o push-forward de |û(ξ)|dξ por ξ ↦ ξ/|ξ|.

**Teorema.** Seja u₀ real, div u₀ = 0, com ‖u₀‖_{χ⁻¹} < 3ν/2 (média nula em T³). Então existe uma única solução global mild em C([0,∞); χ⁻¹) ∩ L¹(χ¹), com ‖u(t)‖_{χ⁻¹} + (ν − (2/3)‖u₀‖_{χ⁻¹})∫₀ᵗ‖u‖_{χ¹} ≤ ‖u₀‖_{χ⁻¹}.
- *Prova:* a de Lei–Lin, trocando a constante 1 por 2/3 em (2.6)–(2.7).

**Ótimo para o método e resposta a (c).** sup Ñ/(A₋₁A₁) = 2/3.
- Atinge-se com cascas finas R−½ ≤ |k| ≤ R+½ e |û_k| constante. As direções equidistribuem (soma de Riemann), então Ñ/A₀² → 2/3 e A₀²/(A₋₁A₁) → 1 simultaneamente.
- 2√2 é atingido por um par real da soma (p ⊥ q, |p| = |q|), mas a cota ΣTaa ≤ (sup T)(Σa)² **nunca** é justa.
  - Para um par ortogonal isolado, Ñ/A₀² = √2/4, metade de 1/√2, porque os pares p = ±q contam 0.
  - Nenhuma medida em S² se concentra em pares ortogonais. O supremo da forma quadrática é 8/3 < 2√2.
- Logo √2 não é ótimo para este método; 3/2 é.

## 4. Literatura (busca extensa, out/2026): nenhuma melhoria da constante encontrada
| fonte | limiar enunciado |
|---|---|
| Lei–Lin, CPAM 64 (2011); arXiv 1203.2699 [LL] | ‖v₀‖_{X⁻¹} < μ, constante 1, sem usar v̂ ⊥ ξ |
| Bae, PAMS 143 (2015) | "the recent work of Lei-Lin in a slightly different setting"; só li o resumo |
| Ambrose–Lopes Filho–Nussenzveig Lopes, PAMS 152 (2024); arXiv 2205.12383 [ALN] | T³, ε₀ < μ²/(4C(1+μ)²), mais fraco; diz que Lei–Lin "only necessary … < μ" |
| Zhang–Yin, arXiv 1306.3735 | NS: < ν (reprova Lei–Lin); NS generalizado: ≤ Cν com C não explícito |
| Benameur, arXiv 1312.2136 [Be] | repete < ν (com 𝓕 = ∫e^{−ixξ}, o que é folgado por (2π)³) |
| Lei–Lin–Zhou, ARMA 2015 (helicidade) | funcional Ḣ^{1/2} helicoidal, sem relação com a constante χ⁻¹ |
| Melo et al. EJDE 2023; Jlali, Symmetry 2025; Aurazo-Alvarez–Neves 2025 | constantes não explícitas |

- Só li resumos de Cannone–Wu (Fourier–Herz), do livro de Lemarié-Rieusset e de Liu–Zhang; não os li inteiros.
- O argumento é elementar (ângulo + simetrização + Björck), então pode existir como folclore ou em fonte não indexada.
- Status: **aparentemente novo**, para √2 e para 3/2.

## 5. Numérica em C (`code/ns_leilin_check.c`, gcc -O2; lemas em `code/ns_leilin_lemmas.py`)
**Controles.**
- Energia Σ Re⟨û_k, W_k⟩ e helicidade Σ Re⟨ik×û_k, W_k⟩ ficam em ~10⁻¹⁷ relativo em todos os campos.
- A identidade 4Ñ = ΣTaa vale até 10⁻¹².
- Casos exatos: 2 modos ortogonais circulares dão ρ = A₋₁A₁/N = 4√2; 3 eixos dão ρ = 3√2. Ambos batem com o teste T2.

| teste | campos | máx observado |
|---|---|---|
| aleatórios: 4 tipos (log-normal, casca, lei de potência, polarização linear), caixa M = 2..10, até ~4000 modos | 1620 | N/N1 ≤ 1; N1/N2 = 0.822; N2/Ñ = 0.844; **Ñ/A₀² = 0.6619**; Bj/A₀² = 0.66661 |
| cascas uniformes R = 2..13 (até 2178 modos) | 12 | Ñ/A₀² sobe a 0.66544 (R = 13), com A₀²/(A₋₁A₁) = 0.9995 |
| adversarial: max ¼ΣTaa/A₀² por replicador (Baum–Eagon) na bola \|k\| ≤ R | R = 4, 6, 8 (2108 pts) | 0.6553, 0.6616, **0.6632** → 2/3; nunca perto de 1/√2 = 0.7071; o suporte ótimo é uma casca |
| N verdadeiro: subida de encosta em N/(A₋₁A₁), 2–16 classes | 103 reinícios | 0.2675, logo ρ_min ≤ 3.74 (T2 achou 3.499) |

- Todas as desigualdades N ≤ N1 ≤ N2 ≤ Ñ ≤ (2/3)A₀² ≤ A₀²/√2 valeram em todos os campos.
- O que isso **sugere** (não prova): 2/3 é o supremo da etapa Ñ.

## 6. (d) Dá para ir além?
- **No nível Ñ, não:** 3/2 é exato (§3).
- Ir além exige usar o que Ñ esquece: a polarização (|k·û_p| < |k_⊥|a_p salvo alinhamento), a projeção P_k (que mata o termo "plano×plano" do par) e o cancelamento de fases em Σ_{p+q=k}.
- **Obstrução.** O extremal de Ñ (casca isotrópica) é onde N/Ñ é menor: N1/N2 ≈ 0.08–0.2 por cancelamento de fases. Já os suportes esparsos "livres de somas", com N ≈ Ñ, têm Ñ/A₀² ≲ 0.47.
- A constante verdadeira C* = sup N/(A₋₁A₁) satisfaz 0.2675 (aqui) ≤ C* ≤ 2/3, ou 0.2858 pelo T2, a conferir.
- **Teto duro do método** (A₋₁ como funcional de Lyapunov): ν/C* ≤ 3.74ν. Por escala existem campos com A₋₁ ≈ 3.74ν e d⁺A₋₁/dt > 0.
- Entre 1.5ν e ≈ 3.5ν o problema é extremal, conjunto polarização × suporte. Rota natural: a decomposição helicoidal (coeficientes de Waleffe), que dá um núcleo em S² × {±} para uma nova forma quadrática à la Björck.

Referências: [LL] arxiv.org/abs/1203.2699 · [ALN] arxiv.org/abs/2205.12383, doi 10.1090/proc/16615 · Bae: ams.org/proc/2015-143-07/S0002-9939-2015-12266-6 · Zhang–Yin: arxiv.org/abs/1306.3735 · [Be] arxiv.org/abs/1312.2136 · LLZ: arxiv.org/abs/1505.00142 · Björck, Ark. Mat. 3 (1956) 255–269.
