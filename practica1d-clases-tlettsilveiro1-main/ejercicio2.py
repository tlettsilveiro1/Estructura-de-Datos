# Ejercicio 2: Modelar una computadora
# 
# En este archivo debés crear la clase Computadora siguiendo las consignas del README.
# Recordá:
# - Definir atributos relevantes en el constructor (__init__), con valores por defecto.
# - Implementar el método __str__ para mostrar la información esencial.
# - Instanciar al menos 3 computadoras con distintos valores.
# - Llevar la cuenta de computadoras creadas (usar variable de clase).
# - Implementar al menos 2 métodos de los sugeridos (updateOS, PM, addRAM, getCapacity).
# - Crear otra clase para un componente (ej: Disco, RAM, etc.) con su propio __init__, __str__ y al menos un método.
# 
# ¡No olvides probar todos los métodos y comentar tu criterio para los valores
class Computadora:
    cantidad = 0  # variable de clase para llevar la cuenta de computadoras creadas

    def __init__(self, marca="Desconocida", modelo="Desconocido", cpu="Intel i5", 
                 ram=8, storage=256, os="Windows 10", anio=2023):
        self.marca = marca
        self.modelo = modelo
        self.cpu = cpu
        self.ram = ram  # en GB
        self.storage = storage  # en GB
        self.os = os
        self.anio = anio

        Computadora.cantidad += 1  # incrementamos contador de computadoras

    def __str__(self):
        return (f"{self.marca} {self.modelo} ({self.anio})\n"
                f"CPU: {self.cpu}, RAM: {self.ram}GB, Storage: {self.storage}GB\n"
                f"Sistema operativo: {self.os}")

    # Método 1: Actualizar sistema operativo
    def updateOS(self, nuevo_os):
        self.os = nuevo_os
        print(f"Sistema operativo actualizado a {self.os} en {self.marca} {self.modelo}.")

    # Método 2: Agregar RAM
    def addRAM(self, cantidad_ram):
        self.ram += cantidad_ram
        print(f"Se agregaron {cantidad_ram}GB de RAM. Total RAM: {self.ram}GB.")

    # Método adicional opcional: mostrar capacidad de hardware
    def getCapacity(self, componente):
        if componente.lower() == "ram":
            return self.ram
        elif componente.lower() == "storage":
            return self.storage
        else:
            return print("Seleccionar 'ram' o 'storage'")

class DiscoDuro:
    def __init__(self, marca="Generic", capacidad=512, tipo="SSD"):
        self.marca = marca
        self.capacidad = capacidad
        self.tipo = tipo  # HDD o SSD

    def __str__(self):
        return f"{self.marca} {self.tipo} - {self.capacidad}GB"

    # Método: expandir capacidad
    def expandir(self, nueva_capacidad):
        if nueva_capacidad > self.capacidad:
            self.capacidad = nueva_capacidad
            print(f"Capacidad del disco duro expandida a {self.capacidad}GB")
        else:
            print("La nueva capacidad debe ser mayor a la actual.")


pc1 = Computadora(marca="Dell", modelo="Inspiron 15", cpu="Intel i7", ram=16, storage=512, os="Windows 11", anio=2022)
pc2 = Computadora(marca="Apple", modelo="MacBook Pro", cpu="M1", ram=8, storage=256, os="macOS Monterey", anio=2021)
pc3 = Computadora(marca="HP", modelo="Pavilion", cpu="AMD Ryzen 5", ram=16, storage=1024, os="Windows 10", anio=2023)
print(pc1)
print(pc2)
print(pc3)
print(f"Cantidad de computadoras creadas: {Computadora.cantidad}")

disco1 = DiscoDuro("Seagate", 512, "SSD")
print(disco1)
disco1.expandir(1024)
print(disco1)