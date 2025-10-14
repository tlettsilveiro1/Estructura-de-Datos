def remover_elemento(lista, elemento):
    lista[:] = [x for x in lista if x != elemento]
    return lista

texto = "banana"
resultado = remover_elemento(texto, "a")

#El programa sale con error ya que la cadena es inmutable a diferencia de una lista que es mutable
