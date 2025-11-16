[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21081735)
# Guía Práctica de Conjuntos en Python

## Ejercicio 1

Crear una clase `Persona` (si no lo hiciste antes), la cual tiene como atributos el nombre (string), un id (int) y la edad (int). A partir de esta clase, definí un conjunto (`set`) de personas dentro de una función `main()`.

Se deben crear 4 personas, las cuales se deberán añadir al conjunto. Una vez añadidas las 4 personas al conjunto, se debe visualizar el conjunto total usando el método `__str__` de la clase Persona.

---

## Ejercicio 2

Realizá un programa que permita mantener actualizada la información de los diferentes hoteles que forman parte de la cadena de hoteles “Estructuras y nada más”. De cada hotel se deben mantener actualizados los atributos nombre (string), idHotel (int), zona (string) y precio (int).

Las zonas donde podrán estar los hoteles son: "playa", "montaña" o "rural". El precio por noche es un dato en euros que podrá tomar valores entre 40 y 150.

Los id de los hoteles son únicos e irrepetibles. Para el almacenamiento de los hoteles, deberás usar un conjunto.

El programa realizará las siguientes tareas:
- Carga de datos
- Visualización de los hoteles que tiene la cadena
- Dada una zona por el usuario, mostrar los hoteles disponibles y el precio por noche

---

## Ejercicio 3

En matemática, muchas operaciones están definidas sobre conjuntos, como la unión, intersección y diferencia.

Teniendo en cuenta los métodos ofrecidos por un `set` en Python, se pueden computar estas operaciones utilizando los métodos `union`, `intersection` y `difference`.

Escribí una función que pueda utilizarse como un ‘calculador de conjuntos’ para estas 3 operaciones sobre conjuntos de enteros no negativos.

La función recibirá una lista, donde cada lista contendrá dos conjuntos y la operación que debe realizarse entre ellos.

Debe imprimir en pantalla, para cada línea, la salida correspondiente.

Ejemplo de uso y salida esperada:

```python
operaciones = [
	["union", {1, 2, 3}, {3, 4, 5}],
	["interseccion", {1, 2, 3}, {3, 4, 5}],
	["diferencia", {1, 2, 3}, {3, 4, 5}]
]


# Salida:
{1, 2, 3, 4, 5}
{3}
{1, 2}
```

---

## Ejercicio 4

Se tiene una lista de n números enteros. También hay dos conjuntos disjuntos, A y B, cada uno con m números enteros.

- Todo lo que representa algo positivo para vos está contenido en el conjunto A.
- Todo lo que representa algo negativo para vos está contenido en el conjunto B.

Usando esta información, debés realizar un programa que te permita determinar tu estado de felicidad según la información dada. Tu felicidad inicial es 0.

Para cada número x en la lista:
- Si x está en A, sumás +1 a tu felicidad.
- Si x está en B, restás -1 a tu felicidad.
- Si x no está en ninguno de los conjuntos, tu felicidad no cambia.

Ejemplo:
La lista contiene los números: `[1, 2, 3, 4, 5, 6, 7]`.
El conjunto A (números positivos) contiene `{1, 3, 5}`.
El conjunto B (números negativos) contiene `{2, 4, 6}`.
Mi estado de felicidad es 0.

---

## Ejercicio 5

Implementá un sistema que registre transacciones realizadas por clientes y permita análisis de compras. Para esto, diseñá una clase `Cliente`, que represente a cada usuario en una tienda. Cada cliente debe tener un nombre y una lista de productos que ha comprado. Además, implementá una clase `Tienda`, que administre la lista de clientes y sus compras.

Tareas a implementar en la clase Tienda:
1. Registrar nuevos clientes y sus compras.
2. Obtener el producto más comprado en la tienda.
3. Determinar el cliente con mayor variedad de compras.
4. Buscar qué clientes han comprado un producto específico.
5. Comparar dos clientes y listar los productos que tienen en común.

Estructura de datos: Los clientes y sus compras deben almacenarse en diccionarios, donde la clave es el nombre del cliente y el valor es un conjunto con los productos comprados.

Ejemplo:
```python
tienda = Tienda()
tienda.agregar_cliente("Juan", {"Laptop", "Mouse", "Teclado"})
tienda.agregar_cliente("Ana", {"Smartphone", "Auriculares"})
tienda.agregar_cliente("Carlos", {"Laptop", "Teclado", "Monitor"})

print(tienda.producto_mas_comprado())  # Debe devolver el producto con más apariciones.
print(tienda.comparar_clientes("Juan", "Carlos"))  # Debe devolver productos en común.
```

---

## Ejercicio 6

Implementá un sistema que permita modelar el registro y análisis de partidos en un torneo de fútbol. Para esto, diseñá una clase `Equipo`, que represente a cada equipo con su nombre y estadísticas (victorias, derrotas, goles a favor y en contra). Además, creá una clase `Campeonato`, que administre los partidos jugados y permita realizar análisis de rendimiento.

Tareas a implementar en la clase Campeonato:
- Registrar un partido entre dos equipos, indicando el resultado.
- Determinar el equipo con más victorias en el torneo.
- Calcular la diferencia total de goles por equipo.
- Filtrar los partidos en los que hubo empate.
- Comparar dos equipos y determinar quién ganó más veces en sus encuentros directos.

Los partidos deben almacenarse en tuplas, con el formato:
```python
("Equipo A", "Equipo B", 3, 2)  # Equipo A ganó 3-2 contra Equipo B
```

Ejemplo:
```python
campeonato = Campeonato()
campeonato.registrar_partido("Equipo A", "Equipo B", 3, 2)
campeonato.registrar_partido("Equipo C", "Equipo D", 1, 1)

print(campeonato.equipo_con_mas_victorias())  # Debe devolver el equipo con más triunfos.
print(campeonato.partidos_empatados())  # Debe listar los encuentros con empate.
```