class Hotel:
    def __init__(self, nombre, idHotel, zona, precio):
        self.nombre = nombre
        self.idHotel = idHotel
        self.zona = zona
        self.precio = precio

    def __str__(self):
        return f"Hotel(nombre={self.nombre}, idHotel={self.idHotel}, zona={self.zona}, precio={self.precio}€)"

    # Necesario para que el hotel pueda estar en un set
    def __eq__(self, other):
        if isinstance(other, Hotel):
            return self.idHotel == other.idHotel  # ID único
        return False

    def __hash__(self):
        return hash(self.idHotel)


def cargar_hoteles():
    hoteles = set()
    
    # Ejemplo de carga de 3 hoteles, se puede ampliar
    while True:
        nombre = input("Ingrese el nombre del hotel (o 'fin' para terminar): ")
        if nombre.lower() == "fin":
            break

        try:
            idHotel = int(input("Ingrese el ID del hotel (número único): "))
        except ValueError:
            print("ID debe ser un número entero. Intente nuevamente.")
            continue #Se usa para que se repita el while otra vez, evita que siga (salta al siguiente ciclo)

        zona = input("Ingrese la zona del hotel (playa/montaña/rural): ").lower()
        if zona not in ["playa", "montaña", "rural"]:
            print("Zona inválida. Intente nuevamente.")
            continue

        try:
            precio = int(input("Ingrese el precio por noche (40-150€): "))
            if precio < 40 or precio > 150:
                print("Precio fuera de rango. Intente nuevamente.")
                continue
        except ValueError:
            print("Precio debe ser un número entero. Intente nuevamente.")
            continue

        hotel = Hotel(nombre, idHotel, zona, precio)
        if hotel in hoteles:
            print("Ya existe un hotel con ese ID. No se agregará.")
        else:
            hoteles.add(hotel)
            print("Hotel agregado correctamente.\n")
    
    return hoteles


def mostrar_hoteles(hoteles):
    print("\nHoteles de la cadena:")
    for hotel in hoteles:
        print(hotel)


def mostrar_hoteles_por_zona(hoteles):
    zona = input("Ingrese la zona que desea consultar (playa/montaña/rural): ").lower()
    if zona not in ["playa", "montaña", "rural"]:
        print("Zona inválida.")
        return

    print(f"\nHoteles disponibles en la zona {zona}:")
    encontrados = False
    for hotel in hoteles:
        if hotel.zona == zona:
            print(f"{hotel.nombre} - Precio por noche: {hotel.precio}€")
            encontrados = True

    if not encontrados:
        print("No hay hoteles disponibles en esta zona.")


def main():
    hoteles = cargar_hoteles()
    mostrar_hoteles(hoteles)
    mostrar_hoteles_por_zona(hoteles)


# Ejecutamos el programa
main()