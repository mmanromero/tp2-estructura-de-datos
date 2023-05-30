from bal2 import *
import pickle
import matplotlib.pyplot as plt

def recorrer_diccionario(diccionario):
    for key in diccionario.keys():
        print(diccionario[key])

try:
    with open("archivobalneario.pkl", "rb") as f:   #abro el pickle
        balneario=pickle.load(f)
except FileNotFoundError:
        balneario=Balneario("Carpas y sombrillas")
        balneario.cargar_empleado("Leandro Díaz", "21333333", "M")

us=input("Ingrese su código de empleado: ")
validar= balneario.validar_contraseña(us)

while validar==False:
    decision=input("Desea ingresar otro usuario? (presione Enter, o si no, cualquier otra tecla para salir): ")
    if decision =="":
        us=input("Ingrese su código de empleado: ")
        validar=balneario.validar_contraseña(us)
    else:
        validar=""
 
if validar==True:
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

        choice=input("""¿Qué desea hacer?
                1- Acciones con empleados
                2- Acciones con clientes
                3- Visualizar clientes
                4- Ver clientes adeudados
                5- Visualizar disponibilidad de carpas
                6- Visualizar disponibilidad de sombrillas
                7- Salir
                Opción: """)

        if choice=="7":
            break

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

                elif choice_empleado=="2":
                    dni_empleado=input("Ingrese el DNI del empleado a eliminar de los registros: ")
                    try:
                        print("El empleado eliminado es: ", balneario.eliminar_empleado(dni_empleado))
                    except ValueError as e:
                        print("Error!!", e)
                
                elif choice_empleado=="3":
                    recorrer_diccionario(balneario.dicemp)

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

                elif choice_empleado=="5":
                    break

                else:
                    print("La opción ingresada no es válida.")


        elif choice=="2":
            registrado=input("¿El cliente ya está registrado en el sistema?(s o n): ")
            
            #OPCIÓN DE: CLIENTE NO ESTÁ REGISTRADO --> LO REGISTRO
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

            #OPCIÓN DE: CLIENTE ESTÁ REGISTRADO --> LO VALIDO
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

                        if choice2=="1":
                            tipo_reserva=input("Qué va a reservar? (Sombrilla: s, Carpa: c): ")
                            if tipo_reserva.lower()=="s" or tipo_reserva.lower()=="c":
                                print("Actualmente, estas son las opciones (los números representan los días por los cuales permanecerá ocupada, los 0 representan disponibilidad): ")
                                balneario.ver_matriz(tipo_reserva)
                                #AGREGAR FILA Y COLUMNA
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
                                                #print(precio)
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
                        
                        elif choice2=="3":
                            try:
                                print("La deuda actual del cliente es de ${}".format(balneario.dicclientes[dni_trabajado].deuda))
                                monto_abonado=input("¿Cuánto abonará el cliente? ")
                                balneario.cobrar(dni_trabajado, monto_abonado)
                            except ValueError as e:
                                print("Error!", e)
                            except KeyError as e:
                                print("Error!", e)
                        
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


                        elif choice2=="5":
                            break

                        else:
                            print("La elección no era una opción.")
        
                        finalización=input("Desea hacer algo más con este cliente? (ENTER para continuar, cualquier tecla para salir): ")
                        if finalización!="":
                            break

        elif choice=="3":
            recorrer_diccionario(balneario.dicclientes)

        elif choice=="4":
            print("Los DNI de los clientes deudores son los siguientes: \n")
            for cliente in balneario.dicclientes.keys():
                if balneario.dicclientes[cliente].deuda!=0:
                    print(str(cliente)+". Deuda: "+"$"+ str(balneario.dicclientes[cliente].deuda))
                        
        elif choice=="5":
            balneario.ver_matriz("c")

        elif choice=="6":
            balneario.ver_matriz("s")


        decision=input("¿Desea continuar? (presione ENTER para continuar, y cualquier otra tecla para salir): ")
        if decision!="":
            break

balneario.revisar_matriz("c")
balneario.revisar_matriz("s")
balneario.cargar_archivos()
balneario.crear_backup_contraseñas()
print("Ha salido del programa.")



