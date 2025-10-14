class Vehiculo:
    def __init__(self, patente, marca, anio, posicion = 0):
        self.patente = patente
        self.marca = marca
        self.anio = anio
        self.posicion = posicion  #seria lo mismo que poner "self.posicion=0" y sacar el atributo posicion

    def __str__(self):
        return f"Vehiculo: #{self.patente}\nMarca: {self.marca}\nAño: {self.anio}"

    def __eq__(self, otro):
        return (self.patente == otro.patente and
                self.marca == otro.marca and
                self.anio == otro.anio)


class Vehiculo_terrestre(Vehiculo):
    patentes_registradas = set()

    def __init__(self, patente, marca, anio, ruedas):
        if patente in Vehiculo_terrestre.patentes_registradas:
            raise ValueError(f"La patente {patente} ya está registrada en un vehículo terrestre.")
        super().__init__(patente, marca, anio)
        self.ruedas = ruedas
        Vehiculo_terrestre.patentes_registradas.add(patente)


class Auto(Vehiculo_terrestre):
    def __init__(self, patente, marca, anio):
        super().__init__(patente, marca, anio, ruedas=4)
#Como ruedas es fijo, no se trae la variable ruedas de la clase padre, si no que se crea un nuevo atributo (que se llama 
#igual) para asignarle el valor fijo. Como no se trae esa variable, se podria no agregarla en la clase padre y el codigo
#seguiria funcionando pero se agrega para asegurar que todo vehiculo terrestre tenga ruedas.

    def trasladarse(self, desplazamiento):
        self.posicion += desplazamiento
        return f"El Auto {self.patente} avanzó {desplazamiento} km por tierra."


class Camion(Vehiculo_terrestre):
    def __init__(self, patente, marca, anio):
        super().__init__(patente, marca, anio, ruedas=None) #Otra forma de escribir lo de las ruedas(comparado al de Auto)
        self.ruedas = 8

    def trasladarse(self, desplazamiento):
        self.posicion += desplazamiento
        return f"El Camion {self.patente} avanzó {desplazamiento} km por tierra."


class Vehiculo_acuatico(Vehiculo):
    def __init__(self, patente, marca, anio):
        super().__init__(patente, marca, anio)


class Lancha(Vehiculo_acuatico):
    def __init__(self, patente, marca, anio, marca_motor):
        super().__init__(patente, marca, anio)
        self.marca_motor = marca_motor

    def trasladarse(self, desplazamiento):
        self.posicion += desplazamiento
        return f"La Lancha {self.patente} avanzó {desplazamiento} km por agua a motor."


class Velero(Vehiculo_acuatico):
    def __init__(self, patente, marca, anio, cantidad_velas):
        super().__init__(patente, marca, anio)
        self.cantidad_velas = cantidad_velas

    def trasladarse(self, desplazamiento):
        self.posicion += desplazamiento
        return f"El Velero {self.patente} avanzó {desplazamiento} km por agua a vela."


class Anfibio(Vehiculo_terrestre, Vehiculo_acuatico):
    def __init__(self, patente, marca, anio, marca_motor):
        Vehiculo_terrestre.__init__(self, patente, marca, anio, ruedas=4)
        self.marca_motor = marca_motor

    def trasladarse(self, desplazamiento):
        self.posicion += desplazamiento
        return f"El Anfibio {self.patente} avanzó {desplazamiento} km por tierra."

    def trasladarse_por_agua(self, desplazamiento):
        self.posicion += desplazamiento
        return f"El Anfibio {self.patente} avanzó {desplazamiento} km por agua a motor."

if __name__=='__main__':
    # Crear instancias
    auto1 = Auto("AA123BB", "Ford", 2020)
    camion1 = Camion("BB456CC", "Mercedes", 2018)
    lancha1 = Lancha("LC789", "Yamaha", 2021, "Yamaha Motor")
    velero1 = Velero("VL321", "Beneteau", 2019, 2)
    anfibio1 = Anfibio("AN111", "Gibbs", 2022, "Honda Motor")

    # Probar traslados
    print(auto1.trasladarse(10))
    print(camion1.trasladarse(20))
    print(lancha1.trasladarse(15))
    print(velero1.trasladarse(12))
    print(anfibio1.trasladarse(8))         # por tierra
    print(anfibio1.trasladarse_por_agua(5))  # por agua

    # Mostrar posiciones actuales
    print("\nPosiciones finales:")
    print(f"Auto: {auto1.posicion} km")
    print(f"Camión: {camion1.posicion} km")
    print(f"Lancha: {lancha1.posicion} km")
    print(f"Velero: {velero1.posicion} km")
    print(f"Anfibio: {anfibio1.posicion} km")
