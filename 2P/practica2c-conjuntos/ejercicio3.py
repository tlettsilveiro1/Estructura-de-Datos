# Ejercicio 3 (resolucion no interactiva)
def calculador_de_conjuntos(operaciones):
    for operacion in operaciones:
        nombre_operacion = operacion[0].lower()  # "union", "interseccion" o "diferencia"
        conjunto1 = operacion[1]
        conjunto2 = operacion[2]

        if nombre_operacion == "union":
            resultado = conjunto1.union(conjunto2)
        elif nombre_operacion == "interseccion":
            resultado = conjunto1.intersection(conjunto2)
        elif nombre_operacion == "diferencia":
            resultado = conjunto1.difference(conjunto2)
        else:
            print("Operación no reconocida:", nombre_operacion)
            continue  # Saltar a la siguiente operación

        print(resultado)

operaciones = [
    ["union", {1, 2, 3}, {3, 4, 5}],
    ["interseccion", {1, 2, 3}, {3, 4, 5}],
    ["diferencia", {1, 2, 3}, {3, 4, 5}]
]
calculador_de_conjuntos(operaciones)

#-----------------------------------------0------------------------------------------------
# Ejercicio 3 (resolucion intectiva)
def leer_conjunto(mensaje):
    """
    Función para leer un conjunto de números enteros no negativos desde el usuario.
    Se ingresa como números separados por espacios.
    """
    while True:
        entrada = input(mensaje)
        try:
            numeros = entrada.split()
            conjunto = set()
            for num in numeros:
                n = int(num)
                if n < 0:
                    raise ValueError("Solo se permiten enteros no negativos.")
                conjunto.add(n)
            return conjunto
        except ValueError as e:
            print("Entrada inválida. Intente nuevamente:", e)


def calculador_interactivo():
    while True:
        print("\n--- Calculador de conjuntos ---")
        print("Operaciones disponibles: union, interseccion, diferencia")
        operacion = input("Ingrese la operación (o 'salir' para terminar): ").lower()
        if operacion == "salir":
            print("Finalizando calculador...")
            break
        if operacion not in ["union", "interseccion", "diferencia"]:
            print("Operación inválida. Intente nuevamente.")
            continue

        conjunto1 = leer_conjunto("Ingrese los elementos del primer conjunto (separados por espacios): ")
        conjunto2 = leer_conjunto("Ingrese los elementos del segundo conjunto (separados por espacios): ")

        if operacion == "union":
            resultado = conjunto1.union(conjunto2)
        elif operacion == "interseccion":
            resultado = conjunto1.intersection(conjunto2)
        elif operacion == "diferencia":
            resultado = conjunto1.difference(conjunto2)

        print("Resultado:", resultado)


# Ejecutar el calculador interactivo
calculador_interactivo()