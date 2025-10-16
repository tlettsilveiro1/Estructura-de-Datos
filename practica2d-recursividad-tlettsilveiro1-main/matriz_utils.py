class MatrizUtils:
    def suma_matriz(self, matriz):
        # Caso base: matriz vacía
        if len(matriz) == 0:
            return 0
        else:
            # Sumar los elementos de la primera fila
            suma_fila = self.sumar_fila(matriz[0])
            # Llamada recursiva con el resto de la matriz
            return suma_fila + self.suma_matriz(matriz[1:])

    # Método auxiliar recursivo para sumar una fila (lista)
    def sumar_fila(self, fila):
        if len(fila) == 0:
            return 0
        else:
            return fila[0] + self.sumar_fila(fila[1:])


mat_utils = MatrizUtils()
print(mat_utils.suma_matriz([[1, 2], [3, 4]]))  # 10