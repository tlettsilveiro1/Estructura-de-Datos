class Cancion:
    def __init__(self, titulo, artista, anio):
        self.titulo = titulo
        self.artista = artista
        self.anio = anio
        self.siguiente = None

    def __str__(self):
        return f"{self.titulo} - {self.artista} ({self.anio})"

class ListaReproduccion:
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0

    def agregar(self, titulo, artista, anio):
        """Agrega una canción al final de la lista"""
        nueva_cancion = Cancion(titulo, artista, anio)
        if self.cabeza is None:
            self.cabeza = nueva_cancion
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva_cancion
        self.tamanio += 1

    def eliminar(self, titulo):
        """Elimina la primera canción que coincida con el título"""
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.titulo == titulo:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                self.tamanio -= 1
                print(f"Canción '{titulo}' eliminada.")
                return True
            anterior = actual
            actual = actual.siguiente

        print(f"No se encontró la canción '{titulo}'.")
        return False

    def mostrar(self):
        """Muestra todas las canciones en la lista"""
        if self.cabeza is None:
            print("La lista de reproducción está vacía.")
            return
        actual = self.cabeza
        while actual:
            print(actual)
            actual = actual.siguiente

    def obtener_cancion(self, titulo):
        """Devuelve la canción cuyo título coincide"""
        actual = self.cabeza
        while actual:
            if actual.titulo == titulo:
                return actual
            actual = actual.siguiente
        return None


if __name__ == "__main__":
    playlist = ListaReproduccion()

    playlist.agregar("Bohemian Rhapsody", "Queen", 1975)
    playlist.agregar("Imagine", "John Lennon", 1971)
    playlist.agregar("Smells Like Teen Spirit", "Nirvana", 1991)

    print("Lista de reproducción:")
    playlist.mostrar()

    print("\nEliminar 'Imagine':")
    playlist.eliminar("Imagine")
    playlist.mostrar()

    print("\nBuscar 'Bohemian Rhapsody':")
    cancion = playlist.obtener_cancion("Bohemian Rhapsody")
    if cancion:
        print("Encontrada:", cancion)