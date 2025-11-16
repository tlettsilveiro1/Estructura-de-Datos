from collections import deque
import numpy as np

class Socio:
    def __init__(self, id_socio, nombre, apellido):
        self._id_socio = id_socio
        self._nombre = nombre
        self._apellido = apellido
        # Atributo requerido por la consigna (punto 2.1)
        self._reservas_realizadas = []

    @property #hace que la funcion se comporte como un atributo (se puede llamar si el parentesis), sirve para encapsulamiento
    def id_socio(self):
        return self._id_socio

    @id_socio.setter #Sirve para proteger atributos internos (_edad, _nombre, etc.) y tener validaciones o cálculos automáticos al accederlos o modificarlos.
    def id_socio(self, value):
        self._id_socio = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, value):
        self._apellido = value

    @property
    def reservas_realizadas(self):
        return self._reservas_realizadas

    @reservas_realizadas.setter
    def reservas_realizadas(self, value):
        self._reservas_realizadas = value

    def __str__(self):
        return f"Socio: {self.nombre} {self.apellido} (ID: {self.id_socio})"

    def __repr__(self): #Como esta definido aca, no tiene ningun sentido (sirve para mostrar cosas especiales a programadores)
        return self.__str__()


class SolicitudReserva:
    def __init__(self, tipo_de_clase, cantidad_de_personas, numero_dia, id_socio):
        self._tipo_de_clase = tipo_de_clase
        self._cantidad_de_personas = cantidad_de_personas
        self._numero_dia = numero_dia
        self._id_socio = id_socio

    @property
    def tipo_de_clase(self):
        return self._tipo_de_clase

    @tipo_de_clase.setter
    def tipo_de_clase(self, value):
        self._tipo_de_clase = value

    @property
    def cantidad_de_personas(self):
        return self._cantidad_de_personas

    @cantidad_de_personas.setter
    def cantidad_de_personas(self, value):
        self._cantidad_de_personas = value

    @property
    def numero_dia(self):
        return self._numero_dia

    @numero_dia.setter
    def numero_dia(self, value):
        self._numero_dia = value

    @property
    def id_socio(self):
        return self._id_socio

    @id_socio.setter
    def id_socio(self, value):
        self._id_socio = value

    def __str__(self):
        return f"Sol. {self.id_socio} - {self.tipo_de_clase} (Día {self.numero_dia})"


class Reserva:
    def __init__(self, tipo_de_clase, cantidad_de_personas, dia, id_socio):
        self._tipo_de_clase = tipo_de_clase
        self._cantidad_de_personas = cantidad_de_personas
        self._dia = dia
        self._id_socio = id_socio

    @property
    def tipo_de_clase(self):
        return self._tipo_de_clase

    @tipo_de_clase.setter
    def tipo_de_clase(self, value):
        self._tipo_de_clase = value

    @property
    def cantidad_de_personas(self):
        return self._cantidad_de_personas

    @cantidad_de_personas.setter
    def cantidad_de_personas(self, value):
        self._cantidad_de_personas = value

    @property
    def dia(self):
        return self._dia

    @dia.setter
    def dia(self, value):
        self._dia = value

    @property
    def id_socio(self):
        return self._id_socio

    @id_socio.setter
    def id_socio(self, value):
        self._id_socio = value

    def __str__(self):
        return f"Reserva: {self.id_socio} - {self.tipo_de_clase} ({self.dia})"


class TipoMembresia:
    def __init__(self, nombre_membresia, descuento):
        self._nombre_membresia = nombre_membresia
        self._descuento = descuento

    @property
    def nombre_membresia(self):
        return self._nombre_membresia

    @nombre_membresia.setter
    def nombre_membresia(self, value):
        self._nombre_membresia = value

    @property
    def descuento(self):
        return self._descuento

    @descuento.setter
    def descuento(self, value):
        self._descuento = value

    def __str__(self):
        return f"Membresía: {self.nombre_membresia} ({self.descuento}%)"

    # Agregamos __eq__ para facilitar búsquedas y eliminaciones si fuera necesario
    # Aunque la implementación de modificar/eliminar la haremos manual
    def __eq__(self, other): #Sirve para comparar objetos (con '==')
        if isinstance(other, TipoMembresia):
            return self.nombre_membresia == other.nombre_membresia
        return False


# --- ESTRUCTURAS DE DATOS (con modificación permitida) ---
class Nodo: #Codigo generico de nodo con modificacion para este ejercicio (esta en practica 2b)
    def __init__(self, dato):
        self._dato = dato
        self._siguiente = None

    @property
    def dato(self):
        return self._dato

    @dato.setter
    def dato(self, value):
        self._dato = value

    @property
    def siguiente(self):
        return self._siguiente

    @siguiente.setter
    def siguiente(self, value):
        self._siguiente = value

    def __str__(self):
        siguiente = self.siguiente.dato if self.siguiente else None
        return f"{self.dato} y mi siguiente es {siguiente}"


class ListaEnlazada: #Codigo generico de lista enlazada simple (esta en practica 2b)
    def __init__(self):
        self.inicio = None

    def esVacia(self):
        return self.inicio == None

    def agregarAlFinal(self, dato):
        nodo = Nodo(dato)
        if self.esVacia():
            self.inicio = nodo
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo

    def agregarAlInicio(self, dato):
        nodo = Nodo(dato)
        if self.esVacia():
            self.inicio = nodo
        else:
            nodo.siguiente = self.inicio
            self.inicio = nodo

    def __str__(self):
        elementos = []
        actual = self.inicio
        if actual == None:
            return "La lista esta vacia"
        else:
            while actual:
                elementos.append(str(actual.dato))
                actual = actual.siguiente
            return "->".join(elementos)

    def mostrar(self):
        if self.esVacia():
            print("La lista esta vacia")
        else:
            actual = self.inicio
            while actual:
                print(actual.dato)  # Imprime solo el dato, no la info del nodo
                actual = actual.siguiente

    def buscar_reemplazar(self, dato, nuevo):
        if self.esVacia():
            print("La lista esta vacia")
        else:
            actual = self.inicio
            while actual:
                if actual.dato == dato:
                    actual.dato = nuevo
                    return True
                else:
                    actual = actual.siguiente
            return False


# --- IMPLEMENTACIÓN DEL SISTEMA ---
class SistemaGym:
    historial_clases = [
        ["lunes", "yoga", 10, 15000.00],
        ["martes", "spinning", 15, 22500.50],
        ["miércoles", "funcional", 12, 18000.00],
        ["jueves", "pilates", 8, 14400.00],
        ["viernes", "yoga", 11, 16500.00],
        ["lunes", "spinning", 14, 21000.00],
        ["martes", "funcional", 10, 15000.00],
        ["miércoles", "pilates", 9, 16200.75],
        ["jueves", "yoga", 13, 19500.00],
        ["viernes", "spinning", 16, 24000.90],
        ["lunes", "funcional", 11, 16500.00],
        ["martes", "pilates", 7, 12600.00],
        ["miércoles", "yoga", 14, 21000.00],
        ["jueves", "spinning", 12, 18000.00],
        ["viernes", "funcional", 13, 19500.00],
        ["lunes", "pilates", 10, 18000.50],
        ["martes", "yoga", 12, 18000.00],
        ["miércoles", "spinning", 15, 22500.00],
        ["jueves", "funcional", 9, 13500.00],
        ["viernes", "pilates", 8, 14400.00],]

    # --- MÉTODO AÑADIDO (Extensión de clase) ---
    def __init__(self):
        # Usamos un diccionario para socios para búsqueda rápida por ID (O(1))
        self.socios = {}
        # Usamos la ListaEnlazada como Cola para solicitudes (FIFO)
        self.solicitudes_pendientes = deque()
        # Usamos una ListaEnlazada para membresías (como pide la consigna)
        self.membresias = ListaEnlazada()
        # (Opcional) Un registro de reservas procesadas
        self.reservas_confirmadas = []

        # Datos para validación
        self.dias_semana = {
            1: "lunes",
            2: "martes",
            3: "miércoles",
            4: "jueves",
            5: "viernes",
            6: "sábado",
            0: "domingo",
        }
        self.clases_validas = ["yoga", "spinning", "funcional", "pilates"]

    # --- MÉTODOS A IMPLEMENTAR ---
    def agregar_socio(self, socio):
        # 3.1. Agregar un socio (Validando ID único)
        if socio.id_socio in self.socios:
            raise ValueError(f"Ya existe un socio con el ID {socio.id_socio}")
        self.socios[socio.id_socio] = socio
        print(f"Socio {socio.nombre} (ID: {socio.id_socio}) agregado.")

    def cargar_reservas(self, solicitudes_de_reserva):
        # 3.2. Cargar solicitudes (en la cola)
        count = 0
        for sol in solicitudes_de_reserva:
            self.solicitudes_pendientes.append(sol)
            count += 1
        print(f"Se cargaron {count} solicitudes de reserva.")

    def mostrar_solicitudes_pendientes(self):
        """Muestra las solicitudes pendientes de forma legible"""
        if not self.solicitudes_pendientes:
            print("No hay solicitudes pendientes.")
            return
        print(f"Solicitudes pendientes ({len(self.solicitudes_pendientes)}):")
        for i, solicitud in enumerate(self.solicitudes_pendientes, 1):
            print(f"  {i}. {solicitud}")

    def procesar_siguiente_solicitud(self):
        # 3.3. Procesar siguiente solicitud (FIFO)
        # 1. Tomar la siguiente solicitud
        if not self.solicitudes_pendientes:
            raise IndexError("No hay reservas para procesar")
        solicitud = self.solicitudes_pendientes.popleft()

        # 2. Validar
        if not (0 <= solicitud.numero_dia <= 6):
            raise ValueError(f"Día {solicitud.numero_dia} inválido")
        if solicitud.tipo_de_clase not in self.clases_validas:
            raise ValueError(f"Clase '{solicitud.tipo_de_clase}' inválida")
        if solicitud.id_socio not in self.socios:
            raise KeyError(f"Socio ID {solicitud.id_socio} no encontrado")

        # 3. Crear la reserva
        nombre_dia = self.dias_semana[solicitud.numero_dia]
        nueva_reserva = Reserva(
            id_socio=solicitud.id_socio,
            tipo_de_clase=solicitud.tipo_de_clase,
            cantidad_de_personas=solicitud.cantidad_de_personas,
            dia=self.dias_semana[solicitud.numero_dia],)

        # 4. Asociar al socio
        socio = self.socios[solicitud.id_socio]
        socio.reservas_realizadas.append(nueva_reserva)

        # (Opcional) Guardar en el sistema
        self.reservas_confirmadas.append(nueva_reserva)
        print(f"Reserva procesada para el socio con ID: {solicitud.id_socio} con día {nombre_dia}")

    def agregar_membresia(self, membresia):
        # 3.4. Agregar nueva membresía (al final de la lista)
        # Asumimos que el chequeo de duplicados no es necesario
        self.membresias.agregarAlFinal(membresia)
        print(f"Membresía '{membresia.nombre_membresia}' agregada.")

    def modificar_membresia(self, nombre_membresia, nuevo_descuento):
        # 3.4. Modificar membresía (recorriendo la lista enlazada)
        actual = self.membresias.inicio
        encontrado = False
        while actual and not encontrado:
            if actual.dato.nombre_membresia == nombre_membresia:
                actual.dato.descuento = nuevo_descuento
                encontrado = True
            actual = actual.siguiente
        if not encontrado:
            raise KeyError(f"Membresía '{nombre_membresia}' no encontrada")
        print(f"Membresía modificada para el tipo {nombre_membresia}")

    def eliminar_membresia(self, nombre_membresia):
        # 3.4. Eliminar membresía (recorriendo y re-enlazando)
        if self.membresias.esVacia():
            print("Membresía no encontrada.")
            return
        actual = self.membresias.inicio
        previo = None
        encontrado = False
        while actual:
            if actual.dato.nombre_membresia == nombre_membresia and not encontrado:
                encontrado = True
                if previo is None:
                    # El nodo a eliminar es el primero
                    self.membresias.inicio = actual.siguiente
                else:
                    # El nodo a eliminar está en medio o al final
                    previo.siguiente = actual.siguiente
            previo = actual
            actual = actual.siguiente
        if not encontrado:
            raise KeyError(f"Membresía '{nombre_membresia}' no encontrada")
        print(f"Membresía '{nombre_membresia}' eliminada.")

    def generar_estadisticas(self):
        # 3.5. Generar estadísticas con NumPy
        print("--- Estadísticas del Gimnasio ---")
        if len(self.historial_clases) == 0:
            print("No hay datos históricos para analizar.")
            return
        try:
            # Convertir la lista de listas a un array de NumPy
            # Usamos dtype=object para manejar tipos mixtos (strings y números)
            historial = np.array(self.historial_clases, dtype=object)

            # --- 1. Promedio de ingreso total por día ---
            print("Promedio de ingreso por día:")
            # Obtenemos los días únicos (lunes, martes, ...)
            dias_unicos = np.unique(historial[:, 0]) #elementos unicos sobre la primera columna
            for dia in dias_unicos:
                # Filtramos el array para obtener solo las filas de ese día
                this_day = historial[:, 0] == dia
                filas_dia = historial[this_day]
                # Extraemos la columna de ingresos (índice 3) y la convertimos a float
                ingresos_dia = filas_dia[:, 3].astype(float)
                # Calculamos el promedio
                promedio = np.mean(ingresos_dia)
                print(f"{dia.capitalize()}: ${promedio:.2f}")
            print("\n")  # Separador

            # --- 2. La clase que tuvo la mayor cantidad acumulada de socios ---
            # Obtenemos los tipos de clase únicos
            clases_unicas = np.unique(historial[:, 1])
            # Diccionario para almacenar la cantidad acumulada de socios por tipo de clase
            socios_por_clase = {}
            for clase in clases_unicas:
                # Filtramos el array para obtener solo las filas de esa clase
                filas_clase = historial[historial[:, 1] == clase]
                # Extraemos la columna de cantidad de socios y sumamos
                cantidad_total = np.sum(filas_clase[:, 2].astype(int))
                socios_por_clase[clase] = cantidad_total
            # Encontramos la clase con mayor cantidad acumulada
            clase_max = max(socios_por_clase, key=socios_por_clase.get)
            cantidad_max = socios_por_clase[clase_max]
            print("Clase con mayor cantidad acumulada de socios:")
            print(f"Tipo de clase: {clase_max.capitalize()}")
            print(f"Cantidad total de socios: {cantidad_max}")
        except ImportError:
            print("Error: Se requiere la biblioteca NumPy para esta función.")
        except Exception as e:
            print(f"Ocurrió un error inesperado al generar estadísticas: {e}")


# --- CÓDIGO PRINCIPAL DE PRUEBA (Main) ---
if __name__ == "__main__":
    # 1. Inicializar sistema
    sistema = SistemaGym()
    print("Sistema GymFlex iniciado.")
    print("-" * 30)
    # 2. Agregar Socios (3.1)
    s1 = Socio(101, "Ana", "Gomez")
    s2 = Socio(102, "Luis", "Perez")
    s3 = Socio(103, "Carla", "Ruiz")

    try:
        sistema.agregar_socio(s1)
    except ValueError as e:
        print(f"Error al agregar socio: {e}")
    try:
        sistema.agregar_socio(Socio(101, "Otro", "Nombre"))  # Prueba de ID duplicado
    except ValueError as e:
        print(f"Error al agregar socio: {e}")
    try:
        sistema.agregar_socio(s2)
    except ValueError as e:
        print(f"Error al agregar socio: {e}")
    try:
        sistema.agregar_socio(s3)
    except ValueError as e:
        print(f"Error al agregar socio: {e}")
    print("-" * 30)

    # 3. Gestionar Membresías (3.4)
    m_oro = TipoMembresia("Oro", 20)
    m_plata = TipoMembresia("Plata", 10)
    m_bronce = TipoMembresia("Bronce", 5)
    sistema.agregar_membresia(m_oro)
    sistema.agregar_membresia(m_plata)
    sistema.agregar_membresia(m_bronce)
    print("\nMembresías actuales:")
    sistema.membresias.mostrar()
    print("\nModificando membresías...")
    try:
        sistema.modificar_membresia("Plata", 15)  # Modificación exitosa
    except KeyError as e: #aparece cuando intentás acceder a una clave (key) que no existe en un diccionario.
        print(f"Error al modificar membresía: {e}")
    try:
        sistema.modificar_membresia("Diamante", 50)  # Modificación fallida
    except KeyError as e:
        print(f"Error al modificar membresía: {e}")
    print("\nEliminando membresías...")
    try:
        sistema.eliminar_membresia("Oro")  # Eliminar el primero
    except KeyError as e:
        print(f"Error al eliminar membresía: {e}")
    try:
        sistema.eliminar_membresia("Diamante")  # Eliminar fallido
    except KeyError as e:
        print(f"Error al eliminar membresía: {e}")
    print("\nMembresías restantes:")
    sistema.membresias.mostrar()
    print("-" * 30)

    # 4. Cargar Solicitudes (3.2)
    solicitudes = [
        SolicitudReserva("yoga", 1, 0, 101),  # Lunes, Ana (Válida)
        SolicitudReserva("spinning", 2, 1, 102),  # Martes, Luis (Válida)
        SolicitudReserva("zumba", 1, 2, 103),  # Miércoles, Carla (Actividad inválida)
        SolicitudReserva("funcional", 1, 8, 101),  # Día inválido
        SolicitudReserva("pilates", 1, 4, 205),  # Viernes, Socio inexistente
        SolicitudReserva("funcional", 1, 3, 103),]  # Jueves, Carla (Válida)
    sistema.cargar_reservas(solicitudes)
    print()
    sistema.mostrar_solicitudes_pendientes()
    print("-" * 30)

    # 5. Procesar Solicitudes (3.3)
    print("Procesando reservas...")
    try:
        sistema.procesar_siguiente_solicitud()  # Procesa Yoga (Ana)
    except (ValueError, KeyError, IndexError) as e: #IndexError ocurre cuando intentás acceder a un índice que no existe en una lista, tupla o string.
        print(f"Error al procesar solicitud: {e}")
    try:
        sistema.procesar_siguiente_solicitud()  # Procesa Spinning (Luis)
    except (ValueError, KeyError, IndexError) as e:
        print(f"Error al procesar solicitud: {e}")
    try:
        sistema.procesar_siguiente_solicitud()  # Procesa Zumba (Inválida)
    except (ValueError, KeyError, IndexError) as e:
        print(f"Error al procesar solicitud: {e}")
    try:
        sistema.procesar_siguiente_solicitud()  # Procesa Funcional (Día inválido)
    except (ValueError, KeyError, IndexError) as e:
        print(f"Error al procesar solicitud: {e}")
    try:
        sistema.procesar_siguiente_solicitud()  # Procesa Pilates (Socio inválido)
    except (ValueError, KeyError, IndexError) as e:
        print(f"Error al procesar solicitud: {e}")
    try:
        sistema.procesar_siguiente_solicitud()  # Procesa Funcional (Carla)
    except (ValueError, KeyError, IndexError) as e:
        print(f"Error al procesar solicitud: {e}")
    try:
        sistema.procesar_siguiente_solicitud()  # Cola vacía
    except (ValueError, KeyError, IndexError) as e:
        print(f"Error al procesar solicitud: {e}")
    print("-" * 30)

    # 6. Verificar reservas de socios
    print("Reservas de Ana Gomez (ID 101):")
    for r in s1.reservas_realizadas:
        print(f"  - {r.tipo_de_clase} el día {r.dia}")
    print("\nReservas de Carla Ruiz (ID 103):")
    for r in s3.reservas_realizadas:
        print(f"  - {r.tipo_de_clase} el día {r.dia}")
    print("-" * 30)

    # 7. Generar Estadísticas (3.5)
    sistema.generar_estadisticas()
    print("-" * 30)