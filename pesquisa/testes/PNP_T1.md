# PNP T1 — Complexidade exata de circuitos no modelo ATK (SAT, CaDiCaL 3.0.1)

**Hipóteses testadas (PNP_frontier §5 T1, Q1).** C_ATK(XORₙ) = 4(n−1) e C_ATK(OUₙ) = n−1. Também se mede C_ATK/C_U2,
C_ATK/C_B2 e a folga sobre `cota_linear`.

**Método.**
- *Modelo.* `ATK.Shannon.Circuito` (ramo `ccr-46709b88-u9mbgb`): portas e/ou/não; `nao` ignora a 2ª entrada. A porta k
  lê fios < n+k; um fio ≥ n+k lê `false` (`getD … false`). A saída é o último fio.
- *CNF própria.* Seletores one-hot A, B sobre os fios anteriores e 'F' (= false), op one-hot, valores v[k][x] para os
  2ⁿ inputs. No modo **fiel**, as referências a fios futuros viram um só 'F' (preserva a satisfatibilidade).
- *Modo sb* (válido para mínimos de f simétrica, não constante, que depende de todas as entradas; provas minhas):
  a<b em ∧/∨ e b=a em ¬; nenhuma leitura de 'F'; toda porta não-saída é lida; funções das portas distintas, não constantes
  e ≠ entradas; portas adjacentes independentes em ordem lexicográfica; a 1ª porta lê x₀ e (x₀ ou x₁).
- *Cota derivada* (só onde marcada †): #¬ ≤ s − C_U2(f), porque absorver as ¬ deixa um circuito U2 de s−#¬ portas.
- *Bases de controle e verificação.* B2 (16 funções, portas normalizadas) e U2 (B2 sem ⊕). Toda solução SAT é
  decodificada e reavaliada por uma transcrição literal de `avalia`.

**Controles (todos passaram).**
1. B2, MOD3ʳₙ: 3, 4, 4 (n = 3) e 7, 7, 6 (n = 4), iguais à tabela de Knuth citada por Kulikov–Pechenev–Slezkin.
2. U2, XORₙ: 3, 6, 9 para n = 2, 3, 4, igual a 3(n−1) (Schnorr).
3. Fiel contra sb, com o mesmo mínimo em 9 casos: OU₂₋₄, XOR₂₋₃, MAJ₃, MOD3ʳ₃.
4. ATK OUₙ = n−1 para n ≤ 6 (conectividade); o circuito canônico de 12 portas para XOR₄ satisfaz a CNF sb.

**Resultados** (exato = UNSAT provado em s−1; tempos de parede numa CPU dividida com o Lean)

| f | n | C_B2 | C_U2 | **C_ATK** | #¬ no ótimo | ATK/U2 | ATK/B2 | `cota_linear` ⌈(n−1)/2⌉ |
|---|---|---|---|---|---|---|---|---|
| OU | 2–6 | n−1 | n−1 | **n−1** | 0 | 1 | 1 | 1–3 |
| XOR | 2 / 3 / 4 | n−1 | 3 / 6 / 9 | **4 / 8 / 12†** | 1 / 2 / 3 | 1.33 | 4 | 1 / 1 / 2 |
| XOR | 5 | 4 | 12 (Schnorr) | [14, 16]‡ | – | – | – | 2 |
| MAJ | 3 | 4 | 4 | **4** | 0 | 1 | 1 | 1 |
| MAJ | 5 | 10? (Knuth, de memória) | [9, 10] | **10** | 0 (monótono) | 1–1.11 | 1? | 2 |
| MOD3⁰/¹/² | 3 | 3 / 4 / 4 | 5 / 6 / 6 | **6 / 7 / 7** | 1 / 1 / 1 | 1.2 / 1.17 / 1.17 | 2 / 1.75 / 1.75 | 1 |
| MOD3⁰/¹/² | 4 | 7 / 7 / 6 | 10 / 10 / 9 | **12 / 12 / 10** | 2 / 1 / 1 | 1.2 / 1.2 / 1.11 | 1.71 / 1.71 / 1.67 | 2 |

**Notas da tabela.**
- † XOR₄ em s = 11: UNSAT em 100 s com #¬ ≤ 2. Sem a cota, s = 10 é UNSAT (77 s), mas s = 11 dá timeout em 600 s.
  s = 12 é SAT (272 s), com 3 blocos (a∨b)∧¬(a∧b).
- ‡ XOR₅: o 14 vem da teoria (Schnorr 12 mais ≥ 2 ¬ por Markov); s = 14 deu timeout em 500 s; o 16 é a cadeia de blocos
  verificada. MAJ₅: s = 9 é UNSAT em 89 s, só com sb. Em U2, s ≤ 8 é UNSAT e s = 9, 10 deram timeout.

**Interpretação.**
- *O que o teste mostra.*
  - **C_ATK(XORₙ) = 4(n−1) para n = 2, 3, 4** (n = 4 usa a cota †), com uma ¬ por bloco.
  - C_ATK(OUₙ) = n−1 para n ≤ 6.
  - Os valores ATK de MAJ₃, MAJ₅, MOD3ʳ₃ e MOD3ʳ₄ são novos (não tabelados). Em MAJ, as ¬ não ajudam.
  - Contra C_U2 + I(f) (I(f) = mínimo de negações de Markov): igualdade em MOD3ʳ₃, MOD3⁰₄ e MOD3²₄; falha em XOR₃
    (8 > 7), XOR₄ (12 > 11) e MOD3¹₄ (12 > 11, com um ótimo de 1 ¬ e miolo U2 de 11 > C_U2).
  - A folga sobre `cota_linear` vai de 2× (OU) a 8× (XOR₃); XOR₄ dá 12 contra 2.
- *O que ele sugere.* 4(n−1) é o alvo certo para `xor_cota`. Os números finitos não provam o caso geral.
- *Limites.*
  - O modo sb e a cota † são argumentos de normalização meus, sem verificação formal (o fiel só cobre n ≤ 3); sem DRAT.
  - n = 5 só fechou para OU₅ e MAJ₅. B2 MOD3⁰₅ (s = 8), U2 MAJ₅ e XOR₅ deram timeout; MOD3ʳ₅ não foi tentado.
  - A soma das sub-execuções passou das 15 min (~70 min de parede; cada chamada ≤ 10 min).

**A seguir.** (1) LRAT das UNSAT (T4) e `encode_sound`. (2) XOR₄ em s = 11 sem a cota † e n = 5 por cube-and-conquer,
quando houver CPU livre. (3) THR²ₙ, TRI₄ e T2 sobre os ótimos de MOD3₄.

Código: `research/tests/code/PNP_T1_{enc,run,one}.py`; resultados em `research/tests/work/PNP_T1_*.jsonl` e `work/pnp_shm/`
(os CNFs foram para /dev/shm porque o disco / encheu com o build do Lean).
