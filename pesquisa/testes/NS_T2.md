# NS T2: constante κ* do argumento de Lei–Lin em T³ (reduzido)

**Hipótese testada (Q4).** κ* = inf_u A_{−1}A_1/N > 1, onde:
- A_s = Σ|k|^s|û_k|;
- N é a parte não linear de d⁺/dt A_{−1}, contando o termo de derivada à direita nos modos nulos de S + S.

Lei–Lin dá κ* ≥ 1. A heurística do frontier é κ* ≥ 2/√3 numa casca.

**Resultado analítico obtido durante o teste: κ\* ≥ √2. É um esboço e precisa de checagem independente.**
1. *Fator angular.* Como û_p ⊥ p, vale |k·û_p| ≤ |k| sin∠(k,p) |û_p|. Logo N ≤ Ñ := Σ_{p,q} sin∠(p+q, p) |û_p||û_q|.
2. *Simetrização.* Simetrizando em (p,q) ↔ (q,p) e q ↔ −q, com |û_{−q}| = |û_q|, vem Ñ = ¼ Σ_{p,q} |û_p||û_q| T. Aqui T = (1+r) sinθ (1/|p+q| + 1/|p−q|), com |p| = 1, |q| = r e θ = ∠(p,q).
3. *Cota de T.* Com x = 2r/(1+r²), T = √(1+x)·sinθ·[(1+x cosθ)^{−1/2} + (1−x cosθ)^{−1/2}]. T cresce com x, e em x = 1 vale T = 2 sin(θ/2) + 2 cos(θ/2) ≤ 2√2.
4. *Conclusão.* N ≤ A_0²/√2 ≤ A_{−1}A_1/√2. O limiar de Lei–Lin melhora para χ^{−1}(u₀) < √2·ν (normalização e^{ik·x}; na do ATK, < 2√2πν). O argumento vale igual em ℝ³.
- Conferência numérica: o máximo de T numa grade de 2·10⁶ pontos é 2.828427 = 2√2, atingido em (r, θ) = (1, π/2).
- Uma busca rápida na web não achou a melhoria; isso não exclui que ela exista na literatura.

**Método** (`tests/code/NS_T2.c`, em C puro, sem numpy/scipy).
- G_k = −iP_kΣ_{p+q=k}(k·û_p)û_q por convolução direta, saídas em |k_i| ≤ 2M; gradiente analítico de f = log A_{−1} + log A_1 − log N.
- L-BFGS próprio; depois, poda dos modos com |v|² < 10⁻⁶·máx e reotimização. Também crescimento guloso, suportes pequenos aleatórios e suportes explícitos.

**Controles (todos passaram).**
- *Implementação.* Gradiente vs diferenças finitas: erro relativo ≤ 4·10⁻⁶. Energia e helicidade (Σ Re⟨û_k, G_k⟩ = Σ Re⟨ω̂_k, G_k⟩ = 0) até 10⁻¹³. (u·∇u)(x) no espaço físico bate com Σ iW_k e^{ik·x} até 10⁻¹³. ρ(su) = ρ(u).
- *Derivada temporal.* d/dt A_{−1} por passo de Euler (ν = 0) bate com N: 184.074616 contra 184.074600 em dt = 10⁻⁷, o que confirma o termo dos modos nulos.
- *Lei–Lin (κ\* ≥ 1 recuperado).* N ≤ A_0² ≤ A_{−1}A_1 em toda configuração avaliada; o menor ρ visto foi 3.499. A cota angular N ≤ Ñ ≤ A_0²/√2 valeu em 40 configurações aleatórias e em todas as saídas do otimizador (máx Ñ/A_0² = 0.622 < 0.707).
- *Configurações analíticas exatas.* Dois modos ortogonais: ρ = 4√2 = 5.656854. u = 2a(cos z, cos x, cos y) (3 eixos): ρ = 3√2 = 4.242641. A conta à mão dá N_par = 2(sin(θ/2) + cos(θ/2))ab para |p| = |q|: a projeção P_k mata exatamente o termo plano × plano.

**Parâmetros efetivos e reduções.** M ∈ {1, 2, 3, 4} (spec: 2 e 3); reinícios: cerca de 80 em M = 2, 75 em M = 3 e só 3 em M = 4. No lugar de Nelder–Mead em famílias de tríades/quartetos, usei suportes explícitos de 2–3 modos e suportes aleatórios de 3–16 classes, com L-BFGS. Tempo total: cerca de 6 min de relógio.

**Resultados.** ρ_min por tamanho de suporte (classes ±k): 2 → 5.657, 3 → 4.243, 4 → 4.029, 5 → 3.867, 6 → 3.811, 8 → 3.711, 11 → 3.647.

| configuração | ρ_min |
|---|---|
| M = 2, caixa inteira, sem poda | 4.93 |
| M = 2, caixa inteira, com poda (9 classes) | 3.578 |
| M = 3, com poda (12 classes) | **3.4988** |
| M = 4, com poda | 3.622 (só 3 reinícios) |

**Estrutura dos minimizadores.**
- **N_suporte ≈ 0, ou seja, N vem 100% de modos fora do suporte.** O suporte é "livre de somas": não há tríades internas, então não há ângulos de tríade a reportar.
- Escala quase única: A_{−1}A_1/A_0² ≈ 1.01, em 3–6 cascas vizinhas.
- Ñ/A_0² ≈ 0.59 (o teto é 0.707) e N/Ñ ≈ 0.48: a perda de ≈ ½ vem da projeção e das polarizações.

**Interpretação honesta.**
- *O que o teste mostra.* √2 ≤ κ*(T³) ≤ 3.499. A cota inferior é analítica e ainda não conferida. A superior é uma configuração explícita, avaliada em ponto flutuante.
- **κ\* > 1 deixa de ser hipótese**, se o esboço estiver certo. O frontier esperava ρ_min ≈ 1.1–1.15; o argumento de Lei–Lin perde um fator ≥ √2, e a numérica sugere uma perda em torno de 3.5.
- *O que fica só sugerido.* O valor de κ*. ρ_min ainda cai com o tamanho do suporte (4.24 → 3.50), então **não é estável em M** e não estimo o ínfimo.
- O máximo do par isolado (T = 2√2, ganho ½) sugere 2√2 ≈ 2.83 como piso natural de configurações livres de somas, mas não é prova.

**Limites.** Otimização local de objetivo não suave, logo só cotas superiores; a busca em M = 4 é rasa. A rede ℤ³ só aproxima as direções do contínuo. A cota √2 é um esboço de uma página que ainda não passou por revisão.

**Próximo.**
1. Escrever e checar a prova de κ* ≥ √2: é curta (Cauchy–Schwarz + lema de T) e formalizável em Lean na biblioteca χ^s. Fazer uma busca bibliográfica direcionada (Bae; Ambrose et al.).
2. Tentar provar que a projeção dá mais um fator, N ≤ c·Ñ com c < 1 em configurações gerais (rumo a κ* ≥ 2√2?). Buscar suportes simétricos livres de somas com M ≥ 5 (direções icosaédricas, cascas finas) para ver se ρ desce a 2√2 ou estabiliza.
