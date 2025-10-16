from __future__ import annotations
import random
import csv

class Dni:
    @staticmethod        
    def validar_dni(dni):
        if not isinstance(dni, int):
            raise ValueError("El dni debe ser un numero entero")
        
        if dni <10000000 or dni > 99999999:
            raise ValueError("El dni debe tener 8 dígitos")
        

class Jugador:
    dnis = []

    @staticmethod        
    def validar_nombre(nombre):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser un string")

        if len(nombre) == 0:
            raise ValueError("El nombre no puede ser vacio")
        
        if len(list(filter(lambda caracter: caracter.isdigit(), nombre)) )> 0:
            raise ValueError("El nombre no puede incluir números.")


    def __init__(self, nombre: str, dni: int):
        
        Jugador.validar_nombre(nombre)
        Dni.validar_dni(dni)

        if dni in Jugador.dnis:
            raise ValueError(f"Ya existe un jugador con DNI {dni}.")

        Jugador.dnis.append(dni)

        self.nombre = nombre
        self.dni = dni
        self.cartas = []

    def recibir_carta(self, carta):
        if not isinstance(carta, Carta):
            raise ValueError("Objeto recibido no es una Carta.")
        self.cartas.append(carta)

    def puntaje_total(self):
        return sum(map(lambda carta: carta.obtener_puntaje(), self.cartas))
    
    def get_dni(self):
        return self.dni
    
    def get_nombre(self):
        return self.nombre

    def __repr__(self):
        return f"Jugador:{self.nombre}, dni={self.dni}, Cartas:{self.cartas}"


class Carta:
    def __init__(self, numero):
        Carta.validar_numero(numero)
        self.numero = numero

    @staticmethod
    def validar_numero(numero):
        if numero < 10 or numero > 20:
            raise ValueError("El numero de la carta debe estar entre 10 y 20.")

    def obtener_valor(self):
        pass

    def __str__(self):
        return f"Carta {self.color} numero {self.numero}"
    
    def __repr__(self):
        return self.__str__()
    
class CartaRoja(Carta):

    def __init__(self, numero):
        super().__init__(numero)
        self.color = "roja"

    def obtener_puntaje(self):
        return self.numero


class CartaAmarilla(Carta):

    def __init__(self, numero):
        super().__init__(numero)
        self.color = "amarilla"

    def obtener_puntaje(self):
        return self.numero + 10


class CartaVerde(Carta):

    def __init__(self, numero):
        super().__init__(numero)
        self.color = "verde"


    def obtener_puntaje(self):
        return self.numero * 3

class Juego:
    def __init__(self):
        self.jugadores = {}
        self.finalizado = False

    def validar_finalizado(self):
        if self.finalizado:
            raise ValueError("El juego se encuentra finalizado")

    def agregar_jugador(self, jugador: Jugador):
        if not isinstance(jugador, Jugador):
            raise ValueError("Debe agregarse una instancia de Jugador.")
        
        if jugador.get_dni() in self.jugadores:
            raise ValueError(f"El jugador con DNI {jugador.dni} ya está en este juego.")
        
        self.validar_finalizado()

        self.jugadores[jugador.dni] = jugador

    def asignar_carta(self, dni: int):
        self.validar_finalizado()
        Dni.validar_dni(dni)

        jugador = self.jugadores.get(dni)
        if jugador is None:
            raise ValueError(f"No existe un jugador con DNI {dni} en este juego.")
        
        peso = random.random()
        numero = random.randint(10, 20)

        if peso < 0.5:
            carta = CartaRoja(numero)
        elif peso < 0.8:
            carta = CartaAmarilla(numero)
        else:
            carta = CartaVerde(numero)

        jugador.recibir_carta(carta)


    def mostrar_jugadores(self):
        """
        Debe imprimir exactamente como en el ejemplo:
        Nombre: X, DNI: Y, Cartas: [ Carta roja de 10 puntos, Carta verde de 20 puntos ]
        """
        for jugador in self.jugadores.values():
            print(jugador)

    def finalizar_juego(self):
        self.validar_finalizado()
        self._finalizado = True
        
        ranking = sorted(self.jugadores.values(),
                         key=lambda j: j.puntaje_total(),
                         reverse=True)
        for jugador in ranking:
            print(f"{jugador.get_nombre()}: {jugador.puntaje_total()} puntos")
        
        ganador = ranking[0]    
        print(f'\nEl ganador es: {ganador.get_nombre()} (DNI: {ganador.get_dni()})')

    def generar_csv(self):
        """
        Genera un CSV con los jugadores que superen 'umbral' puntos.
        Formato:
        dni,jugador,puntaje
        36554771,Mariano Perez,95
        """
        if not self._finalizado:
            raise ValueError("Para generar el CSV primero se debe finalizar el juego.")
        
        jugadores_filtrados = list(filter(lambda jugador: jugador.puntaje_total() > 50, self.jugadores.values()))
        
        with open("jugadores.csv", mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["dni", "jugador", "puntaje"])
            for j in jugadores_filtrados:
                writer.writerow([j.get_dni(), j.get_nombre(), j.puntaje_total()])


if __name__ == "__main__":
    jugador1 = Jugador("Mariano Perez", 36554771)
    jugador2 = Jugador("Juana Fernandez", 39554112)

    # Crear juego y agregar jugadores
    juego = Juego()
    juego.agregar_jugador(jugador1)
    juego.agregar_jugador(jugador2)

    # Asignaciones aleatorias (puede tocar más de una vez al mismo jugador)
    juego.asignar_carta(36554771)
    juego.asignar_carta(36554771)
    juego.asignar_carta(36554771)

    juego.asignar_carta(39554112)
    juego.asignar_carta(39554112)
    juego.asignar_carta(39554112)

    # Mostrar jugadores y sus cartas en el formato requerido
    print()
    juego.mostrar_jugadores()
    print()
    juego.finalizar_juego()

    # Extra: generar CSV con jugadores > 50 puntos
    juego.generar_csv() 