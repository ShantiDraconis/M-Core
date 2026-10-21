# Contaminated/NotImported — quarentena

Arquivos aqui **não são importados por nenhum alvo de build** (nenhum `lakefile` aponta para esta
pasta). Ficam por histórico e para estudo, nunca como evidência. Movidos na arrumação de
22/10/2026, depois da auditoria de 21/10/2026.

| Arquivo | Por que está aqui |
| --- | --- |
| `atk-kernel-experimentos/AxiomaHipotetico.lean` (+ `.out`) | Declara `axiom S`, `hS`, `W` e `axiom Wc : Mundo especContraditoria`, e deriva `theorem falso : False`. Experimento deliberado: prova qualquer coisa. |
| `lean-MCore/Poincare.lean` | Usa a sintaxe `constant` do Lean 3, não compila no Lean 4 e nunca foi importado. `MATERIAL_PRODUCER_GAPS := 0` é uma constante digitada, provada por `rfl`. O único "teorema" projeta um campo de um certificado recebido como hipótese. |
| `lean-MCore/POINCARE_ATK_CLAIM.md` | Declara `CLOSED_UNCONDITIONAL` e `MATERIAL_PRODUCER_GAPS: 0` por fiat, a partir do trabalho de Perelman. Não é um resultado do kernel. Desde set–out/2026 existem duas formalizações externas de Poincaré em Lean (Qin–Liao–Khaitan–Chow, arXiv 2609.33842; frenzymath, arXiv 2610.08329), ainda não verificadas aqui. |

Status de produtor, quando existir, sai de `atk-kernel/scripts/status_calculado.py`, nunca de uma
constante escrita à mão.
