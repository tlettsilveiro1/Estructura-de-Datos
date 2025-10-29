[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=20955416)

# Guía Práctica: Pilas y Colas

## Práctica N.º 8

---

### Ejercicio 1: Implementación de la clase `Pila` (Obligatorio)


Hacé una **clase** llamada `Pila` que funcione como una secuencia de nodos anidados. El constructor de la clase tiene que guardar la referencia al nodo cima.


Los métodos a implementar son:
- `apilar`: agregá un elemento a la cima de la pila.
- `desapilar`: eliminá y devolvé el elemento de la cima.
- `es_vacia`: devolvé `True` si la pila está vacía.
- `visualizar_pila`: imprimí o devolvé una representación de la pila.


La pila tiene que guardar información de libros que llegan a una biblioteca para su organización. Cada libro debe tener:
- Nombre/s del autor
- Fecha de publicación
- Editorial
- Número ISSN (código de 8 dígitos)

```python
# class Libro: ...
# class Nodo: ...
# class Pila:
#     def apilar(self, libro): ...
#     def desapilar(self): ...
#     def es_vacia(self): ...
#     def visualizar_pila(self): ...
# (Completar la implementación)
```

---

### Ejercicio 2: Implementación de la clase `Cola` (Obligatorio)


Hacé una **clase** llamada `Cola` usando una lista como estructura interna.


Los métodos a implementar son:
- `encolar`: agregá un elemento al final de la cola.
- `desencolar`: eliminá y devolvé el primer elemento de la cola.
- `es_vacia`: devolvé `True` si la cola está vacía.
- `visualizar_cola`: imprimí o devolvé una representación de la cola.
- `longitud`: devolvé la cantidad de elementos en la cola.


La cola tiene que guardar información de personas que están esperando para votar en las elecciones.

```python
# class Persona: ...
# class Cola:
#     def encolar(self, persona): ...
#     def desencolar(self): ...
#     def es_vacia(self): ...
#     def visualizar_cola(self): ...
#     def longitud(self): ...
# (Completar la implementación)
```

---

### Ejercicio 3: Evaluador de expresiones RPN (Notación Polaca Inversa)


Hacé una función que evalúe expresiones aritméticas en notación polaca inversa (RPN, también llamada postfija). La función tiene que soportar los siguientes operadores básicos:
- `+` (suma)
- `-` (resta)
- `*` (multiplicación)
- `/` (división)

Los operandos pueden ser números enteros o flotantes. La función tiene que procesar la expresión y devolver el resultado numérico.

```python
# def evaluar_rpn(expresion):
#     # Usar una pila para los operandos
#     # Procesar cada token: si es número, apilar; si es operador, desapilar dos operandos y aplicar la operación
#     # (Completar la función)
```

---

### Ejercicio 4: Atención de pacientes en consultorio


Hacé una **clase** llamada `ColaDePacientes` que permita:
- Encolar pacientes por nombre.
- Atender al próximo paciente (desencolar y devolver el nombre).

Hacé un programa que permita al usuario:
- Ingresar nuevos pacientes.
- Indicar que un consultorio se liberó e imprimir el próximo paciente en espera.

```python
# class ColaDePacientes:
#     def encolar(self, nombre): ...
#     def proximo_paciente(self): ...
# # Programa principal: usar input() para interactuar
# (Completar la implementación)
```

---

### Ejercicio 5: Apilar cartas con reglas


Hacé una **clase** que permita apilar cartas una debajo de otra, pero solo si la carta a apilar es de un número inmediatamente inferior y de distinto palo. Si intentás apilar una carta incorrecta, tiene que lanzar una excepción.

Agregá el método `__str__` para imprimir las cartas apiladas hasta el momento.

```python
# class Carta: ...
# class PilaDeCartas:
#     def apilar(self, carta): ...
#     def __str__(self): ...
# (Completar la implementación y validaciones)
```

---

### Ejercicio 6: Sublista más larga de números consecutivos


Dada una lista de números enteros, hacé una función que encuentre la sublista más larga de números consecutivos.

```python
# def sublista_consecutivos_mas_larga(lista):
#     # Recorrer la lista y buscar la secuencia más larga
#     # (Completar la función)
```