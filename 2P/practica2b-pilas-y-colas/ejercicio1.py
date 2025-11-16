# Ejercicio 1: Implementación de la clase Pila (usando deque)
from collections import deque   # Importamos deque para manejar la pila de forma eficiente

# Clase que representa un libro
class Libro:
    def __init__(self, autor, fecha_publicacion, editorial, issn):
        self.autor = autor
        self.fecha_publicacion = fecha_publicacion
        self.editorial = editorial
        self.issn = issn

    def __str__(self):
        return f"{self.autor} | {self.fecha_publicacion} | {self.editorial} | ISSN: {self.issn}"


# Clase principal: la pila (gráficamente se ve así: Cima → [B] → [A])
# Usamos deque en lugar de nodos enlazados, pero la lógica de pila (LIFO) se mantiene igual.
class Pila:
    def __init__(self):
        self.cima = deque()   # Inicializamos la pila vacía con deque

    # Método para verificar si la pila está vacía
    def es_vacia(self):
        return len(self.cima) == 0

    # Método para apilar un libro (agregar al tope)
    def apilar(self, libro):
        # append() agrega al final del deque, que representa la "cima" de la pila
        self.cima.append(libro)
        # Hace el mismo trabajo que el enlace de nodos en la versión anterior,
        # pero internamente deque ya maneja la referencia al último elemento.

    # Método para desapilar (quitar y devolver el libro del tope)
    def desapilar(self):
        if self.es_vacia():
            print("La pila está vacía, no se puede desapilar.")
            return None
        # pop() elimina y devuelve el último elemento agregado (la cima de la pila)
        libro = self.cima.pop()
        return libro

    # Método para visualizar toda la pila
    def visualizar_pila(self):
        if self.es_vacia():
            print("La pila está vacía.")
        else:
            print("📚 Pila de libros:")
            # Recorremos el deque desde la cima hacia la base (de derecha a izquierda)
            for libro in reversed(self.cima):
                print(" ->", libro)
            # Esto reemplaza el recorrido manual de nodos en la versión anterior


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