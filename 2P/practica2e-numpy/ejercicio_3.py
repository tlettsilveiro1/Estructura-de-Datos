import numpy as np

def es_triangular_superior(matriz):
    # Convertimos a arreglo NumPy (por si viene como lista)
    matriz = np.array(matriz)
    
    # Verificamos que sea cuadrada
    if matriz.shape[0] != matriz.shape[1]: #compara los valores de la tupla (que sean iguales)
        print("La matriz no es cuadrada")
        return False
    
    # Creamos una matriz con los elementos por debajo de la diagonal principal
    debajo_diagonal = np.tril(matriz, k=-1)   # 'tril' = triangular inferior y '-1' mueve la diagonal hacia abajo
    
    # Verificamos si todos los elementos debajo de la diagonal son 0
    if np.all(debajo_diagonal == 0):
        print("Es triangular superior")
        return True
    else:
        print("No es triangular superior")
        return False


M = [
    [1, 2, 3],
    [0, 4, 5],
    [0, 0, 6]
]
es_triangular_superior(M)

M = [
    [1, 2, 3],
    [0, 4, 5],
    [7, 0, 6]
]
es_triangular_superior(M)