#Para saber si se mantiene la mutabilidad de un objeto cuando se modifica, se debe ver si la direccion
#de memoria donde esta guardado cambia

# APPEND
numeros = [1, 2, 3]
print("ID antes:", id(numeros))
numeros.append(4)  # modifica la lista en el lugar
print("ID después:", id(numeros))


# EXTEND
frutas = ["manzana", "pera"]
print("ID antes:", id(frutas))
frutas.extend(["naranja", "uva"])
print("ID después:", id(frutas))


# INSERTED
colores = ["rojo", "azul"]
print("ID antes:", id(colores))
colores.insert(1, "verde")
print("Lista después de insert:", colores)
print("ID después:", id(colores))


#REMOVE
animales = ["perro", "gato", "pez", "gato"]
print("ID antes:", id(animales))
animales.remove("gato")  # elimina el primer "gato"
print("Lista después de remove:", animales)
print("ID después:", id(animales))


#POP
letras = ["a", "b", "c", "d"]
print("ID antes:", id(letras))
eliminado = letras.pop(2)
print("Elemento eliminado:", eliminado)
print("Lista después de pop:", letras)
print("ID después:", id(letras))