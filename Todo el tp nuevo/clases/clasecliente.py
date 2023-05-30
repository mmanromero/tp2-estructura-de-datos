from clasepersona import Persona
from clasebalneario import Balneario
from extras.funcionesextra import chequear_flotante

#asumo que los datos que me entran son STR de los inputs
class Cliente(Persona):
    def __init__(self, nombre, dni, sexo, tel, num_tarjeta):
        if type(tel)!=str or len(tel)!=10:
            raise ValueError("El número de teléfono no cumple con el formato adecuado.")
        if type(num_tarjeta)!=str or len(num_tarjeta)!=16:
            raise ValueError("El número de tarjeta no cumple con el formato adecuado.")
        super().__init__(nombre, dni, sexo)
        self.tel=int(tel)
        self.num_tarjeta=int(num_tarjeta)
        self.deuda=0

    def __str__(self):
        return "Datos del cliente:\nNombre: {}, DNI: {}, Sexo: {}, Numtel: {}, Numtarjeta: {}".format(self.nombre,self.dni,self.sexo,self.tel,self.num_tarjeta)

#CREAR OBJETO
#devuelve true si logra cargarlo (necesita que le mandes los datos antes), false si no puede registrarlo
    def registrar_cliente(nombre_pedido, dni_pedido, sexo_pedido, numtel, numtarjeta):
        try:
            if (dni_pedido.isdigit()):
                if int(dni_pedido) not in Balneario.dicclientes.keys():
                    cl=Cliente(nombre_pedido,dni_pedido,sexo_pedido,numtel, numtarjeta)
                    Balneario.dicclientes[int(dni_pedido)]=cl
                    return True
                else:
                     raise ValueError("Ese cliente ya se encuentra registrado.")
            else:
                 raise ValueError("El DNI ingresado no cumple con el formato requerido.")
        except ValueError as e:
            print("Error !", e, "El cliente no fue registrado.")
            return False

#MODIFICAR DATOS
#en el diccionario, vas a buscar el dni, una vez que lo encontrás, desde ese empleado que encontraste haces empleado.cambiardatos()
#le pasás el tipo de dato que querés cambiar (números asociados a las opciones en el menú) y el valor cargado
#corrobora la info que le llega, si lo cambia devuelve true y si no lo cambia False    
    def cambiardatos(self, tipo_dato, nuevo_dato):
        if tipo_dato=="1":
            self.nombre=nuevo_dato
            carga=True
        elif tipo_dato=="2":
            if nuevo_dato.lower().strip() not in ["f","m"]:
                carga=False
                raise ValueError("El sexo ingresado no es válido.")
            self.sexo=nuevo_dato
            carga=True
        elif tipo_dato=="3":
            if not(nuevo_dato.isdigit()) or len(nuevo_dato)!=10:
                carga=False
                raise ValueError("El número de teléfono ingresado no cumple con los requerimientos")
            self.tel=nuevo_dato
            carga=True
        elif tipo_dato=="4":
            if not(nuevo_dato.isdigit()) or len(nuevo_dato)!=16:
                carga=False
                raise ValueError("El número de tarjeta no cumple con el formato requerido.")
            self.num_tarjeta=nuevo_dato
            carga=True
        else:
            raise ValueError("La opción ingresada no es válida.")
        return carga

#PAGAR
    def saldar_deuda(self,monto_abonado):
        if self.deuda!=0:
            if chequear_flotante(monto_abonado):
                if float(monto_abonado)>0 and float(monto_abonado)<=self.deuda:
                    self.deuda-=float(monto_abonado)
                    print("Ahora, la deuda restante es de: {}$".format(self.deuda))
                else:
                    raise ValueError("El monto ingresado no es válido.")
            else:
                raise ValueError("El monto ingresado no cumple con el formato requerido.")
        else:
            raise ValueError("El cliente no tiene una deuda que saldar.")


#ELIMINAR OBJETO --> creemos que no es necesario eliminar a un cliente, sino que queden datos históricos por las dudas de quienes pasaron por el balneario
    def eliminar_cliente():
        pass
