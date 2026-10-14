# atk-ns

Verificação independente, no CI deste repositório, da prova formal da OpenAI
([`openai/NavierStokesAndEuler`](https://github.com/openai/NavierStokesAndEuler), commit `8937a8f`,
setembro de 2026) das alternativas (C) e (D) do problema do milênio de Navier–Stokes (Clay).

- `AtkNS/FCDefinicoes.lean`: definições copiadas do formal-conjectures (Google DeepMind,
  Apache-2.0), independentes da cópia da OpenAI.
- `AtkNS/ClayNS.lean`: `ClayNS := A ∨ B ∨ C ∨ D` com essas definições; `clayC`, `clayD`,
  `clayNS` a partir dos teoremas da OpenAI, convertendo as estruturas campo a campo.
- Lean `v4.34.0-rc2`, Mathlib `v4.34.0-rc2` (as versões da OpenAI). O CI compila a prova da
  OpenAI do código-fonte e exige só `propext`, `Classical.choice`, `Quot.sound`.

A prova é da OpenAI, não do ATK. (A) — existência global sem força — continua aberta; é o alvo
da obrigação O3 do ATK.
