class Persona:
    def __init__(self):
        self.__tipoDoc = ""
        self.__documento = ""
        self.__nombre = ""
        self.__apellido = ""
        self.__peso = 0.0
        self.__estatura = 0.0
        self.__edad = 0
        self.__sexo = ""

    def get_tipoDoc(self):
        return self.__tipoDoc

    def set_tipoDoc(self, tipoDoc):
        self.__tipoDoc = tipoDoc
    
    def get_documento(self):
        return self.__documento

    def set_documento(self, documento):
        self.__documento = documento
        
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, apellido):
        self.__apellido = apellido
        
    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso
        
    def get_estatura(self):
        return self.__estatura

    def set_estatura(self, estatura):
        self.__estatura = estatura
        
    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad
        
    def get_sexo(self):
        return self.__sexo

    def set_sexo(self, sexo):
        self.__sexo = sexo  

    def pedirDatos(self):
        self.set_tipoDoc(input("Ingrese Tipo de documento: "))
        self.set_documento(input("Ingrese Número de documento: "))
        self.set_nombre(input("Ingrese Nombre de la persona: "))
        self.set_apellido(input("Ingrese Apellido de la persona: "))
        self.set_peso(float(input("Ingrese Peso de la persona en kg: ")))
        self.set_estatura(float(input("Ingrese Estatura de la persona en mts: ")))
        self.set_edad(int(input("Ingrese la edad de la persona: ")))
        self.set_sexo(input("Seleccione el Sexo de la persona (M/F): ").upper())

    def mostrarPersona(self):
        print("Tipo de documento:", self.get_tipoDoc(), "\n"
              "Número de documento:", self.get_documento(), "\n"
              "Nombre:", self.get_nombre(), "\n"
              "Apellido:", self.get_apellido(), "\n"
              "Peso:", self.get_peso(), "\n"
              "Estatura:", self.get_estatura(), "\n"
              "Edad:", self.get_edad(), "\n"
              "Sexo:", self.get_sexo(), "\n")
        
    def calcularImc(self):
        pesoActual = self.get_peso() / (self.get_estatura() ** 2)
        if pesoActual < 20:
            print("El peso de la persona está por debajo de lo ideal")
        elif pesoActual >= 20 and pesoActual <= 25:
            print("El peso de la persona es ideal")
        else:
            print("La persona tiene sobrepeso")

    def mayorEdad(self):
        if self.get_edad() >= 18:
            print("La persona es mayor de edad")
        else:
            print("La persona es menor de edad")