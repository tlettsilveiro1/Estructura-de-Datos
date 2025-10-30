# Ejercicio 6
class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.victorias = 0
        self.derrotas = 0
        self.goles_a_favor = 0
        self.goles_en_contra = 0

    def registrar_partido(self, goles_favor, goles_contra): #Se hace cada equipo por separado, en un partido se hace dos veces
        self.goles_a_favor += goles_favor
        self.goles_en_contra += goles_contra
        if goles_favor > goles_contra:
            self.victorias += 1
        elif goles_favor < goles_contra:
            self.derrotas += 1
        # Si es empate, no se suma a victorias ni derrotas


class Campeonato:
    def __init__(self):
        self.equipos = {}  # Diccionario: nombre -> objeto Equipo
        self.partidos = []  # Lista de tuplas: (equipoA, equipoB, golesA, golesB)

    def registrar_partido(self, nombreA, nombreB, golesA, golesB):
        # Si los equipos no existen, los creamos
        if nombreA not in self.equipos:
            self.equipos[nombreA] = Equipo(nombreA)
        if nombreB not in self.equipos:
            self.equipos[nombreB] = Equipo(nombreB)

        equipoA = self.equipos[nombreA]
        equipoB = self.equipos[nombreB]

        # Actualizamos estadísticas de cada equipo
        equipoA.registrar_partido(golesA, golesB)
        equipoB.registrar_partido(golesB, golesA)

        # Guardamos el partido en la lista como una tupla
        self.partidos.append((nombreA, nombreB, golesA, golesB))

    def equipo_con_mas_victorias(self):
        max_victorias = -1 #se pone (-1) para que se pueda usar (>) y no se cambie cuando el siguiente es igual
        equipo_max = None
        for equipo in self.equipos.values():
            if equipo.victorias > max_victorias:
                max_victorias = equipo.victorias
                equipo_max = equipo.nombre
        return equipo_max

    def diferencia_total_goles(self):
        resultado = {}
        for nombre, equipo in self.equipos.items():
            resultado[nombre] = equipo.goles_a_favor - equipo.goles_en_contra
        return resultado

    def partidos_empatados(self):
        empates = [] # Lista de tuplas (solo partidos empatados): (equipoA, equipoB, golesA, golesB)
        for partido in self.partidos:
            if partido[2] == partido[3]:  # golesA == golesB
                empates.append(partido)
        return empates

    def comparar_equipos(self, nombreA, nombreB):
        if nombreA not in self.equipos or nombreB not in self.equipos:
            return "Alguno de los equipos no existe."

        victoriasA = 0
        victoriasB = 0
        for partido in self.partidos:
            eqA, eqB, golesA, golesB = partido #asignacion multiple
            if (eqA == nombreA and eqB == nombreB):
                if golesA > golesB:
                    victoriasA += 1
                elif golesB > golesA:
                    victoriasB += 1
            elif (eqA == nombreB and eqB == nombreA): #chequear que el partido no este guardado alreves
                if golesB > golesA:
                    victoriasA += 1
                elif golesA > golesB:
                    victoriasB += 1

        if victoriasA > victoriasB:
            return f"{nombreA} ganó más veces en los encuentros directos ({victoriasA} a {victoriasB})"
        elif victoriasB > victoriasA:
            return f"{nombreB} ganó más veces en los encuentros directos ({victoriasB} a {victoriasA})"
        else:
            return f"Empate en los encuentros directos ({victoriasA} a {victoriasB})"


# ------------------ EJEMPLO DE USO ------------------
campeonato = Campeonato()
campeonato.registrar_partido("Equipo A", "Equipo B", 3, 2)
campeonato.registrar_partido("Equipo C", "Equipo D", 1, 1)
campeonato.registrar_partido("Equipo A", "Equipo C", 2, 2)
campeonato.registrar_partido("Equipo B", "Equipo D", 0, 1)

print("Equipo con más victorias:", campeonato.equipo_con_mas_victorias())
print("Diferencia total de goles por equipo:", campeonato.diferencia_total_goles())
print("Partidos empatados:", campeonato.partidos_empatados())
print(campeonato.comparar_equipos("Equipo A", "Equipo C"))