class EvaluadorPalabras:
    def __init__(self, valores_letras):
        self.valores = valores_letras
        self.ultima_evaluacion = {}    # Guarda el resultado anterior (dentro de la misma corrida)

    def calcular_puntaje(self, palabra):
        puntaje = 0
        for letra in palabra.lower():
            puntaje += self.valores.get(letra, 1)# Si la letra existe en el diccionario usa su valor, si no vale 1
        return puntaje

    def obtener_palabra_maxima(self, lista_palabras):
        self.ultima_evaluacion = {}  # reinicia del registro anterior
        max_palabra = None
        max_puntaje = -1

        for palabra in lista_palabras:
            puntaje = self.calcular_puntaje(palabra)
            self.ultima_evaluacion[palabra] = puntaje

            if puntaje > max_puntaje:
                max_puntaje = puntaje
                max_palabra = palabra

        return max_palabra


# Crear evaluador con reglas de puntuación
valores_letras = {
    'a': 2,
    'n': 3,
    'f': 5,
    'z': 5
}

evaluador = EvaluadorPalabras(valores_letras)

# Evaluar lista de palabras
palabras = ["cono", "mazazo", "fanzine", "fhan", "marsupial"]
palabra_ganadora = evaluador.obtener_palabra_maxima(palabras)

print(f"Palabra ganadora: {palabra_ganadora}")
print(f"Puntaje: {evaluador.calcular_puntaje(palabra_ganadora)}")

# Obtener detalles de la última evaluación
print(f"Todas las puntuaciones: {evaluador.ultima_evaluacion}")
