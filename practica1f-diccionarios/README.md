[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=20412720)
# GUIA PRÁCTICA 6

## DICCIONARIOS

### Ejercicio 1 [Obligatorio]

Utilizando la información de las ventas de las diferentes zonas de influencia de cada uno los vendedores de la empresa "Si se puede", usted debe realizar un programa modularizado en clases que permita realizar las siguientes tareas:

1. Crear un diccionario que permita manejar la información de las ventas en cada zona de cada vendedor.
2. Preguntar al usuario si desea modificar alguna información existente en la data, de ser así pedir nombre del vendedor, la zona de influencia y el valor de la venta a modificar.
3. Visualizar las ventas totales de la empresa
4. Visualizar la zona de mayores ventas.

Vendedor  | Norte | Sur  | Este | Oeste
--------- | ----- | ---- | ---- | -----
Nicolas   | 3528  | 2400 | 1200 | 8200
Daniela   | 3824  | 6786 | 5598 | 3612
Maria     | 8008  | 4653 | 8425 | 1000
Francisco | 5833  | 6356 | 2548 | 1386

### Ejercicio 2 [Obligatorio]

Implemente una clase `EvaluadorPalabras` que encapsule la lógica de puntuación de palabras estilo Scrabble.

**Requisitos:**

La clase debe:

- Almacenar un diccionario con los valores de puntuación para cada letra
- Calcular el puntaje de una palabra individual (letras no definidas valen 1 punto)
- Encontrar la palabra con mayor puntaje de una lista dada
- Mantener un registro de la última evaluación realizada

**Ejemplo de uso esperado:**

```python
# Crear evaluador con reglas de puntuación
valores_letras = {
    'a': 2,
    'n': 3,
    'f': 5,
    'z': 5
}

evaluador = EvaluadorPalabras(valores_letras)

# Evaluar lista de palabras
palabras = ["cono", "mazazo", "fanzine", "fhan", "marsupial"]
palabra_ganadora = evaluador.obtener_palabra_maxima(palabras)

print(f"Palabra ganadora: {palabra_ganadora}")
print(f"Puntaje: {evaluador.calcular_puntaje(palabra_ganadora)}")

# Obtener detalles de la última evaluación
print(f"Todas las puntuaciones: {evaluador.ultima_evaluacion}")
```

**Salida esperada:**

```
Palabra ganadora: fanzine
Puntaje: 20
Todas las puntuaciones: {'cono': 8, 'mazazo': 12, 'fanzine': 20, 'fhan': 11, 'marsupial': 13}
```

### Ejercicio 3

Escriba una función que dado un conjunto de diccionarios (clave: string, contenido: real) devuelva un único diccionario (clave: string, valor conjunto de reales).

**Ejemplo**

Input:

```python
[
    {"Pan": 22.8, "Pollo": 33.85},
    {"Mermelada": 42.5, "Pan": 23.55, "Tomate": 18.3},
    {"Pan": 28.0, "Tomate": 19.5, "Pollo": 34.6}
]
```

La función debe devolver:

```python
{
    "Pan": [22.8, 23.55, 28.0],
    "Pollo": [33.85, 34.6],
    "Mermelada": [42.5],
    "Tomate": [18.3, 19.5]
}
```

### Ejercicio 4

Cree una clase `RepositorioCSV` que permita almacenar la información del diccionario resultante anterior en un archivo CSV y posteriormente leerlo. Todas las filas del CSV tieneen que tener la misma cantidad de columnas, complete con cero los faltantes.

### Ejercicio 5

Escribir un programa que genere un archivo CSV con la siguiente información:

Book                                   | Author              | Year Released
-------------------------------------- | ------------------- | -------------
To Kill A Mockingbird                  | Harper Lee          | 1960
A Brief History of Time                | Stephen Hawking     | 1988
The Great Gatsby                       | F. Scott Fitzgerald | 1922
The Man Who Mistook His Wife for a Hat | Oliver Sacks        | 1985
Pride and Prejudice                    | Jane Austen         | 1813

Con el archivo ya creado, realice otro programa que le pregunte al usuario si desea agregar una nueva línea de información y CUÁNTAS líneas nuevas serían las que desea agregar y hágalo.

### Ejercicio 6

Usar el archivo del ejercicio 5 y a través de una función solicite al usuario que ingrese un año de inicio y un año de final, y le muestre la información filtrada entre esos 2 años.

**Ejemplo 1**

```
Año inicio: 1980
Año final: 1990
```

Resultado:

Book                                   | Author              | Year Released
-------------------------------------- | ------------------- | -------------
A Brief History of Time                | Stephen Hawking     | 1988
The Man Who Mistook His Wife for a Hat | Oliver Sacks        | 1985
