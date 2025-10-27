from ejercicio_3_biblioteca import Biblioteca, BibliotecaError
from ejercicio_3_libro import Libro
from ejercicio_3_usuario import UsuarioBasico, UsuarioVip #se puede poner * para traer todo

if __name__ == "__main__":
    print("Gestion de bibloteca")
    bibl = Biblioteca("Alejandria")
    print(bibl.get_nombre())
    print(bibl.get_libros())
    libro1 = Libro("El principito", 1943, "Infantil")
    libro2 = Libro("La divina comedia", 1320, "Clásico")
    libro3 = Libro("Cien años de soledad", 1967, "Novela")
    libro4 = Libro("Fantasía épica", 2005, "Fantasía")
    libro5 = Libro("Libro no prestado", 2010, "Misterio")

    print(libro2.titulo)
    print(libro3.titulo)
    bibl.agregar_libro(libro1)
    bibl.agregar_libro(libro2)
    bibl.agregar_libro(libro3)
    bibl.agregar_libro(libro4)
    bibl.agregar_libro(libro5)
    print("Comparo principito")
    print(libro1 is libro3)
    print(libro1 == libro3) # __eq__(principito, libro_3) principito.__eq__(libro_3)
    print(bibl.get_libros())
    print(bibl.cantidad_libros())
    paco = UsuarioBasico("Paco")
    ana = UsuarioVip("Ana")
    try:                   #Aunque el codigo este dentro del try, para el programa es lo mismo
        bibl.agregar_usuario(paco)
        bibl.agregar_usuario(ana)
    except BibliotecaError as b:
        print(b)
    except Exception as e:
        print(e)
    
    print(bibl.get_usuarios())
    print(bibl.get_libros())
    bibl.prestar_libro(paco, libro1)
    bibl.prestar_libro(ana, libro2)
    print(bibl.get_libros())

    # Probar métodos nuevos

    print("\n--- Lectores de Honor ---")
    lectores_honor = bibl.obtener_lectores_de_honor()
    for u in lectores_honor:
        print(u.nombre, "-", u.total_prestamos, "prestamos acumulados")

    print("\n--- Libros nunca prestados ---")
    libros_no_prestados = bibl.listar_libros_no_prestados2()
    for libro in libros_no_prestados:
        print(libro.titulo)

    print("\n--- Promedio de préstamos por usuario ---")
    promedio = bibl.promedio_prestamos_por_usuario2()
    print("Promedio por usuario:", promedio)

    print("\n--- Libro más antiguo prestado por cada usuario ---")
    for u in bibl.usuarios:
        antiguo = u.libro_mas_antiguo_prestado()
        if antiguo != "N/A":
            print(u.nombre, "-", antiguo.titulo, "-", antiguo.anio_publicacion)
        else:
            print(u.nombre, "- N/A")

    print("\n--- Géneros por popularidad ---")
    ranking = bibl.generos_por_popularidad2()
    for genero, cant in ranking:
        print(genero, ":", cant, "préstamos")
