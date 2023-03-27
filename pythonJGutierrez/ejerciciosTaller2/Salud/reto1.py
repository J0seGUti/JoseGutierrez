class Persona:
    def __init__(self, tipo_doc='', documento='', nombre='', apellido='', peso=0.0, estatura=0.0, edad=0, sexo=''):
        self.tipo_doc = tipo_doc
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.peso = peso
        self.estatura = estatura
        self.edad = edad
        self.sexo = sexo

    def pedir_datos(func):
        def wrapper(self, *args, **kwargs):
            self.tipo_doc = input("Ingrese Tipo de documento: ")
            self.documento = input("Ingrese Número de documento: ")
            self.nombre = input("Ingrese Nombre de la persona: ")
            self.apellido = input("Ingrese Apellido de la persona: ")
            self.peso = float(input("Ingrese Peso de la persona en kg: "))
            self.estatura = float(input("Ingrese Estatura de la persona en mts: "))
            self.edad = int(input("Ingrese la edad de la persona: "))
            self.sexo = input("Escoja el Sexo de la persona (M/F): ").upper()
            return func(self, *args, **kwargs)
        return wrapper

    @pedir_datos
    def mostrar_persona(self):
        print("Tipo de documento:", self.tipo_doc, "\n"
              "Número de documento:", self.documento, "\n"
              "Nombre:", self.nombre, "\n"
              "Apellido:", self.apellido, "\n"
              "Peso:", self.peso, "\n"
              "Estatura:", self.estatura, "\n"
              "Edad:", self.edad, "\n"
              "Sexo:", self.sexo, "\n")

    def calcular_imc(self):
        peso_actual = self.peso / (self.estatura ** 2)
        if peso_actual < 20:
            print("El peso de la persona está por debajo de lo ideal")
        elif peso_actual >= 20 and peso_actual <= 25:
            print("El peso de la persona es ideal")
        else:
            print("La persona tiene sobrepeso")

    def mayor_edad(self):
        if self.edad >= 18:
            print("La persona es mayor de edad")
        else:
            print("La persona es menor de edad")
