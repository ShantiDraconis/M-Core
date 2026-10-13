# ATK genuine-object replacements — 2026-10-13

These calculations are **specific examples**, not universal conjecture proofs. No Lean kernel was run for this file.

## RH genuine finite Gram entry
For x in (0,1), define f2(x)={1/(2x)}-(1/2){1/x}, where braces denote fractional part. On x in (1/(n+1),1/n], f2(x)=1/2 when n is odd and 0 otherwise. Thus integral f2 dx = (1/2) ln 2 and integral f2^2 dx=(1/4)ln 2. With target chi=1 and G=[ln2/4], b=[ln2/2], the exact squared L2 projection residual is D1=1-ln2≈0.3068528194400547. This is one genuine Nyman-Beurling generator, not a proof of density. The quantitative K* depends on the selected indexing and full generator family.

## NS genuine 3D periodic solution
On the three-torus [0,2pi]^3, nu=1, u(t,x,y,z)=(exp(-t) sin z,0,0), p=0 solves incompressible NS: div u=0, (u·grad)u=0, ∂t u=Δu. Curl u=(0,exp(-t)cos z,0). y(t)=1/2 ||curl u||_2²=2*pi³*exp(-2t); Z²(t)=||grad curl u||_2²=4*pi³*exp(-2t). Stretch=0. This is a genuine smooth flow but cannot establish universal coefficients across all flows.

## BSD genuine elliptic curve
E/Q: y²=x³-x is nonsingular (discriminant 64). P=(0,0) and Q=(1,0) are rational points of order 2, so canonical heights h(P)=h(Q)=<P,Q>=0. Their 2x2 height determinant is zero. **Do not use them as a free Mordell-Weil basis or infer the curve's regulator from this matrix.** Need independent nontorsion points on a positive-rank curve to calculate a nonzero rank-2 regulator.

## Hodge genuine algebraic cycle
For X=P²_C, H is the class of a hyperplane P¹. Its cohomology class is algebraic and integral_X H²=1. This establishes a concrete case only, not the universal Hodge conjecture.

## Beal genuine integer instance
3³+6³=3⁵; gcd(3,6,3)=3. Does not prove universal Beal.

## Audit scope
Previous synthetic RH matrix G=[[2,1],[1,2]], NS cB=1/4 cT=1/3, BSD height matrix [[2,1],[1,3]], and Hodge diagonal toy matrix must retain MODEL labels. No unverified numeric substitution is promoted to a terminal parameter. This is not a sweep of all branches and repositories.
