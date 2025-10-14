def imprimir_bitonica_inversa(cadena: str):
    no=""
    if len(cadena) < 3:
        no="no" # mínimo 3 caracteres para bajar y luego subir

    i = 1
    
    # 1) Parte decreciente
    while i < len(cadena) and cadena[i] < cadena[i-1]:
        i += 1

    # Si no bajó nada o bajó toda la cadena, no es válida
    if i == 1 or i == len(cadena):
        no="no"
    
    # 2) Parte creciente
    while i < len(cadena) and cadena[i] > cadena[i-1]:
        i += 1

    # 3) Si terminó justo al final, es bitónica inversa
    if not i == len(cadena):
        no="no"
    print(f'La cadena "{cadena}" {no} es bitónica inversa')


def main():
    cadena = "zyxbcde"
    imprimir_bitonica_inversa(cadena)
    # Debería imprimirse:
    # La cadena "zyxbcde" es bitónica inversa
    cadena = "abcdwef"
    imprimir_bitonica_inversa(cadena)
    # Debería imprimirse:
    # La cadena "abcdwef" no es bitónica inversa
    cadena = "86479"
    imprimir_bitonica_inversa(cadena)
    # Debería imprimirse:
    # La cadena "86479" es bitónica inversa


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
