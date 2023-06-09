
# import sympy
from sympy import *

# Use sympy.eigenvals() method
matD = Matrix([[2, 0, 0],
              [0, 1, 0],
              [0, 0, -2]])
matUplusL = Matrix([[0, 1, -1],
                   [-1, 0, -1],
                   [-1, -1, 0]])

mat = matD.inv() * matUplusL
print(mat)
d = mat.eigenvals()
print(d)
a = 2.1784/2 + (1/4) * (1/(1+0.125**3) + 1/(1+0.375**3) + 1/(1+0.625**3) + 1/(1+0.875**3) + 1/(1+1.125**3) + 1/(1+1.375**3) + 1/(1+1.625**3) + 1/(1+1.875**3))
print(a)


A = Matrix([[3,2],
            [1,2]])
print(A.eigenvals())


ans = 16/(16+0.5**2) + 16/(16+1.5**2) + 16/(16+2.5**2) + 16/(16+3.5**2)
print(ans/2 + 3.13118/2)

mat = Matrix([[0, 0, 2],
              [0, 2, 0],
              [3, 0, 0]])
print(mat.transpose().inv())