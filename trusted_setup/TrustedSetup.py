from py_ecc.bn128 import G1,G2, multiply, add, pairing, eq

from functools import reduce

def inner_product(points, coeffs):
    return reduce(add, map(multiply, points, coeffs))

# Trusted Setup

tau = 88
degree = 3


# tau^3, tau^2, tau, 1
structure_reference_string = [multiply(G1, tau**i) for i in range (degree, -1, -1)]
print(structure_reference_string)
## Evaluate
## p(x) = 4x^2 + 7x + 8

coeffs = [0, 4, 7,8]

poly_at_tau = inner_product(structure_reference_string, coeffs)
print(poly_at_tau)


## verifying a trusted setup was generated properly
# we have the reference string = G1, G1*t, G1*t^2, G1*t^3 and a O value = t*G2
# we compute the pairing e(G1, G1*t^2)
# separately e(G1*t, G1*t) and compare.
# based on the exponent property of bilinearity,
# e(G1, G1*t^2) = e(G1, G1)^t^2
# and  e(G1*t, G1*t) = e(G1, G1)^t^2 equation holds.


pairing_left = pairing(multiply(G2, tau), multiply(G1, tau**2))
pairing_right = pairing(multiply(G2,tau), multiply(G1,tau))

assert pairing_right == pairing_right, "verification failed, ceremony is not trusted"
