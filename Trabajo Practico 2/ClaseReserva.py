import datetime
class Reserva():

    def __init__(self,num_reserva, dias_estadia, tipo_reserva,cliente):
        self.num_reserva=num_reserva
        self.precio=0
        self.fechacomienzo=datetime.datetime.now()
        self.tipo_reserva=tipo_reserva
        self.cliente=cliente
        self.estadia=int(dias_estadia)
        self.vencimiento=datetime.datetime.now()+datetime.timedelta(dias_estadia)
    #La clase Reserva tiene un método __init__ que inicializa los atributos num_reserva, 
    # precio, fechacomienzo, tipo_reserva, cliente, estadia y vencimiento. fechacomienzo 
    # se establece como la fecha y hora actuales utilizando datetime.datetime.now(). 
    # vencimiento se establece sumando dias_estadia a la fecha y hora actuales utilizando 
    # datetime.timedelta.
   
    def __str__(self):   # Método para representar el objeto Reserva como una cadena de texto
        return "Reserva: {}, días de estadía total: {}".format(self.numreserva,self.tiempo_estadia)
    
if __name__=="__main__":
    from datetime import timedelta
     # Calcula la diferencia de días entre la fecha "2025/04/08" y la fecha y hora actuales
    print((datetime.strptime("2025/04/08","%Y/%m/%d")-datetime.now()).days) 
    # Imprime la fecha y hora actuales más dos días
    print(datetime.now()+ datetime.timedelta(days=2))