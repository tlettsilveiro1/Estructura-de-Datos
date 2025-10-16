# Implemente una aplicación de lista de tareas (to-do list) con las siguientes
# funcionalidades:
#
# 1. Ver todas las tareas pendientes y completadas
# 2. Agregar una nueva tarea con descripción y prioridad (1-5)
# 3. Marcar una tarea como completada por ID
# 4. Eliminar una tarea por ID
# 5. Guardar y cargar tareas desde un archivo JSON
#
# Las tareas deben persistir entre ejecuciones del programa en un archivo
# `tareas.json`. Cada tarea debe tener:
#
# - ID único
# - descripción
# - prioridad
# - estado (pendiente/completada)
# - fecha de creación.

from datetime import datetime

# -------------------- Funciones de la App --------------------
def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas registradas.")
        return    #Corta la funcion si no hay tareas
    
    print("\n📋 Lista de tareas:")
    for t in tareas:
        print(f"ID: {t['id']} | {t['descripcion']} | Prioridad: {t['prioridad']} | Estado: {t['estado']} | Creada: {t['fecha']}")

def agregar_tarea(tareas):
    descripcion = input("Descripción de la tarea: ").strip()
    if descripcion == "":
        print("La descripción no puede estar vacía.")
        return     #Corta la funcion si la descripcion esta vacia
    
    while True:    #Cuando da error, nunca pasa por el break (porque ejecuta el raise) y va directo al except. Como no hay break,
        try:                                                                # vuelve a empezar el while
            prioridad = int(input("Prioridad (1-5): "))
            if prioridad < 1 or prioridad > 5:
                raise ValueError
            break
        except ValueError:
            print("Debes ingresar un número entre 1 y 5.")
    
    if not tareas:    #sirve para asignar un ID unico
        nuevo_id = 1
    else:
        max_id = 0
        for t in tareas:
            if t["id"] > max_id:
                max_id = t["id"]
        nuevo_id = max_id + 1
    
    tarea = {       #crea un diccionario con la nueva tarea
        "id": nuevo_id,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "estado": "pendiente",      #por defecto la tarea se crea como pendiente
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    
    tareas.append(tarea)
    print("✅ Tarea agregada correctamente.")

def completar_tarea(tareas):   #marca una tarea como completada
    try:
        tarea_id = int(input("Ingrese el ID de la tarea a completar: "))
    except ValueError:
        print("ID inválido.")
        return
    
    for t in tareas:
        if t["id"] == tarea_id:
            if t["estado"] == "completada":
                print("La tarea ya estaba completada.")
            else:
                t["estado"] = "completada"
                print("✅ Tarea marcada como completada.")
            return
    
    print("No se encontró una tarea con ese ID.")

def eliminar_tarea(tareas):
    try:
        tarea_id = int(input("Ingrese el ID de la tarea a eliminar: "))
    except ValueError:
        print("ID inválido.")
        return
    
    for t in tareas:
        if t["id"] == tarea_id:
            tareas.remove(t)
            print("🗑️ Tarea eliminada correctamente.")
            return
    
    print("No se encontró una tarea con ese ID.")

# -------------------- Menú Principal --------------------
def menu():
    tareas = []
    
    while True:
        print("\n--- MENÚ ---")
        print("1. Ver todas las tareas")
        print("2. Agregar nueva tarea")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("Saliendo... ¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

# -------------------- Ejecutar Programa --------------------
if __name__ == "__main__":
    menu()
