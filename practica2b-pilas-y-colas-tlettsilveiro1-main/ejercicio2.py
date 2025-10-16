# Ejercicio 2: Implementación de la clase Cola
# Clase que representa a una persona que espera para votar
class Persona:
    def __init__(self, nombre, dni, mesa):
        self.nombre = nombre
        self.dni = dni
        self.mesa = mesa

    def __str__(self):
        return f"{self.nombre} (DNI: {self.dni}, Mesa: {self.mesa})"


# Clase que representa una cola usando una lista (graficamente se ve asi:  [A](frente) — [B] — [C](Final) )
class Cola:
    def __init__(self):
        self.elementos = []  # lista interna que guarda las personas

    # Agrega una persona al final de la cola
    def encolar(self, persona):
        self.elementos.append(persona)

    # Elimina y devuelve la primera persona de la cola
    def desencolar(self):
        if self.es_vacia():
            print("La cola está vacía, no hay nadie para atender.")
            return None
        return self.elementos.pop(0)

    # Devuelve True si la cola está vacía
    def es_vacia(self):
        return len(self.elementos) == 0

    # Muestra el contenido actual de la cola
    def visualizar_cola(self):
        if self.es_vacia():
            print("La cola está vacía.")
        else:
            print("🧍‍♀️🧍‍♂️ Cola de personas esperando para votar:")
            for persona in self.elementos:
                print(" ->", persona)

    # Devuelve la cantidad de personas en la cola
    def longitud(self):
        return len(self.elementos)



# Crear personas
p1 = Persona("Juan Pérez", 40123456, 12)
p2 = Persona("María Gómez", 38999888, 12)
p3 = Persona("Carlos Díaz", 37654321, 12)

# Crear la cola e ir encolando personas
cola_votacion = Cola()
cola_votacion.encolar(p1)
cola_votacion.encolar(p2)
cola_votacion.encolar(p3)

# Visualizar la cola actual
cola_votacion.visualizar_cola()

# Desencolar una persona (la primera en la fila)
print("\nAtendiendo a la primera persona...")
persona_atendida = cola_votacion.desencolar()
print("Persona atendida:", persona_atendida)

# Mostrar nuevamente la cola
print("\nEstado actual de la cola:")
cola_votacion.visualizar_cola()

# Mostrar la cantidad actual de personas
print("\nCantidad de personas en la cola:", cola_votacion.longitud())