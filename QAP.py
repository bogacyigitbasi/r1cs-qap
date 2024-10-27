## z = x^4 - 5y^2.x^2
# lets create the R1CS
# v1 == x*x
# v2 == v1*v1
# v3 == -5*y*y
# -v2 + z == v3 *v1
# witness vector w = [1, z, x, y, v1, v2, v3]

## construct the matrices
import numpy as np
L = np.array([
    [0,0,1,0,0,0,0],
    [0,0,0,0,1,0,0],
    [0,0,0,-5,0,0,0],
    [0,0,0,0,0,0,1]
])

R = np.array([
    [0,0,1,0,0,0,0],
    [0,0,0,0,1,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0]
])

O = np.array([
    [0,0,0,0,1,0,0],
    [0,0,0,0,0,1,0],
    [0,0,0,0,0,0,1],
    [0,1,0,0,0,-1,0]
])

## unit test

x=4
y =-2
v1= x*x
v2 =v1 *v1
v3 = -5*y*y
z= v3*v1 + v2

# witness
w = np.array([1, z, x, y, v1, v2, v3])
assert all (np.equal(np.matmul(L, w)*np.matmul(R, w), np.matmul(O, w)))


## end of unit test

# Finite Field using galois

import galois

GF = galois.GF(79) # picked a low prime

# lets make sure we dont have negative numbers in the arrays
# we convert negative numbers to their congruent representation
# add 79 and take mod of it

L = (L+79) % 79
R = (R+79) % 79
O = (O+79) % 79

# lets print and check
# print(L)
# print(R) # replaced -5 with 74
# print(O) # replaced -1 with 78

L_galois = GF(L)
# print(L_galois)
R_galois = GF(R)
# print(R_galois)
O_galois=GF(O)
# print(O_galois)

# [[ 0  0  1  0  0  0  0]
#  [ 0  0  0  0  1  0  0]
#  [ 0  0  0 74  0  0  0]
#  [ 0  0  0  0  0  0  1]]
# [[0 0 1 0 0 0 0]
#  [0 0 0 0 1 0 0]
#  [0 0 0 1 0 0 0]
#  [0 0 0 0 1 0 0]]
# [[ 0  0  0  0  1  0  0]
#  [ 0  0  0  0  0  1  0]
#  [ 0  0  0  0  0  0  1]
#  [ 0  1  0  0  0 78  0]]

## unit test under finite field

x = GF(4)
y = GF(-2+79)
v1 = x*x
v2 = v1*v1
v3 = GF(-5+79)*y*y

out = v3*v1 + v2

witness = GF(np.array([1, out, x, y ,v1,v2,v3]))

assert all(np.equal(np.matmul(L_galois, witness)*np.matmul(R_galois, witness), np.matmul(O_galois, witness)))


## cool we have the matrices. now its time for creating vectors from columns
# and create lagrange polynomials
# interpolating these vectors.
# v1 == x*x
# v2 == v1*v1
# v3 == -5*y*y
# -v2 + z == v3 *v1
# witness vector w = [1, z, x, y, v1, v2, v3]
# since we have 4 rows, the points we will interpolate are x = [1,2,3,4]

def interpolate_columns(col):
    xs = GF(np.array([1,2,3,4]))
    return galois.lagrange_poly(xs, col)

# numpy has a function "apply_along_axis" which is practically a loop
# iterates over columns, and collect results in an array
# axis 0 is the columns

U_polys = np.apply_along_axis(interpolate_columns, 0, L_galois)
V_polys = np.apply_along_axis(interpolate_columns, 0, R_galois)
W_polys = np.apply_along_axis(interpolate_columns, 0, O_galois)


# print(U_polys)
# print(V_polys)
# print(W_polys)

# [Poly(0, GF(79)) Poly(0, GF(79)) Poly(13x^3 + 41x^2 + 22x + 4, GF(79))
#  Poly(42x^3 + 22x^2 + 35x + 59, GF(79))
#  Poly(40x^3 + 75x^2 + 49x + 73, GF(79)) Poly(0, GF(79))
#  Poly(66x^3 + 78x^2 + 15x + 78, GF(79))]
# [Poly(0, GF(79)) Poly(0, GF(79)) Poly(13x^3 + 41x^2 + 22x + 4, GF(79))
#  Poly(39x^3 + 43x^2 + 72x + 4, GF(79))
#  Poly(27x^3 + 74x^2 + 64x + 72, GF(79)) Poly(0, GF(79)) Poly(0, GF(79))]
# [Poly(0, GF(79)) Poly(66x^3 + 78x^2 + 15x + 78, GF(79)) Poly(0, GF(79))
#  Poly(0, GF(79)) Poly(13x^3 + 41x^2 + 22x + 4, GF(79))
#  Poly(53x^3 + 76x^2 + 34x + 74, GF(79))
#  Poly(39x^3 + 43x^2 + 72x + 4, GF(79))]

## computing h(x)
# since there are 4 rows we already know t(x) = (x-1)(x-2)(x-3)(x-4)
# QAP is
# L*w x R*w = O*w + h(x)*t(x)

def inner_product_polynomials_with_witness(polys, witness):
    total = GF(0)
    for p,w in zip(polys, witness):
        total += p*w
    print(total)
    return total



term1= inner_product_polynomials_with_witness(U_polys, witness)
term2= inner_product_polynomials_with_witness(V_polys, witness)
term3= inner_product_polynomials_with_witness(W_polys, witness)

# t = (x-1)(x-2)(x-3)(x-4)
t = galois.Poly([1, 78], field = GF) * galois.Poly([1, 77], field = GF)* galois.Poly([1, 76], field = GF) * galois.Poly([1, 75], field = GF)
h = (term1 * term2 - term3) // t


assert term1 * term2 == term3 + h * t, "division has a remainder"

