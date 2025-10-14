[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=20112151)
# Guia Práctica

## Tema: Funciones

Estos ejercicios pueden ser resueltos con lo aprendido en Informática General. Ya conociendo la lógica fundamental de resolución, resuélvelos utilizando las nuevas herramientas enseñadas en la clase teórica:

- Funciones Lambda
- Funciones de primera clase: `map`, `filter`, `reduce`.
- Funciones built-in como `zip`, `enumerate`, métodos de cadena, etc.

### Ejercicio 1

Implemente la funcion "contar_simbolos" que permita contar la cantidad total de caracteres alfabéticos, dígitos y caracteres especiales en una cadena y las retorne en forma de una lista.
Reimplemente utilizando funciones lambda y de primera clase y compare las soluciones.

```python
resultado = contar_simbolos("Hola Mundo 123!@#")
print(resultado)  # Debería imprimir [10, 3, 4]
```

______________________________________________________________________

### Ejercicio 2

Realizar una función que, dada una cadena de caracteres y un carácter como parámetros, encuentre la cantidad máxima de ocurrencias del carácter en la cadena.
Reimplemente utilizando funciones lambda y de primera clase y compare las soluciones.

```
>>> repeticiones = contar_repeticiones("Welcome to w3resource.com", "e")
>>> print(f"Cantidad de veces que se repitió: {repeticiones}")
Cantidad de veces que se repitió: 4
```

______________________________________________________________________

### Ejercicio 3

Realizar una función que, dada una cadena de caracteres reemplace las letras minúsculas por mayúsculas y viceversa.
Reimplemente utilizando funciones lambda y de primera clase y compare las soluciones.

```python
>>> resultado = cambiar_mayusculas_minusculas("Hola Mundo")
>>> print(resultado)
hOLA mUNDO
```

______________________________________________________________________

## Tema: Cadenas

### Ejercicio 4

Realizar una función que dadas dos cadenas de caracteres de igual longitud `n`, verifique si existe alguna permutación posible en cualquiera de las cadenas, de modo que cada carácter de una cadena sea mayor o igual a cada carácter de la otra cadena, en el índice correspondiente. La función debe devolver `True` si es posible la permutación en caso contrario devolverá `False`.

#### Ejemplo 1:

```
cadena1: "adb"
cadena2: "cda"
Después de la permutación:
cadena1: "adb"
cadena2: "adc"
Salida: True
```

#### Ejemplo 2:

```
cadena1: "gfg"
cadena2: "agd"
Salida: True
```

### Ejercicio 5

Realizar una función que, dada una cadena de caracteres retorne una lista con la palabra mas larga en la posicion 0 y la palabra mas corta en la posicion 1. Imprima por pantalla para lograr la siguiente salida.

#### Ejemplo 1

```
cadena: "Estructuras de Datos"
cadena_larga: "Estructuras"
cadena_corta: "de"
```

### Ejercicio 6

Realizar una función que, dada una cadena de caracteres, cuente la cantidad de cada uno de los caracteres que se encuentran en la cadena.

```
cadena: "Estructuras de Datos"
e	2
s	3
t	3
r	2
u	2
a	2
d	2
o	1
```

### Ejercicio 7

Realizar una función que, dada una lista `palabras` y dos palabras, encuentre la distancia mínima entre las palabras dadas dentro de la lista.

#### Ejemplo 1

```
palabras=["La","materia","Estructuras","de","Datos","es","genial"]


primeraPalabra="La"
segundaPalabra="es"
La distancia mínima entre "la" y "es" es: 5
```

#### Ejemplo 2

```
palabras=["La","materia","Estructuras","de","Datos","es","de","las","mas","geniales"]


primeraPalabra="de"
segundaPalabra="geniales"
La distancia mínima entre "de" y "geniales" es: 3
```

### Ejercicio 8

Realizar una función que, dada una cadena de caracteres, reemplace cada subcadena de caracteres idénticos por un solo carácter seguido del número hexadecimal que representa la cantidad de veces que se repite el carácter. Posteriormente la cadena obtenida debe ser escrita y visualizada en forma al revés.
Todas las letras que representen un número hexadecimal deben convertirse en letras minúsculas.

#### Ejemplo 1

```
frase="aaaaaaaaaaa"
Salida: "ba"


Análisis:
a se repite 11 veces
En hexadecimal el número 11 se representa por la b


Salida:
"ab"
Pero la salida debe escribirse al revés, por tanto la salida final debe ser:
"ba"
```

#### Ejemplo 2

```
frase="abc"
Salida: "1c1b1a"
```

### Ejercicio 9

Realizar una función que, dada una cadena de caracteres y un número entero `k`, reduzca el tamaño de la cadena de acuerdo con las siguientes indicaciones:
Debe escoger un grupo de `k` caracteres idénticos consecutivos y eliminarlos de la cadena
Esta operación se debe poder repetir la cantidad de veces necesarias hasta que ya no sea posible hacerlo.

### Ejercicio 10

Realizar una función que, dada una cadena de caracteres visualice si la cadena introducida es una cadena bitónica inversa o no.
Una cadena bitónica inversa, es una cadena en la que los caracteres están dispuestos en orden decreciente seguido de valores crecientes según el código ASCII.

#### Ejemplo 1

```
cadena = "zyxbcde"
Salida: la cadena "zyxbcde" es bitónica inversa
```

#### Ejemplo 2

```
Cadena= "abcdwef"
Salida: la cadena "abcdwef" No es bitónica inversa
```

#### Ejemplo 3

```
Cadena= "86479"
Salida: la cadena "86479" es bitónica inversa
```

### Ejercicio 11

Crear un programa que añada números a una lista hasta que se introduzca un número negativo. A continuación se debe crear una nueva lista igual que la anterior pero eliminando los números duplicados. Mostrar en la consola la segunda lista para comprobar que los duplicados se han eliminado e imprimir el id de la lista.

#### Ejemplo 1

```
Números introducidos= 1,3,45,23,0,0,45,-12
lista_inicial=[1,3,45,23,0,0,45]
lista_sin_repetidos=[1,3,45,23,0]
id 2298653961600
```

### Ejercicio 12

Escriba un programa que permita crear una lista de palabras y que contenga las siguientes opciones:
Contar: Se pide al usuario una cadena y debe imprimir la cantidad de veces que aparece la cadena en la lista
Modificar: Se pide al usuario una cadena y otra cadena para modificar la primera cadena y se modifican todas las apariciones de la primera cadena por la segunda en la lista.
Eliminar: Se pide al usuario una cadena y se la elimina de la lista
Salir

#### Ejemplo 1

```python
lista=["hola","yo","estoy","feliz","en","ITBA",".","ITBA","es","una","de","las","mejores","Universidades","de","Argentina"]
```

a. Cadena ingresada: "ITBA".
`Repeticiones: 2`

b. Cadena a modificar "ITBA"
Se debe modificar por: "el Instituto Tecnologico de Buenos Aires"

```python
lista=["hola","yo","estoy","feliz","en","el Instituto Tecnologico de Buenos Aires",".","el Instituto Tecnologico de Buenos Aires","es","una","de","las","mejores","Universidades","de","Argentina"]
```

c. Cadena a Eliminar: "hola"

```python
lista=["yo","estoy","feliz","en","el Instituto Tecnologico de Buenos Aires",".","el Instituto Tecnologico de Buenos Aires","es","una","de","las","mejores","Universidades","de","Argentina"]
```

### Ejercicio 13

Crear un programa con el siguiente menú:

- Añadir un número a la lista: Se pide un numero al usuario y se añade al final de la lista
- Añadir un número a la lista en una posición: Se pide un número y posición al usuario y si la posición existe en la lista lo añade a la misma
- Longitud de la lista: Muestra el número de elementos de la lista
- Eliminar el último número: Muestra el último número de la lista y lo borra
- Eliminar un número: Pide una posición al usuario y si la posición existe en la lista lo borra de ella
- Contar apariciones: Pide un numero al usuario y devuelve cuantas apariciones hay en la lista
