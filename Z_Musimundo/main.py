import csv
import random
#Normalmente, para mantener un orden se crea un archivo por cada clase y para el main
# ========== CLASE BASE ==========
class Producto:
    def __init__(self, titulo, artista, anio, codigo):
        if anio <= 0:
            raise ValueError("El año de lanzamiento debe ser positivo.")
        if not Producto.validar_codigo(codigo):
            raise ValueError(f"Código de barras inválido: {codigo}")
        self.titulo = titulo
        self.artista = artista
        self.anio = anio
        self.codigo = codigo

    @staticmethod
    def validar_codigo(codigo):
        if len(codigo) != 12 or not codigo.isdigit():
            return False
        checksum = sum(int(digit) * (3 if i % 2 else 1) for i, digit in enumerate(codigo[:-1])) % 10
        checksum = (10 - checksum) % 10
        return checksum == int(codigo[-1])

    def __str__(self):
        return f"{self.titulo} - {self.artista} ({self.anio}) | Código: {self.codigo}"


# ========== CLASES HIJAS ==========
class CD(Producto):
    def __init__(self, titulo, artista, anio, codigo, duracion):
        super().__init__(titulo, artista, anio, codigo)
        if duracion <= 0:
            raise ValueError("La duración del CD debe ser positiva.")
        self.duracion = duracion

    def __str__(self):
        return f"CD: {super().__str__()} | Duración: {self.duracion} min"


class Vinilo(Producto):
    def __init__(self, titulo, artista, anio, codigo, diametro):
        super().__init__(titulo, artista, anio, codigo)
        if diametro <= 0:
            raise ValueError("El diámetro del vinilo debe ser positivo.")
        self.diametro = diametro

    def __str__(self):
        return f"Vinilo: {super().__str__()} | Diámetro: {self.diametro}''"


# ========== CLASE TIENDA ==========
class Tienda:
    #El diccionario producto va como instancia de clase porque no se comparte entre todas las 
    #tiendas, cada una tiene una independiente al resto, y no va productos despues del primer 
    #"self" porque inicialmente no se saben los productos de cada tienda
    def __init__(self):
        self.productos = {}  # clave: código de barras, valor: instancia de Producto
    
    def agregar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar instancias de Producto.")
        if producto.codigo in self.productos:
            raise ValueError(f"Ya existe un producto con el código {producto.codigo}.")
        self.productos[producto.codigo] = producto

    def eliminar_producto(self, codigo):
        if codigo not in self.productos:
            raise KeyError(f"No existe un producto con el código {codigo}.")
        del self.productos[codigo]

    def buscar_producto(self, codigo):
        if codigo not in self.productos:
            raise KeyError(f"No existe un producto con el código {codigo}.")
        return self.productos[codigo]

    def mostrar_productos(self): #pide mostrar los productos ordenados por año de publicacion ascendiente
        for producto in sorted(self.productos.values(), key=lambda p: p.anio):
            print(producto)
    
#    def mostrar_productos(self): #muestra los productos ordenados por año de publicacion descendiente
#        for producto in sorted(self.productos.values(), key=lambda p: p.anio, reverse=True):
#            print(producto)


    def guardar_csv(self, nombre_archivo):
        try:
            with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(["Título", "Artista", "Año", "Tipo", "Atributo Adicional", "Código"])
                for producto in self.productos.values():
                    if isinstance(producto, CD):
                        tipo = "CD"
                        extra = f"{producto.duracion} min"
                    elif isinstance(producto, Vinilo):
                        tipo = "Vinilo"
                        extra = f"{producto.diametro}''"
                    else:
                        tipo = "Desconocido"
                        extra = ""
                    escritor.writerow([producto.titulo, producto.artista, producto.anio, tipo, extra, producto.codigo])
        except Exception as e:
            raise IOError(f"No se pudo guardar en CSV: {e}")


# ========== FUNCIONES AUXILIARES ==========
def generar_codigo_barras():
    codigo = [random.randint(0, 9) for _ in range(11)]
    checksum = sum(int(digit) * (3 if i % 2 else 1) for i, digit in enumerate(codigo)) % 10
    checksum = (10 - checksum) % 10
    codigo.append(checksum)
    return ''.join(map(str, codigo))


# ========== EJEMPLO DE USO ==========
if __name__ == "__main__":
    try:
        tienda = Tienda()

        cd1 = CD("Back in Black", "AC/DC", 1980, generar_codigo_barras(), 42)
        vinilo1 = Vinilo("Abbey Road", "The Beatles", 1969, generar_codigo_barras(), 12)
        cd2 = CD("Thriller", "Michael Jackson", 1982, generar_codigo_barras(), 39)

        tienda.agregar_producto(cd1)
        tienda.agregar_producto(vinilo1)
        tienda.agregar_producto(cd2)

        print("\n--- Productos en la tienda ---")
        tienda.mostrar_productos()

        print("\n--- Buscar producto ---")
        encontrado = tienda.buscar_producto(cd1.codigo)
        print("Encontrado:", encontrado)

        print("\n--- Guardar CSV ---")
        tienda.guardar_csv("tienda.csv")
        print("Archivo CSV guardado con éxito.")

    except Exception as e:
        print("Error:", e)