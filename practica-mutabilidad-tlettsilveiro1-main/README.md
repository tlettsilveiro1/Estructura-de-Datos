[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=20112156)
# Guia Práctica

## Tema: Mutabilidad

### Ejercicio 1 [Obligatorio]

Complete en este archivo la siguiente tabla de tipos de datos con su mutabilidad (mutable/inmutable) y un ejemplo de código que justifique su afirmación.

| Tipo de dato | Mutabilidad         | Ejemplo      |
| :----------- | :------------------ | :----------- |
| **Int**      | `mutable/inmutable` | `tu ejemplo` |
| **Str**      |                     |              |
| **Float**    |                     |              |
| **List**     |                     |              |
| **Tuple**    |                     |              |
| **Complex**  |                     |              |
| **Dict**     |                     |              |

______________________________________________________________________

### Ejercicio 2 [Obligatorio]

Investigar 5 métodos que le permitan modificar una lista dada. Luego implemente en el archivo main.py un ejemplo de código (función) con cada uno de los métodos investigados y demuestre en cada uno de estos ejercicios que la lista es un tipo de dato mutable.

______________________________________________________________________

### Ejercicio 3 [Obligatorio]

Realizar 3 ejemplos de cómo Python representa los números complejos.
¿Los complejos son mutables o inmutables? ¡¡Demuéstralo!!

______________________________________________________________________

### Ejercicio 4 [Obligatorio]

Desarrolle una función de nombre `reemplazar` que reciba tres parámetros: una cadena de texto, una posición i (donde i debe ser menor que la longitud de la cadena) y un carácter. Debe retornar una nueva cadena donde el carácter en la posición i de la cadena original ha sido reemplazado por el carácter proporcionado como argumento.

Ejemplo:

```python
original = "casado"
modificado = reemplazar(original, 2, "z")
print(modificado) # cazado
```

______________________________________________________________________

### Ejercicio 5 [Obligatorio]

is es una palabra reservada de Python que permite determinar si dos variables apuntan a la misma dirección de memoria, basado en esta definición ¿que valor se obtendrá de las siguientes expresiones? Debe usar el intérprete de Python.
Agregue el resultado obtenido (True o False) en este archivo a continuación:

#### Resolver

```python
profe= "Agostina"
mi_profe= "Agostina"
print(profe is mi_profe)

pro= "Agostina?"
pro_Agos= "Agostina?"
print(pro is pro_Agos)

a="a"
b="b"
print(a is b)

ver="!"
ver_mas="!"
print(ver is ver_mas)

numero1=120
numero2=120
print(numero1 is numero2)

numero1=12000000
numero2=12000000
print(numero1 is numero2)

lista1=[1,2,3,4]
lista2=[1,2,3,4]
print(lista1 is lista2)

lista3=lista1
print(lista3 is lista1)

lista4=lista1[:]
print(lista4 is lista1)
```

______________________________________________________________________

### Ejercicio 6 [Obligatorio]

Realizar una función de nombre `remover_elemento` que reciba como parámetros una lista de elementos y un elemento que se desea eliminar de la lista y retorne la lista con los elementos eliminados si coinciden con el parámetro que paso el usuario. El id de la lista antes de eliminar elementos ¿Debería ser el mismo id luego de que se eliminen elementos? ¿Por qué sí o por qué no?

#### Ejemplo 

```python
frutas = ["banana", "pera", "mandarina"]
frutas_amarillas = remover_elemento(frutas, "mandarina")
print(frutas_amarillas is frutas)
```

______________________________________________________________________

### Ejercicio 7 [Obligatorio]

Utilice la misma función del ejercicio anterior, pero en vez de pasar como parámetro una lista, pase una cadena. ¿Obtiene el mismo resultado? ¿Por qué? ¿Cuál es la diferencia entre la lista y la cadena?

______________________________________________________________________

### Ejercicio 8 [Obligatorio]

¿Al ejecutar la función probar que visualizarás? Responde a continuación:

Tu respuesta aqui:

```python
def probar():
    a = (1, 2, [1, 2, 3])
    a[2].append(4)
    print(a)

probar()
```
