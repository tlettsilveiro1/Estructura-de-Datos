def contar(lista: list, cadena: str):
    repeticiones = lista.count(cadena)
    print(f"Repeticiones: {repeticiones}")

def modificar(lista: list, cadena: str, cadena_nueva: str):
    for i in range(len(lista)):
        if lista[i] == cadena:
            lista[i] = cadena_nueva
    return 

def eliminar(lista: list, cadena: str):
    while cadena in lista:
        lista.remove(cadena)
    return

def main():
    # Implementar lógica de menú

    lista = ["hola","yo","estoy","feliz","en","ITBA",".","ITBA","es","una","de","las","mejores","Universidades","de","Argentina"]
    contar(lista, "ITBA")
    # Debe imprimirse:
    # Repeticiones: 2
    modificar(lista, "ITBA", "el Instituto Tecnologico de Buenos Aires")
    print(lista)
    # Debe imprimirse:
    # ["hola","yo","estoy","feliz","en","el Instituto Tecnologico de Buenos Aires",".","el Instituto Tecnologico de Buenos Aires","es","una","de","las","mejores","Universidades","de","Argentina"]
    eliminar(lista, "hola")
    print(lista)
    # Debe imprimirse:
    # ["yo","estoy","feliz","en","el Instituto Tecnologico de Buenos Aires",".","el Instituto Tecnologico de Buenos Aires","es","una","de","las","mejores","Universidades","de","Argentina"]


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
