# Auditoria de miniF2F e ProofNet: resumo

Run 43202317750 do workflow `auditoria-benchmarks.yml` (12/11/2026), cada benchmark com o seu próprio Lean e Mathlib,
em commit fixado. Relatórios completos: `miniF2F-test.md`, `miniF2F-valid.md`, `ProofNet.md` (e os `.achados.json`).

| Benchmark (commit, Lean) | Teoremas | Defeitos certificados no kernel | Triviais (uma tática) | Divisão por zero não excluída | Subtração em ℕ | Função totalizada | Divisão inteira |
|---|---|---|---|---|---|---|---|
| miniF2F test ([yangky11/miniF2F-lean4](https://github.com/yangky11/miniF2F-lean4) @ 5746b7d, v4.24.0) | 244 | **2** | 57 | 18 | 18 | 7 | 7 |
| miniF2F valid (idem) | 244 | 0 | 49 | 22 | 21 | 8 | 3 |
| ProofNet ([rahul3613/ProofNet-lean4](https://github.com/rahul3613/ProofNet-lean4) @ 6deae98, v4.20.0) | 360 | **1** | 4 | 18 | 17 | 8 | 4 |
| **Total** | **848** | **3** | **110** | **58** | **56** | **23** | **14** |

## Os três defeitos certificados

1. **`mathd_algebra_208`** (`MiniF2F/Test/mathd_algebra_208.lean:7`): `Real.sqrt 1000000 - 1000000^(1/3) = 900`.
   O expoente `1/3` é divisão em ℕ e vale 0, então `1000000^(1/3) = 1` e o lado esquerdo é 999. A negação foi
   provada por `norm_num` e conferida no kernel: o enunciado é **falso**.
2. **`mathd_algebra_275`** (`MiniF2F/Test/mathd_algebra_275.lean:7`): hipótese `((11:ℝ)^(1/4))^(3x−3) = 1/5`. De
   novo `1/4 = 0` em ℕ, então a hipótese diz `1 = 1/5`. `simp_all` deriva `False` das hipóteses (conferido no
   kernel): o enunciado é **vazio**, qualquer conclusão sairia dele.
3. **`exercise_4_4_9`** (ProofNet, `formal/Herstein.lean:173`): com `p = 2`, a hipótese `Nat.Prime 2` vale e a
   segunda parte pede `¬ ∃ x : ZMod 2, x^2 = 2`, mas `x = 0` resolve (`2 = 0` em `ZMod 2`). A negação do enunciado
   foi provada por `decide` em `p = 2` e conferida no kernel: o enunciado é **falso**. Ele também não corresponde ao
   exercício original (resíduos quadráticos módulo `p`).

Os dois defeitos do miniF2F têm a mesma causa, divisão inteira num expoente. Os dois aparecem também na coluna de
risco `divisao_inteira`, que aponta onde procurar.

## Como ler os números

- **Os defeitos certificados são um mínimo.** O auditor só marca o que uma tática padrão prova e o kernel aceita.
  Estudos de 2026 que comparam com o enunciado informal acham muito mais: 56 % de ProofNet infiel (*Ground False*,
  NeurIPS 2026) e mais da metade do miniF2F com discrepâncias (*miniF2F-Lean Revisited*). Este auditor não faz essa
  comparação.
- **"Trivial" não é defeito.** Muitos problemas `mathd` do miniF2F são contas que `norm_num` fecha de propósito. A
  coluna serve para a revisão humana procurar formalizações que perderam a dificuldade.
- **Riscos não são defeitos.** São condições laterais que as táticas não derivam das hipóteses. Alguns são
  inofensivos, como `log z ≠ 0` a partir de `1 < z`.
- **Caminhos no ProofNet.** O workflow copia `formal/<Fonte>.lean` para `Auditados/<Fonte sem hífen>.lean` sem mudar
  as linhas, então `Auditados/Herstein.lean:173` é `formal/Herstein.lean:173`.

## Conferência independente

`Confere.lean` refaz os três com provas escritas à mão, sem o auditor: `m208_falso`, `m275_vazio`, `pn449_falso`.
No Lean v4.19.0 com Mathlib v4.19.0, `#print axioms` dá `[propext, Classical.choice, Quot.sound]` para os três.
