# RH — "1/2 com cauda" (22/10/2026)

**Resultado.** As três leituras de "1/2 tem uma cauda" estão decididas no kernel (`atk-kernel/ATK/CaudaMeio.lean`,
7 teoremas, axiomas padrão):

1. **Cauda decimal infinita** (0,4999… ou 0,5000…): é exatamente 1/2 (`dizima_noves`, `cauda_decimal_exata`).
2. **Cauda verdadeira**, Re ρ = 1/2 + ε com ε ≠ 0:
   * vem em par com 1/2 − ε na mesma altura, e o centro continua exatamente 1/2 (`cauda_par`);
   * refuta RH (`cauda_refuta`);
   * deixa um piso B > 0 em D_∞ (`cauda_piso`), mas esse piso some com a altura: B ≤ 2|ε|/γ²
     (`barreira_le_cauda`). Para D_N enxergá-la, seria preciso D_N < 2|ε|/γ² (`deteccao_exige`).
3. **Cauda que encolhe**, ε_n → 0 ao longo de zeros distintos: as alturas vão a infinito
   (`ATK.TruncamentoZero.aproximantes_sobem`).

## Quanto o produtor D_N precisaria para enxergar uma cauda

O piso é B = (2ε)·|1−ρ|²/|ρ|⁴. Para o N necessário, a coluna supõe que a queda observada D_N ≈ C₀/log N continua
(C₀ = 2 + γ_E − log 4π = 0,04619). Essa parte é heurística. Código: `codigo/cauda_deteccao.py`.

| γ | ε | B | N necessário |
| --- | --- | --- | --- |
| 14,13 | 0,25 | 2,5·10⁻³ | 10⁸ |
| 14,13 | 0,01 | 1,0·10⁻⁴ | 10²⁰¹ |
| 14,13 | 10⁻⁶ | 1,0·10⁻⁸ | 10^(2·10⁶) |
| 10³ | 0,01 | 2·10⁻⁸ | 10^(10⁶) |
| 3·10¹² | 0,25 | 5,6·10⁻²⁶ | 10^(3,6·10²³) |
| 3·10¹² | 10⁻⁶ | 2,2·10⁻³¹ | 10^(9·10²⁸) |

Uma cauda abaixo da altura 3·10¹² já está excluída por verificação rigorosa (Platt–Trudgian). Acima disso, o
produtor D_N não a enxerga em nenhum cálculo realizável. Uma cauda se detecta por **contagem**, não por
precisão. O par 1/2 ± ε + iγ não muda o sinal de Z(t) na reta, então o princípio do argumento conta dois zeros
onde Z não troca de sinal. É assim que o método de Turing funciona.
