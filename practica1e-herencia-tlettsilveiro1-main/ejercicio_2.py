#Como todos los datos (elementos) dentro del archivo csv es string se puede trabajar suponiendo que la fecha
#tambien es un string con un formato especial, pero es conveniente para asegurarse que lo que ingreasa el
#usuario sea una fecha cuando agrega una fila

import csv
from functools import reduce
from datetime import datetime

class AnalizadorSUBEFuncional:
    def __init__(self, archivo):
        try:
            with open(archivo, "r", encoding="utf-8") as f:  
                reader = csv.DictReader(f)
                self.datos = list(        #Guarda todo en una lista de diccionarios
                    map(lambda fila: {   #esta funcion cumple el mismo objetivo que un for, recorre cada fila
                        "fecha": datetime.strptime(fila["indice_tiempo"], "%Y-%m-%d"),
                        "total": int(fila["total"]),
                        "colectivo": int(fila["colectivo"]),
                        "lancha": int(fila["lancha"]),
                        "subte": int(fila["subte"]),
                        "tren": int(fila["tren"])
                    }, reader)   #convierte cada fila es un diccionario de strings (con formato)
                )
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {archivo}.")
            self.datos = []
        except Exception as e:
            print(f"Error leyendo el archivo: {e}")
            self.datos = []

    def uso_maximo_por_mes(self, transporte, año):
        datos_año = list(filter(lambda x: x["fecha"].year == año, self.datos))

        # Diccionario de totales por mes usando reduce
        total_por_mes = dict(
            map(
                lambda mes: (
                    mes,
                    reduce(
                        lambda acc, x: acc + x[transporte],
                        filter(lambda x: x["fecha"].month == mes, datos_año),
                        0
                    )
                ),
                range(1, 13)
            )
        )

        mes_max = max(total_por_mes, key=lambda m: total_por_mes[m])
        return mes_max, total_por_mes[mes_max]

    def medio_mas_utilizado(self, año, mes):
        datos_mes = list(filter(lambda x: x["fecha"].year == año and x["fecha"].month == mes, self.datos))
        if not datos_mes:
            return None, 0

        medios = ["colectivo", "lancha", "subte", "tren"]
        totales = dict(map(lambda medio: (medio, reduce(lambda acc, x: acc + x[medio], datos_mes, 0)), medios))

        medio_max = max(totales.items(), key=lambda x: x[1])
        return medio_max  # devuelve tupla (medio, total)

    def promedio_mensual(self):
        años = set(map(lambda x: x["fecha"].year, self.datos))
        meses = range(1, 13)
        promedios = dict(
            map(
                lambda año_mes: (
                    año_mes,
                    reduce(
                        lambda acc, x: acc + x["total"],
                        filter(lambda x: x["fecha"].year == año_mes[0] and x["fecha"].month == año_mes[1], self.datos),
                        0
                    ) / max(len(list(filter(lambda x: x["fecha"].year == año_mes[0] and x["fecha"].month == año_mes[1], self.datos))), 1)
                ),
                ((año, mes) for año in años for mes in meses)
            )
        )
        return promedios

    def orden_por_transporte(self, año):
        datos_año = list(filter(lambda x: x["fecha"].year == año, self.datos))
        medios = ["colectivo", "lancha", "subte", "tren"]
        totales = dict(map(lambda medio: (medio, reduce(lambda acc, x: acc + x[medio], datos_año, 0)), medios))
        return sorted(totales.items(), key=lambda x: x[1])

    def tendencias_mensuales(self):
        años = set(map(lambda x: x["fecha"].year, self.datos))
        meses = range(1, 13)
        medios = ["colectivo", "lancha", "subte", "tren"]

        resumen = dict(
            map(
                lambda año_mes: (
                    año_mes,
                    dict(map(
                        lambda medio: (
                            medio,
                            reduce(
                                lambda acc, x: acc + x[medio],
                                filter(lambda x: x["fecha"].year == año_mes[0] and x["fecha"].month == año_mes[1], self.datos),
                                0
                            )
                        ),
                        medios
                    ))
                ),
                ((año, mes) for año in años for mes in meses)
            )
        )
        return resumen


if __name__ == "__main__":
    analizador = AnalizadorSUBEFuncional("total-usuarios-por-dia.csv")

    # 1. Mes con mayor uso de lancha en 2020
    mes, total = analizador.uso_maximo_por_mes("lancha", 2020)
    print(f"Mayor uso de lancha en 2020 fue en el mes {mes} con {total} viajes.")

    # 2. Medio más utilizado en marzo 2020
    medio, total = analizador.medio_mas_utilizado(2020, 3)
    print(f"En marzo 2020 el medio más usado fue {medio} con {total} viajes.")

    # 3. Promedio mensual de usuarios
    promedios = analizador.promedio_mensual()
    print("Promedios mensuales de usuarios:")
    for (año, mes), promedio in promedios.items():
        print(f"{año}-{mes:02d}: {promedio:.0f}")

    # 4. Medios ordenados por uso en 2021
    ordenados = analizador.orden_por_transporte(2021)
    print("Uso de transportes en 2021 (menor a mayor):")
    for medio, total in ordenados:
        print(f"{medio}: {total}")

    # 5. Tendencias mensuales (ejemplo para 2020 enero)
    tendencias = analizador.tendencias_mensuales()
    print("Tendencias enero 2020:", tendencias[(2020, 1)])