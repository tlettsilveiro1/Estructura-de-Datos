def imprimir_distancia_minima(palabras: list, palabra1: str, palabra2: str):
    indice1 = -1
    indice2 = -1
    min_distancia = float("inf")  # valor muy grande, para que no empiece desde 0 y pueda encontrar la solucion

    for i in range(len(palabras)):
        if palabras[i].lower() == palabra1.lower():
            indice1 = i
        if palabras[i].lower() == palabra2.lower():
            indice2 = i

        # si encontramos ambas, calculamos la distancia
        if indice1 != -1 and indice2 != -1:
            distancia = abs(indice1 - indice2)
            if distancia < min_distancia:
                min_distancia = distancia
    print(f'La distancia mínima entre "{palabra1}" y "{palabra2}" es:{min_distancia}')


def main():
    palabras=["La","materia","Estructuras","de","Datos","es","genial"]
    primera_palabra="La"
    segunda_palabra="es"
    imprimir_distancia_minima(palabras, primera_palabra, segunda_palabra)
    # Debería imprimirse:
    # La distancia mínima entre "la" y "es" es: 5
    palabras1=["La","materia","Estructuras","de","Datos","es","de","las","mas","geniales"]
    primera_palabra1="de"
    segunda_palabra1="geniales"
    imprimir_distancia_minima(palabras1, primera_palabra1, segunda_palabra1)
    # Debería imprimirse:
    # La distancia mínima entre "de" y "geniales" es: 3


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
