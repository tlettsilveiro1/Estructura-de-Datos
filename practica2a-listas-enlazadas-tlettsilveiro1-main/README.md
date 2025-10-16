[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=20813857)
# Guia Práctica

## Tema: Listas enlazadas

### Ejercicio 1 (obligatorio)

Crea una clase llamada ListaCircularEnlazada que tenga almacena datos de tipo entero y como atributos debe tener nodo cabeza y el tamaño de la lista actualizado.
Usted debe Implementar los siguientes métodos en la clase ListaCircularEnlazada:

- Agregar un nuevo nodo al final de la lista circular
- Eliminar un nodo específico de la lista circular dado el valor contenido en ella
- Mostrar todos los valores almacenados en los nodos en la lista circular, respectivamente.
- Método para obtener el nodo siguiente al nodo actual en la lista circular.

### Ejercicio 2 (obligatorio)

Haciendo uso de la lista implementada en el Ejercicio 1 escriba un método `append(dato)` que permita ingresar un nodo a la lista por referencia, es decir dado el valor de un dato en la lista introducir un nuevo nodo inmediatamente después del anterior.

### Ejercicio 3 (obligatorio)

Escriba un método `merge(otra_lista)` que toma dos listas enlazadas de enteros creadas usando la implementación hecha en la clase teórica y las una en una sola lista de la siguiente manera:
Lista1Elemento1, Lista2Elemento1, Lista1Elemento2, Lista2Elemento2, etc.
De no ser iguales los tamaños de ambas listas, al final de la lista generada deben quedar los elementos de la lista más grande.

#### Ejemplo

```python
lista=[1,2,4,6,10,100,3,8,0,123]
lista2=[3,8,0,123]
listafinal=[1,3,2,8,4,0,6,123,10,100,3,8,0,123]
```

### Ejercicio 4

Crea una clase llamada ListaEnlazada que almacena la información de los estudiantes de Estructuras de Datos. Todo estudiante es una persona y debe tener como atributos adicionales el listado de las materias que está viendo, legajo y carrera que estudia.
La lista debe tener como atributo un nodo cabeza. Usted debe implementar los siguientes métodos:

- Agregar los estudiantes a la lista organizados por orden alfabético por apellido
- Eliminar un estudiante de la lista dado su legajo
- Visualizar la materia el promedio de materias que ven los estudiantes
- Visualizar la información de cada estudiante incluyendo el listado de las materias que está viendo

### Ejercicio 5

Implementar una lista de reproducción de música: una lista de reproducción es una estructura de datos que permite almacenar canciones y acceder a ellas en orden. Para implementar una lista de reproducción utilizando una lista enlazada simple, cada nodo debe contener información sobre las canciones: el título, el artista, el año de grabación y el puntero del nodo apuntaría a la siguiente canción en la lista.