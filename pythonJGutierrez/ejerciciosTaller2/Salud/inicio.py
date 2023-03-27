from reto1 import Persona

class Inicio:
    def __init__(self):
        self.persona = Persona()

    def ejecutar(self):
        self.persona.pedirDatos()
        self.persona.mostrarPersona()
        self.persona.calcularImc()
        self.persona.mayorEdad()

inicio = Inicio()
inicio.ejecutar()