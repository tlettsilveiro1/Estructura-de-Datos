from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from collections import deque

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None

@dataclass(frozen=True) #es para clases con solo guardar datos, y el 'frozen' garantiza que los datos no se modifiquen
class Llamada:
    cliente: str
    tipo: str
    ticket: int
    timestamp: datetime
    operador: Optional[str] = None

    def __str__(self):
        return f'El llamado corresponde al cliente {self.cliente}, del tipo {self.tipo}, ticket {self.ticket}, {self.timestamp}, operador asignado: {self.operador}'
    
class Operador:
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._ocupado = False # de base lo ponemos libre, cuando se ocupa ponemos True 
        self._llamadas_atendidas = 0 #int llamadas atendidas como contador para luego usar para analisis de datos 

    @property
    def nombre(self):
        return self._nombre

    @property
    def ocupado(self):  #Este atributo es interno, no debería modificarse ni accederse directamente desde afuera
        return self._ocupado

    @property
    def llamadas_atendidas(self):
        return self._llamadas_atendidas

    def ocupar(self): # cuando se ocupa aumento el contador por 1 
        self._ocupado = True
        self._llamadas_atendidas += 1

    def desocupar(self):
        self._ocupado = False

    def __repr__(self): #No cumple ninguna funcion, igual al '__str__'
        return f"Operador({self.nombre}, ocupado={self.ocupado})"
    def __str__(self):
        return f"Operador({self.nombre}, ocupado={self.ocupado})"

class SistemaCallCenter:
    def __init__(self):
        self.operadores = set()
        self.tipos_validos = set() #asi con el set directo esta bueno para que ese ateributo sea unico 
        self.cola_llamadas = deque() #Se trata como una COLA
        self.llamadas_en_curso = {}
        self.ticket_counter = 1
        self.historial_head = None
        self.pila_undo = []

    def registrar_operador(self, operador:Operador):
        if operador.nombre in {op.nombre for op in self.operadores}:
            raise ValueError("Operador duplicado")
        self.operadores.add(operador)

    def definir_tipo_consulta(self, tipo):
        self.tipos_validos.add(tipo)

    def recibir_llamada(self, cliente, tipo):
        if tipo not in self.tipos_validos:
            raise ValueError("Tipo no válido")

        ticket = self.ticket_counter
        self.ticket_counter += 1

        llamada = Llamada(cliente, tipo, ticket, datetime.now())
        self.cola_llamadas.append(llamada)
        return ticket

    def _buscar_operador_disponible(self):
        for op in self.operadores:
            if not op.ocupado:
                return op
        return None

    def atender_siguiente(self):
        if not self.cola_llamadas:
            return "No hay llamadas pendientes"

        oper = self._buscar_operador_disponible()
        if not oper:
            return "No hay operadores disponibles"

        llamada = self.cola_llamadas.popleft()
        oper.ocupar()

        llamada_asignada = Llamada(
            cliente=llamada.cliente,
            tipo=llamada.tipo,
            ticket=llamada.ticket,
            timestamp=llamada.timestamp,
            operador=oper.nombre
        )

        self.llamadas_en_curso[llamada.ticket] = llamada_asignada #agrega llamada al diccionario de llamadas en cuerso con el ticket como llave 
        self.pila_undo.append((llamada_asignada, oper)) #pila undo lleva registro de las llamadas activas con su operador 
        return llamada_asignada

    def finalizar_llamada(self, ticket):
        if ticket not in self.llamadas_en_curso:
            raise ValueError("Ticket no encontrado")

        llamada = self.llamadas_en_curso.pop(ticket)
        operador = self._buscar_operador_por_nombre(llamada.operador)
        operador.desocupar()

        nodo = Nodo(llamada)
        nodo.next = self.historial_head # aca se utiliza la lista enlazada para llevar un registro de las llamadas hechas 
        self.historial_head = nodo

    def _buscar_operador_por_nombre(self, nombre): #buscar operador clave para poder llamarlo como variable 
        for op in self.operadores:
            if op.nombre == nombre:
                return op
        raise ValueError("Operador no encontrado")

    def deshacer_ultima_asignacion(self):
        if not self.pila_undo:
            return "Nada para deshacer"

        llamada, operador = self.pila_undo.pop()
        operador.desocupar()
        self.llamadas_en_curso.pop(llamada.ticket, None) #elimina esa llamada en particular
        self.cola_llamadas.insert(0, llamada) #lo mismo que hacer 'appendleft(llamada)'
        return f"Deshecha asignación del ticket {llamada.ticket}"

#Ejemplo de Uso 
s = SistemaCallCenter()

s.definir_tipo_consulta("facturación")
s.definir_tipo_consulta("técnico")

s.registrar_operador(Operador("Ana"))
s.registrar_operador(Operador("Luis"))

t1 = s.recibir_llamada("Juan", "facturación")
t2 = s.recibir_llamada("María", "técnico")

print(s.atender_siguiente())
print(s.atender_siguiente())

s.finalizar_llamada(t1)
s.finalizar_llamada(t2)

print(s.deshacer_ultima_asignacion())

print(s._buscar_operador_disponible())
print(s._buscar_operador_por_nombre('Luis'))