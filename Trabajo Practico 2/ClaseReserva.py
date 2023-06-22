import datetime
class Reserva():

    def __init__(self,num_reserva, dias_estadia, tipo_reserva,cliente):
        """
        Constructor de la clase Reserva.

        Parámetros:
        - self: referencia al objeto actual de la clase.
        - num_reserva: número de reserva.
        - dias_estadia: cantidad de días de estadía.
        - tipo_reserva: tipo de reserva.
        - cliente: cliente asociado a la reserva.

        Acciones:
        - Inicializa un objeto Reserva.
        - Establece los atributos num_reserva, precio, fechacomienzo, tipo_reserva, cliente, estadia y vencimiento.
        """
        self.num_reserva=num_reserva
        self.precio=0
        self.fechacomienzo=datetime.datetime.now()
        self.tipo_reserva=tipo_reserva
        self.cliente=cliente
        self.estadia=int(dias_estadia)
        self.vencimiento=datetime.datetime.now()+datetime.timedelta(dias_estadia)
    
    def __str__(self):
        """
        Método para representar el objeto Reserva como una cadena de texto.

        Parámetros:
        - self: referencia al objeto actual de la clase.

        Retorna:
        - Una cadena de texto que muestra el número de reserva y los días de estadía total.

        Acciones:
        - Retorna una representación legible de la reserva en forma de cadena de texto.
        """
        return "Reserva: {}, días de estadía total: {}".format(self.num_reserva,self.estadia)
    
if __name__=="__main__":
    from datetime import timedelta
     # Calcula la diferencia de días entre la fecha "2025/04/08" y la fecha y hora actuales
    print((datetime.strptime("2025/04/08","%Y/%m/%d")-datetime.now()).days) 
    # Imprime la fecha y hora actuales más dos días
    print(datetime.now()+ datetime.timedelta(days=2))