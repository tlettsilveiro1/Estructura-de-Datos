class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return f"{self.nombre} {self.apellido} (DNI: {self.dni})"

class Estudiante(Persona):
    def __init__(self, nombre, apellido, dni, legajo, carrera, materias):
        super().__init__(nombre, apellido, dni)
        self.legajo = legajo
        self.carrera = carrera
        self.materias = materias  # lista de materias
        self.promedio = self.calcular_promedio()

    def calcular_promedio(self):
        """
        Calcula un promedio ficticio entre 1 y 10 para cada materia.
        En la práctica, podría recibir las notas reales.
        """
        if not self.materias:
            return 0
        import random
        return round(sum(random.randint(1,10) for _ in self.materias)/len(self.materias),2)

    def __str__(self):
        materias_str = ", ".join(self.materias)
        return f"{self.nombre} {self.apellido} | Legajo: {self.legajo} | Carrera: {self.carrera} | Materias: [{materias_str}] | Promedio: {self.promedio}"


class NodoEstudiante:
    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, estudiante):
        """ Agrega estudiantes ordenados alfabeticamente por apellido """ # "suponer que en la lista esta Ana(cabeza) y Carlos"
        nuevo_nodo = NodoEstudiante(estudiante) #"Beatriz"
        # 1️⃣ Caso 1: lista vacía o insertar al inicio
        if self.cabeza is None or estudiante.apellido.lower() < self.cabeza.estudiante.apellido.lower(): # "Beatriz < Ana"
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            return
        # 2️⃣ Caso 2: recorrer para encontrar la posición correcta, la primera condicion esta paraque pueda ir ultimo 
        actual = self.cabeza #"Ana"
        while actual.siguiente and actual.siguiente.estudiante.apellido.lower() < estudiante.apellido.lower(): #"Carlos" y "Carlos < Beatriz"
            actual = actual.siguiente
        # 3️⃣ Insertar después de "actual"
        nuevo_nodo.siguiente = actual.siguiente #"Carlos"
        actual.siguiente = nuevo_nodo #"beatriz", aunque sea una var. local se pueden hacer cambios permanentes ya que es una referencia al nodo (no copia)

    def eliminar(self, legajo):
        """ Elimina estudiante dado su legajo """
        actual = self.cabeza
        anterior = None #Necesario guardar el anterior para hacer la coneccion entre nodos cuando se elimina

        while actual:
            if actual.estudiante.legajo == legajo:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                print(f"Estudiante con legajo {legajo} eliminado.")
                return True #El 'True' no es necesario, ya que cuando se ejecuta no se asigna a ninguna variable
            anterior = actual
            actual = actual.siguiente
        print(f"No se encontró estudiante con legajo {legajo}.")
        return False #El 'False' no es necesario, ya que cuando se ejecuta no se asigna a ninguna variable

    def mostrar_materias_promedio(self):
        """ Muestra la materia y el promedio de todos los estudiantes """
        actual = self.cabeza
        while actual:
            print(f"{actual.estudiante.apellido}, {actual.estudiante.nombre} | Materias: {actual.estudiante.materias} | Promedio: {actual.estudiante.promedio}")
            actual = actual.siguiente

    def mostrar_estudiantes(self):
        """ Muestra la información completa de cada estudiante """
        actual = self.cabeza
        while actual:
            print(actual.estudiante)
            actual = actual.siguiente


if __name__ == "__main__":
    lista = ListaEnlazada()

    est1 = Estudiante("Ana", "Gonzalez", "12345678", 101, "Ingeniería", ["Matemática", "Física"])
    est2 = Estudiante("Juan", "Alvarez", "23456789", 102, "Lic. Sistemas", ["Programación", "Algoritmos"])
    est3 = Estudiante("Luis", "Fernandez", "34567890", 103, "Ingeniería", ["Química", "Matemática"])

    lista.agregar(est1)
    lista.agregar(est2)
    lista.agregar(est3)

    print("Lista de estudiantes (ordenada por apellido):")
    lista.mostrar_estudiantes()

    print("\nPromedio y materias de los estudiantes:")
    lista.mostrar_materias_promedio()

    print("\nEliminar estudiante con legajo 102:")
    lista.eliminar(102)
    lista.mostrar_estudiantes()