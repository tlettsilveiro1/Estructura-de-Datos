def comparar_sumas(Matriz):
    filas = len(Matriz)
    columnas = len(Matriz[0])

    # 1️⃣ Calcular sumas de filas
    suma_filas = []
    for i in range(filas):
        suma = 0
        for j in range(columnas):
            suma += Matriz[i][j]
        suma_filas.append(suma)

    # 2️⃣ Calcular sumas de columnas
    suma_columnas = []
    for j in range(columnas):
        suma = 0
        for i in range(filas):
            suma += Matriz[i][j]
        suma_columnas.append(suma)

    # 3️⃣ Mostrar las sumas (opcional, solo para entender)
    print("Suma filas =", suma_filas)
    print("Suma columnas =", suma_columnas)

    # 4️⃣ Buscar coincidencias
    for i in range(len(suma_filas)):
        for j in range(len(suma_columnas)):
            if suma_filas[i] == suma_columnas[j]:
                print("La suma de fila", i + 1, "es igual a la suma de la columna", j + 1)
                return  # terminamos al encontrar la primera coincidencia

    # 5️⃣ Si no hay coincidencias
    print("Ninguna suma de filas es igual a la suma de ninguna de las columnas")


Matriz = [[50, 75, 46],
          [22, 80, 125]]
comparar_sumas(Matriz)

Matriz = [[50, 75, 46],
          [22, 80, 65]]
comparar_sumas(Matriz)