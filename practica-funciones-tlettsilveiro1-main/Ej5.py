def obtener_palabras_extremas(cadena: str):
    palabras = cadena.split()   # separar la cadena en palabras
    palabra_larga = max(palabras, key=len)
    palabra_corta = min(palabras, key=len)
    return [palabra_larga, palabra_corta]


def main():
    cadena = "Estructuras de datos"
    lista = obtener_palabras_extremas(cadena)
    cadena_larga = lista[0]
    cadena_corta = lista[1]
    print(cadena, cadena_larga, cadena_corta, sep="\n")
    # Debería imprimirse:
    # "Estructuras de datos"
    # "Estructuras"
    # "de"


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
