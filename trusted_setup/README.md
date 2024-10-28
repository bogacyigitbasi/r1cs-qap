**Trusted Setup**

- We use to evaluate a polynomial at a secret value.
- Any polynomial can be written as the inner product of two vectors, a coefficient vector and the successive powers of x

x^3 + 5x^2 + 6x + 14 = [1, 5, 6, 14].[x^3, x^2, x, 1]

- now suppose that we pick a secret scalar value T and compute
  [T^3, T^2, T, 1]
- Then multiply T with a generator point G on an elliptic curve group.

[O1,O2, O3, O4] = [T^3*G, T^2*G, T*G, 1*G]

- Now we can give [O1,O2, O3, O4] to anyone (its called structure reference string) to let them compute the value of g(T) in any polynomial without having the value of T is!

- It is trusted cause the discrete logarithm value is unknown for the verifier, but prover knows it.

- Okay, lets say we have a structured reference string, but how do we know it was computed properly?
- We use bilinearity. Bilinearity has a vital role in verifying that a trusted setup was generated correctly.

**Verification of the honest trusted setup**

- In a trusted setup, we want to ensure that all participants followed protocol and generated parameters without introducing a hidden knowledge or malicious alterations.

- Use G1 and G2 elliptic curve groups and a target group Gt
- g, g^t, g^t^2, g^t^3 ... where t (tau) is a secret random value
- using bilinearity, check set up that elements are correctly formed.
  if P = g^t and Q = g^t^2 we can veify that Q is indeed t times P by checking
  e(P,P) = e (g,Q) this checks Q = P^t

## verifying a trusted setup was generated properly

# we have the reference string = G1, G1*t, G1*t^2, G1*t^3 and a O_2 value = t*G2

# we compute the pairing e(G1, G1\*t^2)

# separately e(G1*t, G1*t) and compare.

# based on the exponent property of bilinearity,

# e(G1, G1\*t^2) = e(G1, G1)^t^2

# and e(G1*t, G1*t) = e(G1, G1)^t^2 equation holds.

See code example.

**Multiparty Computation**

- We cant just assume the person who generated structured reference string actually deleted tau (t)
- IF we introduce an algorithm for multiple parties to create the srs, as long as one of them is honest then the discrete logs of the srs will remain unknown.

- First Alice generates the srs as ([On,..O2,O1,G1], O_2) and share it with Bob
- Bob verifies the srs is correct by using bilinear pairings
- Bob selects his own secret parameter l and compute a new srs like
  ([l^n*On,..., l^n-1*On-1,l^2*O2, l*O1,G1], l\*O_2)
- now we have the discrete logs as ([(tl)^n,...,(tl)^2,(tl),1],tl) if either Alice or Bob delete their secret, then its not recoverable.

**Use of trusted setup in ZK-Snarks**
Evaluating a polynomial on a structured reference string doesnt reveal information about the polynomial to the verifier and the prover doesnt know what point they are evaluating on.
