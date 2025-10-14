def reducir(cadena: str, k: int):
    while True:  #este while se va a repetir en el infinito porque nunca se puede cambiar la condicion (necesita el break)
        nueva_frase = ""
        i = 0
        cambio = False  # para saber si eliminamos algo en esta vuelta

        while i < len(cadena):
            # Contar cuántas veces se repite el caracter actual
            count = 1
            while i + count < len(cadena) and cadena[i + count] == cadena[i]:
                count += 1

            if count >= k:  # eliminamos este bloque
                cambio = True
                i += count  # saltamos todo el bloque
            else:
                nueva_frase += cadena[i]
                i += 1

        cadena = nueva_frase
        if not cambio:  # permite hacer varias veces el proceso (vueltas) y salir del while (si no sigue en el infinito)
            break
    return cadena



def main():
    cadena = "estpeeptaraestee" 
    k = 2
    cadena_reducida = reducir(cadena, k)
    print(cadena_reducida)


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
