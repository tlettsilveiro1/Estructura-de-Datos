def comprimir_y_revertir_hexa(cadena: str):
    if not cadena:  # caso cadena vacía (quiere decir que la cadena es FALSE)
        return ""
    
    bloques = []
    contador = 1

    for i in range(1, len(cadena)):
        if cadena[i] == cadena[i - 1]:
            contador += 1
        else:
            bloques.append(format(contador, "x") + cadena[i - 1])
            contador = 1
    bloques.append(format(contador, "x") + cadena[-1]) # último grupo

    # ahora invertimos el orden de los BLOQUES
    bloques.reverse()

    # unimos en una sola cadena
    return "".join(bloques)

def main():
    frase = "aaaaaaaaaaa"
    salida = comprimir_y_revertir_hexa(frase)
    print(salida)
    # Debería imprimirse:
    # "ba"
    frase = "abc"
    salida = comprimir_y_revertir_hexa(frase)
    print(salida)
    # Debería imprimirse:
    # "1c1b1a"


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
