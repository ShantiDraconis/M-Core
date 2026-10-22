# NS T1: auditoria de escala da explosão forçada da OpenAI (sympy)

**Hipótese testada.** Os expoentes anunciados (ℓ_r ≍ τ^{1/2}, ℓ_z ≍ τ^{1/2−h}, u_θ, u_z ≍ τ^{−1/2−h}, u_r = O(τ^{−1/2}), 0 < h < 1/100) são compatíveis com as condições necessárias clássicas de explosão: Leray, L³ (ESS/Seregin), Serrin, BKM, CKN e Tipo II/KNSS. Hipótese da varredura: toda janela viável tem Re_loc → ∞, e a margem Tipo II pode ir a 0.

**Insumos que são alegações de fonte, não verificadas aqui** (frontier §1.2, que parafraseia o PDF da OpenAI, Thm 1.1 e o mecanismo): os expoentes (a, b, c) = (1/2, 1/2−h, 1/2+h), a cota u_r = O(τ^{−1/2}), sup_t ‖u‖₂ < ∞ e f ∈ C_c^∞. Tudo o mais é cálculo deste teste.

**Método** (`tests/code/NS_T1.py`, saída em `tests/work/NS_T1_out.txt`).
- *Anzats de núcleo.* Volume ℓ_r²ℓ_z; U_r = τ^{−d} com d = c + b − a (incompressibilidade); |∇u| ~ max U_i/min(ℓ_r, ℓ_z); ν = 1.
- *Verificação.* Cada condição é testada com `solve_univariate_inequality` em h e intersectada com (0, 1/100).
- *CKN.* Calculado de dois modos: (i) núcleo inteiro em B_r; (ii) núcleo **truncado** a B_r(x*), usando o princípio de Laplace para leis de potência, com τ = τ₀^x e o mínimo de uma função linear por partes.
- **Controle.** Reproduzir as 7 contas do frontier §1.3(2). Passou: d = 1/2, ‖u‖_L³ ~ τ^{−4h/3}, enstrofia ~ τ^{−1/2−3h}, Tipo II τ^{−h}, Re_loc τ^{−h}, CKN ingênuo τ^{−3h}. O expoente truncado foi conferido numericamente contra a rotina genérica em h = 0.001, 0.005 e 0.0099, com concordância até 10⁻⁶.

**Resultados no ponto OpenAI** (expoentes de τ):

| quantidade | expoente | condição | vale em todo (0, 1/100)? |
|---|---|---|---|
| energia do núcleo | 1/2 − 3h | limitada | sim |
| enstrofia / ∫ | −1/2 − 3h | ≥ taxa de Leray e integrável | sim / sim |
| ‖u‖_∞ | −1/2 − h | Leray (≤ −1/2) | sim |
| ‖u‖_L³ ; ‖u‖²_Ḣ^{1/2} | −4h/3 ; −3h | → ∞ (ESS/Seregin) | sim |
| ‖ω‖_∞ | −1 − h | ∫ = ∞ (BKM) | sim |
| ∫‖u‖_q^p, (q,p) = (4,8), (6,4), (9,3), (∞,2) | −1 − hp(1 + 1/q) | divergem (Serrin) | sim |
| CKN r⁻¹∬_{Q_r}\|∇u\|², r = √τ₀ | ingênuo −3h; **truncado −2h/(1−2h)** | ≥ ε | sim |
| ‖u‖_∞√τ ; Re_loc ; ℓ_z/ℓ_r | −h ; −h ; −h | Tipo II ; → ∞ | sim |

**B4 (escala v = λu(λx, t₀ + λ²s))** (B4 = barreira de forçamento criticamente pequeno, frontier §2):
- **(i) λ = τ₀^{−1/2}, a convenção do frontier.**
  - Reproduz os números de B4: ‖v₀‖₂² ~ τ₀^{1/2}, ‖g‖_{L¹L³} ≲ τ₀ e ‖g‖_{L¹L^∞} ≲ τ₀^{1/2}.
  - Porém **a explosão ocorre em s* = τ₀², não em s = 1**.
  - Os expoentes de ‖g‖_{L¹Ẇ^{k,p}} (k = 0..3; p = 3, ∞) são 1, 1/2, 1/2, 0, 0, −1/2, −1/2, −1. Só k − 3/p < 1 fica pequeno.
- **(ii) λ = τ₀^{+1/2}, explosão em s = 1 com ν fixo.**
  - ‖v₀‖₂² ~ τ₀^{−1/2} → ∞; a parte do núcleo é τ₀^{−3h}.
  - A força fica pequena em todas as normas testadas (expoentes 1 a 3).
- ‖v₀‖_L³ ~ τ₀^{−4h/3} nos dois casos.

**Varredura** (a, b, c) ∈ [0.3, 1]³ com passo 0.005 (2 803 221 pontos; impostos também c ≥ 1 − a e c ≥ a):
- Há 123 957 pontos viáveis, com a ∈ [0.40, 0.99], b ∈ [0.30, 0.985] e c ∈ [0.50, 0.99]. O ponto OpenAI com h = 0.005 é viável.
- A margem Tipo II mínima é 0.005, o passo da grade: ela pode ir a 0.
- **4010 pontos viáveis têm Re_loc = O(1)**, exatamente na fronteira c = a. Exemplo: (0.505, 0.30, 0.505). A cota máxima do expoente de Re_loc é 0.245.

**Interpretação honesta.**
- *O que o teste mostra.* Nenhuma condição necessária clássica é violada pelos expoentes anunciados. A explosão é marginalmente supercrítica: toda margem é ∝ h. Não é evidência de correção, só ausência de inconsistência dimensional.
- **Correção 1 ao frontier.** Com o núcleo alongado (ℓ_z > r) truncado a B_r, o expoente CKN é −2h/(1−2h) ≈ −2h, e não −3h. A conclusão (→ ∞) não muda.
- **Correção 2 ao frontier (B4).** "Energia < ε" e "explosão no tempo 1" não valem juntas por escala com ν fixo.
  - A versão correta é: energia, ‖f‖_{L¹L³} e ‖f‖_{L¹L^∞} pequenos, com explosão no tempo τ₀² → 0. Isso ainda dá o corolário "não existe Φ(‖u₀‖₂, ‖f‖)".
  - A alternativa: explosão em 1, com força pequena em W^{3,∞} mas energia grande.
  - Usar a família em ν exigiria saber como E depende de ν, o que as fontes não dão.
- **Hipótese da varredura.** Só vale na parte "margem Tipo II → 0". "Re_loc → ∞ em toda janela" é falsa na fronteira c = a, que é permitida pela restrição imposta c ≥ a. Fora dela, a hipótese é tautológica.

**Limites.** Análise dimensional de um só núcleo autossimilar: ignora os pulsos não axissimétricos, o campo externo e os logaritmos. As condições são só necessárias. O CKN truncado supõe o núcleo centrado em x*.

**Próximo.** (1) Extrair do PDF a energia total E(t) e as normas de f perto de t = 1 (planicidade) para refazer B4 com dados reais. (2) Testar a família em ν. (3) Repetir a auditoria para o Euler sem força da OpenAI.
