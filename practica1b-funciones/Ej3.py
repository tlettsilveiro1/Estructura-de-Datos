def cambiar_mayusculas_minusculas(cadena: str):
    nueva_cadena = ""
    for caracter in cadena:
        if caracter.islower():      
            nueva_cadena += caracter.upper()
        elif caracter.isupper():     
            nueva_cadena += caracter.lower()
        else:                        
            nueva_cadena += caracter
    return nueva_cadena
# Tambien se puede usar la funcion de cadena.swapcase() que es mas simple y devuelve lo pedido

def main():
    resultado = cambiar_mayusculas_minusculas("Hola Mundo")
    print(resultado)
    # Debería imprimirse:
    # hOLA mUNDO


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
