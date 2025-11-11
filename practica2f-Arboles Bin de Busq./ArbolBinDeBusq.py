class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecho, valor)


    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierdo, valor)
        else:
            return self._buscar_recursivo(nodo.derecho, valor)


    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo

        # 1️⃣ Buscar el nodo a eliminar
        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, valor)
        else:
            # 2️⃣ Caso encontrado

            # Caso A: Sin hijos
            if nodo.izquierdo is None and nodo.derecho is None:
                return None

            # Caso B: Un solo hijo
            elif nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo

            # Caso C: Dos hijos
            else:
                sucesor = self._minimo_valor(nodo.derecho)
                nodo.valor = sucesor.valor
                nodo.derecho = self._eliminar_recursivo(nodo.derecho, sucesor.valor)

        return nodo

    def _minimo_valor(self, nodo):
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual


    def mostrar_inorden(self): #Recorrer el arbol Inorden
        self._mostrar_inorden_rec(self.raiz)

    def _mostrar_inorden_rec(self, nodo):
        if nodo is not None:
            self._mostrar_inorden_rec(nodo.izquierdo)
            print(nodo.valor)
            self._mostrar_inorden_rec(nodo.derecho)

    
    def suma_niveles_pares_resta_impares(self):
        return self._suma_recursiva(self.raiz, 0)

    def _suma_recursiva(self, nodo, nivel):
        if nodo is None:
            return 0

        # Calcular valor según el nivel
        if nivel % 2 == 0:
            valor_actual = nodo.valor     # nivel par → sumar
        else:
            valor_actual = -nodo.valor    # nivel impar → restar

        # Recorrer los hijos (incrementando nivel)
        suma_izq = self._suma_recursiva(nodo.izquierdo, nivel + 1)
        suma_der = self._suma_recursiva(nodo.derecho, nivel + 1)

        return valor_actual + suma_izq + suma_der


    def suma_multiplos_de_2(self):
        return self._suma_multiplos_de_2_recursivo(self.raiz)

    def _suma_multiplos_de_2_recursivo(self, nodo):
        if nodo is None:
            return 0  # caso base

        suma = 0
        # Si el valor es múltiplo de 2, se suma
        if nodo.valor % 2 == 0:
            suma += nodo.valor

        # Recorrer ramas izquierda y derecha
        suma += self._suma_multiplos_de_2_recursivo(nodo.izquierdo)
        suma += self._suma_multiplos_de_2_recursivo(nodo.derecho)
        return suma


    # Recorrido en orden
    def inorden(self):
        self._inorden_recursivo(self.raiz)

    def _inorden_recursivo(self, nodo):
        if nodo is not None:
            self._inorden_recursivo(nodo.izq)
            print(nodo.valor)
            self._inorden_recursivo(nodo.der)

    # Método recursivo para contar hojas
    def contar_hojas(self):
        return self._contar_hojas_recursivo(self.raiz)

    def _contar_hojas_recursivo(self, nodo):
        if nodo is None:
            return 0
        # Si el nodo no tiene hijos, es una hoja
        if nodo.izq is None and nodo.der is None:
            return 1
        # Caso recursivo: sumar hojas del subárbol izquierdo y derecho
        return self._contar_hojas_recursivo(nodo.izq) + self._contar_hojas_recursivo(nodo.der)


    # ✅ Recorrido postorden NO recursivo
    def postorden_no_recursivo(self):
        if self.raiz is None:
            return

        pila1 = []
        pila2 = []

        pila1.append(self.raiz)

        while len(pila1) > 0:
            nodo = pila1.pop()
            pila2.append(nodo)

            # Primero los hijos izquierdo y derecho
            if nodo.izq is not None:
                pila1.append(nodo.izq)
            if nodo.der is not None:
                pila1.append(nodo.der)

        # Imprimir en el orden postorden
        while len(pila2) > 0:
            nodo = pila2.pop()
            print(nodo.valor)


arbol = ArbolBinarioBusqueda()
arbol.insertar(8)
arbol.insertar(3)
arbol.insertar(10)
arbol.insertar(1)
arbol.insertar(6)
arbol.insertar(9)
arbol.insertar(14)

print("Árbol original (inorden):")
arbol.mostrar_inorden()

resultado1 = arbol.suma_niveles_pares_resta_impares()
print("Resultado de suma niveles pares - impares:", resultado1)

resultado2 = arbol.suma_multiplos_de_2()
print("Suma de los elementos múltiplos de 2:", resultado2)

print("Elementos en inorden:")
arbol.inorden()

print("Cantidad de hojas del árbol:", arbol.contar_hojas())

print("Recorrido postorden (no recursivo):")
arbol.postorden_no_recursivo()

print("\nEliminar hoja (1):")
arbol.eliminar(1)
arbol.mostrar_inorden()

print("\nEliminar nodo con un hijo (10):")
arbol.eliminar(10)
arbol.mostrar_inorden()

print("\nEliminar nodo con dos hijos (3):")
arbol.eliminar(3)
arbol.mostrar_inorden()