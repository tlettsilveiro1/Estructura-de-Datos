import csv
from ejercicio_3 import *
class RepositorioCSV:
    def __init__(self, archivo):
        self.archivo = archivo

    def guardar(self, datos):
        datos = combinar_diccionarios(datos)
        max_len = max(len(valores) for valores in datos.values()) #da el largo maximo de todas las lista 
        with open(self.archivo, "w", newline="") as f:
            writer = csv.writer(f)
            for clave, valores in datos.items():
                fila = [clave] + valores[:]  # copiamos lista
                # Completar con ceros si faltan columnas
                while len(fila) < max_len + 1:  # +1 porque está la clave
                    fila.append(0)
                writer.writerow(fila)

    def leer(self):
        resultado = {}
        with open(self.archivo, "r", newline="") as f:
            reader = csv.reader(f)
            for fila in reader:
                clave = fila[0]
                # Convertir a float y descartar ceros de relleno al final
                valores = [float(x) for x in fila[1:] if float(x) != 0.0]
                resultado[clave] = valores
        return resultado


entrada = [
    {"Pan": 22.8, "Pollo": 33.85},
    {"Mermelada": 42.5, "Pan": 23.55, "Tomate": 18.3},
    {"Pan": 28.0, "Tomate": 19.5, "Pollo": 34.6}]

repo = RepositorioCSV("productos.csv")

# Guardar
repo.guardar(entrada)
print("✅ Archivo CSV guardado.")

# Leer
salida = repo.leer()
print("📊 Diccionario reconstruido:")
print(salida)