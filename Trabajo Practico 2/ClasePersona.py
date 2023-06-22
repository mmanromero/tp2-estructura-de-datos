class Persona():
    set_dnis=set()

    def __init__(self, nombre, dni, sexo):
            """
        Constructor de la clase Persona.

        Parámetros:
        - self: referencia al objeto actual de la clase.
        - nombre: nombre de la persona.
        - dni: número de documento de la persona.
        - sexo: género de la persona.

        Lanza:
        - ValueError: si ocurre un error en el formato del DNI o del sexo, o si el DNI ya está registrado.

        Acciones:
        - Inicializa un objeto Persona con los atributos especificados.
        - Valida el formato del DNI y del sexo.
        - Verifica que el DNI no esté registrado previamente.
        """
            if type(dni)!=str or len(dni)!=8 or not dni.isdigit() or dni in Persona.set_dnis:
                raise ValueError("El DNI no cumple con el formato requerido o ya está registrado.")
            if sexo.upper() !="M" and sexo.upper()!="F":
                raise ValueError("El sexo no cumple con el formato requerido.")
            self.nombre=nombre.title()
            self.dni=int(dni)
            self.sexo=sexo.upper()

    #def __str__(self):
    #    return "{}. DNI: {}, SEXO: {}".format(self.nombre,self.dni,self.sexo)


if __name__ =="__main__":
    p=Persona("josefina geoghegan", 23454532,"M")
    print(p)