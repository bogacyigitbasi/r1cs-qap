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

