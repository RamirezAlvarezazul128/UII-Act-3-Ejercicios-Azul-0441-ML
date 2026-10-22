# Ramirez Azul NC 0441
# Array indexing in NumPy
import numpy as np
n0441 = np.array([10, 20, 30, 40, 50])
print(n0441)
print(n0441[0])
print(n0441[3])
print(n0441[-1])
print(n0441[-2])
print("----------------------------------------")
n0441 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(n0441)
print(n0441[0, 0])
print(n0441[1, 2])
print(n0441[-1, -1])
print(n0441[-2, -2])
print("----------------------------------------")
# 3D array 2x(2x3)
n0441 = np.array([
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
 #1   
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
])
print(n0441)
print(n0441[0,0,0])
print(n0441[1,1,2])
print(n0441[-1,-1,-2])
print("Ramirez Azul NC 0441")









