[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21081105)

# PRÁCTICA NO. 10

## RECURSIÓN

En esta práctica vas a trabajar con recursividad en Python. Recordá que la recursividad es una técnica donde una función se llama a sí misma para resolver un problema dividiéndolo en subproblemas más simples.

---


### Ejercicio 1
Escribí un método recursivo dentro de una clase llamada `ListaUtils` que muestre por pantalla los elementos de una lista, uno por línea.

**Ejemplo:**
```python
utils = ListaUtils()
utils.mostrar_lista([1, 2, 3, 4])
# Salida:
# 1
# 2
# 3
# 4
```

---


### Ejercicio 2
Escribí un método recursivo dentro de la clase `ListaUtils` que determine si una lista de enteros es capicúa (es decir, se lee igual de izquierda a derecha que de derecha a izquierda).

**Ejemplo:**
```python
utils = ListaUtils()
utils.es_capicua([1, 2, 3, 2, 1])  # True
utils.es_capicua([1, 2, 3, 4])     # False
```

---


### Ejercicio 3
Escribí un método recursivo dentro de una clase llamada `MatrizUtils` que calcule la suma de todos los elementos de una matriz (lista de listas) de enteros.

**Ejemplo:**
```python
mat_utils = MatrizUtils()
mat_utils.suma_matriz([[1, 2], [3, 4]])  # 10
```

---


### Ejercicio 4
Escribí un método recursivo dentro de la clase `ListaUtils` que busque si un número entero se encuentra en un vector (lista) de enteros.

**Ejemplo:**
```python
utils = ListaUtils()
utils.buscar_numero([5, 8, 3, 7], 3)  # True
utils.buscar_numero([5, 8, 3, 7], 9)  # False
```

---


### Ejercicio 5
Escribí un método recursivo dentro de una clase llamada `NumeroUtils` que sume los dígitos de un número entero positivo.

**Ejemplo:**
```python
num_utils = NumeroUtils()
num_utils.sumar_digitos(1234)  # 10
num_utils.sumar_digitos(505)   # 10
```

---


### Ejercicio 6
Escribí un método recursivo dentro de la clase `ListaUtils` que devuelva el número más pequeño de un vector (lista) de enteros.

**Ejemplo:**
```python
utils = ListaUtils()
utils.minimo_vector([8, 3, 5, 1, 9])  # 1
```

---


### Ejercicio 7
Escribí un método recursivo dentro de la clase `NumeroUtils` que invierta un número entero.

**Ejemplo:**
```python
num_utils = NumeroUtils()
num_utils.invertir_numero(1234)  # 4321
num_utils.invertir_numero(100)   # 1
```

---


### Ejercicio 8
Escribí un método recursivo dentro de una clase llamada `PalabraUtils` que determine si una palabra es palíndroma (se lee igual de izquierda a derecha que de derecha a izquierda).

**Ejemplo:**
```python
pal_utils = PalabraUtils()
pal_utils.es_palindromo("reconocer")  # True
pal_utils.es_palindromo("python")     # False
```
