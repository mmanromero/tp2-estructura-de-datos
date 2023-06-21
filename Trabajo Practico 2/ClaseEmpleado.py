from FuncionesAdicionales import generar_cod
from ClasePersona import *
from random import *

class Empleado(Persona):
    set_codemps=set()
    try:
        def __init__(self, nombre, dni, sexo, contra):
                super().__init__(nombre, dni, sexo)
                codemp=generar_cod()
                while codemp in Empleado.set_codemps:
                    codemp=generar_cod()
                self.codemp=codemp
                self.contra=contra
                Empleado.set_codemps.add(codemp)                
        def __str__(self):
            return "Datos del empleado: Nombre: {}, DNI: {}, Sexo: {}. Código de empleado: {}".format(self.nombre,self.dni,self.sexo,self.codemp)
    except ValueError as e:
        print("Error!", e)   



# class Empleado(Persona):
#     set_codemps=set()
#     try:
#         def __init__(self, nombre, dni, sexo):
#                 super().__init__(nombre, dni, sexo)
#                 codemp=generar_cod()
#                 while codemp in Empleado.set_codemps:
#                     codemp=generar_cod()
#                 self.codemp=codemp
#                 Empleado.set_codemps.add(codemp)
#                 print("Este es el código del empleado autogenerado, el empleado deberá guardarlo para ingresar al sistema: {}".format(self.codemp))
#                 contra=input("A continuación, el empleado debe ingresar su nueva contraseña (5 caracteres mínimo): ")
#                 while len(contra)<5:
#                     contra=input("Contraseña inválida, vuelva a ingresarla (5 caracteres mínimo): ")
#                 self.contra=contra
        
#         def __str__(self):
#             return "Datos del empleado: Nombre: {}, DNI: {}, Sexo: {}. Código de empleado: {}".format(self.nombre,self.dni,self.sexo,self.codemp)

#     except ValueError as e:
#         print("Error!", e)   