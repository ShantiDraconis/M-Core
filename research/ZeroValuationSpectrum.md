# Zero–valuation–spectrum bridge

For a finite complex matrix A, p_A(z)=det(zI-A). The equivalence p_A(lambda)=0 iff ker(lambda I-A) is nontrivial follows from invertibility iff determinant is nonzero. The order of the characteristic polynomial at lambda equals algebraic multiplicity by definition. Jordan normal form shows geometric multiplicity <= algebraic multiplicity, with equality for diagonalizable matrices, including Hermitian matrices.

For nonzero real entries a_i, R_ij=a_i/a_j is an outer product with R²=nR, rank 1, trace n. Hence p_R(z)=z^(n-1)(z-n). B=aa^T is positive semidefinite, rank 1, B²=||a||² B, p_B(z)=z^(n-1)(z-||a||²). Exact SymPy computation for a=(63,64,79,92,94,98,103,109,111) returned rank 1 for both, p_R=z^8(z-9), p_B=z^8(z-76021), nullities 8 at zero and 1 at nonzero eigenvalues. Jordan control [[2,1],[0,2]] has p=(z-2)^2 and nullity 1 at 2. These parameters are illustrative, not special to zeta.

Infinite-dimensional bridge: for positive self-adjoint trace-class A, det(I+wA)=product_k(1+w mu_k), where positive eigenvalues mu_k are repeated by multiplicity. All determinant zeros are negative real and their orders equal corresponding eigenvalue multiplicities. Conversely if the entire real function G(w)=xi(1/2+sqrt(w)) has only negative real zeros lambda_k, its order 1/2 genus-zero factorization gives a positive diagonal trace-class A with mu_k=-1/lambda_k, since sum |lambda_k|^-1 converges. Thus existence of such A with G(w)/G(0)=det(I+wA) is equivalent to RH. Constructing A independently without assuming RH remains OPEN.

Status: analytic proofs and exact finite symbolic calculations; Lean not compiled; no claim of RH proof.
