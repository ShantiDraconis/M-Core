# M-Core v2 — master audit protocol

Goal: turn structural observations into falsifiable executable tests and Lean proof obligations without promoting calibration or analogy into theorem status.

1. Freeze S0. Any modification is a new experiment.
2. A1: prove analytically that degree-one amplitude homogeneity plus one positive witness excludes a universal fixed upper gap on an amplitude-unbounded class.
3. A2: represent dependencies as a directed graph. Reject any proof in which G1 or its coefficient depends downstream on the target/conclusion it is used to establish.
4. A3: never assert `same quotient`. Supply explicit G,H and explicit paths approaching the same zero locus. Prove G,H→0 and compute/derive distinct path limits.
5. A4: separate scale invariance from threshold claims. Proving I(u_lambda)=I(u) does not by itself prove Phi≈0.6, epsilon0≈0.6, or tau_max rigidity. Those require independent hypotheses/theorems.
6. Normalization I*: before claiming it is bounded or degree zero, compute amplitude and critical-scaling homogeneity symbolically. `I/(1+||u||)` is not automatically homogeneous because of the additive 1.
7. Each Millennium adapter must define its own domain, functional, scaling action, zero locus, dependency graph, and target theorem. Never transfer omega/Y/a(t), numerical constants, or implications between problems by analogy.
8. Status every claim as PROVED, CONDITIONAL, NUMERICAL_EVIDENCE, DEFINITION/INTERFACE, or OPEN.
9. Python establishes executable witnesses/regressions. Lean establishes only the statements actually typechecked without `sorry` or unreported axioms.
10. Stop at the first open bridge and state it exactly. Do not infer a prize solution from passing infrastructure tests.

Immediate target: close matrix obligations 15–19, then formulate obligation 20 precisely enough to attempt proof or falsification. Only after that introduce a problem-specific I* candidate.
