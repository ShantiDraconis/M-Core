# As conjecturas no `s` de Riemann: taxonomia e parâmetros conjuntos (09/11/2026)

Documento de fronteira. **Nenhum teorema novo** e nada vai para o kernel: as equivalências abaixo são clássicas
ou elementares. Serve de mapa do que de fato compartilha a infraestrutura de `ζ` (produto de Euler, equação
funcional, centro em `s = ½`) e do que só compartilha o formato de um enunciado. RH, GRH, BSD, Tate, Hodge,
YM, NS, P vs NP e Beal continuam OPEN_MATH; Poincaré é teorema (Perelman).

Números conferidos em `codigo/conjecturas_em_s.py` (só biblioteca padrão; saída em `codigo/conjecturas_em_s.json`).

## 0. Convenção

Toda função `L` vai para a **normalização analítica**: `Λ(s) = γ(s) L(s)` com `γ(s) = q^{s/2} ∏_{j=1}^{d} Γ_ℝ(s + μ_j)`,
`Γ_ℝ(s) = π^{−s/2} Γ(s/2)`, `Γ_ℂ(s) = Γ_ℝ(s) Γ_ℝ(s + 1)`, e `Λ(s) = ε · Λ̄(1 − s)`. Então a faixa crítica é
`0 < Re s < 1`, o **centro** é `s = ½` e o eventual **polo** fica em `s = 1`, como em `ζ`.

## 1. O que se junta de verdade: o monoide das funções `L`

Cada `F` carrega o vetor de parâmetros

  `P(F) = (d, q, μ, ε, m, r, Θ)`:

grau `d`, condutor `q`, deslocamentos `μ = (μ_1, …, μ_d)`, sinal `ε` (`|ε| = 1`), ordem do polo em `s = 1` (`m`),
ordem do zero em `s = ½` (`r`) e `Θ(F) = sup{Re ρ : F(ρ) = 0, 0 < Re ρ < 1}`.

**Regra do produto** (elementar): `P(FG) = (d_F + d_G, q_F q_G, μ_F ∪ μ_G, ε_F ε_G, m_F + m_G, r_F + r_G, max(Θ_F, Θ_G))`.
Os zeros não triviais do produto são a união, então `Θ` é o máximo.

**Paridade** (teorema, para `F` autodual com `ε = ±1`): de `Λ(½ + u) = ε Λ(½ − u)` sai `ε = (−1)^r`.

| `F` | `d` | `q` | `μ` | `ε` | `m` | `r` |
|---|---|---|---|---|---|---|
| `ζ(s)` | 1 | 1 | `(0)` | `1` | 1 | 0 (`ζ(½) = −1,4603545…`) |
| `L(s, χ)`, `χ` primitivo mod `q` | 1 | `q` | `(a)`, `a = (1 − χ(−1))/2` | `τ(χ)/(i^a √q)` | 0 | — |
| `ζ_K(s)`, `[K : ℚ] = n` | `n` | `\|D_K\|` | `0^{r₁+r₂}, 1^{r₂}` | 1 | 1 | pode ser `> 0` (Armitage 1972) |
| `L*(E, s) = L(E, s + ½)` | 2 | `N_E` | `(½, 3/2)` | `w_E` | 0 | `r_an(E)` |
| `L*(f, s)`, nova de peso `k`, nível `N` | 2 | `N` | `((k−1)/2, (k+1)/2)` | `±1` | 0 | — |
| `L*(H^w(X), s) = L(H^w(X), s + w/2)` | `b_w` | condutor de `X` | dado pelos `h^{p,q}` e, em `H^{p,p}`, por `h^{p,±}` (ação de `F_∞`; Serre 1970) | — | Tate (abaixo) | — |

As conjecturas como enunciados sobre `P(F)`:

* **RH**: `Θ(ζ) = ½`. **GRH**: `Θ(F) = ½` para toda `F`. Para uma família finita, **GRH para todas ⟺ `Θ(∏F_i) = ½`**:
  a junção é uma equivalência.
  Na distância de Báez-Duarte, a rodada 110 (`ZeroClasses/BDMonoide.lean`, `juncao`) certifica a direção do teto: a taxa
  `κ` de `D_N^{∏F_i}(σ)` dá `F_i ≠ 0` em `Re s > σ − κ/2` para todos os fatores (incondicional para `ζ`; para `L(s, χ)`, sob
  a hipótese de reta boa).
* **BSD**: `r(L*(E)) = rank E(ℚ)` e `L*^{(r)}(E, ½)/r! = Ω_E Reg_E #Ш ∏ c_p / (#E(ℚ)_tors)²`. Juntar curvas só dá a
  soma: `r(∏ L*(E_i)) = Σ rank E_i(ℚ)` é **mais fraco** que BSD para cada uma.
* **Tate** (a forma aritmética de Hodge): `−ord_{s=1} L*(H^{2p}(X), s)` = posto dos ciclos algébricos de codimensão `p`
  sobre o corpo de definição. Para `X` = ponto (`p = 0`) é o polo simples de `ζ_K` em `s = 1`.
* **Hodge** sobre `ℂ` não tem função `L`. Para `X` definida sobre um corpo de números, a única entrada da teoria de Hodge
  no monoide é o fator `Γ` de `L(H^w(X), s)`. Ele é fixado pelos números `h^{p,q}` e, em peso par, pela decomposição
  `h^{p,p} = h^{p,+} + h^{p,−}` sob a conjugação complexa `F_∞` (Serre 1970); os `h^{p,q}` sozinhos não bastam. Exemplo:
  corpos quadráticos reais e imaginários têm ambos `h^{0,0} = 2`, com fatores `Γ_ℝ(s)²` e `Γ_ℝ(s)Γ_ℝ(s+1)`.
  Hodge é teorema para `p = 1` (Lefschetz (1,1)). Para divisores de variedades abelianas sobre corpos de números, Faltings
  (1983) prova a forma **cohomológica** de Tate (as classes invariantes por Galois são algébricas); a forma com polo acima
  exige ainda a continuação analítica e a ordem do polo de `L`, que não seguem disso. Hodge e Tate não são equivalentes.
* **Beal** entra pelo **condutor**. No método modular, a curva de Frey de uma solução tem condutor dado pelo radical de
  `abc` (a menos da parte em 2); para FLT (`p ≥ 5`) o rebaixamento de nível leva a uma forma nova de nível 2, e
  `S₂(Γ₀(2)) = 0`. Fora dos casos de assinatura resolvidos (Darmon–Merel `(p, p, 2)`, `(p, p, 3)`), não há enunciado
  único em `s`.

### Exemplo conferido: `Z = ζ · L*(11a1) · L*(37a1)`

| | `11a1` (`y² + y = x³ − x² − 10x − 20`) | `37a1` (`y² + y = x³ − x`) | `Z` |
|---|---|---|---|
| `d`, `q` | 2, 11 | 2, 37 | 5, 407 |
| `ε` | `+1` (`a₁₁ = 1`) | `−1` (`a₃₇ = −1`) | `−1` |
| `r` | 0 | 1 | 1 |
| valor central | `L(E, 1) = 0,25384186085591` | `L′(E, 1) = 0,30599977383405` | — |
| `Ω_E` | `1,26920930428` (1 componente real) | `5,98691729246` (2 componentes) | — |
| BSD | `L/Ω = 0,2 = 1 · 5/5²` (`c₁₁ = 5`, `#tors = 5`) | `L′/Ω = 0,05111140824 = Reg` | — |

`ε(Z) = (−1)^{r(Z)} = −1` confere a paridade. **RH ∧ GRH(11a1) ∧ GRH(37a1) ⟺ `Θ(Z) = ½`**; BSD para as duas curvas
não se reduz a uma afirmação sobre `Z`.

## 2. Mesmo formato, fora do monoide: parâmetros de abscissa

Aqui a conjectura diz que uma **abscissa** (a borda de um semiplano de analiticidade ou de convergência) tem um certo
valor. RH também é desse tipo, e é o único caso nas duas famílias.

| Conjectura | Função de `s` | Abscissa | Valor conjecturado | Kernel |
|---|---|---|---|---|
| RH | `1/ζ(s)`; `D_N(σ)` | `Θ`; `κ(σ) = 2(σ − Θ)` | `Θ = ½` | `BDTheta.rh_iff_Teta`; `BDPisoExato.kappa_exato`, `rh_iff_taxa_um` (#186) |
| RH (gás de primos) | `Tr (−1)^F e^{−sH} = Σ μ(n) n^{−s} = 1/ζ(s)` | continuação de `1/ζ` | até `Re s > ½` | `Fracoes.FermionsRH.rh_iff_continuaAte` |
| YM | `Ĉ(s) = ∫₀^∞ e^{st} C(t) dt` (correlação conexa) | `Δ` (analítica em `Re s < Δ`) | `Δ > 0`, uniforme no volume | toy: `Fracoes.Primons.lacuna_primons` (`Δ = log 2`) |
| P vs NP | `D_A(s) = Σ T_A(n) n^{−s}` | `Θ_P = inf_A σ_c(D_A)` | `P = NP ⟺ Θ_P < ∞` | `Conditional.PvsNP.pneNP_iff_sat_not_in_P`, `CookLevinNP.cookLevin` |
| ETH (mais forte que P ≠ NP) | `Σ_v T_A(v) e^{−sv}` | `c₃ = inf{c : 3-SAT em 2^{cv}}` | `c₃ > 0` | `Fracoes.SAT.schoening` (`c₃ ≤ log₂(4/3)`) |
| NS | índice de Sobolev `s` (real) | `s_c = d/2 − 1` | `‖u(t)‖_{Ḣ^{1/2}}` limitada em todo `[0, T]` | — |

Notas:

* **YM e o produto de Euler.** Sistemas independentes têm `Z_{A⊗B} = Z_A Z_B` e lacuna `min(Δ_A, Δ_B)`. O produto de Euler
  `ζ(s) = ∏_p (1 − p^{−s})^{−1}` é exatamente esse produto tensorial de osciladores de frequência `log p` (o gás de primos
  de Julia–Spector), com lacuna `log 2`. É o único ponto em que a linguagem de YM e a de RH usam literalmente o mesmo `s`
  (`s` = tempo euclidiano `β`). A teoria de Yang–Mills em `ℝ⁴` não é um produto desses, e a existência dela faz parte do
  problema.
* **P vs NP.** `A` é polinomial `⟺ σ_c(D_A) < ∞` (coeficientes `≥ 0`: `T_A ≤ Cn^k` dá convergência em `Re s > k + 1`;
  convergência em `σ₀` dá `T_A(n) ≤ C n^{σ₀}`). Os coeficientes não são multiplicativos, não há equação funcional, e
  reduções compõem expoentes **multiplicativamente** (`κ(B∘R) ≤ max(r, r·κ(B))` para uma redução de expoente `r`): nenhuma ferramenta da `ζ` se aplica, e o
  argumento relativiza (Baker–Gill–Solovay 1975).
* **NS.** Escala `u_λ(t, x) = λ u(λ²t, λx)`: `‖u_λ(0)‖_{Ḣ^s} = λ^{s − ½}‖u(0)‖_{Ḣ^s}`. Cadeia crítica em `ℝ³`:
  `Ḣ^{1/2} ⊂ L³ ⊂ Ḃ^{−1+3/p}_{p,∞} ⊂ BMO^{−1}` (Koch–Tataru 2001: dados pequenos em `BMO^{−1}` dão solução global).
  Limitação em `Ḣ^{1/2}` impede explosão (Kenig–Koch 2011); em `L³`, Escauriaza–Seregin–Šverák (2003). Se há explosão
  em `T*`, `‖u(t)‖_{Ḣ^s} ≥ c_s (T* − t)^{−(2s−1)/4}` para `s > ½` (Leray). O `½` vem da dimensão (`s_c = d/2 − 1`:
  0, ½, 1 em `d = 2, 3, 4`), sem mapa para o `½` de `ζ`.

## 3. Beal: o parâmetro `χ(x, y, z)`

Para `A^x + B^y = C^z` primitiva, o parâmetro natural é `χ = 1/x + 1/y + 1/z − 1` (característica da orbifold):

| `(x, y, z)` | `(3, 3, 3)` | `(3, 3, 4)` | `(3, 3, 5)` | `(3, 4, 4)` | `(3, 3, 6)` | `(4, 4, 4)` |
|---|---|---|---|---|---|---|
| `χ` | `0` | `−1/12` | `−2/15` | `−1/6` | `−1/6` | `−1/4` |

Com `x, y, z ≥ 3`, `χ ≤ 0`, e `χ = 0` só em `(3, 3, 3)` (Euler: sem solução). Para `χ < 0` e assinatura fixa há
finitas soluções primitivas (Darmon–Granville 1995). A conjectura de Fermat–Catalan (finitas soluções com `χ < 0` no
total) segue de `abc`; as 10 conhecidas têm todas um expoente 2, logo nenhuma contradiz Beal. `χ` não entra no monoide:
o elo com funções `L` é o condutor da curva de Frey (§1).

## 4. O que não se junta

* **Hodge sobre `ℂ`**, além da estrutura de Hodge real (`h^{p,q}`, `h^{p,±}`) no fator `Γ`.
* **Poincaré** (teorema). A `ζ` espectral do Laplaciano tem abscissa `d/2` (Weyl), que só vê a dimensão; o espectro não
  determina a topologia (Vignéras 1980).
* **P vs NP e NS** com qualquer função `L`: não há produto de Euler, fatoração única nem simetria espectral; a letra `s`
  é a mesma, a infraestrutura não.

## 5. Tabela-mestra

| Problema | Variável | Parâmetro que decide | Enunciado | Família |
|---|---|---|---|---|
| RH | `s` de Riemann | `Θ(ζ)` | `Θ = ½` | monoide `L` e abscissa |
| GRH | `s` de Riemann | `Θ(F)` | `Θ = ½` (junta por produto) | monoide `L` |
| BSD | `s` de Riemann | `r`, coeficiente líder | `r = rank`, fórmula de BSD | monoide `L` |
| Tate / Hodge aritmético | `s` de Riemann | `m` em `s = 1` | `m` = posto dos ciclos | monoide `L` |
| Hodge (`ℂ`) | — | `h^{p,q}`, `h^{p,±}` (só no fator `Γ`) | `Hdg^p` gerado por ciclos | nenhuma |
| Beal | — | `χ(x, y, z)`; condutor de Frey | sem solução primitiva com `χ ≤ 0` | condutor ⟶ monoide |
| YM | tempo euclidiano `β = s` | `Δ` | `Δ > 0` | abscissa |
| P vs NP | `s` de Dirichlet | `Θ_P` | `Θ_P < ∞ ⟺ P = NP` | abscissa (elementar) |
| NS | Sobolev `s` | `s_c = ½` | `Ḣ^{1/2}` limitada | coincidência dimensional |
| Poincaré | — | — | teorema | — |

## Fontes

* J.-P. Serre, *Facteurs locaux des fonctions zêta des variétés algébriques*, Sém. Delange–Pisot–Poitou (1969/70).
* J. Tate, *Algebraic cycles and poles of zeta functions* (1965).
* J. V. Armitage, *Zeta functions with a zero at s = ½*, Invent. Math. 15 (1972).
* H. Darmon, A. Granville, *On the equations z^m = F(x, y) and Ax^p + By^q = Cz^r*, Bull. LMS 27 (1995).
* T. Baker, J. Gill, R. Solovay, *Relativizations of the P =? NP question*, SIAM J. Comput. 4 (1975).
* C. Kenig, G. Koch, *An alternative approach to regularity for the Navier–Stokes equations in critical spaces*,
  Ann. IHP (C) 28 (2011); L. Escauriaza, G. Seregin, V. Šverák, Russ. Math. Surveys 58 (2003); H. Koch, D. Tataru,
  Adv. Math. 157 (2001).
* J. E. Cremona, *Algorithms for Modular Elliptic Curves* (tabelas de `11a1`, `37a1`).
