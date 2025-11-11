class Nodo:
	def __init__(self, dato):
		self.dato = dato
		self.siguiente = None
	def __str__(self):
		siguiente = self.siguiente.dato if self.siguiente else None
		return f'{self.dato} y mi siguiente es {siguiente}'

class ListaEnlazada:
	def __init__(self):
		self.inicio = None
	def esVacio(self):
		return self.inicio == None
	def agregarAlFinal(self, nodo):
		if self.esVacio():
			self.inicio = nodo
		else:
			actual = self.inicio
			while actual.siguiente:
				actual = actual.siguiente
			actual.siguiente = nodo
	def agregarAlinicio(self, nodo):
		if self.esVacio():
			self.inicio = nodo
		else:
			nodo.siguiente = self.inicio
			self.inicio = nodo
	def __str__(self):
		elementos = []
		actual = self.inicio
		if actual == None:
			return 'La lista esta vacia'
		else:
			while actual:
				elementos.append(str(actual.dato))
				actual = actual.siguiente
			return '->'.join(elementos)
	def mostrar(self):       #hace lo mismo que el “__str__” pero mas facil y simple
		if self.esVacio():
			print('La lista esta vacía')
		else:
			actual = self.inicio
			while actual:
				print(actual)
				actual = actual.siguiente
	def remplazar(self, dato, nuevo):
		if self.esVacia():
			print('La lista esta vacía')
		else:
			actual = self.inicio
			while actual:
				if actual.dato == dato:
					actual.dato = nuevo
					return True
				else:
					actual = actual.siguiente
			return False
	def eliminar(self, dato):
		if self.esVacia():
			raise ValueError("La lista está vacía")
		actual = self.inicio
		previo = None
		while actual:
			if actual.dato == dato:
				if previo is None:
					self.inicio = actual.siguiente
				else:
					previo.siguiente = actual.siguiente
				return True
			previo = actual
			actual = actual.siguiente
		raise ValueError("Dato no encontrado")


if __name__ == '__main__':
	nodo1 = Nodo(1)
	nodo2 = Nodo(2)
	nodo3 = Nodo(3)
	nodo4 = Nodo(13)
	nodo4 = Nodo(-1)   #Se sobreescribe el nodo4
	lista = ListaEnlazada()
	lista.agregarAlinicio(nodo4)
	lista.agregarAlinicio(nodo3)
	lista.agregarAlFinal(nodo1)
	lista.agregarAlFinal(nodo2)
	lista.mostrar()  #output esperado es “3 y mi siguiente es -1  // -1 y mi siguiente es 1 // 1 y mi siguiente es 2  // 2 y mi siguiente es None”
	print(lista)    #output esperado es “3->-1->1->2”, viene del metodo “__str__”