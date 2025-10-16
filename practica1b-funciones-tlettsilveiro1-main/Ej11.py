def eliminar_repetidos(lista: list):
    lista_sin_repetidos = []
    for elemento in lista:
        if elemento not in lista_sin_repetidos:
            lista_sin_repetidos.append(elemento)
    return lista_sin_repetidos


def main():
    lista_inicial = [1, 3, 45, 23, 0, 0, 45]
    while True:
        numero = int(input("Introduce un número (negativo para terminar): "))
        if numero < 0:
            break #Se pone el break antes de agregar el numero para salir de while antes de agregar el numero
        lista_inicial.append(numero)
    lista_sin_repetidos = eliminar_repetidos(lista_inicial)
    print(lista_sin_repetidos)
    # Debería imprimirse:
    # [1, 3, 45, 23, 0]


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
