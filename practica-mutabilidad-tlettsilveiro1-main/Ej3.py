#CREACION DIRECTA
z1 = 3 + 4j
print("Número complejo:", z1)
print("Parte real:", z1.real)
print("Parte imaginaria:", z1.imag)

#USANDO COMPLEX
z2 = complex(2, -5)  # igual a 2 - 5j
print("Número complejo:", z2)

#OPERACIONES
z3 = 1 + 2j
z4 = 2 + 3j
print("Suma:", z3 + z4)        # (3+5j)
print("Multiplicación:", z3 * z4)  # (-4+7j)
print("Conjugado:", z3.conjugate())  # (1-2j)


#DEMOSTRACION DE INMUTABILIDAD
z = 3 + 4j
print("ID antes:", id(z))
z = z + 1 
print("ID después:", id(z))