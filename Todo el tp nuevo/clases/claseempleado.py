from extras.funcionesextra import generar_cod
from clasepersona import Persona
from clasebalneario import Balneario

class Empleado(Persona):
    set_codemps=set()
    #este set solo sirve para que el codemp que se crea aleatoriamente no se repita de forma rápida y efectiva
    try:
        def __init__(self, nombre, dni, sexo):
                super().__init__(nombre, dni, sexo)
                codemp=generar_cod()
                while codemp in Empleado.set_codemps:
                    codemp=generar_cod()
                self.codemp=codemp
                Empleado.set_codemps.add(codemp)
                print("Este es el código del empleado autogenerado, el empleado deberá guardarlo para ingresar al sistema: {}".format(self.codemp))
                contra=input("A continuación, el empleado debe ingresar su nueva contraseña (5 caracteres mínimo): ")
                while len(contra)<5:
                    contra=input("Contraseña inválida, vuelva a ingresarla (5 caracteres mínimo): ")
                self.contra=contra
        
        def __str__(self):
            return "Datos del empleado: Nombre: {}, DNI: {}, Sexo: {}. Código de empleado: {}".format(self.nombre,self.dni,self.sexo,self.codemp)

    except ValueError as e:
        print("Error!", e)  

#Crear objeto -->pide los datos en el menú, y se corroboran dentro de la clase empleado, cuando se crea el emp
    def cargar_empleado(nom_cargado, dni_cargado, sexo_cargado):
        if int(dni_cargado) not in Balneario.dicemps.keys():  
            emp=Empleado(nom_cargado,dni_cargado,sexo_cargado)
            Balneario.dicemp[int(dni_cargado)]=emp
            Balneario.dicusuarios[emp.codemp]=emp.contra
        else:
            raise ValueError("Ese empleado ya fue cargado.")

#Modificar datos -->ponés en el menú empleado.cambiarcontraseña y hace el proceso (osea, tenés que buscarlo en el diccionario primero)
    def cambiar_contraseña(self):
        contraseña_antigua=input("Ingresar la contraseña anterior: ")
        if contraseña_antigua==self.contra:
            contraseña_nueva=input("Ingresar la nueva contraseña (5 caracteres mínimo): ")
            while len(contraseña_nueva)<5:
                contraseña_nueva=input("Contraseña inválida, vuelva a ingresarla (5 caracteres mínimo): ")
            print("La nueva contraseña es: ", contraseña_nueva)
            self.contra=contraseña_nueva
            Balneario.dicusuarios[self.codemp]=contraseña_nueva
        else:
            raise ValueError("La contraseña ingresada no coincide con la contraseña actual del empleado. No podrá modificarse.")

#ELIMINAR OBJETO
#otra forma, pero desde sí mismo, el empleado se autoelimina, tiene más sentido el de abajo?
    def eliminar_empleado(self):
        Persona.set_dnis.discard(self.dni)
        Empleado.set_codemps.discard(self.codemp)
        Balneario.dicemp.pop(self.dni)
        Balneario.dicusuarios.pop(self.codemp)
        return self

#la función en el menú principal va a pedir el dni, va a chequear si está registrado, y si está registrado, llama a esta función con el objeto empeleado del diccionario
#viene un objeto empleado desde afuera (ya corroborado que está en el diccionario de empleados)
    def eliminar_empleado(empleado):
        Persona.set_dnis.discard(empleado.dni)
        Empleado.set_codemps.discard(empleado.codemp)
        empleadoeliminado=Balneario.dicemp.pop(empleado.dni)
        Balneario.dicusuarios.pop(empleado.codemp)
        return empleadoeliminado
