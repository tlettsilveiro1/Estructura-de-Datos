def contar_repeticiones(cadena: str, caracter: str):
    contador = 0
    for c in cadena:
        if c == caracter:
            contador += 1
    return contador


def main():
    repeticiones = contar_repeticiones("Welcome to w3resource.com", "e")
    print(f"Cantidad de veces que se repitió: {repeticiones}")
    # Debería imprimirse:
    # Cantidad de veces que se repitió: 4


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
