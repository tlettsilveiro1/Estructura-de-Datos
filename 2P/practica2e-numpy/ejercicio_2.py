import numpy as np

def comparar_sumas_numpy(M):
    # Convertir la lista en un array NumPy, no olvidar (para que funcionen las funciones)
    matriz = np.array(M)
    
    # 1️⃣ Calcular sumas por fila y por columna
    suma_filas = np.sum(matriz, axis=1)     # axis=1 → suma horizontal (por fila)
    suma_columnas = np.sum(matriz, axis=0)  # axis=0 → suma vertical (por columna)
    
    # 2️⃣ Mostrar las sumas (para verificar)
    print("Suma filas =", suma_filas)
    print("Suma columnas =", suma_columnas)
    
    # 3️⃣ Buscar coincidencias entre alguna fila y alguna columna
    for i in range(len(suma_filas)):
        for j in range(len(suma_columnas)):
            if suma_filas[i] == suma_columnas[j]:
                print(f"La suma de fila {i+1} es igual a la suma de la columna {j+1}")
                return
    
    # 4️⃣ Si no hay coincidencias
    print("Ninguna suma de filas es igual a la suma de ninguna de las columnas")


Matriz = [[50, 75, 46],
          [22, 80, 125]]
comparar_sumas_numpy(Matriz)

Matriz = [[50, 75, 46],
          [22, 80, 65]]
comparar_sumas_numpy(Matriz)