[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21262069)
# Guia Práctica

## Tema: Numpy

### Ejercicio 1 (obligatorio)

Realizar una función que determine si dos vectores son iguales. Dos vectores son iguales si y solo si los elementos de uno de los vectores son igual al cuadrado de los elementos del otro vector, sin importar el orden de los elementos.

#### Ejemplo 1

```python
vectora = [121, 144, 19, 161, 19, 144, 19, 11] 
vectorb = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
```
Imprime por pantalla
```
Los dos vectores son iguales
```

#### Ejemplo 2

```python
vectora = [121, 144, 19, 161, 19, 144, 9, 11] 
vectorb = [121, 14641, 20736, 361, 25, 361, 20736, 361]
```
Imprime por pantalla
```
Los dos vectores NO son iguales
```

### Ejercicio 2

Diseña una función que, dada una matriz, determine si la suma de los elementos de cualquiera de sus filas es igual a la suma de los elementos de cualquiera de sus columnas.

#### Ejemplo 1

```python
Matriz=[[ 50, 75, 46],[ 22, 80, 125]]
```
Dara como resultado:
Suma filas= 171 y 227
Suma columnas= 72, 155, 171

Imprime por pantalla

```
La suma de fila 1 es igual a la suma de la columna 2
```
#### Ejemplo 2

```python
Matriz=[[ 50, 75, 46],[ 22, 80, 65]]
```
Dara como resultado:
Suma filas= 171 y 167
Suma columnas= 72, 155, 110

Imprime por pantalla
```
Ninguna suma de filas es igual a la suma de ninguna de las columnas
```

### Ejercicio 3 (obligatorio)

Realizar una función que dada una matriz visualice si ésta es una matriz cuadrada triangular superior. 
Una matriz es cuadrada triangular superior si todos los elementos por debajo de la diagonal principal son nulos

#### Ejemplo

$$
\begin{pmatrix}
1 & 2 & 3 \\
0 & 4 & 5 \\
0 & 0 & 6
\end{pmatrix}
$$

Imprime
```
Es triangular superior
```

### Ejercicio 4

Escribir un programa NumPy para calcular la inversa de una matriz dada.
NOTA: Debe investigar cómo se calcula la inversa de una matriz usando la librería NumPy

### Ejercicio 5

Escribir una función que reciba dos matrices y devuelva la suma entre ellas.

### Ejercicio 6 (obligatorio)

Diseña una función que, dado un vector o una matriz, calcule la media, la mediana y la desviación estándar usando NumPy.

Parte A (vector):
- Entrada: un vector (lista o ndarray).
- Salida: imprimir y devolver media, mediana y desviación estándar del vector.

Ejemplo:
```python
vector = [1, 2, 2, 3, 4]
```
Salida esperada (aproximada):
```
Media: 2.4
Mediana: 2.0
Desviación estándar: 1.0198039027185568
```

Parte B (matriz):
- Entrada: una matriz (lista de listas o ndarray).
- Para cada fila y para cada columna, imprimir media, mediana y desviación estándar.
- Indicar claramente la fila/columna correspondiente.

Ejemplo:
```python
M = [[1, 2, 3],
     [4, 5, 6]]
```
Salida esperada (resumida):
```
Fila 1 - media: 2.0, mediana: 2.0, std: 0.816...
Fila 2 - media: 5.0, mediana: 5.0, std: 0.816...
Columna 1 - media: 2.5, mediana: 2.5, std: 1.5
Columna 2 - ...
```