from reto1 import Persona

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.cargo = ""
        self.valorhora = 0.0
        self.horastrabajadas = 0
        self.departamento = ""

    def pedirDatos(self):
        super().pedirDatos()
        self.cargo = input("Cargo: ")
        self.valorhora = float(input("Valor por hora: "))
        self.horastrabajadas = int(input("Horas trabajadas: "))
        self.departamento = input("Departamento: ")
        print("\n")

    def calcularHonorarios(self):
        total = self.valorhora * self.horastrabajadas
        reteica = total * 0.00966
        honorarios = total - reteica
        return honorarios

    def imprimirEmpleado(self):
        print("Tipo de documento:", self.tipoDoc, "\n"
              "Número de documento:", self.documento, "\n"
              "Nombre:", self.nombre, "\n"
              "Apellido:", self.apellido, "\n"
              "Cargo:", self.cargo, "\n"
              "Horas trabajadas:", self.horastrabajadas, "\n"
              "Valor por hora:", self.valorhora, "\n"
              "Total a pagar:", self.calcularHonorarios(), "\n")
        
empleado = Empleado()
empleado.pedirDatos()
empleado.imprimirEmpleado()
