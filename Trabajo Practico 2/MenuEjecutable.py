import sys
import pickle
from ClaseBalneario import Balneario
from FuncionesAdicionales import chequear_flotante, recorrer_diccionario
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox


try:
    with open("archivobalneario.pkl", "rb") as f:   #abro el pickle
        balneario=pickle.load(f)
except FileNotFoundError:
        balneario=Balneario("Carpas y sombrillas")
        balneario.cargar_empleado("Leandro Díaz", "21333333", "M")

#Definimos la clase LoginWidget que hereda de QWidget y representa la interfaz de inicio de sesión:
class LoginWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Inicio de Sesión')
        self.setGeometry(300, 300, 300, 200)

        self.user_label = QLabel('Codemp:', self)
        self.user_label.move(20, 20)

        self.user_input = QLineEdit(self)
        self.user_input.move(80, 20)

        self.password_label = QLabel('Contraseña:', self)
        self.password_label.move(20, 60)

        self.password_input = QLineEdit(self)
        self.password_input.move(100, 60)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.submit_button = QPushButton('Iniciar Sesión', self)
        self.submit_button.move(100, 100)
        self.submit_button.clicked.connect(self.verify_credentials)

#Definimos el método verify_credentials que se ejecuta cuando se hace clic en el botón de inicio de sesión. 
#Este método verifica las credenciales ingresadas por el usuario:
    def verify_credentials(self):
        codemp = self.user_input.text()
        contraseña = self.password_input.text()

#validar contraseña la traemos desde balneario para poder ver que el empleado se encuentre registrado en el sistema
        if balneario.validar_contraseña(codemp, contraseña):
            self.close()
            self.usuario = codemp
            self.contraseña = contraseña
        else:
            self.user_input.setText('')
            self.password_input.setText('')
            QMessageBox.warning(self, 'Credenciales inválidas', 'Credenciales inválidas. Vuelve a intentarlo.')

#En la parte principal del programa, creamos una instancia de QApplication:
if __name__ == '__main__':
    app = QApplication(sys.argv)

#Dentro de un bucle while True, creamos una instancia de LoginWidget, 
#mostramos la interfaz de inicio de sesión y ejecutamos la aplicación:
    while True:
        login_widget = LoginWidget()
        login_widget.show()
        app.exec_()

        if hasattr(login_widget, 'usuario') and hasattr(login_widget, 'contraseña'):
            break
        else:
            respuesta = QMessageBox.question(None, 'Salir', '¿Deseas salir del programa?',
                                             QMessageBox.Yes | QMessageBox.No)
            if respuesta == QMessageBox.Yes:
                sys.exit()

    #Si quisiésemos usarlas, las variables del usuario y la contraseña ingresados se buscan de esa forma
    # print("Usuario:", login_widget.usuario)
    # print("Contraseña:", login_widget.contraseña)

#UNA VEZ QUE SE CIERRA LA INTERFAZ, COMIENZA A FUNCIONAR EL SISTEMA EN LA TERMINAL

#Una vez que se valida la contraseña, se ingresa al Sistema de Balneario y se pide la cotización de los productos para el día
    print("Bienvenido al sistema de reservas del Balneario")
    cotizacioncarpa=input("Antes de comenzar, ingrese la cotización de hoy para el precio por día de las carpas: ")
    while not(chequear_flotante(cotizacioncarpa)):
        cotizacioncarpa=input("Formato inválido, ingrése el valor nuevamente: ")
    cotizacionsombrilla=input("Ingrese la cotización de hoy para el precio por día de las sombrillas: ")
    while not(chequear_flotante(cotizacionsombrilla)):
        cotizacionsombrilla=input("Formato inválido, ingrése el valor nuevamente: ")
    cotizacionsombrilla=float(cotizacionsombrilla)
    cotizacioncarpa=float(cotizacioncarpa)

    comenzar=True
    while comenzar==True:

    #Brindamos opciones al empleado
        choice=input("""¿Qué desea hacer?
                    1- Acciones con empleados
                    2- Acciones con un cliente
                    3- Visualizar clientes registrados
                    4- Visualizar clientes adeudados
                    5- Visualizar disponibilidad de carpas
                    6- Visualizar disponibilidad de sombrillas
                    7- Visualizar reservas
                    8- Salir
                    Opción: """)
        if choice=="8":
            break

    #OPCION 1 --> ACCIONES CON EMPLEADOS 
        elif choice=="1":
                empezar_empleado=True
                while empezar_empleado==True:
                    choice_empleado=input("""¿Qué desea hacer?
                    1-Registrar un nuevo empleado
                    2-Eliminar un empleado
                    3-Visualizar empleados
                    4-Cambiar contraseña de empleado
                    5-Volver al menú principal
                    Opción: """)

        #Entramos dentro de las opciones de empleados
        #1)Registrar un empleado--> Pedimos la información en el menú y lo registramos con la función del Balneario
                    if choice_empleado=="1":
                        registrar_empleado=""
                        while registrar_empleado=="":
                            nombre=input("Ingrese el nombre del empleado: ")
                            dni_ingreso=input("Ingrese el DNI del empleado: ")
                            sex=input("Ingrese el sexo del empleado (M o F): ")
                            try:
                                registro=balneario.cargar_empleado(nombre,dni_ingreso,sex)
                                break
                            except ValueError as e:
                                print("Error!", e)
                                repetir=input("Desea volver a intentarlo? (ENTER para continuar, cualquier otra tecla para salir)")
                                if repetir!="":
                                    break

        #2)Eliminar un empleado --> pedimos su DNI y lo eliminamos con la función del propio sistema
                    elif choice_empleado=="2":
                        dni_empleado=input("Ingrese el DNI del empleado a eliminar de los registros: ")
                        try:
                            print("El empleado eliminado es: ", balneario.eliminar_empleado(dni_empleado))
                        except ValueError as e:
                            print("Error!!", e)
        
        #3)Visualizar empleados --> con la propia función del sistema lo recorremos e imprimimos uno por uno
                    elif choice_empleado=="3":
                        if len(balneario.dicemp)!=0:
                            recorrer_diccionario(balneario.dicemp)
                        else:
                            print("Actualmente, no hay empleados registrados en el sistema.")

        #4)Cambiar la contraseña del empleado cuyo DNI se ingrese. Primero se valida el DNI y luego se pide la contraseña y se cambia desde el sistema.
                    elif choice_empleado=="4":
                        pedirdenuevo=True
                        while pedirdenuevo==True:    
                            dni_cambio=input("Ingrese el DNI del empleado que desea cambiar su contraseña: ")
                            if dni_cambio.isdigit():
                                if int(dni_cambio) not in balneario.dicemp.keys():
                                    volver=input("El DNI no se encuentra registrado, desea ingresar otro? (ENTER para seguir, otra tecla para salir)")
                                    if volver!="":
                                        pedirdenuevo=False
                                else:
                                    break
                            else:
                                volver=input("El DNI ingresado no tiene el formato correcto, desea ingresar otro? (ENTER para seguir, otra tecla para salir)")
                                if volver!="":
                                    pedirdenuevo=False
                        if pedirdenuevo==True:
                            try:
                                balneario.cambiar_contraseña(dni_cambio)
                            except ValueError as e:
                                print("Error!!", e)

        #5) Salir de las acciones del empleado o (abajo) la opción no es válida
                    elif choice_empleado=="5":
                        break
                    else:
                        print("La opción ingresada no es válida.")

    #OPCIÓN 2--> ACCIONES CON CLIENTES
        #Una vez que entramos a trabajar con un cliente, queremos ver si está o no registrado  
        elif choice=="2":
                registrado=input("¿El cliente ya está registrado en el sistema?(s o n): ")
        
        #Opción n = "no registrado" --> pedimos la información e intentamos registrarlo con la función Balneario
                if registrado.lower().strip()=="n":
                    comenzar_cliente=True
                    while comenzar_cliente==True:
                        print("Registre al cliente:\n")
                        nom=input("Ingrese el nombre del cliente: ")
                        dni_cliente=input("Ingrese el DNI del cliente: ")
                        sexo_cliente=input("Ingrese el sexo del cliente (M o F): ")
                        numero_cliente=input("Ingrese el número de teléfono del cliente (10 dígitos): ")
                        tarjeta=input("Ingrese el número de tarjeta del cliente (16 dígitos): ")
                        continuar=balneario.registrar_cliente(nom,dni_cliente,sexo_cliente.strip(),numero_cliente,tarjeta) 
                        if continuar!=True:
                            seguir_cliente=input("Desea volver a intentarlo? (ENTER para continuar, cualquier tecla para salir)")
                        else:
                            print("El cliente fue registrado.")
                            dni_trabajado=int(dni_cliente)
                            break
                        if seguir_cliente!="":
                            break        

        #Opción s = "registrado" --> pedimos el DNI del cliente y confirmamos que esté o no registrado
                elif registrado.lower().strip()=="s":
                    continuar=False
                    while continuar==False:
                        dni_cliente=input("Ingrese el DNI del cliente: ")
                        if dni_cliente.isdigit():
                            continuar=balneario.validar_cliente(dni_cliente.strip())
                            decision_cliente=""
                            if continuar==False:
                                decision_cliente=input("El cliente no se encuentra registrado, desea volver a intentarlo? (ENTER para continuar, cualquier otra tecla para cancelar)")
                        else:
                            decision_cliente=input("El DNI ingresado no cumple con el formato requerido, quiere volver a intentarlo? (ENTER para continuar, cualquier otra tecla para cancelar)")
                            if decision_cliente!="":
                                continuar=False
                            break
                    if continuar==True:
                        dni_trabajado=int(dni_cliente)

                else:
                    continuar=False
                    print("La opción elegida no estaba entre las posibles.")

        #Una vez que registramos o encontramos al cliente, guardamos su DNI y ofrecemos opciones al empleado para trabajar con él:
                if continuar==True:
                        print(balneario.dicclientes[dni_trabajado])
                        comenzar2=True
                        while comenzar2==True:
                            choice2=input("""Qué quiere hacer con su cliente?
                            1-Asignar reserva
                            2-Modificar estadía
                            3-Cobrar
                            4-Modificar datos
                            5-Salir
                            Opción: """)

        #1) Hacer una reserva (a nombre del cliente con el que se trabaja) --> Se pide la info. y se hace la reserva (asignando lugar, ofreciendo la fila en la que se quiera ubicar, y calculando el precio)
                            if choice2=="1":
                                tipo_reserva=input("Qué va a reservar? (Sombrilla: s, Carpa: c): ")
                                if tipo_reserva.lower()=="s" or tipo_reserva.lower()=="c":
                                    print("Actualmente, estas son las opciones (los números representan los días por los cuales permanecerá ocupada, los 0 representan disponibilidad): ")
                                    balneario.ver_matriz(tipo_reserva)
                                    metodo_eleccion=input("Desea elegir una fila? O prefiere una asignación automática de lugar? (Fila: F, Automático: A): ")
                                    if metodo_eleccion.lower().strip()!="f" and metodo_eleccion.lower().strip()!="a":
                                        print("El método elegido no es válido.")
                                    else:
                                        if metodo_eleccion.lower()=="f":
                                            fila_requerida=input("Elija la fila que desea: ")
                                        else:
                                            fila_requerida=None
                                        dias=input("Ingrese la cantidad de días de hospedaje: ")
                                        if dias.isdigit():  #DIAS CHEQUEAR MAYOR A 0 CON INT
                                            if int(dias)>0:
                                                try:
                                                    precio_dia=lambda tipo_reserva:cotizacioncarpa if tipo_reserva.lower().strip()=="c" else cotizacionsombrilla
                                                    precio=precio_dia(tipo_reserva)
                                                    print(precio)
                                                    reserva_realizada=balneario.asignar_reserva(tipo_reserva,metodo_eleccion,int(dias), int(dni_trabajado),precio,fila_requerida)
                                                    balneario.ver_matriz(tipo_reserva)
                                                except ValueError as e:
                                                    print("Error!", e)
                                            else:
                                                print("Los días ingresados deben ser mayores a 0, deberá volver a comenzar la operación.")
                                        else:
                                            print("El formato de los días ingresados no es correcto, deberá volver a comenzar la operación.")
                                else:
                                    print("La opción ingresada no es válida.")

        #2)Agregar días a la estadía del cliente
                            elif choice2=="2":
                                try:
                                    d_extra=input("Ingrese días que se desea agregar a la estadía: ")
                                    if d_extra.isdigit():
                                        if int(d_extra)>0:
                                            try:
                                                if dni_trabajado in balneario.reservas_vigentes.keys():
                                                    tipo=balneario.reservas_vigentes[dni_trabajado].tipo_reserva
                                                    precio_dia=lambda tipo_reserva:cotizacioncarpa if tipo_reserva.lower().strip()=="c" else cotizacionsombrilla
                                                    precio=precio_dia(tipo)
                                                    balneario.modificar_estadia(d_extra,dni_trabajado, precio)
                                                else:
                                                    print("Ese cliente no tiene una reserva vigente a su nombre para modificar.")

                                            except ValueError as e:
                                                print("Error!!", e)
                                        else:
                                            raise ValueError("El número de días ingresado debe ser mayor a 0. La modificación no puede ser llevada a cabo.")
                                    else:
                                        raise ValueError("El número de días ingresado no cumple con el formato válido.La modificación no puede ser llevada a cabo.")
                                except ValueError as e:
                                    print("Error!", e)

        #3)Cobrar al cliente (se le resta de la deuda el monto que quiera abonar)                        
                            elif choice2=="3":
                                try:
                                    print("La deuda actual del cliente es de ${}".format(balneario.dicclientes[dni_trabajado].deuda))
                                    monto_abonado=input("¿Cuánto abonará el cliente? ")
                                    balneario.cobrar(dni_trabajado, monto_abonado)
                                except ValueError as e:
                                    print("Error!", e)
                                except KeyError as e:
                                    print("Error!", e)

        #4)Modificar datos del cliente --> puede modificar tantas características como desee                        
                            elif choice2=="4":
                                seguir=True
                                while seguir==True:
                                    modificacion=input("""Qué desea modificar?
                                    1-NOMBRE
                                    2-SEXO
                                    3-NÚMERO CELULAR
                                    4-NÚMERO DE TARJETA
                                    5-SALIR
                                    Opción: """)
                                    while modificacion not in ["1","2","3","4","5"]:
                                        modificacion=input("La opción ingresada no es válida, ingrese otra: ")
                                        if modificacion=="5":
                                            seguir=False
                                            break
                                    else:
                                        if modificacion!="5":
                                            seguir_modificando=""
                                            while seguir_modificando =="":
                                                nuevodato=input("Ingrese nuevo dato: ")
                                                try:
                                                    modificado=balneario.modificar_datos_cliente(dni_trabajado,nuevodato,modificacion)
                                                    break
                                                except ValueError as e:
                                                    print("Error!!",e)
                                                    decision=input("Desea volver a ingresar el dato? (presione ENTER, si no, cualquier tecla para salir)")
                                                    if decision!="":
                                                        seguir_modificando="no"
                                            continuar=input("Desea modificar otro dato? (ENTER para seguir, otra tecla para terminar)")
                                            if continuar!="":
                                                seguir=False
                                        else:
                                            seguir=False
                                            break

        #5)Opción de salir + elección inválida en el else + opción de seguir o no con este cliente
                            elif choice2=="5":
                                break
                            else:
                                print("La elección no era una opción.")
            
                            finalización=input("Desea hacer algo más con este cliente? (ENTER para continuar, cualquier tecla para salir): ")
                            if finalización!="":
                                break

    #OPCIÓN 3--> VISUALIZAR LA LISTA DE CLIENTES REGISTRADOS EN EL SISTEMA DEL BALNEARIO
        elif choice=="3":
                if len(balneario.dicclientes)!=0:
                    recorrer_diccionario(balneario.dicclientes)
                else:
                    print("No hay clientes registrados en el sistema actualmente.")

    #OPCIÓN 4--> VISUALIZAR LA LISTA DE LOS CLIENTES DEUDORES
        elif choice=="4":
                if len(balneario.dicclientes)!=0:
                    print("Los DNI de los clientes deudores son los siguientes: \n")
                    for cliente in balneario.dicclientes.keys():
                        if balneario.dicclientes[cliente].deuda!=0:
                            print(str(cliente)+". Deuda: "+"$"+ str(balneario.dicclientes[cliente].deuda))
                else:
                    print("No existen en este momento clientes registrados con deuda.")

    #OPCIONES 5 Y 6--> VISUALIZAR LAS MATRICES                        
        elif choice=="5":
                balneario.ver_matriz("c")
        elif choice=="6":
                balneario.ver_matriz("s")

    #OPCIÓN 7--> GRÁFICOS CON LAS RESERVAS
        elif choice=="7":
                continuar_reservas=""
                while continuar_reservas=="":
                    opciones=input("""Qué quiere visualizar?
                                1-Lista reservas
                                2-Grafico reservas
                                3-Volver al menu principal
                                Opción: """)
                    if opciones=="1":
                        balneario.ver_reserva()
                    elif opciones=="2":
                        balneario.ver_Grafico_Reservas()            
                    elif opciones=="3":
                        break
                    else:
                        print("La elección no era una opción.")
                    continuar_reservas=input("Desea hacer algo más con las reservas? (ENTER para continuar, cualquier tecla para salir): ")
                    # if continuar_reservas!="":
                    #     break


        decision=input("¿Desea continuar? (presione ENTER para continuar, y cualquier otra tecla para salir): ")
        if decision!="":
                break

    balneario.revisar_matriz("c")
    balneario.revisar_matriz("s")
    balneario.cargar_archivos()
    balneario.crear_backup_contraseñas()
    print("Ha salido del programa.")


