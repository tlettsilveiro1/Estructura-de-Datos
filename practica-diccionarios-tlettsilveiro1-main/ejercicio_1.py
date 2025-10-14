class Empresa:
    def __init__(self, ventas):
        self.ventas = ventas

    def modificar_venta(self, vendedor, zona, nuevo_valor): #Debe ingresarse exacto como aparece
        if vendedor in self.ventas and zona in self.ventas[vendedor]:
            self.ventas[vendedor][zona] = nuevo_valor
            print("Venta modificada con éxito.")
        else:
            print("El vendedor o la zona no existen.")

    def ventas_totales(self):
        total = 0
        for vendedor in self.ventas:
            for zona in self.ventas[vendedor]:
                total += self.ventas[vendedor][zona]
        return total

    def zona_mayores_ventas(self):
        # Sumar las ventas por zona
        zonas = {"Norte": 0, "Sur": 0, "Este": 0, "Oeste": 0}
        for vendedor in self.ventas:
            for zona in self.ventas[vendedor]:
                zonas[zona] += self.ventas[vendedor][zona]

        # Encontrar la zona con mayor venta
        max_zona = None
        max_valor = -1
        for zona in zonas:
            if zonas[zona] > max_valor:
                max_valor = zonas[zona]
                max_zona = zona

        return max_zona, max_valor



ventas = {
    "Nicolas": {"Norte": 3528, "Sur": 2400, "Este": 1200, "Oeste": 8200},
    "Daniela": {"Norte": 3824, "Sur": 6786, "Este": 5598, "Oeste": 3612},
    "Maria":   {"Norte": 8008, "Sur": 4653, "Este": 8425, "Oeste": 1000},
    "Francisco": {"Norte": 5833, "Sur": 6356, "Este": 2548, "Oeste": 1386}}
empresa = Empresa(ventas)

# Preguntar si quiere modificar
opcion = input("¿Desea modificar alguna venta? (s/n): ")
if opcion.lower() == "s":
    vendedor = input("Ingrese el nombre del vendedor: ")
    zona = input("Ingrese la zona (Norte, Sur, Este, Oeste): ")
    nuevo_valor = int(input("Ingrese el nuevo valor de venta: "))
    empresa.modificar_venta(vendedor, zona, nuevo_valor)

# Mostrar resultados
for key, value in ventas.items():
    print(key, value)
print("Ventas totales de la empresa:", empresa.ventas_totales())
zona, valor = empresa.zona_mayores_ventas()    #forma para asiganr dos variable a la vez
print("La zona con mayores ventas es:", zona, "con", valor)
