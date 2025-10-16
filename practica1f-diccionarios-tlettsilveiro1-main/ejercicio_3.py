def combinar_diccionarios(lista_diccionarios):
    resultado = {}

    for dic in lista_diccionarios:
        for clave, valor in dic.items():
            if clave not in resultado:
                resultado[clave] = []
            resultado[clave].append(valor)

    return resultado

entrada = [
    {"Pan": 22.8, "Pollo": 33.85},
    {"Mermelada": 42.5, "Pan": 23.55, "Tomate": 18.3},
    {"Pan": 28.0, "Tomate": 19.5, "Pollo": 34.6}
]

salida = combinar_diccionarios(entrada)
print(salida)