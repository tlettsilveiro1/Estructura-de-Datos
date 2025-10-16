class ListaUtils:
    def mostrar_lista(self, lista):
        # Caso base: si la lista está vacía, no hay nada que mostrar
        if len(lista) == 0:
            return
        else:
            # Mostrar el primer elemento
            print(lista[0])
            # Llamar recursivamente con el resto de la lista
            self.mostrar_lista(lista[1:])


    def es_capicua(self, lista):
        # Caso base: lista vacía o de un solo elemento
        if len(lista) <= 1:
            return True
        # Si los extremos son distintos, no es capicúa
        if lista[0] != lista[-1]:
            return False
        # Caso recursivo: comparar el resto de la lista sin los extremos
        return self.es_capicua(lista[1:-1])

    def buscar_numero(self, lista, numero):
        # Caso base: lista vacía -> no se encontró
        if len(lista) == 0:
            return False
        # Si el primer elemento coincide, lo encontró
        if lista[0] == numero:
            return True
        # Caso recursivo: buscar en el resto de la lista
        return self.buscar_numero(lista[1:], numero)

    def minimo_vector(self, lista):
        # Caso base: si hay un solo elemento, es el mínimo
        if len(lista) == 1:
            return lista[0]
        else:
            # Calcular el mínimo del resto de la lista
            minimo_resto = self.minimo_vector(lista[1:])
            # Comparar con el primer elemento
            if lista[0] < minimo_resto:
                return lista[0]
            else:
                return minimo_resto



utils = ListaUtils()
utils.mostrar_lista([1, 2, 3, 4])

utils.mostrar_lista([1, 2, 3, 4])  # Esto sí imprime 1,2,3,4

print(utils.es_capicua([1, 2, 3, 2, 1]))  # True
print(utils.es_capicua([1, 2, 3, 4]))     # False

print(utils.buscar_numero([5, 8, 3, 7], 3))  # True
print(utils.buscar_numero([5, 8, 3, 7], 9))  # False

print(utils.minimo_vector([8, 3, 5, 1, 9]))  # 1