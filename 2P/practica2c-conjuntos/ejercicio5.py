# Ejercicio 5
class Cliente:
    def __init__(self, nombre, productos=None):
        self.nombre = nombre
        if productos is None: #la creacion del set solo ocurre la primera vez (momento que se crea el objeto)
            self.productos = set()
        else:
            self.productos = set(productos)  # Convertimos a set por seguridad

    def agregar_productos(self, productos):
        for producto in productos:
            self.productos.add(producto)


class Tienda:
    def __init__(self):
        # Diccionario: clave = nombre del cliente, valor = conjunto de productos
        self.clientes = {}

    def agregar_cliente(self, nombre, productos):
        if nombre in self.clientes:
            # Si el cliente ya existe, agregamos productos
            self.clientes[nombre].agregar_productos(productos)
        else:
            # Si no existe, creamos un nuevo cliente
            self.clientes[nombre] = Cliente(nombre, productos) #se repite el nombre, una como clave de acceso rápida y otra como parte de los datos del cliente.

    def producto_mas_comprado(self):
        contador_productos = {}
        for cliente in self.clientes.values():
            for producto in cliente.productos:
                if producto in contador_productos:
                    contador_productos[producto] += 1
                else:
                    contador_productos[producto] = 1

        # Buscamos el producto con mayor cantidad de apariciones
        max_cantidad = 0
        producto_mas = None
        for producto, cantidad in contador_productos.items():
            if cantidad > max_cantidad:
                max_cantidad = cantidad
                producto_mas = producto
        return producto_mas

    def cliente_mayor_variedad(self):
        max_variedad = 0
        cliente_variedad = None
        for nombre, cliente in self.clientes.items():
            if len(cliente.productos) > max_variedad:
                max_variedad = len(cliente.productos)
                cliente_variedad = nombre
        return cliente_variedad

    def clientes_que_compraron(self, producto):
        resultado = []
        for nombre, cliente in self.clientes.items():
            if producto in cliente.productos:
                resultado.append(nombre)
        return resultado

    def comparar_clientes(self, nombre1, nombre2):
        if nombre1 not in self.clientes or nombre2 not in self.clientes:
            return set()  # Si alguno no existe, retornamos conjunto vacío
        productos1 = self.clientes[nombre1].productos
        productos2 = self.clientes[nombre2].productos
        return productos1.intersection(productos2)


# ------------------ EJEMPLO DE USO ------------------
tienda = Tienda()
tienda.agregar_cliente("Juan", {"Laptop", "Mouse", "Teclado"})
tienda.agregar_cliente("Ana", {"Smartphone", "Auriculares"})
tienda.agregar_cliente("Carlos", {"Laptop", "Teclado", "Monitor"})

print("Producto más comprado:", tienda.producto_mas_comprado())
print("Cliente con mayor variedad:", tienda.cliente_mayor_variedad())
print("Clientes que compraron Laptop:", tienda.clientes_que_compraron("Laptop"))
print("Productos en común entre Juan y Carlos:", tienda.comparar_clientes("Juan", "Carlos"))