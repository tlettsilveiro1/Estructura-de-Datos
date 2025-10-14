def contar_simbolos(cadena: str):
    letras = 0
    numeros = 0
    especiales = 0
    
    for caracter in cadena:
        if caracter.isalpha():
            letras += 1
        elif caracter.isdigit():
            numeros += 1
        else:                       # Todo lo demás se considera carácter especial
            especiales += 1
    return [letras, numeros, especiales]


def main():
    resultado = contar_simbolos("Hola Mundo 123!@#")
    print(resultado)  # Debería imprimir [10, 3, 4]


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
