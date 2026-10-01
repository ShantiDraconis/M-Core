# EXPANSÃO DA MATEMÁTICA MATERIAL — 2026-10-01

Status: PRODUCER-FIRST / FORWARD-ONLY / NO-SCAFFOLD-ESCAPE

Este documento consolida a matemática nova que surge ao comprimir as sete lanes até seus produtores materiais reais. Ele distingue:
- leis e operadores já formalizados;
- reduções exatas;
- rotas falsificadas;
- evidência externa;
- resíduos OPEN_MATH que ainda exigem matemática genuína.

Nenhuma equivalência ou wrapper é promovido a prova de um endpoint aberto.

---

## 1. Estrutura universal da matemática nova

Cada lane tem a forma

TYPE(E)
→ MINIMAL_INHABITANT(E)
→ EXACT_PRODUCER(E)
→ TERMINAL(E).

A composição global é válida apenas quando o EXACT_PRODUCER da mesma semântica concreta está habitado.

Novas classes universais observadas:

### 1.1 Produtor de majorante
Dados:
- função erro D(N) ≥ 0;
- majorante eps(N) ≥ 0;
- D(N) ≤ eps(N);
- eps(N) → 0.

Operador:
D ≤ eps ∧ eps→0 ⇒ D→0.

Instância RH:
D = DN; eps_K(N)=K/log(N+2).

Leis:
- monotonicidade em K;
- upward closure dos certificados;
- qualquer K'≥K preserva fechamento.

### 1.2 Produtor de orçamento subcrítico
Dados:
- decomposição S=B+T;
- B≤c_B X;
- T≤c_T X;
- c_B+c_T<1.

Operador:
S≤(c_B+c_T)X, com theta=c_B+c_T<1.

Instância NS:
X=nu*z; S=stretch.

Lei:
delta=1-theta>0 gera dissipação estrita.

### 1.3 Produtor por witness não-vácuo
Dados:
- espaço regulado;
- operador físico ligado ao mesmo modelo;
- gap uniforme positivo;
- estado de norma positiva;
- ortogonalidade ao vácuo.

Operador:
bloqueia modelos Unit/vazios e torna a exclusão espectral material.

Instância YM:
A1MaterialWitnessV3.

### 1.4 Produtor por realização algébrica
Dados:
- objeto geométrico concreto;
- representação semântica;
- witness finito;
- transporte fiel.

Instância Hodge:
H01UniversalMaterialProducer → ConcreteHodgeMaterialTarget.

### 1.5 Produtor universal de contraexemplos
Dados:
para cada candidato M, construir x(M) tal que M falha na linguagem alvo.

Instância P02:
UniversalCounterexampleProducer / CanonicalSATP02Producer.

### 1.6 Produtor escalar de exclusão
Dados:
um invariante escalar canônico cujo lower bound é equivalente ao endpoint.

Instância Beal:
TripleGCD(a,b,c)>1.

### 1.7 Produtor acoplado analítico-aritmético
Dados:
o mesmo objeto deve alimentar invariantes dos dois lados da identidade.

Instância BSD:
a mesma curva E/Q deve determinar rank, L-series, período, regulador, Sha,
Tamagawa, torsão e leading coefficient.

---

## 2. RIEMANN

### 2.1 Objetos concretos já existentes
- concreteNBData;
- concreteGeneratorFamily;
- rho_a(x)={1/(a x)};
- chi=1_(0,1);
- finite span V_N;
- distance d_N;
- DN_N=d_N^2;
- Gram matrix G_N;
- target vector b_N;
- optimal coefficient witnesses;
- normal equations.

### 2.2 Leis já formalizadas
- DN≥0;
- best approximation;
- finite coefficient approximants belong to V_N;
- coefficient error→0 ⇒ FiniteSpanApproximatesChi;
- FiniteSpanApproximatesChi ↔ DNLimit=0;
- Gram residual ↔ DNLimit=0;
- normal-equation reduced energy formula;
- majorant squeeze;
- logMajorant(K,N)=K/log(N+2) tends to zero;
- monotonicity in K.

### 2.3 Operadores novos
ConcreteLogMajorantCertificate
→ VanishingUpperBound
→ DNToZero
→ DNLimit=0
→ ConcreteGramResidual
→ FINAL_ROOT.

Commits:
- 38509bc8171af702baacc4503f52134db05709bf
- e9c3b340ba2852c60ca07275b717f2332497a0b7

### 2.4 Matemática aritmética adicional
MobiusDivisorKernel formaliza:
sum_{d|n} mu(d)=1 se n=1; 0 caso contrário.

Isto é uma identidade real reutilizável para coeficientes Möbius, mas não prova o erro L2→0.

### 2.5 Evidência analítica
A auditoria R2 registra:
- fórmula explícita de b_a=(log a+1-gamma)/a;
- redução gcd do Gram;
- forma de Vasyunin/cotangente;
- representação Mellin;
- identidade BCF para o polinômio Riesz–Möbius;
- obstruction term de zeros fora da linha.

### 2.6 Resíduo terminal
Rota quantitativa suficiente:
∃K≥0, ∀N,
DN(N) ≤ K/log(N+2).

Rota analítica mais profunda:
ZERO_RESIDUE_SUM_UNCONDITIONAL_CONTROL.

Nada no repositório atual produz uma dessas duas propriedades sem conteúdo equivalente ao endpoint.

---

## 3. P versus NP

### 3.1 P01
P01 está CLOSED_KERNEL_GREEN_FROZEN_CERTIFIED.
Não reabrir parser, witness-read, verifier, budget ou integrated machine.

### 3.2 P02 objetos
- PolyDTMCandidate;
- CandidateFailureMode;
- UniversalFailure;
- UniversalSATLowerBound;
- CanonicalSATP02Producer;
- NormalizedAdversary;
- EffectiveDiagonalCompiler;
- CanonicalSATFixedPointRealizer;
- CandidateKleeneBridge;
- KleeneUniversalBridge;
- UniformEffectiveCoverage.

### 3.3 Equivalências exatas
UniversalSATLowerBound
↔ UniversalFailure canonical SAT
↔ SAT not in P
↔ Nonempty CanonicalSATP02Producer
↔ Nonempty NormalizedAdversary
↔ operational timeout-or-semantic-mismatch.

UniformEffectiveCoverage
↔ Nonempty KleeneSATBridge.

Commit de adapter:
72149cc18b144260c41681da9c972e6d09e2e77f.

### 3.4 Lei diagonal válida
Se c é ponto fixo do compilador e o realizer prova

CanonicalSAT(bitsOf c)
↔ ¬DeclaredAccepts(M,bitsOf c),

então bitsOf c é um counterexample real para M.

### 3.5 Rotas falsificadas
SemanticAlignmentCore está formalmente refutado por um candidato discriminador de 4 estados.

Literal fixed-point também está CLOSED_BY_FALSIFICATION.

Não reabrir essas rotas.

### 3.6 Resíduo terminal
Para cada M:
construir o realizer semântico genuíno

CanonicalSAT(bitsOf c)
↔ ¬DeclaredAccepts(M,bitsOf c)

nos pontos fixos relevantes,

ou construir diretamente x(M) com ¬CorrectAt(M,SAT,x(M)).

---

## 4. NAVIER–STOKES

### 4.1 Dados canônicos
y(t)=||omega||_2^2
z(t)=||grad omega||_2^2
stretch(t)=∫ omega·S omega.

### 4.2 Lei bulk-tail
stretch=B+T
B≤c_B nu z
T≤delta_T nu z
c_B+delta_T<1

⇒ theta=c_B+delta_T<1

⇒ stretch≤theta nu z.

### 4.3 Ponte canônica
Branch madura:
atk-ns-bulk-tail-to-core-20260930

define:
signedGainCoreOfBulkTail
actualNSToSignedGainCore_of_bulkTail.

Branch adicional:
atk/ns-g1-to-producerfirst-adapter-20261001

commit:
03ad152dc61c65542003a257cbdc17399b73d948

transporta o EnstrophyData mais rico de G1 para NSProducerFirst.

### 4.4 Leis PDE downstream
SignedGainCore
→ SignedGainCertificate
→ FlexibleStretchingBound
→ y' + 2(1-theta)nu z ≤ 2C y^2.

Se C=0 na rota bulk-tail:
y' + 2(1-theta)nu z ≤ 0.

### 4.5 Derivada geométrica
K1aExactFrechetProducer formaliza

xi_eps(w)=w/sqrt(||w||^2+eps^2)

e sua derivada de Fréchet exata, além da chain rule.

Não reabrir K1a.

### 4.6 Três resíduos analíticos
O1: ActualNS → controle uniforme de joint coherence / lei conjunta.

O2: ActualNS → smallness da cauda excepcional com o peso real do kernel singular.

O3: ganho não linear / constants que dão orçamento estritamente subcrítico e coeficiente integrável pela energia.

Essas três peças devem produzir bulk, tail e budget; depois o resto já é mecânico.

---

## 5. HODGE

### 5.1 Firewall
ConcreteAlgebraicityPayload sozinho admite modelo com Variety=Empty.
Isso foi bloqueado.

### 5.2 Target endurecido
ConcreteHodgeMaterialTarget:
- Nonempty G.Variety;
- CycleSpanAdapter G M;
- ConcreteAlgebraicityPayload M.

Commit:
f1f0f848d97c32221c2d929451b0f05b907a1ee0.

### 5.3 Novo produtor universal
H01UniversalMaterialProducer:
- nonemptyVariety;
- spanAdapter;
- para todo X,p,alpha: H01MinimalForwardPayload G M X p alpha.

Commit:
7e834bb99add47f2eea8af582cdd1e3f0b8f9e30.

### 5.4 Operador
H01UniversalMaterialProducer
→ ConcreteAlgebraicityPayload
→ ConcreteHodgeMaterialTarget
→ GradedRationalHodgeConjecture.

### 5.5 Decomposição H01
Por input X,p,alpha:
R1: escolher spread S e descent point D.
R2: produzir cycle witness no ponto escolhido.
R3: provar variational algebraicity / transport.
Adapter span converte o resultado semântico em combinação concreta finita de ciclos.

### 5.6 Resíduos
R0:
modelo real de cohomologia Q, ciclos, cycle-class map e leis do span.

R1:
spread uniforme dependente de X,p,alpha.

R2:
produção do ponto/ciclo algébrico.

R3:
specialization / variational algebraicity.

---

## 6. BSD

### 6.1 Firewall de domínio
BSDArithmeticAnalyticData sozinho é insuficiente.
Existe contraexemplo abstrato com analyticOrder=2 e MWrank=0.

Portanto não quantificar sobre dados Nat não ligados a uma curva.

### 6.2 Estrutura rank
Num domínio Realizable válido:

low-rank theorem + high-rank residual
→ universal rank.

Dado o low-rank theorem,
universal rank ↔ analytic-rank>=2 residual.

### 6.3 Problema de model binding
Não existe no Lean atual um tipo concreto EllipticCurveQ com:
- modelo de Weierstrass;
- Mordell–Weil;
- Hasse–Weil L-series;
- analytic continuation;
- leading coefficient;
- periods;
- regulator;
- Sha;
- Tamagawa;
- torsion.

EllipticCurveQ aparece apenas em documentação/auditoria.

### 6.4 Produtor genuíno a construir
Primeiro:
ConcreteBSDModel E.

Deve ligar todos os invariantes à mesma curva e à mesma normalização.

Depois:
RankProducer(E):
ord_{s=1} L(E,s)=rank E(Q).

RefinedProducer(E):
leading(E)=Omega_E Reg_E |Sha_E| prod c_p / |E(Q)_tors|^2
sob convenções registradas.

### 6.5 Leis novas necessárias
- invariance sob mudança de modelo mínimo corretamente normalizada;
- basis/index law para regulator;
- positivity/integrality para Sha/Tamagawa/torsion quando aplicável;
- same-curve law: nenhum fator pode vir de outra curva;
- leading coefficient só é comparado depois do rank/order estar fixado;
- Sha finiteness não pode ser assumida a partir da própria fórmula BSD.

---

## 7. YANG–MILLS

### 7.1 Colapso descoberto
YMCurrentModelCollapse prova que o antigo
B60ConcretePhysicalAdapter
pode ser habitado por um modelo físico Unit não relacionado.

Logo:
B60 sozinho ≠ produtor material.

B60FieldBundle sozinho também não basta se usa o mesmo carrier abstrato.

### 7.2 Hardening v2
A1PhysicalData liga ao mesmo C:
- cutoff;
- volume;
- observable realization;
- reflection;
- regulated action;
- kernel from action;
- cofinality;
- nontrivial observable.

ReflectionPositivityDataV2:
pairing é a integral exata contra a medida regulada de C.

PositiveTransferDataV2:
transfer operator é o integral operator do kernel da mesma ação.

UniformRegulatorControlV2:
m0>0 e gap uniforme em cutoff pequeno.

### 7.3 Hardening v3
Novo objeto:
RegulatedNonvacuumExcitation:
- regulator/volume admissíveis;
- state no mesmo RegulatedL2Vector;
- regulatedNormSq(state)>0;
- regulatedInner(state,vacuum)=0.

A1MaterialWitnessV3:
V2 + RegulatedNonvacuumExcitation.

Commit:
ea22910e5b737d1236fbde7ad129cc5d8c8c0b8a.

### 7.4 Leis
A1MaterialWitnessV3 → A1ScientificWitnessV2.
Todo v3 tem m0>0.
Todo v3 tem uma excitação regulada de norma positiva.

### 7.5 Resíduo
1. construir A1MaterialWitnessV3 para a construção 4D genuína;
2. formalizar o Hilbert quotient/reconstruction físico;
3. ligar o transfer Hamiltonian ao K14;
4. provar cobertura/densidade do setor físico;
5. transportar o gap regulado uniforme através de cutoff→0 e volume→∞;
6. produzir K30SpectralTransferWitness fiel.

Só depois B60/K30 pode ser consumido como endpoint material.

---

## 8. BEAL

### 8.1 Invariante escalar
TripleGCD(a,b,c)=gcd(a,gcd(b,c)).

### 8.2 Leis
CommonDivisor(q,a,b,c) ⇒ q | TripleGCD.

TripleGCD divide a,b,c.

CommonDivisor não-trivial ⇒ TripleGCD>1.

TripleGCD>1 ⇒ existe CommonDivisor não-trivial.

CommonDivisor ↔ CommonPrime.

### 8.3 Equivalência terminal
BealConjecture
↔ UniversalTripleGCDLowerBound.

### 8.4 Resíduo
Derivar diretamente das equações

a^x+b^y=c^z, x,y,z>2

a lei universal
TripleGCD(a,b,c)>1.

Conductor/local methods são úteis somente se produzirem essa desigualdade.

---

## 9. NOVOS OPERADORES TRANSVERSAIS

### 9.1 weaken
Se um witness quantitativo vale com constante K e a conclusão é monotônica,
pode ser transportado para K'≥K.

Exemplo: RH.

### 9.2 normalize
Side conditions não materiais podem ser normalizadas por max/positive part quando a desigualdade é monotônica.

Exemplo: NS theta,C.

### 9.3 project
Um witness rico pode ser projetado ao carrier mínimo quando nenhum campo usado na prova é perdido.

Exemplo: G1 EnstrophyData → NSProducerFirst.EnstrophyData.

### 9.4 harden
Se um target admite modelos vazios/triviais, adicionar somente as leis mínimas
que excluem o contraexemplo conhecido.

Exemplos:
- Hodge: Nonempty Variety;
- YM: positive-norm vacuum-orthogonal excitation.

### 9.5 falsify-route
Se uma rota estrutural implica uma propriedade falsa num modelo explícito,
congelar a refutação e proibir reabertura.

Exemplos:
- P02 SemanticAlignmentCore;
- P02 literal fixed point;
- BSD arbitrary abstract realizability;
- YM B60-as-material-terminal.

---

## 10. LISTA EXATA DO QUE AINDA PRECISA SER PRODUZIDO

RH:
- um majorante incondicional concreto de DN que tende a zero;
  suficiente: K/log(N+2);
  ou controle incondicional equivalente do residue sum BCF.

P02:
- para cada candidato M, um input SAT concreto de falha;
  ou o realizer semântico Kleene/SAT que produz esse input.

Beal:
- TripleGCD>1 para todo BealData admissível.

NS:
- joint/bulk theorem a partir de ActualNS;
- weighted exceptional-tail theorem;
- strict subcritical/energy-integrable gain.

Hodge:
- concrete model binding;
- universal spread;
- cycle/algebraic point production;
- variational specialization theorem.

BSD:
- tipo concreto de curva E/Q e model binding;
- rank>=2 theorem;
- full refined leading coefficient theorem;
- Sha finiteness + normalization laws.

YM:
- A1MaterialWitnessV3 para YM4 real;
- faithful Hilbert/reconstruction adapter;
- physical spectral coverage;
- limit-preserving positive gap / K30 transfer.

---

## 11. REGRA DE FECHAMENTO

OPEN_MATH fecha somente quando o produtor listado acima tiver um inhabitant
cujo tipo preserve:
- domínio;
- quantificadores;
- constantes;
- scaling;
- semântica;
- dependências;
- provenance.

BUILD GREEN de adapters não muda OPEN_MATH.

Equivalência com o endpoint não muda OPEN_MATH.

Numerical evidence não muda OPEN_MATH.

Somente material inhabitant → endpoint.
