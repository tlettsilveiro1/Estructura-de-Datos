# Ejercicio 4 (no interactiva)
def calcular_felicidad(lista, conjuntoA, conjuntoB):
    felicidad = 0
    for x in lista:
        if x in conjuntoA:
            felicidad += 1
        elif x in conjuntoB:
            felicidad -= 1
        # Si no está en ninguno, no cambia la felicidad
    return felicidad


def main():
    # Ejemplo de datos
    lista = [1, 2, 3, 4, 5, 6, 7]
    conjuntoA = {1, 3, 5}
    conjuntoB = {2, 4, 6}

    estado_felicidad = calcular_felicidad(lista, conjuntoA, conjuntoB)
    print("Mi estado de felicidad es:", estado_felicidad)

# Ejecutamos el programa
main()
#-----------------------------------------0------------------------------------------------
# Ejercicio 4 (resolucion intectiva)
def leer_conjunto_o_lista(mensaje):
    """
    Función para leer números enteros separados por espacios y devolver un set.
    """
    while True:
        entrada = input(mensaje)
        try:
            numeros = entrada.split()
            conjunto = set()
            for num in numeros:
                n = int(num)
                conjunto.add(n)
            return conjunto
        except ValueError:
            print("Entrada inválida. Ingrese solo números enteros separados por espacios.")


def calcular_felicidad(lista, conjuntoA, conjuntoB):
    felicidad = 0
    for x in lista:
        if x in conjuntoA:
            felicidad += 1
        elif x in conjuntoB:
            felicidad -= 1
    return felicidad


def main():
    print("=== Calculadora de felicidad ===")

    lista = list(leer_conjunto_o_lista("Ingrese la lista de números (separados por espacios): "))
    conjuntoA = leer_conjunto_o_lista("Ingrese los números positivos (conjunto A): ")
    conjuntoB = leer_conjunto_o_lista("Ingrese los números negativos (conjunto B): ")

    estado_felicidad = calcular_felicidad(lista, conjuntoA, conjuntoB)
    print("\nTu estado de felicidad es:", estado_felicidad)

# Ejecutamos el programa
main()