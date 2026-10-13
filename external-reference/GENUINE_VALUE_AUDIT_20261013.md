# ATK genuine-value audit — 2026-10-13

Status: SOURCE / mathematical derivations only / KERNEL NOT RUN / OPEN_MATH true.

## Scope actually inspected
- Branch listings: first 100 branches each for ShantiDraconis/M-Core, m-core-riemann, m-core-bsd, m-core-hodge, m-core-yang-mills, m-core-beal, m-core-p-vs-np; each response indicated further pages. No exhaustive sweep performed.
- ShantiDraconis/m-core-navier-stokes returned repository-not-found; actual NS producer is referenced in M-Core at ShantiDraconis/navier-stokes-critical-barrier-audit.
- RH GATE_LEDGER.json (main): hard_atomic_remaining=1; terminal FiniteSpanApproximatesChi concreteGeneratorFamily; GREEN frozen equivalence is NOT a proof of density.
- The previously mentioned external-reference/GENUINE_OBJECTS.md and GENUINE_VALUES.csv were not found on the integration branch when checked. Do not claim those files exist.

## Genuine NS example: explicit smooth 3D periodic solution
Take the 3-torus [0,2pi]^3 and viscosity nu>0. Define u(t,x,y,z)=(exp(-nu*t)*sin(z),0,0), p=0.
Then div u=0, (u·grad)u=0, and partial_t u=nu Laplacian u. Hence it is an exact 3D NS solution.
omega=curl u=(0,exp(-nu*t)*cos(z),0).
y(t)=1/2 integral |omega|^2 = 2*pi^3*exp(-2*nu*t).
Z²(t)=integral |grad omega|² = 4*pi^3*exp(-2*nu*t).
S(t)=integral (omega·grad)u·omega=0.
Thus y'=-4*nu*pi^3*exp(-2*nu*t)=-nu*Z² exactly.
At nu=1,t=0: y=2*pi^3; Z²=4*pi^3; S=0.
WARNING: a single zero-stretch solution does not bound universal c_B,c_T,C.

## Genuine BSD example
E/Q: y²=x³-x is nonsingular (discriminant 64). Points P=(0,0), Q=(1,0) have y=0, hence 2-torsion. Therefore canonical heights h(P)=h(Q)=0 and pairing <P,Q>=0. The resulting 2x2 height matrix is zero, and it is NOT a rank-two Mordell-Weil basis. Its determinant zero cannot be substituted for the rank-two regulator.

## Genuine Hodge example
On X=P²_C, let H be the hyperplane class of O(1). H is the class of an actual algebraic divisor and integral_X H²=1. Thus the rational Hodge classes in H²(X,Q) are algebraic in this example. This does not establish the Hodge conjecture for arbitrary smooth projective X.

## RH correction and next calculation
For the Nyman-Beurling generator f_theta(x)={theta/x}-theta*{1/x}, theta=1/2, the integrand changes on infinitely many intervals as x->0. Prior asserted identities <f_1/2,1>=ln(2)/2 and ||f_1/2||²=ln(2)/4 must NOT be imported as proven without explicit integration/audit. Consequently the previous D1=1-ln(2) is QUARANTINED until recomputed. The true finite Gram residual is D1=||chi||² - <f,chi>²/||f||², with chi=1 on (0,1).
The 2x2 synthetic Gram G=[[2,1],[1,2]] yields D=5/6 for b=(1/2,1/2), but is MODEL_ONLY, not a genuine RH bound.

## Remaining endpoints
RH: genuine Gram family and D_N->0; NS: universal signed-gain from actual flows; BSD: genuine non-torsion Mordell-Weil basis and refined BSD identity; Hodge: universal cycle production; PNP: SAT not in P; YM: physical 4D theory and mass gap; Beal: universal exclusion of primitive solutions.
Never replace these endpoints with numerical examples, synthetic axioms, or conditional wrappers.
