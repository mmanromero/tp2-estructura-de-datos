from FuncionesAdicionales import generar_cod  # Importa la función generar_cod desde el módulo FuncionesAdicionales
from ClasePersona import *  # Importa la clase Persona desde el archivo ClasePersona.py
from random import *  # Importa todos los elementos del módulo random

class Empleado(Persona):
    set_codemps=set()
    try:
        def __init__(self, nombre, dni, sexo, contra):
                """
        Constructor de la clase Empleado.

        Parámetros:
        - self: referencia al objeto actual de la clase.
        - nombre: nombre del empleado.
        - dni: número de documento del empleado.
        - sexo: género del empleado.
        - contra: contraseña del empleado.

        Lanza:
        - ValueError: si ocurre un error al generar el código de empleado.

        Acciones:
        - Inicializa un objeto Empleado con los atributos especificados.
        - Genera un código de empleado único.
        """
                super().__init__(nombre, dni, sexo)
                codemp=generar_cod()
                while codemp in Empleado.set_codemps:
                    codemp=generar_cod()
                self.codemp=codemp
                self.contra=contra
                Empleado.set_codemps.add(codemp)    


        def __str__(self):
            """
        Método especial de representación de cadena para la clase Empleado.

        Parámetros:
        - self: referencia al objeto actual de la clase.

        Retorna:
        - str: representación en formato de cadena de los datos del empleado.
        """
            return "Datos del empleado: Nombre: {}, DNI: {}, Sexo: {}. Código de empleado: {}".format(self.nombre,self.dni,self.sexo,self.codemp)
    except ValueError as e:
        print("Error!", e)   
