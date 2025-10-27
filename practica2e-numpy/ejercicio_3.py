def es_triangular_superior(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    # 1️⃣ Comprobar si es cuadrada
    if filas != columnas:
        print("La matriz no es cuadrada")
        return

    # 2️⃣ Verificar los elementos por debajo de la diagonal principal
    for i in range(filas):
        for j in range(columnas):
            # condición: estamos debajo de la diagonal cuando i > j
            if i > j and matriz[i][j] != 0:
                print("No es triangular superior")
                return

    # 3️⃣ Si no se encontró ningún número debajo de la diagonal ≠ 0
    print("Es triangular superior")


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