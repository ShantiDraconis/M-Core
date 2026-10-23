; 1/zeta(3) (ATK.ErrosConstantes.inv_zeta_tres_cotas): com 1,2020568851 < zeta(3) < 1,2020569219
; (soma parcial ate 60 e caudas telescopicas), 0,831907 zeta(3) < 1 < 0,8319075 zeta(3):
; 0,831907 < 1/zeta(3) < 0,8319075 < 0,831908 (o valor do texto).
(set-logic QF_LRA)
(declare-const z Real)
(assert (< 1.2020568851 z)) (assert (< z 1.2020569219))
(assert (not (and (< (* 0.831907 z) 1.0) (< 1.0 (* 0.8319075 z)))))
(check-sat)
