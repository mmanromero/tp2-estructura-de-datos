from FuncionesAdicionales import generar_cod  # Importa la función generar_cod desde el módulo FuncionesAdicionales
from ClasePersona import *  # Importa la clase Persona desde el archivo ClasePersona.py
from random import *  # Importa todos los elementos del módulo random

class Empleado(Persona):  # Definición de la clase Empleado, que hereda de la clase Persona
    set_codemps = set()  # Atributo de clase: conjunto vacío para almacenar los códigos de empleados generados

    def __init__(self, nombre, dni, sexo, contra):  # Constructor de la clase Empleado
        super().__init__(nombre, dni, sexo)  # Llama al constructor de la clase base Persona
        codemp = generar_cod()  # Genera un código de empleado único llamando a la función generar_cod

        while codemp in Empleado.set_codemps:  # Verifica si el código generado ya existe en el conjunto set_codemps
            codemp = generar_cod()  # Si el código existe, genera uno nuevo hasta que sea único

        self.codemp = codemp  # Asigna el código de empleado generado al atributo de instancia codemp
        self.contra = contra  # Asigna el valor del parámetro contra al atributo de instancia contra

        Empleado.set_codemps.add(codemp)  # Agrega el código de empleado al conjunto set_codemps

    def __str__(self):  # Método especial __str__ para representar el objeto Empleado como una cadena
        return "Datos del empleado: Nombre: {}, DNI: {}, Sexo: {}. Código de empleado: {}".format(
            self.nombre, self.dni, self.sexo, self.codemp)  # Retorna una cadena formateada con los datos del empleado




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