# DOI_READY_INDEX

Critério: um item é "DOI-ready" quando o enunciado demonstrado é exato, a prova
passa no kernel com axiomas dentro da política, a reprodução é documentada e o
texto não promete mais do que foi demonstrado.

## Apto como resolução matemática

**Nenhum.** As sete lanes estão em `OPEN_MATH` (`final_proof = 0/7`). Nenhum artigo
deve anunciar a resolução de P vs NP, RH, Beal, Navier–Stokes, Hodge, BSD ou
Yang–Mills com base neste material.

## Apto como registro de software/dados (com o rótulo correto)

| Item | Conteúdo | Rótulo obrigatório | Pendências antes do depósito |
|---|---|---|---|
| Pacote de auditoria `certs/final_global/v1` + `frozen/closed-math-global-green-9a7f1f04` | biblioteca Lean que passa no kernel, auditoria de axiomas reproduzível, inventário de 24 repositórios, bloqueios exatos | "Formal verification infrastructure and audit record; no Millennium problem is solved (final_proof = 0/7)" | integrar a branch de auditoria ao `main` (decisão do mantenedor); nova versão do registro Figshare/Zenodo que cite o `FINAL_GLOBAL_ROOT` |

## Possível contribuição original (requer revisão de literatura antes de qualquer submissão)

| Candidato | O que é de fato | O que falta |
|---|---|---|
| Arquitetura de certificação fail-closed (registro Lean com `provedCount = 0` verificado pelo kernel, firewall, gate preparatório reproduzível) | engenharia de prova / metodologia | comparação com práticas existentes de verificação reproduzível; um artigo de métodos ou de ferramenta é o veículo adequado |
| Formalização de SAT ∈ NP numa MTN concreta (lane P01) | engenharia de formalização de um teorema clássico (Cook, 1971) | concluir `P01VerifierPhase`; comparar com formalizações existentes de Cook–Levin em outros assistentes de prova |

Os teoremas certificados do M-Core são contabilidade de registro, equivalências
lógicas com enunciados oficiais e reduções condicionais; não constituem resultado
matemático novo por si.

## Pacote para revisão externa

Para um revisor reproduzir tudo:

```bash
git clone https://github.com/ShantiDraconis/M-Core && cd M-Core
git checkout atk/global-audit-20261008              # contém a árvore lean/ congelada + o pacote
git diff --stat frozen/closed-math-global-green-9a7f1f04 -- lean MCore   # vazio: mesmos fontes
lake exe cache get && lake build                     # Lean 4.19.0, Mathlib v4.19.0
bash certs/final_global/v1/verify.sh
```

A evidência bruta de cada execução está em `audit-results/<sha>`
(logs por módulo, TSV de axiomas, saída do `freeze.sh`, `lake-manifest.json`).
