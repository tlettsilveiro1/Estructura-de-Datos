# Ejercicio 4: Atención de pacientes en consultorio
# Clase que representa una cola de pacientes
class ColaDePacientes:
    def __init__(self):
        self.cola = []  # Usamos una lista para almacenar los nombres

    # Agregar un nuevo paciente al final de la cola
    def encolar(self, nombre):
        self.cola.append(nombre)
        print(f"✅ Paciente '{nombre}' agregado a la cola.")

    # Atender al siguiente paciente (quitar el primero de la lista)
    def proximo_paciente(self):
        if self.es_vacia():
            print("🏥 No hay pacientes en espera.")
            return None
        siguiente = self.cola.pop(0)
        print(f"➡️ Llamando al paciente: {siguiente}")
        return siguiente

    # Verificar si la cola está vacía
    def es_vacia(self):
        return len(self.cola) == 0

    # Mostrar todos los pacientes en espera
    def mostrar_cola(self):
        if self.es_vacia():
            print("🏥 No hay pacientes en la sala de espera.")
        else:
            print("\n👥 Pacientes en espera:")
            for i in range(len(self.cola)):
                print(f"{i+1}. {self.cola[i]}")
            print()



def menu():
    print("\n--- SISTEMA DE COLA DE PACIENTES ---")
    print("1. Ingresar nuevo paciente")
    print("2. Atender al próximo paciente")
    print("3. Mostrar pacientes en espera")
    print("4. Salir")

# Crear la cola de pacientes
cola = ColaDePacientes()

# Bucle principal
while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del paciente: ")
        cola.encolar(nombre)

    elif opcion == "2":
        cola.proximo_paciente()

    elif opcion == "3":
        cola.mostrar_cola()

    elif opcion == "4":
        print("👋 Saliendo del sistema...")
        break

    else:
        print("❌ Opción no válida. Intente nuevamente.")