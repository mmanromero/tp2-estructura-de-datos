class Persona():
    set_dnis = set()  # Conjunto para almacenar los DNIs registrados
    def __init__(self, nombre, dni, sexo):
        # Validación del formato del DNI y si ya está registrado
        if type(dni) != str or len(dni) != 8 or not dni.isdigit() or dni in Persona.set_dnis:
                raise ValueError("El DNI no cumple con el formato requerido o ya está registrado.")
            # Validación del formato del sexo
        if sexo.upper() !="M" and sexo.upper()!="F":
            raise ValueError("El sexo no cumple con el formato requerido.")
        self.nombre = nombre.title()  # Asignación del nombre (en mayúscula la primera letra de cada palabra)
        self.dni = int(dni)  # Conversión del DNI a entero
        self.sexo = sexo.upper()  # Asignación del sexo (en mayúsculas)
    #def __str__(self):
    #    return "{}. DNI: {}, SEXO: {}".format(self.nombre,self.dni,self.sexo)


if __name__ =="__main__":
    p=Persona("josefina geoghegan", 23454532,"M")
    print(p)