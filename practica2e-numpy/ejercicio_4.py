import numpy as np

# Definir la matriz
A = np.array([
    [1, 2, 3],
    [0, 4, 5],
    [1, 0, 6]
])

# Calcular la inversa con NumPy
inversa = np.linalg.inv(A)

print("Matriz original:\n", A)
print("\nMatriz inversa:\n", inversa)