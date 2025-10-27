#usando la funcion de la libreria
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8, 9],
              [1, 2, 3]])

C = A + B

print("Suma de matrices con NumPy:\n", C)