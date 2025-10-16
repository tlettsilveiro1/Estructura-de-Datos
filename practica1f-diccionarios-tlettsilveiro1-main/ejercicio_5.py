import csv
def crear_csv(nombre_archivo):
    # Datos iniciales
    libros = [
        ["To Kill A Mockingbird", "Harper Lee", 1960],
        ["A Brief History of Time", "Stephen Hawking", 1988],
        ["The Great Gatsby", "F. Scott Fitzgerald", 1922],
        ["The Man Who Mistook His Wife for a Hat", "Oliver Sacks", 1985],
        ["Pride and Prejudice", "Jane Austen", 1813]]

    # Escribir archivo CSV
    with open(nombre_archivo, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Book", "Author", "Year Released"])  # Encabezados
        writer.writerows(libros) # Filas

    print(f"✅ Archivo '{nombre_archivo}' creado con éxito.")

def agregar_lineas(nombre_archivo):
    opcion = input("¿Desea agregar nuevas líneas al archivo? (s/n): ").lower()
    if opcion != "s":
        return print("No se agregaron líneas.")

    n = int(input("¿Cuántas líneas desea agregar? "))

    with open(nombre_archivo, "a", newline="") as f:
        writer = csv.writer(f)
        for i in range(n):
            print(f"\n--- Libro {i+1} ---")
            titulo = input("Título del libro: ")
            autor = input("Autor: ")
            anio = input("Año de publicación: ")
            writer.writerow([titulo, autor, anio])
            #se puede reemplazar las variables por el input directamente

    print(f"✅ {n} línea(s) agregada(s) al archivo.")

archivo = "libros.csv"
crear_csv(archivo) #Crear archivo con datos iniciales, siempre se borra lo anterior
agregar_lineas(archivo) #Preguntar si el usuario quiere agregar más datos
