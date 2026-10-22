# HODGE — parecer independente sobre (P_m^4) para X_m^4 (wave 2, 2026-10-22)

## Veredito
- **Lista combinatória: CONFIRMADA.** Para m ≤ 100, (P_m^4) vale nos m pares {22, 24, 26, 28, 30, 34, 38, 46, 58, 74, 82, 86, 94, 98}
  e falha em {32, 36, 40, 42, 44, 48, 50, 52, 54, 56, 60, 62, 64}, com o mesmo número de órbitas residuais e a mesma dimensão do T1.
  Também confirmados: falha em 25, 35, 55, 65, 85, 95 (1 órbita cada, Aoki 5-standard) e em 33 (1 órbita, (1,4,16,22,25,31));
  vale para todo m ≤ 24 e para 27. **A lista ímpar do enunciado está incompleta:** (P) também falha em 39 (2 tsplit), 45 (2),
  75 (2 std5) e 99 (inflação da classe de 33).
- **Consequência "HC nova para X_m^4": NÃO.** Os 14 m pares já estão cobertos pela literatura: 2p e 2·7² por Aoki; 24, 28 e 30
  por Aoki 2000 (Thm 0.1(i)) e por Miranda–Movasati–Rufino–Villaflor 2026; todos por Kang 2016 (alegado). O cálculo dá
  só uma **prova alternativa elementar** (Shioda 1979 + conta finita) para esses m.

## (a) Definições exatas usadas
Fontes: da Silva 2101.04739, Def. 2.4 e §2 (PDF/ar5iv), que reenuncia Shioda (Math. Ann. 245, 1979); Jumagulov 2608.18134 cita igual.
**Não li Shioda 1979 nem Aoki 1987/2000 no original** (curl ao arXiv, J-STAGE e Project Euclid bloqueados).
- **M_m.** Semigrupo dos x = (x_1..x_{m−1}; y), x_i ≥ 0 e y > 0, com Σ_i ⟨t·i⟩ x_i = m·y para todo t ∈ (ℤ/m)^×.
  M_m(y) é a parte de grau y. Um caractere a = (a_0..a_5) ∈ B_m^4 corresponde a x_k = #{i : a_i = k} com y = 3.
  Somando as equações de t e −t vem #entradas = 2y. Logo M_m(1) = {pares {β, −β}}, o que conferi por força bruta para m ≤ 64.
- **Decomponível.** a = c + d com c, d ∈ M_m; em grau 3, "a contém um par {b,−b}". É **diferente** do D_m^n de MMRV (pareamento
  total = ciclos lineares) e do "tsplit" (duas triplas de soma 0, que **não** estão em M_m).
- **Quase-decomponível.** a + b = c + d com **b ∈ M_m(1)** e c, d ∈ M_m, {c,d} ≠ {a,b}. O PDF de da Silva tem o erro tipográfico
  "a ∈ M_m(1)"; a citação de Jumagulov traz b. Para a indecomponível em grau 3, isso força c, d ∈ M_m(2) com β ∈ c e −β ∈ d.
  Ou seja, a = T ⊔ T′ (3+3), c = T ∪ {−ΣT} e d = T′ ∪ {ΣT}, com ΣT ≢ 0. A dimensão sobe de 4 para 6 (a + b ∈ B_m^6) e o
  resultado parte em **dois caracteres de superfície de Fermat** (B_m^2).
- **(P_m^n).** Todo indecomponível de M_m(y), 3 ≤ y ≤ n/2 + 1, é quase-decomponível (n = 4: só y = 3). Thm 2.5 (Shioda): (P_m^n) ⇒
  HC(X_m^n). O código SAGE de da Silva **filtra os standard** antes: checa "(P) módulo standard", mais fraco que (P_m^n).
- **Aoki standard** (MMRV Def. 3.7; Jumagulov Prop. 1.9). Para d = pk com k ≥ 3: s_{p,i} = (i, i+k, …, i+(p−1)k, −p·i).
  Grau (p+1)/2, válido se k ∤ i. Em X^4 só existe p = 5 (5 | m); p = 7 dá octuplas (X^6).

## (b) Implementação independente e controles
- **Código.** `wave2/code/HODGE_ref_census.c`, sem ler o HODGE_T1*. Enumera multiconjuntos com Σ = 3m, testa Σ⟨ta_i⟩ = 3m
  para t ∈ (ℤ/m)^×, t ≤ m/2, e toma o mínimo lexicográfico da órbita como representante. Os testes literais de decomponível e
  quase-decomponível (subconjuntos de a e de a ⊎ {β,−β}) batem com os atalhos em todo m ≤ 150. Tempo: 7 s até 100, ~3 min de 101 a 150.
- **Segunda implementação** (`HODGE_ref_brute.py`, vetores x de Shioda, M_m(1) por força bruta): contagens idênticas em
  m = 3..16, 21, 25, 32, 33, todos os pares de 22 a 64 e 74, 82, 86, 94, 98.

| Controle | Esperado (fonte) | Obtido |
|---|---|---|
| dim Hdg²_prim, m = 3, 4, 6 (φ = 2: todo H^{2,2}) | h^{2,2} − 1 = 20, 141, 1751 | 20, 141, 1751 ✓ |
| AMV 1711.02628 Tab. 1: m = 5 posto de Hodge 401; m = 6 posto linear 1002 | 400 prim.; 1001 pareáveis | 400; 1001 ✓ |
| Aoki 1983 Thm 3.1: B = D ⇔ m = 4, m primo ou mdc(m, 720) = 1 | 98 valores de m | 0 violações (m ≤ 100) ✓ |
| Picard de superfícies: ρ(X_4^2) = 20, ρ(X_5^2) = 37, ρ(X_6^2) = 86; 3(m−1)(m−2)+1 se mdc(m,6) = 1 | idem | ✓ (m ≤ 13) |
| m ≤ 20 (Shioda), 21 e 27 (da Silva): R = ∅ | ∅ | ∅ ✓ |
| Jumagulov órb/D/QD: 33 → 104/102/1, 39 → 140/137/1, 45 → 245/237/6, 99 → 825/822/2, 105 → 1286/1276/6, 117 → 1117/1113/2, 135 → 1767/1756/8 | idem | idem ✓ |
| Certificado de Jumagulov em 33→66: a=2w, +{1,65}{25,41} = qdec6(2,8,32,41,50,65)+(1,25,44,62) | achado | achado igual ✓ |

**Resultados, m pares com R_m = ∅** (dim = dim Hdg²_prim; orb = órbitas; D/QD = decomponíveis/quase):

| m | dim | orb | D | QD |   | m | dim | orb | D | QD |
|---|---|---|---|---|---|---|---|---|---|---|
| 22 | 277101 | 86 | 80 | 6 | | 46 | 2098581 | 268 | 256 | 12 |
| 24 | 745211 | 355 | 291 | 64 | | 58 | 3981321 | 396 | 381 | 15 |
| 26 | 439081 | 112 | 105 | 7 | | 74 | 7849081 | 604 | 585 | 19 |
| 28 | 644121 | 209 | 188 | 21 | | 82 | 10468401 | 722 | 701 | 21 |
| 30 | 2106431 | 650 | 503 | 147 | | 86 | 11969581 | 786 | 764 | 22 |
| 34 | 909921 | 166 | 157 | 9 | | 94 | 15383781 | 920 | 896 | 24 |
| 38 | 1241821 | 198 | 188 | 10 | | 98 | 17429701 | 1182 | 1148 | 34 |

- **m pares com falha** (R, dimR) são idênticos ao T1: 32 (1, 2880), 36 (9, 69120), 40 (1), 42 (1), 44 (1), 48 (12), 50 (4, 34560),
  52 (1), 54 (20), 56 (7, 51840), 60 (9), 62 (1), 64 (2).
- **Extensão 102..150.** R = ∅ só para os pares 2p: 106, 118, 122, 134, 142, 146. Como 62 = 2·31 falha, "2p ⇒ (P)" não vale sempre.

## (c) Estado da literatura por m (todas as m da lista "vale")
- **Aoki (2p, 2p^e).** MMRV (2609.27301) atribui a Aoki [Aok87] "d potência de primo ou duas vezes potência de primo".
  Jumagulov cita literalmente Aoki 2000 (Comment. Math. Univ. St. Pauli 49), Thm 0.1, que dá HC para toda abeliana de tipo Fermat,
  e para todo X_m^n, se (i) m = 2^a3^b5^c7^d com c = 0 ou d = 0, ou (ii) m = p^e ou 2p^e (p ímpar). Só por citação secundária.
- **MMRV 2026, Thm 1.1.** HC para X_d^n, todo n, d < 65, d ∉ {44, 51, 52}. O caso n = 4 usa Kang.
- **Kang 2016.** Bull. Aust. Math. Soc. 93, 223–230, Cor. 3.2: GHC, logo HC, para X_m^4 com **todo** m.
  MMRV aceita. da Silva 2021, o survey 2105.04695, Favero–Kelly 2026 e Jumagulov 2026 **não citam**. Pelo que li (resumo do PDF),
  a prova usa uma desigualdade de subaditividade µ_1(X^1×X^{n−1}) ≤ max(…) importada de outro trabalho. Para n = 4 isso já
  equivale a GHC de coniveau 1 em X^1×X^3, o que não é elementar. **Status: alegado, não verificado.**
- **Fora de alcance:** Shioda/Ran (m primo, 4, ≤ 20), da Silva (mdc(m,6) = 1, 21, 27), Jumagulov (ímpar ≤ 199).

| m | Fatoração | Já conhecido por | Decisão |
|---|---|---|---|
| 22, 26, 34, 38, 46, 58 | 2p | Aoki (2p); MMRV d < 65; Kang | conhecido |
| 74, 82, 86, 94 | 2p | Aoki (2p); Kang | conhecido |
| 98 | 2·7² | Aoki (2p^e); Kang | conhecido |
| 24, 28, 30 | 2³·3, 2²·7, 2·3·5 | Aoki 2000 (i); MMRV d < 65; Kang | conhecido |
| todos acima | — | (P_m^4) + Shioda 1979 Thm 2.5 | segue do conhecido + conta finita (prova alternativa) |

- **Estrutura indutiva.** Para m = 2p^e e para o caso (i), nenhum q ∈ Q (produtos de um número par de elementos distintos de
  {4} ∪ {primos ≥ 3}) divide m, salvo os q de Aoki 2000 (12, 15, 20, 21, 28). A redução de grau de Aoki (Shioda–Katsura +
  módulo formal) leva tudo a lineares e standard. Também os m "que falham" estão cobertos por Aoki 2000: 32, 36, 40, 42, 48,
  50, 54, 56, 60, 62, 64. Entre os pares 22..64, **só 44 e 52** ficam fora de Aoki 2000 (e entram em MMRV via Kang).

## (d) Órbitas residuais em m = 50 e 56
- **Certificado de pares.** a ⊎ p_1 ⊎ … ⊎ p_k = ⊎ blocos algébricos conhecidos. Os blocos permitidos são: par; quádrupla de
  grau 2 (Lefschetz); sêxtupla std5, tsplit ou quase-decomponível; octupla std7. O lema por trás é o de Shioda iterado
  (join + remoção de par), que é o Thm 1.3/1.4 de Jumagulov, cuja prova impressa está truncada.
  Código: `HODGE_ref_closure.c`; os 261 certificados foram reverificados em Python puro (`HODGE_ref_verify.py`), 0 falhas.
- **m = 50** (4 órbitas). (1,11,21,31,41,45) = s_{5,1} e (2,12,22,32,40,42) = s_{5,2}: **standard**. (1,13,22,32,40,42): não
  standard, fecha com 2 pares: +{2,48}{12,38} = (1,13,38,48) + s_{5,2}. (1,7,27,30,41,44): não standard; não fecha com ≤ 3 pares
  nem levantada a 2m..7m com ≤ 2 pares; fecha com **4 pares**: +{4,46}{14,36}{16,34}{24,26} = (1,26,27,46)+(7,16,36,41)+s_{5,4}.
- **m = 56.** **Nenhuma** das sete é standard (5 ∤ 56), e nenhuma é a ⊎ par = s_{7,i}. **Todas fecham com 2 pares**
  (sêxtupla qdec + quádrupla; blocos em `code/HODGE_ref_out/closure_56.txt`): (1,9,29,37,42,50) e (1,10,29,36,42,50) +{2,54}{18,38};
  (1,15,29,32,43,48) e (1,15,29,36,43,44) +{2,54}{4,52}; (1,18,21,29,49,50) +{2,54}{14,42}; (1,18,29,34,42,44) +{2,54}{6,50};
  (2,10,21,34,49,52) +{14,42}{26,30}.
- **Censo de certificados, m ≤ 100.** Das 284 órbitas residuais, só três ficam sem certificado (k ≤ 4 pares em λ = 1, k ≤ 3 em
  λ = 2, k ≤ 2 em λ = 3): (1,7,19,36,49,50) em m = 54 e (1,23,38,55,74,79) em m = 90, ambos cobertos por Aoki 2000, e
  **(1,20,24,42,61,62) em m = 70 = 2·5·7, sem Aoki nem certificado** — bate com a "parede W_70" de Jumagulov (App. D).

## O que é plausivelmente novo, e o que faltaria para publicar
1. **A lista em si não é publicável como "HC nova".** Todos os 14 m já são conhecidos. No máximo vale como observação:
   HC(X_m^4) para esses m sai só de Shioda 1979 + conta finita, sem Aoki e sem Kang.
2. **Família uniforme "prog4", talvez nova.** Para m = 4q, a_q = {1, 1+q, 1+2q, 1+3q, 2q+4, 4q−8} é residual para q = 8, 11–14,
   16–20 e 22–60. Fecha com o certificado uniforme a_q + {2,−2} + {4,−4} = {1, 4, 2q+1, 2q+4, 4q−8, 4q−2} (qdec) +
   {2, q+1, 3q+1, 4q−4}, verificado para 5 ≤ q ≤ 60, q ≠ 4 (`HODGE_ref_family.py`). Isso fecha as únicas residuais de 44, 52,
   68, 76 e 92, e todas as de 66, 78 e 88 fecham com ≤ 3 pares. Daria HC(X_m^4) para m ∈ {44, 52, 66, 68, 76, 78, 88, 92}
   **sem Kang**.
3. **Para publicar o item 2:** prova escrita do lema de pares múltiplos (correspondências algébricas inversas no join de
   Shioda–Katsura); prova simbólica da família para todo q; decidir Kang 2016 (achar a lacuna ou admitir que X_m^4 já está
   resolvido); comparar com o companheiro [5] de Jumagulov (censo par até 250, não visto); ler Shioda 1979 e Aoki 1987/2000.
4. **O alvo realmente aberto (fora Kang) é m = 70.** A classe (1,20,24,42,61,62) pede ciclos novos (Favero–Kelly) ou o cálculo de
   Aoki com ξ_35.

**Arquivos** em `research/wave2/code/`: HODGE_ref_{census,closure}.c e HODGE_ref_{brute,verify,surface,family}.py.
Saídas em `code/HODGE_ref_out/` (census_3_100.txt com as órbitas, census_101_150.txt, closure_*.txt, brute_*.txt).
