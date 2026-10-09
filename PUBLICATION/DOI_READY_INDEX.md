# DOI_READY_INDEX

Atualizado em 2026-10-09. Um item é "DOI-ready" quando:
- o enunciado demonstrado é exato;
- a prova passa no kernel com axiomas dentro da política;
- a reprodução está documentada;
- o texto não promete mais do que foi demonstrado.

## Apto como resolução matemática

**Nenhum.** As sete lanes estão em `OPEN_MATH` (`final_proof = 0/7`). Nenhum artigo
deve anunciar a resolução de P vs NP, RH, Beal, Navier–Stokes, Hodge, BSD ou
Yang–Mills com base neste material.

## Apto como artefato de software/dados

| Item | Conteúdo exato | Rótulo obrigatório | Pendências |
|---|---|---|---|
| **P01: SAT ∈ NP em Lean 4** (`m-core-p-vs-np@0dd09383`, auditoria `frozen/p01-closure-audit-green-d97a56e1`) | Uma MTN concreta, de fita única e controle finito, sobre o alfabeto `{branco, 0, 1}`, que decide em tempo polinomial a linguagem CNF-SAT sob uma codificação binária fixa. Sem `sorry`; axiomas `propext`, `Classical.choice`, `Quot.sound`. | "Formalização do lado de pertinência (SAT ∈ NP) do teorema de Cook–Levin; não contém NP-dificuldade nem nada sobre P vs NP." | Merge em `main`; um README de reprodução no repositório; licença; registro Zenodo ou Figshare apontando o commit e o run `37913791428`. |
| **Pacote de auditoria M-Core** (`certs/final_global/v2` + `frozen/closed-math-global-green-33983a4c`) | Biblioteca Lean verificada pelo kernel, auditoria de axiomas reproduzível, inventário de 24 repositórios, bloqueios exatos e errata. | "Infraestrutura de verificação formal e registro de auditoria; nenhum problema do Milênio está resolvido (final_proof = 0/7)." | Merge do PR #15; nova versão do registro Figshare `10.6084/m9.figshare.33990856` citando o `FINAL_GLOBAL_ROOT` do v2. |

### Posição frente à literatura (P01)

A formalização do teorema de Cook–Levin completo (SAT é NP-completo) já existe em
outros assistentes de prova:
- Coq: Gäher & Kunze, ITP 2021;
- Isabelle: AFP `Cook_Levin`, de Balbach.

O resultado aqui é só a direção fácil (pertinência a NP). O que tem de específico:
- é feito em Lean 4;
- usa um modelo de fita única com apenas três símbolos;
- tem tempo polinomial explícito.

O veículo adequado é um artefato de software ou uma nota curta de métodos, não um
artigo de resultado.

## Possível contribuição metodológica (exige revisão antes de submeter)

| Candidato | O que é de fato |
|---|---|
| Arquitetura de certificação fail-closed (registro Lean com `provedCount = 0` verificado pelo kernel, firewall de vinculação semântica, gates preparatórios reproduzíveis, errata versionada) | engenharia de prova / metodologia; veículo: artigo de ferramenta ou de métodos |

## Pacote para revisão externa

```bash
git clone https://github.com/ShantiDraconis/M-Core && cd M-Core
git checkout atk/global-audit-20261008          # até o merge do PR #15
lake exe cache get && lake build                  # Lean 4.19.0, Mathlib v4.19.0
bash certs/final_global/v2/verify.sh
```

Para P01 (sem Mathlib):

```bash
git clone https://github.com/ShantiDraconis/m-core-p-vs-np && cd m-core-p-vs-np
git checkout frozen/p01-closure-audit-green-d97a56e1
lake build MCore.Real.P01RawTotalizationProducer
lake env lean audit/P01ClosureAudit.lean
```

Fontes:
- [Gäher & Kunze, *Mechanising Complexity Theory: The Cook-Levin Theorem in Coq*, ITP 2021](https://drops.dagstuhl.de/opus/volltexte/2021/13915/)
- [AFP: Cook_Levin (Isabelle)](https://devel.isa-afp.org/entries/Cook_Levin.html)
