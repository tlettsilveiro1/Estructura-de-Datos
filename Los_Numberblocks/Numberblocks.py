import math
class Numberblock:
    _creados = {}   # Diccionario para guardar todas las instancias (clave: valor numérico)

    def __init__(self, valor, color, personalidades):
        if valor <= 0:
            raise ValueError("El valor debe ser un entero positivo.")
        if color not in ["violeta", "rojo", "naranja", "amarillo", "verde"]:
            raise ValueError("Color inválido para un Numberblock común.")
        self.valor = valor
        self.color = color
        if not isinstance(personalidades, list):
            raise TypeError("Las personalidades deben pasarse en una lista de strings.")
        self.personalidades = personalidades
        self.presentarse()
        #En este caso se utiliza el metodo crear para agregar el personaje al diccionario, sino se usaria "Numberblock._creados[valor] = self"

    @classmethod
    def crear(cls, valor, color, personalidades):
        """Valida si ya existe un personaje con ese valor. Si existe lo devuelve, sino lo crea."""
        if valor in cls._creados:
            return cls._creados[valor]
        nuevo = cls(valor, color, personalidades)
        cls._creados[valor] = nuevo
        return nuevo

    def presentarse(self):
        if self.es_cuadrado():
            print(f"Soy el número {self.valor}, soy {self.color}. Soy un cuadrado perfecto.")
        else:
            print(f"Soy el número {self.valor}, soy {self.color}.")

    def es_cuadrado(self):
        raiz = int(math.sqrt(self.valor))
        return raiz * raiz == self.valor

    def replicar(self):
        # Devuelve un nuevo Numberblock idéntico
        return Numberblock.crear(self.valor, self.color, self.personalidades[:])

    def __eq__(self, otro):
        return isinstance(otro, Numberblock) and \
               self.valor == otro.valor and \
               self.color == otro.color and \
               self.personalidades == otro.personalidades #la "\" sirve para avisar que el codigo sigue en la siguiente linea

    def combinar_con(self, otro):
        if not isinstance(otro, Numberblock):
            raise ValueError("Solo se pueden combinar Numberblocks.")
        nuevo_valor = self.valor + otro.valor
        if nuevo_valor in Numberblock._creados:
            return Numberblock._creados[nuevo_valor].replicar()
        nuevo_color = self.color
        nueva_personalidad = otro.personalidades[:]
        return Numberblock.crear(nuevo_valor, nuevo_color, nueva_personalidad)

    def personalidad(self):
        for p in self.personalidades:
            print(p)

    @classmethod
    def personajes(cls):
        for valor in sorted(cls._creados.keys()):
            nb = cls._creados[valor]
            print(f"{nb.valor} ({nb.color})")


class Rebelblock(Numberblock):

    @classmethod
    def crear(cls, valor, color, personalidades=None):
        """Valida y crea un Rebelblock único por valor."""
        if valor >= 0:
            raise ValueError("Un Rebelblock debe tener valor negativo.")
        if color in ["violeta", "rojo", "naranja", "amarillo", "verde"]:
            raise ValueError("Color inválido para un Rebelblock.")
        if valor in cls._creados:
            return cls._creados[valor]
        nuevo = cls(valor, color, personalidades)
        cls._creados[valor] = nuevo
        return nuevo

    def __init__(self, valor, color, personalidades=None):
        self.valor = valor
        self.color = color
        if personalidades is None:
            self.personalidades = []
        else:
            if not isinstance(personalidades, list):
                raise TypeError("Las personalidades deben pasarse en una lista de strings.")
            self.personalidades = personalidades
        self.presentarse()

    def presentarse(self):
        print(f"Soy {self.valor}, y me jacto de ser negativo.")

    def replicar(self):
        raise Exception("Los Rebelblocks no pueden replicarse.")

    def combinar_con(self, otro):
        raise Exception("Los Rebelblocks no pueden combinarse.")


# ==================== EJEMPLO DE USO ====================
try:
    nb3 = Numberblock.crear(3, "rojo", ["Curioso"])    #el crear chequea que el numberblock no exista y haya uno solo unico
    nb4 = Numberblock.crear(4, "naranja", ["Entusiasta"])
    nb5 = Numberblock.crear(5, "amarillo", ["Independiente", "Romántico"])

    print("\n--- Personalidad nb5 ---")
    nb5.personalidad()

    print("\n--- Replicación ---")
    nb3_rep = nb3.replicar()
    print(nb3_rep == nb3)   # True

    print("\n--- Combinación ---")
    nb7 = nb3.combinar_con(nb4)
    print(nb7.valor, nb7.color)

    print("\n--- Personajes creados ---")
    Numberblock.personajes()

    print("\n--- Rebelblocks ---")
    rb1 = Rebelblock.crear(-3, "negro", ["Rebelde"])
    rb2 = Rebelblock.crear(-3, "negro")  # misma instancia
    print(rb1 is rb2)  # True

except ValueError as e:
    print("Error de valor:", e)

except Exception as e:
    print("Ocurrió un error inesperado:", e)  # Error genérico