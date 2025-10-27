import csv
def filtrar_por_anio(nombre_archivo):
    inicio = int(input("Año inicio: "))
    fin = int(input("Año final: "))

    with open(nombre_archivo, "r", newline="") as f:
        reader = csv.DictReader(f)  # Lee con encabezados como diccionario
        filtrados = []
        for fila in reader:
            anio = int(fila["Year Released"])
            if inicio <= anio <= fin:
                filtrados.append(fila)

    # Mostrar resultados
    if not filtrados:
        print("\n❌ No hay libros en ese rango de años.")
    else:
        print("\nBook                                   | Author              | Year Released")
        print("-------------------------------------- | ------------------- | -------------")
        for fila in filtrados:
            print(f"{fila['Book']:<38} | {fila['Author']:<19} | {fila['Year Released']}")
            #El menor sirve para que minimamente ocupe ese largo y quede parejo (el menor es para alinearlo a la izq.)


archivo = "libros.csv"
filtrar_por_anio(archivo)