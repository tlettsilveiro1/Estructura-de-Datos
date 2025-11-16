# Ejercicio 6: Sublista más larga de números consecutivos (no se usa pilas, colas ni tuplas)
def sublista_consecutivos_mas_larga(lista):
    if len(lista) == 0:
        return []

    sublista_actual = [lista[0]]   # primera sublista
    sublista_mas_larga = [lista[0]]

    # recorrer desde el segundo elemento
    for i in range(1, len(lista)):
        if lista[i] == lista[i - 1] + 1:
            # si es consecutivo, agregar a la sublista actual
            sublista_actual.append(lista[i])
        else:
            # si no es consecutivo, reiniciar
            if len(sublista_actual) > len(sublista_mas_larga):
                sublista_mas_larga = sublista_actual
            sublista_actual = [lista[i]]

    # última comparación fuera del bucle
    if len(sublista_actual) > len(sublista_mas_larga):
        sublista_mas_larga = sublista_actual

    return sublista_mas_larga



lista1 = [1, 2, 3, 10, 11, 12, 13, 2, 3]
lista2 = [5, 6, 7, 8, 1, 2, 3]
lista3 = [10, 9, 8, 7]  # sin secuencias crecientes
lista4 = []  # lista vacía

print(sublista_consecutivos_mas_larga(lista1))  # [10, 11, 12, 13]
print(sublista_consecutivos_mas_larga(lista2))  # [5, 6, 7, 8]
print(sublista_consecutivos_mas_larga(lista3))  # [10]
print(sublista_consecutivos_mas_larga(lista4))  # []