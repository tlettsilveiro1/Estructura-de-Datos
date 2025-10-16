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

    def append(self, dato):  
        """ Explicacion de que hace el metodo
        Inserta un nuevo nodo inmediatamente después del primer nodo que contiene `dato`.
        Solicita el valor del nuevo nodo por input().
        Devuelve True si se insertó, False si la lista está vacía o no se encontró `dato`.
        """
        if self.cabeza is None:
            print("La lista está vacía")
            return False

        actual = self.cabeza
        while True:
            if actual.dato == dato:
                # Pedimos el nuevo valor por input y tratamos de conservar el tipo si es entero
                entrada = input(f"Ingrese el valor a insertar después de {dato}: ")
                # intentar mantener el tipo original (si el nodo es int, convertir)
                if isinstance(actual.dato, int):
                    try:
                        nuevo_valor = int(entrada)
                    except ValueError:
                        # si falla la conversión, dejamos string
                        nuevo_valor = entrada
                else:
                    nuevo_valor = entrada

                nuevo = Nodo(nuevo_valor)
                nuevo.siguiente = actual.siguiente
                actual.siguiente = nuevo
                if actual == self.cola:  # si insertamos después de la cola, actualizarla
                    self.cola = nuevo
                self.tamanio += 1
                return True

            actual = actual.siguiente
            if actual == self.cabeza:
                break

        print(f"El dato {dato} no está en la lista")
        return False

        print(f"El dato {dato} no está en la lista")
        return False

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
    
    def merge(self, otra_lista):
        """ Intercala los nodos de self y otra_lista en una nueva lista """
        nueva_lista = ListaCircularEnlazada()
        actual1 = self.cabeza
        actual2 = otra_lista.cabeza

        # Si alguna de las listas está vacía, devolver la otra
        if not actual1:
            return otra_lista
        if not actual2:
            return self

        # Recorremos hasta completar ambas listas
        terminamos1 = False
        terminamos2 = False
        while not (terminamos1 and terminamos2):
            if not terminamos1:
                nueva_lista.agregar(actual1.dato)
                actual1 = actual1.siguiente
                if actual1 == self.cabeza:
                    terminamos1 = True
            if not terminamos2:
                nueva_lista.agregar(actual2.dato)
                actual2 = actual2.siguiente
                if actual2 == otra_lista.cabeza:
                    terminamos2 = True

        return nueva_lista


if __name__ == "__main__":
    lista = ListaCircularEnlazada()
    lista.agregar(10)
    lista.agregar(20)
    lista.agregar(30)
    lista.agregar(40)

    lista.mostrar()
    # 10 -> 20 -> 30 -> 40 -> (vuelve a la cabeza)

    print("\nInsertar después del 20:")
    lista.append(20) #agregar el 25 despues del 20
    lista.mostrar()
    # 10 -> 20 -> 25 -> 30 -> 40 -> (vuelve a la cabeza)

    print("\nInsertar después del 40 (último):")
    lista.append(40) #agregar el 50 despues del 40
    lista.mostrar()
    # 10 -> 20 -> 25 -> 30 -> 40 -> 50 -> (vuelve a la cabeza)

    print("\nIntentar insertar después de un valor inexistente:")
    lista.append(99) #agregar el 100 despues del 99, no lo permite
    lista.mostrar()

    lista1 = ListaCircularEnlazada()
    lista2 = ListaCircularEnlazada()

    for n in [1,2,4,6,10,100,3,8,0,123]:
        lista1.agregar(n)
    for n in [3,8,0,123]:
        lista2.agregar(n)

    print("Lista 1:")
    lista1.mostrar()
    print("Lista 2:")
    lista2.mostrar()

    lista_final = lista1.merge(lista2)
    print("Lista final:")
    lista_final.mostrar()
