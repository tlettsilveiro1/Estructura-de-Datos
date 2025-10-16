class PalabraUtils:
    def es_palindromo(self, palabra):
        # Caso base: palabra vacía o de un solo caracter
        if len(palabra) <= 1:
            return True
        # Si los extremos no coinciden, no es palíndroma
        if palabra[0] != palabra[-1]:
            return False
        # Caso recursivo: comparar el resto de la palabra
        return self.es_palindromo(palabra[1:-1])
    
    def es_palindromo2(self, palabra, inicio=0, fin=None): #Otra forma de hacerlo, puede ser mas simple
        # Inicializamos el índice final la primera vez que se llama
        if fin is None:
            fin = len(palabra) - 1

        # Caso base: si los índices se cruzan o son iguales, es palíndroma
        if inicio >= fin:
            return True

        # Si los caracteres no coinciden, no es palíndroma
        if palabra[inicio] != palabra[fin]:
            return False

        # Llamada recursiva moviendo los índices hacia el centro
        return self.es_palindromo(palabra, inicio + 1, fin - 1)



pal_utils = PalabraUtils()
print(pal_utils.es_palindromo("reconocer"))  # True
print(pal_utils.es_palindromo("python"))    # False

print(pal_utils.es_palindromo2("reconocer"))  # True
print(pal_utils.es_palindromo2("python"))     # False