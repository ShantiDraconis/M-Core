# Região sem zeros logarítmica — o próximo passo depois de `|t|⁻⁵`

Três módulos novos, 54 teoremas, todos sem `sorry`, sem axiomas novos e auditados pelo CI.
`CLOSED_MATH` continua `false`: nada aqui decide RH.

## O que o kernel prova

**`ATK/ZetaParcial.lean` (8)** — a fórmula de somas parciais, para `Re s > 0`, `s ≠ 1`, `N ≥ 1`:

    ζ(s) = Σ_{n≤N} n^{−s} + N^{1−s}/(s−1) − s ∫_N^∞ {u} u^{−s−1} du        (zeta_parcial)

provada por indução em `N` a partir do caso `N = 1` (`ZetaRegiao.zeta_eq`).

**`ATK/ZetaLog.lean` (39)** — com `N = ⌈2|t|⌉` e `L = log N`, perto de `Re s = 1`:

| teorema | conteúdo |
|---|---|
| `norm_zeta_le_log` | `|ζ(u + iτ)| ≤ e(L + 7)` para `1 − 1/L ≤ u ≤ 2`, `1/2 ≤ |τ| ≤ N` |
| `norm_zeta_sub_le_log` | `|ζ(σ + iτ) − ζ(β + iτ)| ≤ (σ − β)·e(L² + 7L + 13)` (cinco parcelas `parte_a`…`parte_c2`) |
| `regiao_logN` | `|t| ≥ 4`, `ζ(β + it) = 0` ⇒ `β < 1 − 1/(256 K(L)⁴ B(L))`, `K = e(L² + 7L + 13)`, `B = e(L + 7)` |
| **`regiao_log`** | o mesmo com `ℓ = log(3|t|)`: `β < 1 − c(t)`, `c(t) = 1/(256 e⁵ (ℓ² + 7ℓ + 13)⁴ (ℓ + 7))` |
| **`faixa_log`** | todo zero não trivial com `|t| ≥ 4`: `c(t) < Re s < 1 − c(t)` |
| **`faixa_log_simples`** | e `1/(10⁹ ℓ⁹) < Re s < 1 − 1/(10⁹ ℓ⁹)` (`e⁵ < 149` provado em `e_cinco`) |

A prova é a de Mertens/de la Vallée Poussin pela desigualdade 3–4–1, com `x = 1/(256 K⁴ B)`:
`1 ≤ |ζ(1+x)|³ |ζ(1+x+it)|⁴ |ζ(1+x+2it)| ≤ (2/x)³ (2xK)⁴ B = 1/2` se houvesse zero com `β ≥ 1 − x`.

**`ATK/ValleePoussin.lean` (7)** — a lei nova aplicada ao anti-produto de RH:

| teorema | conteúdo |
|---|---|
| **`log_vence_poly`** | para `|t| ≥ 2000`, `c(t)` é **maior** que a largura `1/(256 (9+4|t|)⁴ (3+3|t|))` de `ZetaRegiao` |
| `evita_log` | um zero fora da linha com `|Im ρ| ≥ 4` evita `Re ρ ≤ c(t)` e `Re ρ ≥ 1 − c(t)` |
| **`m_ge_log`** | `m(ρ) ≥ 1/(|ρ|(1/√(2σ − 1) + 1/c(t)))` |
| **`piso_DN_log`** | condensação com piso explícito: `D_N ≥ (1/(|ρ|(1/√(2σ − 1) + 1/c(t))))²` para todo `N` |

## Valores (ponto flutuante, `scripts/valores_vp.py`) — ilustração, não certificação

| t | c_poly(t) (ZetaRegiao) | c_log(t) (regiao_log) | 1/(10⁹ ℓ⁹) | c_log/c_poly |
|---|---|---|---|---|
| 14,1347 (1º zero) | 4,663e-12 | 3,041e-13 | 6,864e-15 | 6,5e-02 |
| 100 | 4,607e-16 | 3,884e-14 | 1,565e-16 | 84 |
| 10³ | 5,036e-21 | 5,581e-15 | 7,397e-18 | 1,1e+06 |
| 10⁶ | 5,086e-36 | 9,006e-17 | 2,739e-20 | 1,8e+19 |
| 10⁹ | 5,086e-51 | 5,377e-18 | 8,912e-22 | 1,1e+33 |
| 10¹² | 5,086e-66 | 6,309e-19 | 7,499e-23 | 1,2e+47 |
| 10²⁰ | 5,086e-106 | 1,121e-20 | 8,682e-25 | 2,2e+85 |

* Cruzamento numérico `c_log = c_poly` em `|t| ≈ 31,29`; o kernel prova o cruzamento a partir de
  `|t| = 2000` (`log_vence_poly`, via `log x ≤ 9·x^{1/9}`). Abaixo de `|t| ≈ 31` a região
  polinomial continua melhor — as duas valem, e `faixa_estreitada` cobre também `1/2 ≤ |t| < 4`.
* Piso de `m(ρ)` junto à borda direita (`σ = 1 − c(t)`): em `t = 10⁶` sobe de `5,1e-42` (região
  polinomial) para `9,0e-23` (logarítmica); em `t = 10¹²`, de `5,1e-78` para `6,3e-31`.
* Para `σ − 1/2 ≥ c(t)²/2` o piso é `≥ c(t)/(2|ρ|)` (`≈ 4,5e-23` em `t = 10⁶`). Abaixo disso o termo
  `1/√(2σ − 1)` domina e o piso vai a `0` quando `σ → 1/2`.

## Leitura correta da "lei de de la Vallée Poussin" no quadro dos estados

* `m(ρ)` é uma **função fixa** de `ρ`; a região não a muda. O que muda é onde um zero fora da linha
  pode estar: `σ < 1 − c(t)` limita o termo `1/(1 − σ)` por `1/c(t)`, e isso dá o piso explícito de
  `m_ge_log`. Nesse sentido o estado `finito` de `D_N` fica "mais caro": uma testemunha a altura `t`
  força `D_N ≥ ≈ (c(t)/2|ρ|)²` em toda a faixa útil.
* O piso **não é uniforme**: decai como `1/(|t| log⁹|t|)` na altura e vai a `0` quando `σ → 1/2`.
  Por isso nenhuma região deste tipo decide entre os estados `zero` e `finito` de `D_N`: isso é RH (O1).
* Potência do log: aqui `9`; a região clássica de de la Vallée Poussin tem potência `1`
  (`σ > 1 − c/log|t|`) e exige a derivada logarítmica `ζ'/ζ` e uma contagem local de zeros
  (próximo alvo formalizável). Regiões de Vinogradov–Korobov (`(log t)^{−2/3}(log log t)^{−1/3}`)
  exigem somas exponenciais. Nenhuma delas chega a uma reta `Re s = a < 1` fixa (quase-RH, aberto).

## Não adotado

O texto colado sugeria um esqueleto com `sorry` (incluindo um `FinalRoot.lean`). Isso violaria o
protocolo (NO_SORRY, NO_ADMIT, NO_NEW_AXIOMS) e não foi feito: cada teorema acima está provado por
completo. O tag `atk-590` foi recusado pelo proxy (403, política); o checkpoint dos 590 é o commit
`cca5d4b`.
