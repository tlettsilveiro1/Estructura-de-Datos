def anadir_numero(lista: list, numero: int):
    lista.append(numero)
    return


def anadir_numero_en_posicion(lista: list, numero: int, posicion: int):
    if 0 <= posicion < len(lista):
        lista.insert(posicion, numero)
    else:
        print("❌ Posición inválida")
    return


def longitud_lista(lista: list):
    print(f"Longitud de la lista: {len(lista)}")
    return


def eliminar_ultimo_numero(lista: list):
    if lista:
        eliminado = lista.pop()
        print(f"Se eliminó el último número: {eliminado}")
    else:
        print("❌ La lista está vacía")
    return


def eliminar_numero_en_posicion(lista: list, posicion: int):
    if 0 <= posicion < len(lista):
        eliminado = lista.pop(posicion)
        print(f"Se eliminó el número {eliminado} en la posición {posicion}")
    else:
        print("❌ Posición inválida")
    return


def contar_apariciones(lista: list, numero: int):
    repeticiones = lista.count(numero)
    print(f"El número {numero} aparece {repeticiones} veces")
    return

def main():
    lista = []
    while True:
        print("\n--- MENÚ ---")
        print("1. Añadir un número a la lista")
        print("2. Añadir un número a la lista en una posición")
        print("3. Longitud de la lista")
        print("4. Eliminar el último número")
        print("5. Eliminar un número por posición")
        print("6. Contar apariciones de un número")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            numero = int(input("Introduce un número: "))
            anadir_numero(lista, numero)

        elif opcion == "2":
            numero = int(input("Introduce un número: "))
            pos = int(input("Introduce la posición: "))
            anadir_numero_en_posicion(lista, numero, pos)

        elif opcion == "3":
            longitud_lista(lista)

        elif opcion == "4":
            eliminar_ultimo_numero(lista)

        elif opcion == "5":
            pos = int(input("Introduce la posición a eliminar: "))
            eliminar_numero_en_posicion(lista, pos)

        elif opcion == "6":
            numero = int(input("Introduce un número a contar: "))
            contar_apariciones(lista, numero)

        elif opcion == "7":
            print("Saliendo del programa...")
            break

        else:
            print("❌ Opción no válida")

        print(f"Lista actual: {lista}")
    return

# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
