class Persona:
    def __init__(self, nombre, id, edad):
        self.nombre = nombre
        self.id = id
        self.edad = edad

    def __str__(self):
        return f"Persona(nombre={self.nombre}, id={self.id}, edad={self.edad})"
    
    # Necesario para que la persona pueda estar en un set
    def __eq__(self, other):
        if isinstance(other, Persona):
            return self.id == other.id  # Consideramos que el ID es único
        return False

    def __hash__(self):
        return hash(self.id)  # Usamos el ID para calcular el hash


def main():
    # Creamos un conjunto vacío de personas
    conjunto_personas = set()

    # Creamos 4 personas
    p1 = Persona("Ana", 1, 25)
    p2 = Persona("Luis", 2, 30)
    p3 = Persona("Marta", 3, 22)
    p4 = Persona("Jorge", 4, 28)

    # Añadimos las personas al conjunto
    conjunto_personas.add(p1)
    conjunto_personas.add(p2)
    conjunto_personas.add(p3)
    conjunto_personas.add(p4)

    # Visualizamos el conjunto completo
    for persona in conjunto_personas:
        print(persona)


# Ejecutamos main
main()