# Este archivo corresponde al Ejercicio 1 de la guía práctica sobre Clases.
# Aquí deberás implementar la clase Camion y resolver los puntos a, b, c, d y f según las consignas
##########################----------------------------------------#################################
# a) Respuesta al codigo dado
#class Camion:
#    def __init__(self, marca, modelo):
#        self.patente = patente
#        self.marca = marca
#        self.carga = carga
#        self.anio = anio

#    def __str__(self):
#        return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"

#El constructor (__init__) recibe marca y modelo pero intenta usar variables patente, carga y anio que no existen.
##########################----------------------------------------#################################
# b) Correccion del codigo dado
class Camion:
    patentes_registradas = set()
    def __init__(self, patente, marca, carga, anio):
         # usamos la validación antes de registrar
        self.patente = self.validar_patente(patente)
        self.marca = marca
        self.carga = carga
        self.anio = anio
        Camion.patentes_registradas.add(patente)
    
    def __str__(self):
        return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"
    
    def __eq__(self, otro):    #Metodo para comparar dos objetos de la clase Camion
        return (self.patente == otro.patente and
                self.marca == otro.marca and
                self.carga == otro.carga and
                self.anio == otro.anio)

    def validar_patente(self, patente):
        """Valida si la patente ya está registrada"""
        if patente in self.patentes_registradas:
            raise ValueError(f'Ya existe un camión con la patente {patente}')
        return patente

furgon1 = Camion("ABC123", "Mercedes", 1000, 2020)
furgon2 = furgon1   #Como se crea el objeto usando la clase si da error
furgon3 = Camion("DEF456", "Volvo", 2000, 2021)
#furgon4 = Camion("ABC123", "Mercedes", 1000, 2020)

#print(furgon1 == furgon2)
#print(furgon1 is furgon2)
#print(furgon3 == furgon4)
#print(furgon3 is furgon4)
#print(furgon1 == furgon4)  #Inicialmente da False pq son distintos objetos en memoria (aunque tengan mismos datos)
##########################----------------------------------------#################################
#c) ¿Qué atributo hace único a nuestros objetos? Identificá el atributo que hace único al objeto Camion y modificá el 
# código para que la comparación de dos objetos de la clase Camion devuelva True cuando ese atributo sea igual.

#El atributo que hace unico a cada camion es la patente, ya que no pueden existir dos camiones con la misma patente.
#Modifique el metodo __eq__ para que compare solo la patente (sea mas eficiente).
#    def __eq__(self, otro):
#        return self.patente == otro.patente
##########################----------------------------------------#################################
#d) Si dos personas tienen el mismo DNI, entonces... ¡Son la misma persona! ¿Cómo evitarías asignar el mismo DNI a dos
# personas distintas? Siguiendo esta analogía, adaptá el código anterior para el caso de los camiones.

#  usamos la validación de la patente antes de registrar
#    def validar_patente(self, patente):
#        if patente in self.patentes_registradas:
#            raise ValueError(f'Ya existe un camión con la patente {patente}')
#        return patente
##########################----------------------------------------#################################
#f) Creacion del Menu
flota = [furgon1, furgon3]  # inicializamos con tus objetos existentes

def registrar_camion(): #Como esta escrito el codigo, si se repite la patente da error a lo ultimo
    try:
        patente = input("Ingrese la patente: ")
        marca = input("Ingrese la marca: ")
        carga = int(input("Ingrese la carga: "))
        anio = int(input("Ingrese el año: "))
        camion = Camion(patente, marca, carga, anio)
        flota.append(camion)
        print("Camión registrado correctamente.")
    except ValueError as e:
        print(f"Error: {e}")

def modificar_carga():
    patente = input("Ingrese la patente del camión a modificar: ")
    encontrado = False
    for camion in flota:
        if camion.patente == patente:
            nueva_carga = int(input("Ingrese la nueva carga: "))
            camion.carga = nueva_carga
            print("Carga actualizada.")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró un camión con esa patente.")

def mostrar_camiones():
    # ordenar del más antiguo al más moderno
    flota.sort(key=lambda c: c.anio)
    for camion in flota:
        print(camion)
        print("-"*20)

def mostrar_marca_mas_frecuente():
    conteo = {}
    for camion in flota:
        if camion.marca in conteo:
            conteo[camion.marca] += 1
        else:
            conteo[camion.marca] = 1
    # encontrar la marca con mayor cantidad
    max_cantidad = 0
    marca_max = None
    for marca in conteo:
        if conteo[marca] > max_cantidad:
            max_cantidad = conteo[marca]
            marca_max = marca
    print(f"La marca más registrada es {marca_max} con {max_cantidad} camiones.")

# Menú principal
def Menu():
    while True:
        print("\n--- Menú Camiones ---")
        print("1. Registrar un nuevo camión")
        print("2. Modificar la carga de un camión")
        print("3. Mostrar lista de camiones (del más antiguo al más moderno)")
        print("4. Mostrar marca más registrada")
        print("5. Salir")
    
        opcion = input("Seleccione una opción: ")
    
        if opcion == "1":
            registrar_camion()
        elif opcion == "2":
            modificar_carga()
        elif opcion == "3":
            mostrar_camiones()
        elif opcion == "4":
            mostrar_marca_mas_frecuente()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

Menu()
