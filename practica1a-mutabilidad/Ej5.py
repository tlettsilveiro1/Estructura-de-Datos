profe= "Agostina"
mi_profe= "Agostina"
print(profe is mi_profe) # Completar en este comentario: ¿qué valor se obtuvo? TRUE

pro= "Agostina?"
pro_Agos= "Agostina?"
print(pro is pro_Agos)  # Completar en este comentario: ¿qué valor se obtuvo? TRUE

a="a"
b="b"
print(a is b)  # Completar en este comentario: ¿qué valor se obtuvo? FALSE

ver="!"
ver_mas="!"
print(ver is ver_mas)  # Completar en este comentario: ¿qué valor se obtuvo? TRUE

numero1=120
numero2=120
print(numero1 is numero2)  # Completar en este comentario: ¿qué valor se obtuvo? TRUE

numero1=12000000
numero2=12000000
print(numero1 is numero2)  # Completar en este comentario: ¿qué valor se obtuvo? TRUE

x = [1, 2, 3]
y = [1, 2, 3]
print("x is y:", x is y)
print("id(x):", id(x))
print("id(y):", id(y))