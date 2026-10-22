(* ATK–Closed Math: núcleo em Isabelle/HOL (Complex_Main), verificado por `isabelle build`.
   Espelha os teoremas de ATK/ClosedMathCEZ.lean, ATK/ClosedMathCompleto.lean,
   ATK/ClosedMathToro.lean e ATK/RHTerminal.lean na parte algébrica/geométrica.
   Sem sorry. Nada aqui afirma a Hipótese de Riemann. *)

theory ClosedMath
  imports Complex_Main
begin

section \<open>Semântica: quatro estados pontuais\<close>

definition critico :: "(complex \<Rightarrow> complex) \<Rightarrow> complex \<Rightarrow> bool" where
  "critico F s \<longleftrightarrow> F s = 0 \<and> Re s = 1/2"
definition externo :: "(complex \<Rightarrow> complex) \<Rightarrow> complex \<Rightarrow> bool" where
  "externo F s \<longleftrightarrow> F s = 0 \<and> Re s \<noteq> 1/2"
definition naozeroC :: "(complex \<Rightarrow> complex) \<Rightarrow> complex \<Rightarrow> bool" where
  "naozeroC F s \<longleftrightarrow> F s \<noteq> 0 \<and> Re s = 1/2"
definition naozeroE :: "(complex \<Rightarrow> complex) \<Rightarrow> complex \<Rightarrow> bool" where
  "naozeroE F s \<longleftrightarrow> F s \<noteq> 0 \<and> Re s \<noteq> 1/2"

theorem classificacao: "critico F s \<or> externo F s \<or> naozeroC F s \<or> naozeroE F s"
  unfolding critico_def externo_def naozeroC_def naozeroE_def by blast

theorem exclusivos:
  "\<not> (critico F s \<and> externo F s)" "\<not> (critico F s \<and> naozeroC F s)"
  "\<not> (critico F s \<and> naozeroE F s)" "\<not> (externo F s \<and> naozeroC F s)"
  "\<not> (externo F s \<and> naozeroE F s)" "\<not> (naozeroC F s \<and> naozeroE F s)"
  unfolding critico_def externo_def naozeroC_def naozeroE_def by blast+

section \<open>Verificador\<close>

theorem checar_correto:
  fixes z m :: complex and r :: real
  assumes "cmod (z - m) \<le> r" and "r < cmod m"
  shows "z \<noteq> 0"
  using assms by auto

section \<open>Operadores\<close>

definition opR :: "complex \<Rightarrow> complex" where "opR s = 1 - cnj s"
definition opS :: "complex \<Rightarrow> complex" where "opS s = 1 - s"
definition opT :: "complex \<Rightarrow> complex" where "opT s = \<i> * cnj s"

lemma R_R: "opR (opR s) = s" by (simp add: opR_def)
lemma S_S: "opS (opS s) = s" by (simp add: opS_def)
lemma T_T: "opT (opT s) = s" by (simp add: opT_def complex_eq_iff)
lemma J_J: "cnj (cnj s) = s" by simp
lemma R_J: "opR (cnj s) = opS s" by (simp add: opR_def opS_def)
lemma J_R: "cnj (opR s) = opS s" by (simp add: opR_def opS_def)
lemma R_S: "opR (opS s) = cnj s" by (simp add: opR_def opS_def)
lemma D_R: "Re (opR s) - 1/2 = - (Re s - 1/2)" by (simp add: opR_def)
lemma TRT: "opT (opR (opT w)) = cnj w + \<i>" by (simp add: opT_def opR_def complex_eq_iff)

lemma TRT_fixo: "opT (opR (opT w)) = w \<longleftrightarrow> Im w = 1/2"
proof
  assume "opT (opR (opT w)) = w"
  then have "Im (cnj w + \<i>) = Im w" by (simp add: TRT)
  then show "Im w = 1/2" by simp
next
  assume h: "Im w = 1/2"
  show "opT (opR (opT w)) = w" unfolding TRT using h by (simp add: complex_eq_iff)
qed

lemma T_isometria: "cmod (opT s - opT w) = cmod (s - w)"
  by (simp add: norm_complex_def opT_def power2_eq_square algebra_simps)

lemma T4_centro: "((1/2 + of_real d + \<i> * of_real t) + (1/2 - of_real d + \<i> * of_real t)) / 2
    = (1/2 :: complex) + \<i> * of_real t"
  by (simp add: field_simps)

lemma T5_separacao: "cmod ((1/2 + of_real d + \<i> * of_real t) - (1/2 - of_real d + \<i> * of_real t)) = 2 * \<bar>d\<bar>"
proof -
  have "(1/2 + of_real d + \<i> * of_real t) - (1/2 - of_real d + \<i> * of_real t) = (of_real (2 * d) :: complex)"
    by simp
  then show ?thesis by (simp add: abs_mult)
qed

lemma T6_coincidencia: "((1/2 + of_real d + \<i> * of_real t) = (1/2 - of_real d + \<i> * of_real t :: complex)) \<longleftrightarrow> d = 0"
proof
  assume "(1/2 + of_real d + \<i> * of_real t) = (1/2 - of_real d + \<i> * of_real t :: complex)"
  then have "Re (1/2 + of_real d + \<i> * of_real t :: complex) = Re (1/2 - of_real d + \<i> * of_real t :: complex)"
    by simp
  then show "d = 0" by simp
qed simp

section \<open>Modelo G e produtores\<close>

definition G :: "real \<Rightarrow> real \<Rightarrow> complex \<Rightarrow> complex" where
  "G d g s = ((s - 1/2 - of_real d)\<^sup>2 + (of_real g)\<^sup>2) * ((s - 1/2 + of_real d)\<^sup>2 + (of_real g)\<^sup>2)"

lemma fator_zero: "(\<i> * of_real g)\<^sup>2 + (of_real g)\<^sup>2 = (0 :: complex)"
  by (simp add: power2_eq_square algebra_simps)

lemma fator_zero': "(- (\<i> * of_real g))\<^sup>2 + (of_real g)\<^sup>2 = (0 :: complex)"
  by (simp add: power2_eq_square algebra_simps)

theorem P1:
  "G d g (1/2 + of_real d + \<i> * of_real g) = 0"
  "G d g (1/2 + of_real d - \<i> * of_real g) = 0"
  "G d g (1/2 - of_real d + \<i> * of_real g) = 0"
  "G d g (1/2 - of_real d - \<i> * of_real g) = 0"
proof -
  have e1: "1/2 + of_real d + \<i> * of_real g - 1/2 - of_real d = \<i> * (of_real g :: complex)" by simp
  have e2: "1/2 + of_real d - \<i> * of_real g - 1/2 - of_real d = - (\<i> * (of_real g :: complex))" by simp
  have e3: "1/2 - of_real d + \<i> * of_real g - 1/2 + of_real d = \<i> * (of_real g :: complex)" by simp
  have e4: "1/2 - of_real d - \<i> * of_real g - 1/2 + of_real d = - (\<i> * (of_real g :: complex))" by simp
  show "G d g (1/2 + of_real d + \<i> * of_real g) = 0" unfolding G_def e1 fator_zero by simp
  show "G d g (1/2 + of_real d - \<i> * of_real g) = 0" unfolding G_def e2 fator_zero' by simp
  show "G d g (1/2 - of_real d + \<i> * of_real g) = 0" unfolding G_def e3 fator_zero by simp
  show "G d g (1/2 - of_real d - \<i> * of_real g) = 0" unfolding G_def e4 fator_zero' by simp
qed

theorem G_R: "G d g (1 - s) = G d g s"
  by (simp add: G_def power2_eq_square algebra_simps)

theorem G_conj: "G d g (cnj s) = cnj (G d g s)"
  by (simp add: G_def)

theorem G_quartica: "G d g (x + 1/2) = x^4 + 2 * ((of_real g)\<^sup>2 - (of_real d)\<^sup>2) * x\<^sup>2
    + ((of_real g)\<^sup>2 + (of_real d)\<^sup>2)\<^sup>2"
  unfolding G_def by (simp add: power2_eq_square power4_eq_xxxx algebra_simps)

theorem P2_critico: "critico (G 0 g) (1/2 + \<i> * of_real g)"
  unfolding critico_def using P1(1)[of 0 g] by simp

theorem P3_externo: "d \<noteq> 0 \<Longrightarrow> externo (G d g) (1/2 + of_real d + \<i> * of_real g)"
  unfolding externo_def using P1(1)[of d g] by simp

lemma G_real: "G d g (of_real x) = of_real (((x - 1/2 - d)\<^sup>2 + g\<^sup>2) * ((x - 1/2 + d)\<^sup>2 + g\<^sup>2))"
  by (simp add: G_def)

theorem P5_NE: "g \<noteq> 0 \<Longrightarrow> naozeroE (G d g) 2"
proof -
  assume hg: "g \<noteq> 0"
  have g2: "0 < g\<^sup>2" using hg by simp
  have pos: "0 < ((2 - 1/2 - d)\<^sup>2 + g\<^sup>2) * ((2 - 1/2 + d)\<^sup>2 + g\<^sup>2)"
    by (intro mult_pos_pos add_nonneg_pos zero_le_power2 g2)
  have "G d g (of_real 2) \<noteq> 0" unfolding G_real using pos by (metis of_real_eq_0_iff less_irrefl)
  then show ?thesis unfolding naozeroE_def by simp
qed

theorem P5_NC: "g \<noteq> 0 \<Longrightarrow> naozeroC (G d g) (1/2)"
proof -
  assume hg: "g \<noteq> 0"
  have g2: "0 < g\<^sup>2" using hg by simp
  have pos: "0 < ((1/2 - 1/2 - d)\<^sup>2 + g\<^sup>2) * ((1/2 - 1/2 + d)\<^sup>2 + g\<^sup>2)"
    by (intro mult_pos_pos add_nonneg_pos zero_le_power2 g2)
  have "G d g (of_real (1/2)) \<noteq> 0" unfolding G_real using pos by (metis of_real_eq_0_iff less_irrefl)
  then show ?thesis unfolding naozeroC_def by simp
qed

theorem simetria_compativel_com_ambos:
  "(\<forall>s. G 0 1 (1 - s) = G 0 1 s) \<and> (\<forall>s. G 1 1 (1 - s) = G 1 1 s) \<and>
   critico (G 0 1) (1/2 + \<i>) \<and> externo (G 1 1) (1/2 + 1 + \<i>)"
  using G_R P2_critico[of 1] P3_externo[of 1 1] by simp

section \<open>Geometrias\<close>

theorem P_esfera:
  fixes a b :: real
  shows "(2*a / (1 + a\<^sup>2 + b\<^sup>2))\<^sup>2 + (2*b / (1 + a\<^sup>2 + b\<^sup>2))\<^sup>2
         + ((a\<^sup>2 + b\<^sup>2 - 1) / (1 + a\<^sup>2 + b\<^sup>2))\<^sup>2 = 1"
proof -
  have hD: "0 < 1 + a\<^sup>2 + b\<^sup>2" by (simp add: add_pos_nonneg)
  then have hD': "(1 + a\<^sup>2 + b\<^sup>2)\<^sup>2 \<noteq> 0" by simp
  have num: "(2*a)\<^sup>2 + (2*b)\<^sup>2 + (a\<^sup>2 + b\<^sup>2 - 1)\<^sup>2 = (1 + a\<^sup>2 + b\<^sup>2)\<^sup>2"
    by (simp add: power2_eq_square algebra_simps)
  have "(2*a / (1 + a\<^sup>2 + b\<^sup>2))\<^sup>2 + (2*b / (1 + a\<^sup>2 + b\<^sup>2))\<^sup>2
         + ((a\<^sup>2 + b\<^sup>2 - 1) / (1 + a\<^sup>2 + b\<^sup>2))\<^sup>2
        = ((2*a)\<^sup>2 + (2*b)\<^sup>2 + (a\<^sup>2 + b\<^sup>2 - 1)\<^sup>2) / (1 + a\<^sup>2 + b\<^sup>2)\<^sup>2"
    by (simp add: power_divide add_divide_distrib)
  also have "\<dots> = 1" unfolding num using hD' by simp
  finally show ?thesis .
qed

theorem Cil_par:
  "cos (2*pi*(1/2 + d)) = - cos (2*pi*d)" "sin (2*pi*(1/2 + d)) = - sin (2*pi*d)"
  "cos (2*pi*(1/2 - d)) = - cos (2*pi*d)" "sin (2*pi*(1/2 - d)) = sin (2*pi*d)"
proof -
  have a: "2*pi*(1/2 + d) = 2*pi*d + pi" by (simp add: algebra_simps)
  have b: "2*pi*(1/2 - d) = pi - 2*pi*d" by (simp add: algebra_simps)
  show "cos (2*pi*(1/2 + d)) = - cos (2*pi*d)" unfolding a by (simp add: cos_add)
  show "sin (2*pi*(1/2 + d)) = - sin (2*pi*d)" unfolding a by (simp add: sin_add)
  show "cos (2*pi*(1/2 - d)) = - cos (2*pi*d)" unfolding b by (simp add: cos_diff)
  show "sin (2*pi*(1/2 - d)) = sin (2*pi*d)" unfolding b by (simp add: sin_diff)
qed

theorem Cil_dist_par:
  "(cos (2*pi*(1/2 + d)) - cos (2*pi*(1/2 - d)))\<^sup>2 + (sin (2*pi*(1/2 + d)) - sin (2*pi*(1/2 - d)))\<^sup>2
     = (2 * sin (2*pi*d))\<^sup>2"
  unfolding Cil_par by (simp add: power2_eq_square algebra_simps)

theorem K_cone: "(\<bar>\<delta>\<bar> * cos th)\<^sup>2 + (\<bar>\<delta>\<bar> * sin th)\<^sup>2 = (\<delta>::real)\<^sup>2"
proof -
  have "(\<bar>\<delta>\<bar> * cos th)\<^sup>2 + (\<bar>\<delta>\<bar> * sin th)\<^sup>2 = \<delta>\<^sup>2 * ((sin th)\<^sup>2 + (cos th)\<^sup>2)"
    by (simp add: power_mult_distrib distrib_left add.commute)
  also have "\<dots> = \<delta>\<^sup>2" by simp
  finally show ?thesis .
qed

theorem tor_R:
  "cos (2*pi*(1 - \<sigma>)) = cos (2*pi*\<sigma>)" "sin (2*pi*(1 - \<sigma>)) = - sin (2*pi*\<sigma>)"
proof -
  have a: "2*pi*(1 - \<sigma>) = 2*pi - 2*pi*\<sigma>" by (simp add: algebra_simps)
  show "cos (2*pi*(1 - \<sigma>)) = cos (2*pi*\<sigma>)" unfolding a by (simp add: cos_diff)
  show "sin (2*pi*(1 - \<sigma>)) = - sin (2*pi*\<sigma>)" unfolding a by (simp add: sin_diff)
qed

theorem tor_linha: "R0 + r * cos (2*pi*(1/2)) = R0 - r" "r * sin (2*pi*(1/2)) = (0::real)"
  by simp_all

definition Kg :: "real \<Rightarrow> real \<Rightarrow> real \<Rightarrow> real" where
  "Kg R0 r th = cos th / (r * (R0 + r * cos th))"

theorem curvatura_linha:
  assumes "0 < r" "r < R0"
  shows "Kg R0 r pi = - 1 / (r * (R0 - r))" "Kg R0 r pi < 0" "Kg R0 r 0 = 1 / (r * (R0 + r))"
proof -
  have p: "0 < r * (R0 - r)" using assms by simp
  show "Kg R0 r pi = - 1 / (r * (R0 - r))" unfolding Kg_def by (simp add: algebra_simps)
  show "Kg R0 r pi < 0" unfolding Kg_def using p by (simp add: algebra_simps divide_neg_pos)
  show "Kg R0 r 0 = 1 / (r * (R0 + r))" unfolding Kg_def by simp
qed

section \<open>Taxonomia ampliada\<close>

theorem P_posneg: "(z\<^sup>2 - a\<^sup>2) * (z\<^sup>2 + b\<^sup>2) = (z - a) * (z + a) * (z - \<i>*b) * (z + \<i>*(b::complex))"
  by (simp add: power2_eq_square algebra_simps)

theorem truncamento_033: "(33/100 :: real) - 1/3 = - 1/300" by simp

theorem cancelamento: "(x::real) \<noteq> 1 \<Longrightarrow> (x\<^sup>2 - 1) / (x - 1) = x + 1"
  by (simp add: power2_eq_square field_simps algebra_simps)

theorem zero_no_infinito: "1 / (1 / w)\<^sup>2 = (w::complex)\<^sup>2" by (simp add: power2_eq_square)

section \<open>Pontes e terminal\<close>

definition transporte_zero :: "(complex \<Rightarrow> complex) \<Rightarrow> (complex \<Rightarrow> complex) \<Rightarrow> (complex \<Rightarrow> complex) \<Rightarrow> (complex \<Rightarrow> complex) \<Rightarrow> bool" where
  "transporte_zero F H phi u \<longleftrightarrow> (\<forall>s. H (phi s) = u s * F s)"

theorem transporte: "transporte_zero F H phi u \<Longrightarrow> F s = 0 \<Longrightarrow> H (phi s) = 0"
  unfolding transporte_zero_def by simp

theorem transporte_iff: "transporte_zero F H phi u \<Longrightarrow> u s \<noteq> 0 \<Longrightarrow> (F s = 0 \<longleftrightarrow> H (phi s) = 0)"
  unfolding transporte_zero_def by simp

theorem criterio_aproximacao:
  fixes F P :: "complex \<Rightarrow> complex" and E L :: real
  assumes "\<forall>s\<in>K. cmod (F s - P s) \<le> E" "\<forall>s\<in>K. L \<le> cmod (P s)" "E < L" "s \<in> K"
  shows "F s \<noteq> 0"
proof
  assume h: "F s = 0"
  have "cmod (F s - P s) \<le> E" using assms(1) assms(4) by blast
  then have "cmod (P s) \<le> E" using h by simp
  moreover have "L \<le> cmod (P s)" using assms(2) assms(4) by blast
  ultimately show False using assms(3) by linarith
qed

theorem cobertura_exclui:
  assumes "\<forall>s\<in>S. \<exists>n. s \<in> K n" "\<forall>n. \<forall>s\<in>K n. F s \<noteq> 0"
  shows "\<forall>s\<in>S. F s \<noteq> 0"
  using assms by blast

section \<open>Tempos verbais\<close>

datatype tempo = Perfeito | Negado | Condicional | Futuro | Presente

fun exige :: "tempo \<Rightarrow> bool \<Rightarrow> bool \<Rightarrow> bool" where
  "exige Perfeito p h = p"
| "exige Negado p h = (\<not> p)"
| "exige Condicional p h = (h \<longrightarrow> p)"
| "exige Futuro p h = True"
| "exige Presente p h = True"

text \<open>Em HOL os tipos não carregam provas: a afirmação é válida quando o tempo é cumprido.\<close>

theorem perfeito_verdadeiro: "exige Perfeito p h \<Longrightarrow> p" by simp
theorem negado_falso: "exige Negado p h \<Longrightarrow> \<not> p" by simp
theorem futuro_vazio: "exige Futuro p h \<and> exige Futuro (\<not> p) h" by simp

end
