To make R1CS -> QAP more concrete from rareskills zk-book
An almost complete example is created here.
**Quick Recap from zk-book**

- We want to verify a solution provided is true. This is not the process of finding
  the correct solution, but a verification compute that approves the proposed solution is true. P-NP problems.
- ZK cant help you to find a solution for a sudoku or coloring problem but can help you to prove to another party that you have a solution if you have computed it already.
- Creating a ZK proof for a problem boils down to translating the problem to a circuit, and having a valid input to the circuit (witness) which ultimately transforms into zk proof.
- The ability to verify a solution to a problem is a prerequisite for creating a zk proof that you have a solution.
- One must be able to construct a Boolean circuit to model the solution efficiently, however NSPACE (finding the optimal chess moves) results in exponentially large circuits making them impractical.
- Arithmetic circuits and Boolean circuits are the equivalent/same. (any boolean circuit can be transformend into an arithmetic circuit) Remember a system of equations can have many solutions, but we are interested in verifying a given solution. We dont meed to find all solutions for an arithmetic circuit.

- we create the arithmetic circuit & matrices and check if Left*w x Right*w = Out\*w where w is the witness vector.

- Then we need to apply Lagrange interpolation, its is used to find the polynomial that passes through a set of n points with the lowest degree.
- Given consisten base of x values to interpolate a vector over, there is a unique polynomial that interpolates a given vector. In other words, every length n vector has a unique polynomial representation.
- Schwartz Zippel Lemma: Nearly all ZK proof algorithms rely on it to achieve succinctness,
- Given two polynomials with degrees dp and dq , the number of points these two poly intersects is less than equal to max (dp, dq)
- If we pick a random value, and evaluate f(u) and g(u) if they are equal then f(x) = g(x)
  or we picked one of the intersection points in finite field p.
- It could be but if we pick the random number d << p then this situation is highly unlikely. We know that two polynomials can intersect at most degree d and if we pick the finite field P is very high, its quite highly unlikely to pick a random value that they can pick to verify
- End goal for the prover to send a small string of data to the verifier so he/she can quickly check.
- Most of the time, a ZK proof is essentially a polynomial evaluated at a random point.

- why this is a great method? cause instead of doing the comparison to verify the compute is correct which would take mxn steps in a matrix (O(n)), we can just do it in O(1)
  **QAP**

- QAP: A quadratic arithmetic program is an arithmetic circuit, specifically a R1CS represented as a set of polynomials. It is derived using Lagrange interpolation, on a Rank1 Constraint System.
- Unlike an R1CS, a Quadratic Arithmetic Program (QAP) can be tested for equality in O(1) time via the Schwartz-Zippel Lemma.

Ex: z = x^4-5y^2x^2
