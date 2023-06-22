# Importa la clase Persona del módulo ClasePersona
from ClasePersona import Persona

# Definición de la clase Cliente que hereda de la clase Persona
class Cliente(Persona):
    """
        Constructor de la clase Cliente que hereda de la clase Persona.

        Parámetros:
        - self: referencia al objeto actual de la clase.
        - nombre: nombre del cliente.
        - dni: DNI del cliente.
        - sexo: sexo del cliente.
        - tel: número de teléfono del cliente.
        - num_tarjeta: número de tarjeta del cliente.

        Lanza:
        - ValueError: si el número de teléfono no cumple con el formato adecuado o si el número de tarjeta no cumple con el formato adecuado.

        Retorna:
        - None.
        """
    def __init__(self, nombre, dni, sexo, tel, num_tarjeta):
        if type(tel)!=str or len(tel)!=10:
            raise ValueError("El número de teléfono no cumple con el formato adecuado.")
        if type(num_tarjeta)!=str or len(num_tarjeta)!=16:
            raise ValueError("El número de tarjeta no cumple con el formato adecuado.")
        super().__init__(nombre, dni, sexo)
        self.tel=str(tel)
        self.num_tarjeta=int(num_tarjeta)
        self.deuda=0

    def __str__(self):
        """
    Método especial de representación de cadena para la clase Cliente.

    Parámetros:
    - self: referencia al objeto actual de la clase.

    Retorna:
    - str: representación en formato de cadena de los datos del cliente.
    """
        return "Datos del cliente:\nNombre: {}, DNI: {}, Sexo: {}, Numtel: {}, Numtarjeta: {}".format(self.nombre,self.dni,self.sexo,self.tel,self.num_tarjeta)
    

if __name__ == "__main__":
    # Crea una instancia de la clase Cliente con los valores de ejemplo
    Cliente("juan", 34233564, "M", "1234567890", "1234567890123456")
