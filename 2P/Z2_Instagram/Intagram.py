from collections import deque

class Posteo:
    def __init__(self, autor, contenido):
        self.autor = autor
        self.contenido = contenido

    def __str__(self):
        return f"{self.autor} publicó: {self.contenido}"
    
    def __repr__(self):
        return self.__str__()

class Usuario:
    #Un atributo de clase es compartido entre todos los objetos, en cambio los atributos pertenecen
    #unicamente al objeto y no se comparte.
    usuarios_existentes = set()
    usuarios = dict()
    tipos_validos = ("personal", "business", "influencer")

    def __init__(self, nombre_usuario, tipo_cuenta):
        
        if tipo_cuenta not in Usuario.tipos_validos:
            raise ValueError(f"Tipo de cuenta inválido. Debe ser uno de: {Usuario.tipos_validos}")

        if nombre_usuario in Usuario.usuarios_existentes:
            raise ValueError(f"El nombre de usuario '{nombre_usuario}' ya existe.")

        self.nombre_usuario = nombre_usuario
        self.tipo_cuenta = tipo_cuenta
        self.amigos = set() # conjunto de nombres de usuario
        self.solicitudes_recibidas = deque() #se va a usar como una 'pila'
        self.posteos = []
        Usuario.usuarios_existentes.add(nombre_usuario)
        Usuario.usuarios[nombre_usuario]= self
        

    def recibir_solicitud(self, otro_usuario:str):
        if otro_usuario == self.nombre_usuario:
            print("No podés enviarte solicitud a vos mismo.")
            return
        if otro_usuario in self.amigos:
            print(f"Ya sos amigo de {otro_usuario}.")
            return
        if otro_usuario not in Usuario.usuarios_existentes:
            print(f"No existe el usuario {otro_usuario}.")
            return
        self.solicitudes_recibidas.append(otro_usuario)
        print(f"{self.nombre_usuario} recibió una solicitud de {otro_usuario}.")
    
    def getNombre(self):
        return self.nombre_usuario

    def aceptar_solicitud(self):
        if not self.solicitudes_recibidas:
            print(f"No hay solicitudes para aceptar.")
            return
        
        ultimo = self.solicitudes_recibidas.pop()  # última solicitud recibida
        ultimo_usuario = Usuario.buscar_usuario(ultimo)
        self.agregar_amigo(ultimo)
        ultimo_usuario.agregar_amigo(self.nombre_usuario)
        print(f"{self.nombre_usuario} aceptó la solicitud de {ultimo}.")
    
    def agregar_amigo(self, user):
        self.amigos.add(user)
        
    def eliminar_solicitud(self):
        if not self.solicitudes_recibidas:
            print(f"No hay solicitudes para eliminar.")
            return
        eliminado = self.solicitudes_recibidas.pop()
        print(f"{self.nombre_usuario} rechazó la solicitud de {eliminado}.")

    def mostrar_amigos(self):
        if not self.amigos:
            print(f"{self.nombre_usuario} no tiene amigos todavía.")
        else:
            print(f"Amigos de {self.nombre_usuario}:")
            for a in self.amigos:
                print(f" - {a}")

    def crear_posteo(self, contenido):
        post = Posteo(self.getNombre(), contenido)
        self.agregar_posteo(post)
        print(f"{self.nombre_usuario} creó un nuevo posteo.")
    
    def agregar_posteo(self,post):
        self.posteos.append(post)

    def ver_mis_posteos(self):
        if not self.posteos:
            print(f"{self.nombre_usuario} no tiene posteos todavía.")
        else:
            print(f"Posteos de {self.nombre_usuario}:")
            print(self.posteos)
    @classmethod #Sirve para definir un método que pertenece a la clase en sí
    def buscar_usuario(cls, nombre):
        return cls.usuarios[nombre]


# ============= Ejemplo de uso (según enunciado) =====================
if __name__ == "__main__":
    ana = Usuario("ana", "personal")
    juan = Usuario("juan", "business")

    juan.recibir_solicitud("ana")
    juan.aceptar_solicitud()

    ana.crear_posteo("Hermoso día para programar")
    ana.crear_posteo("Nuevo producto disponible!")

    ana.ver_mis_posteos()
    ana.mostrar_amigos()
    ana.recibir_solicitud("pedro")
    ana.aceptar_solicitud()