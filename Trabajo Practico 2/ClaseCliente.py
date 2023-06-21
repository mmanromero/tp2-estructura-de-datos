# Importa la clase Persona del módulo ClasePersona
from ClasePersona import Persona

# Definición de la clase Cliente que hereda de la clase Persona
class Cliente(Persona):
    def __init__(self, nombre, dni, sexo, tel, num_tarjeta): 
        if type(tel) != str or len(tel) != 10: # Verifica si el número de teléfono es una cadena de texto de 10 caracteres
            raise ValueError("El número de teléfono no cumple con el formato adecuado.")
        if type(num_tarjeta) != str or len(num_tarjeta) != 16:  # Verifica si el número de tarjeta es una cadena de texto de 16 caracteres
            raise ValueError("El número de tarjeta no cumple con el formato adecuado.")
        super().__init__(nombre, dni, sexo)  # Llama al constructor de la clase padre (Persona) para inicializar los atributos heredados 
        self.tel = str(tel) # Convierte el número de teléfono a una cadena de texto y lo asigna al atributo 'tel'    
        self.num_tarjeta = int(num_tarjeta)  # Convierte el número de tarjeta a un entero y lo asigna al atributo 'num_tarjeta'
        self.deuda = 0  # Inicializa el atributo 'deuda' en 0

    def __str__(self):
        return "Datos del cliente:\nNombre: {}, DNI: {}, Sexo: {}, Numtel: {}, Numtarjeta: {}".format(self.nombre, self.dni, self.sexo, self.tel, self.num_tarjeta)


if __name__ == "__main__":
    # Crea una instancia de la clase Cliente con los valores de ejemplo
    Cliente("juan", 34233564, "M", "1234567890", "1234567890123456")
