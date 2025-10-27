def imprimir_contadores(cadena: str):
    contador = {}   # diccionario vacío
    cadena=cadena.lower()  #toma como igual `E´ y `e´
    for caracter in cadena:
        if caracter != " ":          # no contar espacios
            if caracter in contador: # si ya lo vimos, sumamos 1
                contador[caracter] += 1
            else:                    # si aparece por primera vez
                contador[caracter] = 1
    # Mostrar resultados
    for caracter, cantidad in contador.items():
        print(caracter, cantidad)


def main():
    cadena = "Estructuras de datos"
    imprimir_contadores(cadena)
    # Debería imprimirse:
    # e     2
    # s     3
    # t     3
    # r     2
    # u     2
    # a     2
    # d     2
    # o     1


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
