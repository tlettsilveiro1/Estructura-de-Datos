import numpy as np

def son_vectores_iguales(v1, v2):
    # Convertimos las listas a arrays de NumPy
    arr1 = np.array(v1)
    arr2 = np.array(v2)

    # Elevamos al cuadrado el primero y el segundo, el "**" significa elevado
    cuadrado1 = arr1 ** 2
    cuadrado2 = arr2 ** 2

    # Ordenamos ambos (para que no importe el orden)
    cuadrado1_ordenado = np.sort(cuadrado1)
    cuadrado2_ordenado = np.sort(cuadrado2)

    # Comparamos: uno debe ser igual al cuadrado del otro
    print(np.array_equal(cuadrado1_ordenado, np.sort(arr2)) or np.array_equal(cuadrado2_ordenado, np.sort(arr1)))


vectora = [121, 144, 19, 161, 19, 144, 19, 11] 
vectorb = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

son_vectores_iguales(vectora, vectorb)

vectora = [121, 144, 19, 161, 19, 144, 9, 11] 
vectorb = [121, 14641, 20736, 361, 25, 361, 20736, 361]

son_vectores_iguales(vectora, vectorb)