# Recursive exact point policy

Every constant, variable, parameter, operator, exponent, subexpression and zero retains its original syntax, domain, trajectory, direction, rate, order, dependencies, residual and evidence where applicable. Metadata may itself be a recursive Point. No fixed recursion depth is imposed on finite syntax trees.

Numeric equality is not structural equality. Undefined expressions and indeterminate limit forms retain exact identities without arbitrary numerical evaluation. Partial evaluation uses Option; admissible realizations retain joint constraints.

Examples: 0/2, 0/pi, 0^1, 0/0, a/pi^- and all seven classical indeterminate limit forms. Directions must be appropriate to the domain (ordered, complex, vector, topological). Repeated parameters retain shared dependencies; independent ternary directions give 3^n only when independent.

Residual laws for addition, subtraction, multiplication, division and a/pi^- are in RecursiveExactPoints.lean. Division requires nonzero denominators. Power, log, exponential, valuations and general convergence require domain-specific formal proofs. The 98-entry catalog is a proposed taxonomy, not an exhaustive enumeration or a certified implementation.

Millennium mappings: RH complex zeros and multiplicity; NS vorticity jets and angular concentration; BSD L-function vanishing order; YM spectrum and kernel; Hodge differential and cohomological classes; P/NP satisfaction and witnesses; Beal arithmetic valuations. These are representation targets, not proofs.

Verification: run lake build MCore.Research.UserProgram.RecursiveExactPoints and inspect #print axioms output. No certification until actual successful build. OPEN_MATH remains true. No CI requested by these commits.
