def remover_elemento(lista, elemento):
    lista[:] = [x for x in lista if x != elemento]  # modificamos la lista en el lugar
    return lista

frutas = ["banana", "pera", "mandarina"]
frutas_amarillas = remover_elemento(frutas, "mandarina")
print(frutas_amarillas is frutas)