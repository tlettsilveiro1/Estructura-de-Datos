[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=20172969)
# Guia Práctica

## Tema: Excepciones

Intente resolver los ejercicios detectando y previniendo con try/except la mayor cantidad y variedad de errores de ejecución posibles.

### Ejercicio 1 [Obligatorio]

Diseñen una calculadora que tenga las funciones básicas (suma, resta, multiplicación y división) que operan siempre con dos operandos. El usuario introduce los dos operandos y el operador (`'+'`, `'-'`, `'\*'`, `'/'`). El programa termina cuando el usuario introduce una cadena vacía como operando. Maneja correctamente los posibles casos de error.

### Ejercicio 2 [Obligatorio]

Implemente una aplicación de lista de tareas (to-do list) con las siguientes funcionalidades:

1. Ver todas las tareas pendientes y completadas
2. Agregar una nueva tarea con descripción y prioridad (1-5)
3. Marcar una tarea como completada por ID
4. Eliminar una tarea por ID
5. Guardar y cargar tareas desde un archivo JSON

Las tareas deben persistir entre ejecuciones del programa en un archivo `tareas.json`. Cada tarea debe tener:

- ID único
- descripción
- prioridad
- estado (pendiente/completada)
- fecha de creación.

### Ejercicio 3 [Opcional]

Reformula el programa del punto 3 (to-do list) utilizando clases respetando las mismas funcionalidades. El programa debe tener la clase `Main`, `ToDoManager` y `ToDo`. ¿Se modifica de alguna manera el enfoque para el manejo de excepciones? ¿Aparecen otros casos de excepciones distintos en el nuevo enfoque?
