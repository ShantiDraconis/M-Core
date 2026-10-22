# YM T3 (reduzido) — Espectro exato da matriz de transferência da TGR ℤ₂ em 2+1D

**Hipóteses testadas (YM_frontier §5 T3).**
- (H1) m_L(β) = log(λ₀/λ₁) no fluxo 0 não depende de L para β ≤ 0.5 (|m₄ − m₃| < 1e−3).
- (H2) m_L fica muito acima da taxa de Dobrushin.
- (H3) Para β > 0.76, o desdobramento entre setores de fluxo vai a 0 como e^{−cL}, mas o gap no fluxo 0 continua aberto.

**Método.**
- *Modelo.* Wilson isotrópico, calibre temporal: T = D^{1/2}KD^{1/2}, D = e^{βΣσ_p}, K = ∏_ℓ(e^β + e^{−β}X_ℓ).
- *Base invariante.* Plaquetas (∏σ_p = 1) × holonomias (W_x, W_y). Setores de fluxo elétrico e = (±,±) de dimensão
  2^{L²−1} (8, 256 e 32 768 para L = 2, 3, 4).
- *Cálculo.* C próprio, sem numpy: Lanczos com reortogonalização completa, início aleatório (todos os setores de simetria
  da rede, ≥ 60 iterações) e QL. β ∈ [0.02, 1.2] em passos de 0.02, mais passos de 0.005 em [0.60, 0.90].
- *Controles (todos passaram).*
  1. L = 2 por força bruta na base de elos (32 órbitas, `mpmath.eigsy`): os 32 autovalores e os fluxos batem.
  2. L = 3 por código independente na base de elos (2¹⁸ estados, projetores de calibre e fluxo a cada passo): λ₀, λ₁ e
     λ₀(−+) batem até ~1e−12. Projetar só o início falha: as cargas estáticas têm autovalores **maiores** (tanh β).
  3. Acoplamento forte: m_L → −4 log tanh β. Em β = 0.02, m₃ = m₄ = 15.6490 contra 15.6486; em β = 0.01, m₃ = 18.4209,
     valor da fronteira. A tensão split/L ≈ 1.618 em β = 0.2, contra −log tanh 0.2 = 1.623.

**Resultados** (m_L = gap no fluxo 0; split = log(λ₀(++)/λ₀(−+)))

| β | −4ln tanh β | m₂ | m₃ | m₄ | \|m₄−m₃\| | split₂ | split₃ | split₄ |
|---|---|---|---|---|---|---|---|---|
| 0.02 | 15.6486 | 15.5929 | 15.6490 | 15.6490 | 6e−10 | 7.824 | 11.737 | 15.649 |
| 0.10 | 9.2236 | 8.9627 | 9.2328 | 9.2328 | 7e−06 | 4.591 | 6.915 | 9.223 |
| 0.20 | 6.4906 | 6.0211 | 6.5177 | 6.5183 | 5e−04 | 3.159 | 4.839 | 6.473 |
| 0.30 | 4.9334 | 4.3239 | 4.9569 | 4.9647 | 8e−03 | 2.263 | 3.579 | 4.837 |
| 0.40 | 3.8709 | 3.2181 | 3.7968 | 3.8576 | 6e−02 | 1.572 | 2.574 | 3.547 |
| 0.50 | 3.0877 | 2.5399 | 2.7143 | 2.9310 | 0.22 | 1.020 | 1.662 | 2.350 |
| 0.70 | 2.0143 | 2.3034 | 1.4780 | 1.1083 | 0.37 | 0.360 | 0.322 | 0.353 |
| 0.76 | 1.7784 | 2.4517 | 1.6250 | 1.1963 | 0.43 | 0.262 | 0.167 | 0.121 |
| 0.90 | 1.3346 | 2.9805 | 2.3855 | 2.1479 | 0.24 | 0.131 | 0.044 | 0.0145 |
| 1.00 | 1.0894 | 3.4292 | 2.9907 | 2.8400 | 0.15 | 0.082 | 0.020 | 0.0046 |
| 1.20 | 0.7277 | 4.3653 | 4.1264 | 4.0557 | 0.07 | 0.035 | 0.005 | 0.0007 |

- *Transição (controle 4).* L·split se cruza em β = 0.7521 (L = 2/3) e 0.7546 (L = 3/4), e o mínimo de m_L migra de 0.63
  para 0.72: coerente com β_c = 0.7614 (conferi −½ ln tanh 0.221654, dual de Kramers–Wannier do Ising 3D). O "autodual"
  tanh β = e^{−2β} (0.4407) só vale em d = 4; em 2+1D o gap é suave ali.

**Interpretação** (para L ≤ 4).
- *O que o teste mostra.*
  - **H1 falha:** |m₄ − m₃| < 1e−3 só até β ≈ 0.21; chega a 0.06 em 0.4 e 0.22 em 0.5.
  - **H2 vale:** em β = 0.01 o gap é 18.42, contra as taxas 1.06 (Dobrushin exato) e 0.23 (`lgt`), cerca de 17× e 80×.
  - **H3 vale qualitativamente:** para β ≥ 0.9, split cai 3 a 7× por unidade de L (c ≈ 1.1 a 2.0). O gap no fluxo 0
    fica ≥ 1.43 (L = 4, β ≥ 0.8) e cresce quase linearmente. É gap sem confinamento, com vácuo quase 4 vezes degenerado.
- *O que ele sugere.* O gap em volume finito existe para todo β (Perron–Frobenius). O conteúdo real, a uniformidade em L,
  só aparece em acoplamento forte e não se decide com L ≤ 4 perto de β_c.

**Limites.**
- L ≤ 4. L = 5 (2²⁴ por setor) não rodou por falta de CPU (Lean e o SAT do PNP).
- Sem resolução por momento/paridade: λ₁ é o maior estado excitado de qualquer simetria no fluxo 0.
- Os cruzamentos usam tamanhos muito pequenos.

**A seguir.** (1) L = 5 e 6 com redução por momento, para medir |m₅ − m₄|. (2) Extrapolar β_c(L) e ν.
(3) Enunciar `GapMassa` no fluxo 0 com a uniformidade em L como hipótese explícita.

Código: `research/tests/code/YM_T3.c`, `YM_T3_check.py`, `YM_T3_linkcheck.c`. Dados em `research/tests/work/YM_T3_*.dat`
(~6 min de CPU).
