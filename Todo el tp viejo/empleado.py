from persona import *
from random import *

# Genera un codigo de 5 numeros que es el codgo del empleado y lo devuelve como "cod"
def generar_cod():
    cod = ""  # Variable para almacenar el código generado
    for i in range(5):  # Genera 5 dígitos para el código
        cod += str(randint(0, 9))  # Genera un dígito aleatorio entre 0 y 9 y lo agrega al código
    return cod  # Devuelve el código generado


# Defincion de la clase Empleado que hereda de la clase Persona 
class Empleado(Persona):
    set_codemps = set()  # Conjunto para almacenar los códigos de empleados generados

    try:
        def __init__(self, nombre, dni, sexo):
            super().__init__(nombre, dni, sexo)  # Llamada al constructor de la clase base Persona
            codemp = generar_cod()  # Genera un código de empleado

            # Verifica si el código generado ya existe en el conjunto de códigos de empleados
            while codemp in Empleado.set_codemps:
                codemp = generar_cod()  # Genera un nuevo código si el generado ya existe

            self.codemp = codemp  # Asigna el código de empleado generado al atributo de instancia codemp
            Empleado.set_codemps.add(codemp)  # Agrega el código generado al conjunto de códigos existentes

            # Imprime el código de empleado autogenerado para que el empleado lo guarde y lo use para ingresar al sistema
            print("Este es el código del empleado autogenerado, el empleado deberá guardarlo para ingresar al sistema: {}".format(self.codemp))

            contra = input("A continuación, el empleado debe ingresar su nueva contraseña (5 caracteres mínimo): ")
            
            # Verifica que la contraseña tenga al menos 5 caracteres
            while len(contra) < 5:
                contra = input("Contraseña inválida, vuelva a ingresarla (5 caracteres mínimo): ")

            self.contra = contra  # Asigna la contraseña ingresada al atributo de instancia contra
        
        def __str__(self):
    # Devuelve una cadena formateada con los datos del empleado
            return "Datos del empleado: Nombre: {}, DNI: {}, Sexo: {}. Código de empleado: {}".format(self.nombre, self.dni, self.sexo, self.codemp)

# Captura de excepciones para el caso de ValueError
    except ValueError as e:
        print("Error!", e)  # Imprime un mensaje de error si se produce una excepción de tipo ValueError

   


