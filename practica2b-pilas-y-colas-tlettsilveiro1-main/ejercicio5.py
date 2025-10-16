# Ejercicio 5: Apilar cartas con reglas
# Clase que representa una carta individual
class Carta:
    def __init__(self, numero, palo):
        self.numero = numero     # valor numérico (1 a 13)
        self.palo = palo         # por ejemplo: "corazones", "tréboles", etc.

    def __str__(self):
        return f"{self.numero} de {self.palo}"
    

# Clase que representa la pila de cartas
class PilaDeCartas:
    def __init__(self):
        self.cartas = []   # lista usada como pila

    # Método para apilar una carta bajo las condiciones del ejercicio
    def apilar(self, carta):
        if len(self.cartas) == 0:
            # Si la pila está vacía, se puede apilar cualquier carta
            self.cartas.append(carta)
        else:
            # Obtener la carta que está actualmente en la cima
            carta_superior = self.cartas[-1]

            # Validar las condiciones:
            # 1. La nueva carta debe tener número inferior en 1
            # 2. Debe tener palo distinto
            if carta.numero == carta_superior.numero - 1 and carta.palo != carta_superior.palo:
                self.cartas.append(carta)
            else:
                # Si no cumple las condiciones, lanzar excepción
                raise ValueError(
                    f"No se puede apilar {carta}. "
                    f"Debe ser un número menor y de distinto palo que {carta_superior}."
                )

    # Representación en texto de toda la pila
    def __str__(self):
        if len(self.cartas) == 0:
            return "La pila está vacía."
        else:
            texto = "🃏 Pila de cartas:\n"
            for i in range(len(self.cartas) - 1, -1, -1):  # mostrar desde la cima
                texto += f" -> {self.cartas[i]}\n"
            return texto



try:
    pila = PilaDeCartas()

    carta1 = Carta(13, "corazones")   # Rey de corazones
    carta2 = Carta(12, "tréboles")    # Reina de tréboles
    carta3 = Carta(11, "tréboles")    # Jota de tréboles (mismo palo → error)
    carta4 = Carta(11, "picas")       # Jota de picas (válida)

    pila.apilar(carta1)
    pila.apilar(carta2)
    pila.apilar(carta4)   # válida

    print(pila)

    pila.apilar(carta3)   # lanza excepción
except ValueError as e:
    print("❌ Error:", e)