# ATK — valores calculados e pendências isoladas (2026-10-12)

Origem: `atk-kernel/PARAMETROS_72.md`. Este complemento preserva o mapa de 72 entradas. Números reportados nas execuções dos repositórios; não são provas universais.

## Riemann: valores concretos que substituem o modelo 2×2
| ID | Nome | Valor |
|---|---|---|
| 1 | Gram2_det | 0.198326449587843 |
| 2 | Gram2_eigen_min | 0.111447891180725 |
| 3 | Gram2_eigen_max | 1.77954421108099 |
| 4 | Gram2_condition | 15.9675000776396 |
| 5 | DN2 | 0.289964573742203 |
| 6 | DN3 | 0.0938372284969833 |
| 7 | DN_step | 0.1961273452452197 |
| 8 | DN_ratio | 0.3236161827838 |
| 9 | DN_relative_reduction | 0.6763838172162 |
| 10 | K_star | >= 0.942842305946176, observado N<=1500; finitude ABERTA |
| 45 | DN_concrete | D1..D1500: `m-core-riemann/atk-kernel/numerics/dn_N1500_prec45.csv` |
| 46 | Schur_increment | D(N-1)-D(N)>0 observado N<=1500; monotonia estrutural |
| 47 | Schur_completeness | ABERTO: D_N->0 para distância concreta |
| 48 | uniform_log_rate | ABERTO: sup_N D_N log(N+2)<infinito |

**Auditoria de tipagem:** `m-core-riemann/lean/MCore/Material/Closure.lean` define `ConcreteUniformLogDNBound (DN : Nat → Real)` para DN arbitrário. Exige especialização à distância de Báez-Duarte antes de usar o endpoint para RH.

## Navier–Stokes
- 11–14: Young p=4/3, q=4, coeficientes 27/32 e 27/16 (identidades exatas no contexto da derivação).
- 15: delta de modelo = 5/12; não é constante universal.
- 16–18,20–21: stretch/(νz) máximo reportado = 2.776 (Re100), 5.672 (Re200), 11.458 (Re400). Esses valores **não são** valores individuais de cB* ou cT*; exigem decomposição B/T.
- 19: C_min de Taylor–Green (θ=0.7): 0.000548 / 0.000642 / 0.000688; apenas para os casos calculados.
- 49–53: ABERTOS os casos de denominador zero, orçamento com resto e controle integral.

## Yang–Mills
- 22–33: correlator de referência f(t)=3 exp(-2t)+exp(-5t); f(0)=4, integral de 0 a infinito=17/10, gap do modelo=2; **não** gap físico.
- 34,54–57: ABERTOS operador físico, transporte, sobrejetividade, controle contínuo e gap físico.

## BSD
- 35: Reg(389a1)=0.152460177943144 (caso específico).
- 36: altura canônica reportada de 37a1=0.0511114082399688 (caso específico).
- 37,58: coincidência numérica dos postos em 10 curvas, não teorema universal.
- 38,59: ordem de torção >=1 por conter identidade; conexão ao tipo Lean concreto pendente.
- 39,60: Sha inferido pela fórmula nas 10 curvas: 1,4,9,25; identidade universal ABERTA.

## Hodge
- 40: A invertível implica solução única q=A^-1 b; não garante ciclo algébrico.
- 61–63: ABERTOS realize, algebraicity_proof, gluing_proof.

## Beal
- 41: gcd dos expoentes <=2 apenas sob hipótese de Fermat explicitada no arquivo Lean.
- 42,64–67: ABERTOS exclusão de contraexemplo primitivo, medida, transformação, descida e preservação.

## P ≠ NP
- 43: grau de composição limitado por d*k sob hipóteses polinomiais.
- 44,68–72: ABERTOS limite inferior geral, máquina/aceitação concretas e provas de tempo/semântica.

## Os 24 prioritários — separação rigorosa
- RH: 10,47,48.
- NS: 19,20,21,52.
- YM: 54,55,56,57.
- BSD: 58,59,60. O 59 possui prova matemática elementar, não foi certificado aqui no Lean concreto.
- Hodge: 61,62,63.
- Beal: 64,65,66,67.
- P ≠ NP: 44,71,72.

Total: 24. **Nenhum produtor terminal novo fechado**. `OPEN_MATH=true`.
