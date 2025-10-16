class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
    
    def __str__(self):
        siguiente = self.siguiente.dato if self.siguiente else None
        return f'{self.dato} y mi siguiente es {siguiente}'

class ListaCircularEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
    
    def agregar(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
            nuevo.siguiente = self.cabeza
        else:
            self.cola.siguiente = nuevo
            nuevo.siguiente = self.cabeza
            self.cola = nuevo
        self.tamanio += 1

    def eliminar(self, valor):
        if self.cabeza is None:
            return False

        actual = self.cabeza
        anterior = self.cola

        while True:
            if actual.dato == valor:
                if actual == self.cabeza:
                    if self.cabeza == self.cola:  # solo un nodo
                        self.cabeza = None
                        self.cola = None
                    else:
                        self.cabeza = self.cabeza.siguiente
                        self.cola.siguiente = self.cabeza
                elif actual == self.cola:
                    self.cola = anterior
                    self.cola.siguiente = self.cabeza
                else:
                    anterior.siguiente = actual.siguiente
                self.tamanio -= 1
                return True

            anterior = actual
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        return False

    def mostrar(self):
        if self.cabeza is None:
            print("Lista vacía")
            return
        actual = self.cabeza
        while True:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print("(vuelve a la cabeza)")

    def obtener_siguiente(self, valor):
        if self.cabeza is None:
            return None
        actual = self.cabeza
        while True:
            if actual.dato == valor:
                return actual.siguiente.dato
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        return None


if __name__ == "__main__":
    lista = ListaCircularEnlazada()
    lista.agregar(10)
    lista.agregar(20)
    lista.agregar(30)
    lista.agregar(40)

    lista.mostrar()  
    # 10 -> 20 -> 30 -> 40 -> (vuelve a la cabeza)

    print("Eliminar 20:", lista.eliminar(20))
    lista.mostrar()

    print("Siguiente a 30:", lista.obtener_siguiente(30))
    print("Tamaño:", lista.tamanio)