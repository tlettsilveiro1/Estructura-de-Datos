def permutacion_posible(cadena1, cadena2):
    ordenada1 = sorted(cadena1)
    ordenada2 = sorted(cadena2)

    # Caso 1: ordenada1 >= ordenada2
    mayor_igual_1 = True
    for i in range(len(ordenada1)):
        if ordenada1[i] < ordenada2[i]:   # Si en algún índice falla, es falso
            mayor_igual_1 = False
            break

    # Caso 2: ¿ordenada2 >= ordenada1?
    mayor_igual_2 = True
    for i in range(len(ordenada1)):
        if ordenada2[i] < ordenada1[i]:   # Si en algún índice falla, es falso
            mayor_igual_2 = False
            break

    return mayor_igual_1 or mayor_igual_2


def main():
    cadena1 = "adb"
    cadena2 = "cda"
    salida = permutacion_posible(cadena1, cadena2)
    print(cadena1, cadena2, salida, sep="\n")
    # Debería imprimirse:
    # "adb"
    # "adc"
    # True
    cadena1 = "gfg"
    cadena2 = "agd"
    salida = permutacion_posible(cadena1, cadena2)
    print(salida)
    # Debería imprimirse:
    # True



# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
