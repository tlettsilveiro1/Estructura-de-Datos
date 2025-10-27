# Ejercicio 1: Implementación de la clase Pila
# Clase que representa un libro
class Libro:
    def __init__(self, autor, fecha_publicacion, editorial, issn):
        self.autor = autor
        self.fecha_publicacion = fecha_publicacion
        self.editorial = editorial
        self.issn = issn

    def __str__(self):
        return f"{self.autor} | {self.fecha_publicacion} | {self.editorial} | ISSN: {self.issn}"


# Clase que representa un nodo de la pila
class Nodo:
    def __init__(self, dato):
        self.dato = dato     # guarda el libro
        self.siguiente = None  # referencia al nodo inferior


# Clase principal: la pila (graficamente se ve asi: Cima → [B] → [A] → None)
class Pila:
    def __init__(self):
        self.cima = None   # referencia al nodo superior

    # Método para verificar si la pila está vacía
    def es_vacia(self):
        return self.cima is None

    # Método para apilar un libro (agregar al tope)
    def apilar(self, libro):
        nuevo_nodo = Nodo(libro)
        nuevo_nodo.siguiente = self.cima  #Hace que el nuevo nodo apunte al nodo que antes era la cima.
        self.cima = nuevo_nodo            #Ahora el nuevo es la cima

    # Método para desapilar (quitar y devolver el libro del tope)
    def desapilar(self):
        if self.es_vacia():
            print("La pila está vacía, no se puede desapilar.")
            return None
        libro = self.cima.dato            # obtener el libro de la cima
        self.cima = self.cima.siguiente   # mover la cima hacia abajo
        return libro

    # Método para visualizar toda la pila
    def visualizar_pila(self):
        if self.es_vacia():
            print("La pila está vacía.")
        else:
            actual = self.cima
            print("📚 Pila de libros:")
            while actual is not None:
                print(" ->", actual.dato)
                actual = actual.siguiente



# Crear algunos libros
libro1 = Libro("Gabriel García Márquez", 1967, "Sudamericana", "12345678")
libro2 = Libro("Julio Cortázar", 1963, "Alianza", "87654321")
libro3 = Libro("Isabel Allende", 1982, "Seix Barral", "11223344")

# Crear la pila e ir apilando libros
pila_biblioteca = Pila()
pila_biblioteca.apilar(libro1)
pila_biblioteca.apilar(libro2)
pila_biblioteca.apilar(libro3)

# Visualizar la pila
pila_biblioteca.visualizar_pila()

# Desapilar un libro
print("\nDesapilando un libro...")
libro_removido = pila_biblioteca.desapilar()
print("Libro removido:", libro_removido)

# Visualizar nuevamente la pila
print("\nEstado actual de la pila:")
pila_biblioteca.visualizar_pila()