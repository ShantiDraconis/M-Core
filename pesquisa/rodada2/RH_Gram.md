# RH — Gram de Báez-Duarte: entradas exatas, afirmações repassadas, D_N até N = 8000 (2026-10-22)

**Resumo.** A fórmula de Vasyunin com {mh/k} confere com integração direta independente até 4e−44; a variante com h̄ está errada.
Das afirmações repassadas, (i) e (ii) estão erradas e (iii)–(vi) corretas.
D_N foi calculado para todo N ≤ 8000 em double-double (~24 dígitos corretos). Para N ∈ [256, 8000], D_N·log N ∈ [0,04419; 0,04667] = (0,957–1,010)·C₀. Números finitos não provam nada assintótico.

## 0. Código e controles
- **Ambiente:** libquadmath presente (`__float128`); MPFR/GMP só como `.so`, sem headers, e não foi preciso (§3). Python em `code/`: `RH_Gram_verify.py` (mpmath, tarefas 1–2), `_checkG`, `_cmp`, `_analyze`, `_spec`.
- **`code/RH_Gram_dn.cpp`:** Vasyunin + Cholesky incremental (D_N = D_{N−1} − y_N², y = L⁻¹b) em double, long double, dd (Dot2) e binary128; calcula também c* = L⁻ᵀy, o resíduo direto 1 − 2c·b + cᵀGc e E_N de BCF. Tempos (nice 10): dd N = 8000 em 540 s de CPU (~1 GB); binary128 N = 3000 em 312 s.
- **Dados:** `data/RH_Gram_DN.tsv` (N = 1..7999; g_N = D_N − D_{N+1} = y_{N+1}², η_N = g_N/D_N) e `data/RH_Gram_*.out`.
- **Controles (todos passaram):** (a) integração direta (§1); (b) 16 entradas do C contra mpmath, até (4999, 5000): relativo ≤ 1,1e−26; (c) 5 aritméticas e o CSV de 45 dígitos do kernel, código independente (§3); (d) resíduo direto = Cholesky até 5e−28 em N = 8000.
- **Controle (e):** c* tem forma de Möbius. Em N = 5000, c₁..c₇ = −0,984; 0,973; 0,970; 0,048; 0,915; −0,843; 0,879 ≈ −μ(k)w_k.

## 1. Entradas exatas (Vasyunin 1995; Landreau–Richard 2002, Thm 2.1; Bettin–Conrey 2013, eq. 13)
- Para gcd(h,k) = 1: G_hk = ½(log 2π − γ)(1/h + 1/k) + (k−h)/(2hk)·log(h/k) − π/(2hk)·(V(h,k) + V(k,h)), com G_{dh,dk} = G_hk/d e G₁₁ = log 2π − γ.
  - V(h,k) = Σ_{m<k} {mh/k} cot(πm/k) = −c₀(h̄/k) na notação de Bettin–Conrey (conferido em 5 pares).
- **Integração direta:** G = ∫₀^∞ {t/h}{t/k} t⁻² dt, exata por pedaços até X = M·lcm(h,k). Cauda: Σ_n (−1)ⁿ(n+1)·m_n·L^{−n−2}·ζ(n+2, M), com momentos m_n racionais exatos; M = 20 contra M = 40 difere ≤ 2e−43.
- **Resultado em 20 pares** (os pedidos e mais 15), dps 45: máx |Vasyunin − direto| = **4,2e−44**; G₁₁ − (log 2π − γ) = 6e−45; G_{12,18} − G_{2,3}/6 = 2e−47.
  - A variante com h̄ dentro de V erra até 4,9e−2, em (2,7); só coincide quando h² ≡ 1 (mod k).
  - Valores: G(1,1) = 1,26066140150781262295; G(1,2) = 0,77220925599087313986; G(2,3) = 0,44110350927940217633; G(5,7) = 0,18259428458209896471; G(12,18) = 0,07351725154656702939.

## 2. Afirmações repassadas — veredito
| # | afirmação | veredito | números |
|---|---|---|---|
| i | b_k = (1−γ−log k)/k | **ERRADA** (vale só em k = 1) | b₂ direto = 0,5579658 = (log 2 + 1 − γ)/2; a afirmação dá −0,1351814. Com ela, D₂ = −0,1293 < 0, o que é impossível. |
| ii | ‖ρ₁‖² = log 2π − γ − 1 | **ERRADA** | 0,2606614 é só ∫₀¹{1/x}²; falta ∫₁^∞ x⁻² = 1. Correto: log 2π − γ = 1,2606614015. |
| iii | D₁ = 1 − (1−γ)²/(log 2π − γ) | correta | 0,85821205139551088467 |
| iv | B ∈ (0,77218; 0,77229) | correta | B = ¾(log 2π − γ) − ¼log 2 = 0,77220925599087, pois V(1,2) = 0 |
| v | D₁ − D₂ = (Aq − Bp)²/(A(AC − B²)) | correta | 0,56824747765330815286 (= 2×2 direto); D₂ = 0,28996457374220273181 |
| vi | D_256 ≤ 0,00823372 | correta | D_256 = 0,0082337162772610214416; folga 3,72e−9 (4,5e−7 relativo) |

- (vi) concorda em ≥ 28 dígitos entre dd, binary128 e o CSV do kernel, mas **não é certificado intervalar**. É sensível a índice: D_255 = 0,0082338714 > 0,00823372; o `DN 256` do Lean usa ρ₁..ρ₂₅₆, o que bate.

## 3. Precisão necessária
Erro relativo máximo de D_N na faixa (entre parênteses, dígitos perdidos).

| aritmética (u) | N ≤ 300 | N ≤ 1000 | N ≤ 2000 | N ≤ 3000 | referência |
|---|---|---|---|---|---|
| double (1,1e−16) | 7,5e−13 (3,8) | 4,4e−12 (4,6) | | | binary128 |
| long double (5,4e−20) | 7,0e−16 (4,1) | | | | binary128 |
| dd (1,2e−32) | 3,2e−28 (4,4) | 2,6e−27 (5,3) | 8,2e−27 (5,8) | 2,6e−26 (6,3) | binary128 |
| binary128 (9,6e−35) | 1,0e−30 (4,0) | 6,0e−30 (4,8) | 7,2e−30 (≤ 1500) | | CSV 45 díg. |

- **D_N é bem condicionado**, embora a Gram não seja: o menor pivô de Schur é 7,3e−8 (N = 7980), então κ(G) ≳ 1,7e7. Mas δD = c*ᵀδG c* − 2c*ᵀδb, com ‖c*‖² = 13 / 76 / 187 / 431 (N = 100 / 1000 / 3000 / 8000) e max|c_k| ≤ 1,7.
- A perda cresce como ~N^1,8. Double já daria ≥ 10 dígitos até N ~ 10³; com dd, extrapolo ≥ 24 dígitos em N = 8000.

## 4a. D_N·log N contra C₀ = 2 + γ − log 4π = 0,0461914
| N | 100 | 256 | 1000 | 1500 | 2000 | 3000 | 4000 | 5000 | 6000 | 8000 |
|---|---|---|---|---|---|---|---|---|---|---|
| 10³·D_N | 10,18876 | 8,233716 | 6,555964 | 6,244124 | 6,114100 | 5,613104 | 5,415699 | 5,303494 | 5,233272 | 5,069120 |
| D_N log N / C₀ | 1,016 | 0,988 | 0,980 | 0,989 | 1,006 | 0,973 | 0,972 | 0,978 | 0,986 | 0,986 |

- **Média log-uniforme por bloco diádico**, de [32,64) a [4096,8000): 0,0467 / 0,0474 / 0,0467 / 0,0460 / 0,0453 / 0,0458 / 0,0456 / 0,0454. Não há tendência monótona para C₀.
- **Ajustes** (peso 1/n, N ∈ [100, 8000]):
  - F1 com C₀ fixo, D ≈ C₀/(log N + a + b/log N): a = 0,42, b = −2,36; resíduo rms 1,1%, máximo 3,6%.
  - F2 com C livre, 1/D = (log N + β)/C: C = 0,95 C₀.
  - **São instáveis:** em [2000, 8000], F1 dá a = 1,20 e b = −8,9, e F2 dá 0,89 C₀. Com C livre e termo 1/log N, chega a sair C < 0.
- **O resíduo é uma oscilação lenta de ±1,3%.** O periodograma em log N tem pico em período Δlog N ≈ 2,6 (amplitude 5,9e−4). Em γ₁ = 14,13 a amplitude é 1,1e−4, contra mediana 7,9e−5. Com N ≤ 8000 não se extrai C nem a segunda ordem (Q6).
- **Ajuste no estilo de Landreau–Richard** (d_n ≈ a/√log n, n ≤ 8000): a = 0,21412. LR obtiveram 0,21377 com n ≤ 20 000; √C₀ = 0,21492.
- **Polinômio de BCF** c_k = −μ(k)(1 − log k/log N), que é cota superior: E_N log N = 0,822 / 0,562 / 0,513 / 0,489 em N = 100 / 1000 / 2000 / 3000.
  - Isso é C₀ + K/log N com K ≈ 3,55 estável: compatível com BCF, mas com segunda ordem enorme. Em N = 3000, E_N/D_N = 10,9.

## 4b. Eficiência por passo e_N = η_N·N·log N (média 1 se D ~ C/log N)
| faixa | mín | 1% | 10% | mediana | 90% | 99% | máx | média |
|---|---|---|---|---|---|---|---|---|
| [100, 1000] | 4,8e−7 | 9,8e−5 | 0,014 | 0,43 | 3,0 | 7,2 | 9,9 | 1,07 |
| [1000, 7999] | 6,0e−8 | 2,0e−4 | 0,019 | 0,48 | 2,6 | 6,2 | 15,3 | 0,98 |

- **Cauda pesada nos dois lados.** Em cada bloco diádico a partir de 64, 6–10% dos N têm e_N < 0,01 e 21–29% têm e_N < 0,1. O mínimo por bloco **não cresce**: fica entre 6e−8 e 3e−6 de [256,512) em diante.
- **Menores valores:** N = 6098 (N+1 = 3·19·107) 6,0e−8; 5111 (2³·3²·71) 1,4e−7; 316 (317, primo) 4,8e−7; 898 (29·31) 9,2e−7; 1972 (1973, primo) 9,5e−7. Sem padrão aritmético: parecem passagens quase exatas de y_{N+1} por 0.
- **Por tipo de N+1, em [100, 8000)**, mediana / média:

  | primo | livre de quadrados, ω = 2 | ω = 3 | ω = 4 | com fator quadrado |
  |---|---|---|---|---|
  | 0,29 / 0,67 | 0,42 / 0,84 | 0,51 / 1,06 | 0,81 / 1,44 | 0,57 / 1,13 |

  Os máximos (≈ 10–15) estão em N = 2957, 2969, 2963, com N+1 = 2·3·17·29, 2·3³·5·11, 2²·3·13·19.
- **Veredito:** η_N ≥ c/(N log N) só vale em [100, 8000] com c ≤ 6e−8, o que é inútil; sugere, sem provar, liminf e_N = 0.
- Com c > 1 a cota é refutada por Burnol, pois daria D_M ≤ C(log M)^{−c}. Com c ≤ 1 ela é compatível com o piso.

## 4c. Lei polinomial η_N ≥ c/(N+1): prova de que contradiz Burnol, e a numérica
- **Prova.** Suponha η_N ≥ c/(N+1) para todo N ≥ N₀.
  1. Por D_{N+1} = (1−η_N)D_N e 1 − x ≤ e^{−x}: D_M ≤ D_{N₀} exp(−c Σ_{N₀≤N<M} 1/(N+1)).
  2. Como Σ_{j=N₀+1}^{M} 1/j ≥ log((M+1)/(N₀+1)): D_M ≤ D_{N₀}((N₀+1)/(M+1))^c, logo D_M log M → 0.
- **Contradição (incondicional).** span{ρ_k}_{k≤N} ⊂ B_{1/N}, então D_N ≥ D(1/N)², a distância contínua de BBLS/Burnol.
  - Se RH vale: liminf D_N log N ≥ Σ m_ρ²/|ρ|² ≥ Σ m_ρ/|ρ|² = C₀ (identidade de Rosser).
  - Se RH falha: D_N ↛ 0 e D_N log N → ∞.
  - Nos dois casos liminf ≥ C₀ > 0, contra o item 2. ∎
- **Numérica:** mín de f_N = η_N(N+1) em [16, 7999] = 6,9e−9. A média por bloco cai de 0,36 ([16,32)) para 0,10 ([4096,8000)). O expoente efetivo log(D_N/D_M)/log(M/N) por bloco vai de 0,35 a 0,095, contra o previsto pela lei 1/log N, 0,32 → 0,116.
- **Soma:** Σ_{n<N} η_n vai de 3,850 (N = 1000) a 4,107 (N = 8000). O Δ = 0,257 ≈ Δlog log N = 0,263, e não c·Δlog N = 2,08c.
- **Honestidade:** os dados *não* refutam c ≤ 6,9e−9. Só o teorema refuta, e com c tão pequeno o conflito só aparece quando M^c ≫ log M.

## 4d. Razões diádicas D_{2N}/D_N contra log N/log 2N
| N | 64 | 128 | 256 | 512 | 1024 | 2048 | 125 | 500 | 1000 | 2000 | 4000 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D_2N/D_N | 0,849 | 0,852 | 0,897 | 0,884 | 0,935 | 0,884 | 0,851 | 0,884 | 0,933 | 0,886 | 0,936 |
| previsto | 0,857 | 0,875 | 0,889 | 0,900 | 0,909 | 0,917 | 0,874 | 0,900 | 0,909 | 0,916 | 0,923 |

- Observado/previsto fica em [0,965; 1,029] nos N da tabela. Para todo N ∈ [100, 4000], D_{2N}/D_N ≤ 0,946: **os dados finitos são compatíveis com contração q = 0,946**.
- Quem a refuta é o teorema (`sem_contracao_de_piso_log` + Burnol), não a tabela; é a situação de `amostra_finita_nao_decide`.

## 5. Literatura
- **Landreau–Richard** (Exp. Math. 11 (2002) 349–360): d_n até **n = 20 000**, por Gram–Schmidt (conferido até 10⁴ por determinante, gradiente conjugado e QR). Não informam a precisão nem publicam tabela de d_n; dão o ajuste a = 0,21377 (conjectura 3.1).
- **Depois de LR:** não achei cálculo publicado além de 20 000. Bettin–Conrey (2013) e Darses–Hillion (2020) remetem a LR para a numérica.
- **Comparação:** meus valores (N ≤ 8000) dão a = 0,21412, compatível com LR; o kernel (N ≤ 1500) coincide com os meus até 7e−30.
- **Pisos:** BBLS (Adv. Math. 149, 2000) prova liminf ≥ Σ 1/|ρ|², com zeros distintos; Burnol (Adv. Math. 170, 2002) melhora para m_ρ².
- **BCF** (Proc. Steklov Inst., 2013): sob RH e Σ_{|γ|≤T}|ζ′(ρ)|⁻² ≪ T^{3/2−δ}, E_N(V_N) ~ C₀/log N; com Burnol, D_N ~ C₀/log N.

## Interpretação honesta e próximos passos
- **Mostra:** a Gram exata e (iii)–(vi) estão certas, (i)–(ii) erradas; D_N tem ~24 dígitos até 8000; D_256 ≤ 0,00823372 vale com folga 3,7e−9, ainda sem certificado.
- **Sugere:** D_N log N ≈ (0,96–1,01)·C₀ com oscilação lenta; o ganho por passo é errático, com liminf e_N = 0.
- **Não mostra:** nada sobre RH, sobre O1 ou sobre o limite de D_N log N. Zeros fora da reta são invisíveis nessa escala (B2 do mapa).
- **Próximo:** (1) certificar (vi) via `DN_le`: basta Q(c) ≤ 0,00823372 para c racional ≈ c*, com G_ij em aritmética intervalar; a folga de 3,7e−9 é ≫ o erro de 1e−28. (2) Chegar a N = 20 000 para cruzar com LR (double empacotado, 1,6 GB; a perda de ~6 dígitos permite).
- (3) Derivar K ≈ 3,55 em E_N log N = C₀ + K/log N. (4) Estudar a lei de y_{N+1}/√(D_N/(N log N)): densidade positiva em 0 implicaria liminf e_N = 0.
