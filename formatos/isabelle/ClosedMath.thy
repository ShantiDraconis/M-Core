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
  by (simp add: power_mult_distrib cos_squared_eq algebra_simps)

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

section \<open>Jensen, Turán, Toeplitz (espelha ATK/JensenTuran.lean)\<close>

definition disc3 :: "real \<Rightarrow> real \<Rightarrow> real \<Rightarrow> real \<Rightarrow> real" where
  "disc3 A B C D = B^2*C^2 - 4*A*C^3 - 4*B^3*D - 27*A^2*D^2 + 18*A*B*C*D"

theorem disc3_raizes:
  "disc3 A (-A*(r1+r2+r3)) (A*(r1*r2+r1*r3+r2*r3)) (-A*r1*r2*r3) =
    A^4*((r1-r2)*(r1-r3)*(r2-r3))^2"
  unfolding disc3_def by (simp add: power2_eq_square power3_eq_cube power4_eq_xxxx algebra_simps)

theorem disc3_jensen:
  "disc3 g3 (3*g2) (3*g1) g0 = 27*(4*(g1^2-g0*g2)*(g2^2-g1*g3) - (g1*g2-g0*g3)^2)"
  unfolding disc3_def by (simp add: power2_eq_square power3_eq_cube algebra_simps)

theorem turan3:
  fixes g0 g1 g2 g3 r1 r2 r3 :: real
  assumes hB: "3*g2 = -g3*(r1+r2+r3)" and hC: "3*g1 = g3*(r1*r2+r1*r3+r2*r3)"
    and hD: "g0 = -g3*r1*r2*r3"
  shows "(g1*g2-g0*g3)^2 \<le> 4*(g1^2-g0*g2)*(g2^2-g1*g3)"
proof -
  have E: "disc3 g3 (3*g2) (3*g1) g0 = g3^4*((r1-r2)*(r1-r3)*(r2-r3))^2"
    unfolding hB hC hD by (rule disc3_raizes)
  have p4: "0 \<le> g3^4" by (simp add: zero_le_even_power)
  have P: "0 \<le> g3^4*((r1-r2)*(r1-r3)*(r2-r3))^2"
    by (rule mult_nonneg_nonneg[OF p4 zero_le_power2])
  define D where "D = 4*(g1^2-g0*g2)*(g2^2-g1*g3) - (g1*g2-g0*g3)^2"
  have J: "disc3 g3 (3*g2) (3*g1) g0 = 27*D"
    unfolding D_def by (rule disc3_jensen)
  have Q: "27*D = g3^4*((r1-r2)*(r1-r3)*(r2-r3))^2" using J E by metis
  have "0 \<le> 27*D" using Q P by simp
  then have "0 \<le> D" by linarith
  then show ?thesis unfolding D_def by linarith
qed

theorem jensen_grau2:
  fixes g0 g1 g2 x y :: real
  assumes h2: "g2 \<noteq> 0" and hre: "g2*(x^2 - y^2) + 2*g1*x + g0 = 0"
    and him: "y*(2*(g2*x + g1)) = 0" and hd: "g0*g2 \<le> g1^2"
  shows "y = 0"
proof (rule ccontr)
  assume hy: "y \<noteq> 0"
  have hx: "g2*x + g1 = 0" using him hy by simp
  have hx': "g2*x = -g1" using hx by linarith
  have e1: "g2*(g2*(x^2 - y^2) + 2*g1*x + g0) = 0" using hre by simp
  have e2: "g2^2*y^2 = (g2*x)*(g2*x) + 2*g1*(g2*x) + g0*g2 - g2*(g2*(x^2 - y^2) + 2*g1*x + g0)"
    by (simp add: power2_eq_square algebra_simps)
  have e3: "(g2*x)*(g2*x) + 2*g1*(g2*x) = g1^2 - 2*g1^2"
    unfolding hx' by (simp add: power2_eq_square algebra_simps)
  have K: "g2^2*y^2 = g0*g2 - g1^2" using e1 e2 e3 by linarith
  have a: "0 < g2^2" using h2 by simp
  have b: "0 < y^2" using hy by simp
  have "0 < g2^2*y^2" using a b by (rule mult_pos_pos)
  then show False using K hd by linarith
qed

theorem turan_normalizacao_id:
  "((k+1)*f*a1)^2 - (f*a0)*((k+2)*(k+1)*f*a2) = ((k+1)*f^2)*((k+1)*a1^2 - (k+2)*a0*a2)"
  for k f a0 a1 a2 :: real
  by (simp add: power2_eq_square algebra_simps)

definition D31 :: "real \<Rightarrow> real \<Rightarrow> real \<Rightarrow> real \<Rightarrow> real" where
  "D31 g0 g1 g2 g3 = g1^3 - 2*g0*g1*g2 + g0^2*g3"

theorem tp_a_nao_passa_gamma: "D31 1 3 3 1 = 10" "D31 1 3 6 6 = -3"
  by (simp_all add: D31_def)

theorem turan_momentos_id:
  fixes c q A B M0 M1 M2 :: real
  assumes hA: "0 < A" and hB: "0 < B"
  shows "(c*(q/(2*A))*M1)^2 - (c*M0)*(c*(q^2/(4*A*B))*M2) =
    (c^2*q^2/(4*A^2*B)) * (B*M1^2 - A*(M0*M2))"
proof -
  have a: "A \<noteq> 0" "B \<noteq> 0" using hA hB by simp_all
  show ?thesis using a by (simp add: field_simps power2_eq_square)
qed

theorem cs_nao_implica_turan: "(1::real)^2 \<le> 1*4 \<and> \<not> ((1::real)*(1*4) \<le> 3*1^2)"
  by simp

theorem forma_L6:
  fixes a b c d e f :: real
  shows "a*(6*a-(a+b+c+d+e+f)) + b*(6*b-(a+b+c+d+e+f)) + c*(6*c-(a+b+c+d+e+f)) +
    d*(6*d-(a+b+c+d+e+f)) + e*(6*e-(a+b+c+d+e+f)) + f*(6*f-(a+b+c+d+e+f)) =
    (a-b)^2+(a-c)^2+(a-d)^2+(a-e)^2+(a-f)^2+(b-c)^2+(b-d)^2+(b-e)^2+(b-f)^2+
    (c-d)^2+(c-e)^2+(c-f)^2+(d-e)^2+(d-f)^2+(e-f)^2"
  by (simp add: power2_eq_square algebra_simps)

theorem jensen_gamma_detecta:
  fixes x :: real
  shows "1 + 6*x + 12*x^2 \<noteq> 0"
proof -
  have e: "1 + 6*x + 12*x^2 = 3/4*(4*x+1)^2 + 1/4"
    by (simp add: power2_eq_square algebra_simps)
  have h: "0 \<le> (4*x+1)^2" by simp
  show ?thesis using e h by linarith
qed

theorem jensen_a_disc: "(2*N)^2 - 4*(N*(N-1))*1 = 4*N" for N :: real
  by (simp add: power2_eq_square algebra_simps)

theorem rotacao:
  fixes d t c s :: real
  assumes h: "c^2 + s^2 = 1"
  shows "(d*c - t*s)^2 + (d*s + t*c)^2 = d^2 + t^2"
proof -
  have "(d*c - t*s)^2 + (d*s + t*c)^2 = (d^2 + t^2)*(c^2 + s^2)"
    by (simp add: power2_eq_square algebra_simps)
  then show ?thesis using h by simp
qed

theorem barreira_a_b_t: "be^2 + ga^2 = ((1-be)^2 + ga^2) + (2*be - 1)" for be ga :: real
  by (simp add: power2_eq_square algebra_simps)

theorem ajuste_intercepto:
  fixes l2 l5 :: real
  assumes h1: "6931471803/10000000000 < l2" and h2: "l2 < 6931471808/10000000000"
    and h3: "2231435/10000000 < l5 - 2*l2" and h4: "l5 - 2*l2 < 2231436/10000000"
  shows "304147212/10000000000 * l2 + 152073606/10000000000 * l5 < 658697302176/10000000000000 * l2"
    and "- 354550090176/10000000000000 * l2 + 152073606/10000000000 * l5 < 58/1000000 * l2 - 87/1000000 * l5"
proof -
  show "304147212/10000000000 * l2 + 152073606/10000000000 * l5 < 658697302176/10000000000000 * l2"
    using h1 h2 h3 h4 by linarith
  show "- 354550090176/10000000000000 * l2 + 152073606/10000000000 * l5 < 58/1000000 * l2 - 87/1000000 * l5"
    using h1 h2 h3 h4 by linarith
qed

theorem contraexemplo_pedaco:
  fixes L :: real
  assumes "4054651081081/10000000000000 < L" "L < 4054651081082/10000000000000"
  shows "0 < 1/2 - 2*L + 1/3" and "1/2 - 5/2*L + 1/3 < 0"
proof -
  show "0 < 1/2 - 2*L + 1/3" using assms by linarith
  show "1/2 - 5/2*L + 1/3 < 0" using assms by linarith
qed

theorem b_texto_base:
  fixes g l2 s :: real
  assumes "5772156/10000000 < g" "l2 < 6931471808/10000000000" "11/6 - 2*l2 \<le> s"
  shows "1 - g - s < 0"
  using assms by linarith

theorem G12_tabela:
  fixes g l2 lp :: real
  assumes "g < 5772163/10000000" "6931471803/10000000000 < l2" "11447295/10000000 < lp"
  shows "7722084/10000000 < 1/2*l2 + 3/4*lp - 3/4*g"
  using assms by linarith

theorem produtos_C0:
  fixes g l2 lp d :: real
  assumes h1: "5772156/10000000 < g" and h2: "l2 < 6931471808/10000000000"
    and h3: "6931471803/10000000000 < l2" and h4: "lp < 11447300/10000000"
    and h5: "d < 2231436/10000000" and h6: "2231435/10000000 < d"
  shows "658697302176/10000000000000 * l2 < 2 + g - 2*l2 - lp"
    and "608294424/10000000000 * l2 + 152073606/10000000000 * d < 2 + g - 2*l2 - lp"
proof -
  show "658697302176/10000000000000 * l2 < 2 + g - 2*l2 - lp"
    using h1 h2 h3 h4 by linarith
  show "608294424/10000000000 * l2 + 152073606/10000000000 * d < 2 + g - 2*l2 - lp"
    using h1 h2 h3 h4 h5 h6 by linarith
qed

theorem regiao_vazia:
  fixes u s :: real
  assumes "1/4 < u"
  shows "\<not> (1/2 + u \<le> s \<and> s \<le> 1 - u)"
  using assms by linarith

theorem inv_zeta3:
  fixes z :: real
  assumes "12020568851/10000000000 < z" "z < 12020569219/10000000000"
  shows "831907/1000000 * z < 1" and "1 < 8319075/10000000 * z"
proof -
  show "831907/1000000 * z < 1" using assms by linarith
  show "1 < 8319075/10000000 * z" using assms by linarith
qed

theorem constante_theta:
  fixes P T S :: real
  assumes "4*T = P + 1/2" "S = P/2 - 2*T"
  shows "1/2 + 2*S \<le> 0" and "0 \<le> 1/2 + 2*S"
proof -
  show "1/2 + 2*S \<le> 0" using assms by linarith
  show "0 \<le> 1/2 + 2*S" using assms by linarith
qed

theorem tri_um_x_x2:
  fixes d0 d1 d2 d3 :: real
  assumes "d0 = 1" "d1 = 1" "d2 = d1 - d0" "d3 = d2 - d1"
  shows "d3 < 0"
  using assms by linarith

text \<open>Rodada 9 (ATK/ASWReciproca): 1/(1 - x + x^2) tem b3 = -1 < 0, um menor 1x1 de colunas iniciais
  negativo (ASWRec.cc_de_tn, contrapositiva).\<close>

theorem inv_um_x_x2:
  fixes b0 b1 b2 b3 :: real
  assumes "b0 = 1" "b1 - b0 = 0" "b2 - b1 + b0 = 0" "b3 - b2 + b1 = 0"
  shows "b3 < 0"
  using assms by linarith

text \<open>Rodada 10 (ATK/EdreiInteira): cada passo da descida baixa b1 de L_j >= 1/(a0 |w|); com a0 = 1,
  |w| = 2 e b1 = 1, tres passos dariam b1 < 0.\<close>

theorem descida_tres:
  fixes b0 b1 b2 b3 L0 L1 L2 :: real
  assumes "b0 = 1" "L0 \<ge> 1/2" "L1 \<ge> 1/2" "L2 \<ge> 1/2"
    "b1 = b0 - L0" "b2 = b1 - L1" "b3 = b2 - L2"
  shows "b3 < 0"
  using assms by linarith

text \<open>Rodada 11 (ATK/HadamardGenero0): prodCoef com a0 = 1 e alpha = (1/2, 1/3) da 1 + (5/6)z + (1/6)z^2;
  os coeficientes crescem com o numero de fatores e ficam <= a0 (soma alpha)^n.\<close>

theorem prodcoef_dois:
  fixes p10 p11 p12 p20 p21 p22 :: real
  assumes "p10 = 1" "p11 = 1/2 * 1" "p12 = 0"
    "p20 = p10" "p21 = p11 + 1/3 * p10" "p22 = p12 + 1/3 * p11"
  shows "p11 \<le> p21 \<and> p12 \<le> p22 \<and> p22 \<le> 25/36 \<and> 0 < p22"
proof (intro conjI)
  show "p11 \<le> p21" using assms by linarith
  show "p12 \<le> p22" using assms by linarith
  show "p22 \<le> 25/36" using assms by linarith
  show "0 < p22" using assms by linarith
qed

text \<open>Rodada 12 (ATK/LaguerrePolya): no grau 2, se p = x^2 - s x + P tem raizes reais, p + c p' tambem
  (o discriminante passa a 4c^2 + disc p).\<close>

theorem laguerre_quadratica:
  fixes s P c :: real
  assumes "s*s - 4*P \<ge> 0"
  shows "(2*c - s)*(2*c - s) - 4*(P - c*s) \<ge> 0"
proof -
  have e: "(2*c - s)*(2*c - s) - 4*(P - c*s) = 4*(c*c) + (s*s - 4*P)"
    by (simp add: algebra_simps)
  have "0 \<le> c*c" by simp
  then show ?thesis using assms e by linarith
qed

text \<open>Rodada 13 (ATK/JensenPolya): se g0 + 2 g1 x + g2 x^2 = 0 com g2 > 0, entao g0 g2 <= g1^2 (Turan a
  partir de uma raiz real de J^{2,n}).\<close>

theorem turan_raiz:
  fixes g0 g1 g2 x :: real
  assumes "g2 > 0" "g2*x*x + 2*g1*x + g0 = 0"
  shows "g0*g2 \<le> g1*g1"
proof -
  have e1: "(g2*x + g1)*(g2*x + g1) = g2*(g2*x*x + 2*g1*x + g0) + (g1*g1 - g0*g2)"
    by (simp add: algebra_simps)
  have e: "(g2*x + g1)*(g2*x + g1) = g1*g1 - g0*g2"
    using e1 assms(2) by simp
  have "0 \<le> (g2*x + g1)*(g2*x + g1)" by simp
  then show ?thesis using e by linarith
qed

text \<open>Rodada 14 (ATK/HurwitzJensen): o passo do circulo de Hurwitz (variaveis = normas): |g| >= delta e
  |g - F| < delta/2 dao |F| > delta/2, incompativel com |F(z0)| < delta/2 e |F(z0)| >= |F|.\<close>

theorem hurwitz_circulo:
  fixes delta g e F F0 :: real
  assumes "delta > 0" "g \<ge> delta" "e < delta/2" "F \<ge> g - e" "F0 < delta/2" "F0 \<ge> F"
  shows False
  using assms by linarith

text \<open>Rodada 15 (ATK/TuranDispersao): o integrando simetrizado da identidade de dispersao de ordem 2,
  (t^2 - s^2)(psi t - psi s) >= 0 quando psi e crescente.\<close>

theorem simetrizacao_ordem2:
  fixes t s pt ps :: real
  assumes "t > 0" "s > 0" "t \<le> s \<Longrightarrow> pt \<le> ps" "s \<le> t \<Longrightarrow> ps \<le> pt"
  shows "0 \<le> (t*t - s*s) * (pt - ps)"
proof (cases "t \<le> s")
  case True
  have t0: "0 \<le> t" using assms(1) by linarith
  have s0: "0 \<le> s" using True assms(1) by linarith
  have m: "t*t \<le> s*s" by (rule mult_mono[OF True True s0 t0])
  have a: "t*t - s*s \<le> 0" using m by linarith
  have p: "pt \<le> ps" using assms(3) True by blast
  have b: "pt - ps \<le> 0" using p by linarith
  show ?thesis using a b by (rule mult_nonpos_nonpos)
next
  case False
  then have st: "s \<le> t" by linarith
  have s0: "0 \<le> s" using assms(2) by linarith
  have t0: "0 \<le> t" using st assms(2) by linarith
  have m: "s*s \<le> t*t" by (rule mult_mono[OF st st t0 s0])
  have a: "0 \<le> t*t - s*s" using m by linarith
  have p: "ps \<le> pt" using assms(4) st by blast
  have b: "0 \<le> pt - ps" using p by linarith
  show ?thesis using a b by (rule mult_nonneg_nonneg)
qed

text \<open>Rodada 16 - ATK.ZeroClasses.card_quatro: o quarteto tem 4 pontos distintos quando
  Re z \<noteq> c e Im z \<noteq> 0.\<close>

theorem orbita_quatro:
  fixes x y c :: real
  assumes "x \<noteq> c" "y \<noteq> 0"
  shows "x \<noteq> 2*c - x \<and> y \<noteq> - y"
proof -
  have a: "x \<noteq> 2*c - x"
  proof
    assume "x = 2*c - x"
    then have "x = c" by linarith
    with assms(1) show False by simp
  qed
  have b: "y \<noteq> - y"
  proof
    assume "y = - y"
    then have "y = 0" by linarith
    with assms(2) show False by simp
  qed
  show ?thesis using a b by simp
qed

text \<open>Rodada 16 - ATK.TruncToep.menor3: o menor 3x3 contiguo de Toeplitz.\<close>

theorem menor3:
  fixes a0 a1 a2 a3 :: real
  shows "a1*(a1*a1 - a0*a2) - a0*(a2*a1 - a0*a3) = a1*a1*a1 - 2*a0*a1*a2 + a0*a0*a3"
  by (simp add: algebra_simps)

end
