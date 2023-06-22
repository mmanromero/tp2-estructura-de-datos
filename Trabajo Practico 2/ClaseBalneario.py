from FuncionesAdicionales import chequear_flotante, crear_contraseña_empleado
from ClaseProducto import Sombrilla, Carpa
from ClaseReserva import Reserva
from ClaseEmpleado import Empleado
from ClasePersona import Persona
from ClaseCliente import Cliente
import matplotlib.pyplot as plt
import datetime
import pickle
import csv


#PARA ARRANCAR EL PROGRAMA Y PODER PROBARLO, ABRIR EL ARCHIVO USUARIOS CSV (AHÍ ESTÁN ANOTADAS LAS CONTRASEÑAS Y LOS CÓDIGOS DE EMPLEADOS)

class Balneario():
    def __init__(self, nombre):
        """
        Esta clase representa un balneario y su constructor inicializa sus atributos.

        Parámetros:
        - nombre: Nombre del balneario (cadena de caracteres).
        
        Atributos:
        - nombre: Nombre del balneario.
        - dicemp: Diccionario de empleados, donde las claves son los DNIs de los empleados y los valores son objetos de la clase Empleado.
        - dicclientes: Diccionario de clientes, donde las claves son los DNIs de los clientes y los valores son objetos de la clase Cliente.
        - dicusuarios: Diccionario de usuarios, donde las claves son los códigos de empleado y los valores son contraseñas de acceso.
        - reservas_vigentes: Diccionario de reservas vigentes, donde las claves son los números de reserva y los valores son objetos de la clase Reserva.
        - m_carpas: Matriz de carpas, donde se almacenan objetos de la clase Carpa.
        - m_sombrillas: Matriz de sombrillas, donde se almacenan objetos de la clase Sombrilla.
        """
        self.nombre = nombre
        self.dicemp = dict()
        self.dicclientes = dict()
        self.dicusuarios = dict()
        self.reservas_vigentes = dict()
        self.m_carpas = [[Carpa() for i in range(6)] for i in range(4)]
        self.m_sombrillas = [[Sombrilla() for i in range(5)] for i in range(3)]


#imprimo el nombre del Sistema de asignación de reservas
    def __str__(self) -> str:
        return "Bienvenido a {}".format(self.nombre)
    """
    Método que devuelve una cadena de texto representando al balneario.

    Retorna:
    - Cadena de texto que muestra un mensaje de bienvenida al balneario con su nombre.
    """
    

#busca info en un pickle, lo carga
    def leer_archivos(self,path):
        """
    Método para leer archivos utilizando la biblioteca pickle.

    Argumentos:
    - path: Ruta del archivo a leer.

    Retorna:
    - infobal: Datos del archivo leído.

    Excepciones:
    - FileNotFoundError: Se produce cuando el archivo no se encuentra en la ruta especificada.
    """
        try:
            with open(path, "rb") as f:
                infobal=pickle.load(f)
            return infobal
        except FileNotFoundError as e:
            print("Error! El archivo no se encontró.")



#hace persistir info del balneario en un pickle
    def cargar_archivos(self):
        """
    Método para guardar los datos del balneario en un archivo utilizando la biblioteca pickle.

    Excepciones:
    - FileNotFoundError: Se produce cuando no se encuentra el archivo.
    """
        try:
            with open("archivobalneario.pkl", "wb") as f:
                pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)
        except FileNotFoundError:
            print("Error! El arcvhivo no se encontró.")
    

#carga y crea al emp (corrobora que no esté registrado ya) #LEVANTA ERROR SI NO ESTÁ REGISTRADO
    def cargar_empleado(self, nom_cargado, dni_cargado, sexo_cargado):
        """
    Método para cargar un empleado en el balneario.

    Parámetros:
    - nom_cargado: str, nombre del empleado.
    - dni_cargado: str, DNI del empleado.
    - sexo_cargado: str, sexo del empleado.

    Excepciones:
    - ValueError: Se produce cuando el DNI del empleado ya está registrado en el balneario.

    Funcionalidad:
    - Si el DNI del empleado no está registrado, se generará una contraseña para el empleado y se creará un objeto Empleado con los datos proporcionados. El código de empleado autogenerado se imprimirá por pantalla. El empleado se agregará al diccionario de empleados y al diccionario de usuarios del balneario.
    - Si el DNI del empleado ya está registrado, se lanzará una excepción ValueError indicando que el empleado ya fue cargado.
        """
        if int(dni_cargado) not in self.dicemp.keys():    
            contraseña=crear_contraseña_empleado()
            emp=Empleado(nom_cargado, dni_cargado, sexo_cargado, contraseña)
            print("El empleado fue registrado. Su código de empleado autogenerado es: ", emp.codemp)
            self.dicemp[int(dni_cargado)]=emp
            self.dicusuarios[emp.codemp]=emp.contra
        else:
            raise ValueError("Ese empleado ya fue cargado.")

#crea y registra al cliente
    def registrar_cliente(self, nombre_pedido, dni_pedido, sexo_pedido, numtel, numtarjeta):
        """
    Método para registrar un cliente en el balneario.

    Parámetros:
    - nombre_pedido: str, nombre del cliente.
    - dni_pedido: str, DNI del cliente.
    - sexo_pedido: str, sexo del cliente.
    - numtel: str, número de teléfono del cliente.
    - numtarjeta: str, número de tarjeta del cliente.

    Retorna:
    - bool: True si el cliente fue registrado exitosamente, False en caso contrario.

    Excepciones:
    - ValueError: Se produce cuando el DNI ingresado no cumple con el formato requerido o cuando el cliente ya está registrado.

    Funcionalidad:
    - Se verifica que el DNI ingresado sea un valor numérico. Si es así, se verifica que el DNI no esté registrado previamente.
    - Si el DNI cumple con las condiciones, se crea un objeto Cliente con los datos proporcionados y se agrega al diccionario de clientes del balneario.
    - Si el DNI no cumple con el formato requerido, se lanza una excepción ValueError indicando el error.
    - Si el cliente ya está registrado, se lanza una excepción ValueError indicando que el cliente ya se encuentra registrado.
    - En caso de cualquier excepción, se imprime un mensaje de error y se retorna False.
    """
        try:
            if (dni_pedido.isdigit()):
                if int(dni_pedido) not in self.dicclientes.keys():
                    cl=Cliente(nombre_pedido,dni_pedido,sexo_pedido,numtel, numtarjeta)
                    self.dicclientes[int(dni_pedido)]=cl
                    return True
                else:
                    raise ValueError("Ese cliente ya se encuentra registrado.")
            else:
                raise ValueError("El DNI ingresado no cumple con el formato requerido.")
        except ValueError as e:
            print("Error !", e, "El cliente no fue registrado.")
            return False

#busca el dni del cliente    
    def validar_cliente(self, dni_cliente):
        """
    Método para validar si un cliente está registrado en el balneario.

    Parámetros:
    - dni_cliente: str, DNI del cliente a validar.

    Retorna:
    - bool: True si el cliente está registrado, False en caso contrario.

    Funcionalidad:
    - Se define una función lambda llamada buscar_dni que verifica si el DNI dado se encuentra en el diccionario de clientes del balneario.
    - Se llama a la función buscar_dni pasando el DNI convertido a entero.
    - Si el DNI está presente en el diccionario de clientes, la función buscar_dni retornará True, indicando que el cliente está registrado.
    - Si el DNI no está presente en el diccionario de clientes, la función buscar_dni retornará False, indicando que el cliente no está registrado.
    """
        buscar_dni=lambda dni:True if dni in self.dicclientes.keys() else False
        return buscar_dni(int(dni_cliente))

#pidey verifica la contraseña del emp
    def validar_contraseña(self, codemp_ingresado):
        """
    Método para validar la contraseña de un empleado registrado en el sistema.

    Parámetros:
    - codemp_ingresado: str, Código de empleado ingresado.

    Retorna:
    - bool: True si la contraseña es válida, False en caso contrario.

    Funcionalidad:
    - Verifica si el código de empleado ingresado se encuentra en el diccionario de usuarios del balneario.
    - Si el código de empleado está presente, solicita al usuario ingresar la contraseña.
    - Entra en un bucle hasta que la contraseña ingresada coincida con la contraseña asociada al código de empleado o se ingrese "0" para salir.
    - Si se ingresa "0", retorna False indicando que la validación ha fallado.
    - Si la contraseña coincide, retorna True indicando que la validación ha sido exitosa.
    - Si el código de empleado no está presente en el diccionario de usuarios, muestra un mensaje de error y retorna False.
    """
        if codemp_ingresado in self.dicusuarios.keys():
            contra=input("Ingrese su contraseña: ")
            while self.dicusuarios[codemp_ingresado]!=contra and contra!="0":
                contra=input("Contraseña incorrecta.Vuelva a intentar (o presione 0 para salir): ")
            if contra=="0":
                return False
            else:
                return True
        else:
            print("Ese empleado no está registrado en el sistema.")
            return False

#carga un archivo csv de contraseñas para poder leerlo nosotros y tenerlo de backup
    def crear_backup_contraseñas(self):
        """
    Método para crear un archivo de respaldo de contraseñas de empleados.

    Funcionalidad:
    - Intenta abrir un archivo llamado 'usuarios.csv' en modo escritura.
    - Define los nombres de los campos del archivo CSV como 'usuario' y 'contraseña'.
    - Crea un escritor de CSV utilizando el diccionario de empleados y sus contraseñas.
    - Escribe la fila de encabezado en el archivo CSV.
    - Recorre cada empleado en el diccionario de empleados y escribe una fila en el archivo CSV con el código de empleado y la contraseña.
    - Si ocurre un error al abrir el archivo, muestra un mensaje de error.
    """
        try:
            with open('usuarios.csv', 'w', newline='') as csvfile:
                fieldnames = ['usuario', 'contraseña']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for empleado in self.dicemp.keys():
                    writer.writerow({'usuario': self.dicemp[empleado].codemp, 'contraseña': self.dicemp[empleado].contra})
        except FileNotFoundError:
            print("Error! No se pudo abrir el archivo.")

#acción repetitiva --> busca matriz
    def matrizdetrabajo(self,tipo_reserva):
        """
    Método para obtener la matriz de trabajo según el tipo de reserva.

    Parámetros:
    - tipo_reserva: Tipo de reserva ("S" para sombrilla, "C" para carpa).

    Funcionalidad:
    - Verifica si el tipo de reserva es válido (solo se permite "S" o "C").
    - Define una función lambda que retorna la matriz de carpas si el tipo de reserva es "C" y la matriz de sombrillas si es "S".
    - Retorna la matriz de trabajo correspondiente al tipo de reserva.

    Excepciones:
    - Si el tipo de reserva no es válido, se lanza un ValueError.

    Retorna:
    - La matriz de trabajo según el tipo de reserva.
        """
        if tipo_reserva.lower()=="s" or tipo_reserva.lower()=="c":
            matriz_correcta=lambda x: self.m_carpas if x=="C" else self.m_sombrillas
            return matriz_correcta(tipo_reserva.upper().strip())
        else:
            raise ValueError("Tipo de reserva inválido.")
 
#visualiza la matriz (0 y días restantes)
    def ver_matriz(self, tipo_reserva):
        """
    Método para visualizar la matriz de disponibilidad de carpas o sombrillas.

    Parámetros:
    - tipo_reserva: Tipo de reserva ("S" para sombrilla, "C" para carpa).

    Funcionalidad:
    - Obtiene la matriz correspondiente al tipo de reserva especificado.
    - Recorre la matriz y muestra el estado de cada elemento.
    - Los elementos sin reserva se representan con "D" (disponible).
    - Los elementos con reserva se representan con el número de días restantes hasta su vencimiento.

    Excepciones:
    - Si el tipo de reserva no es válido, se lanza un ValueError.
    """
        print("Al visualizar las matrices, la D representa disponibilidad y el número, los días que restan de ocupación.")
        matriz=self.matrizdetrabajo(tipo_reserva)
        for fila in range(len(matriz)):
            lista=[]
            for columna in range(len(matriz[fila])):
                reser=matriz[fila][columna]
                if reser.estado==None:
                    lista.append("D")
                else:
                    lista.append((reser.estado.vencimiento-datetime.datetime.now()).days)
            print(lista)

#busca lugar en la matriz disponible (asignacion automática o por fila)
    def buscar_posicion_disponible(self, matriz, metodo_busqueda, num_fila=None):
            """
    Método para buscar una posición disponible en la matriz.

    Parámetros:
    - matriz: Matriz de objetos.
    - metodo_busqueda: Método de búsqueda ("F" para búsqueda por fila, "A" para búsqueda aleatoria).
    - num_fila: Número de fila (opcional, solo para búsqueda por fila).

    Retorno:
    - Tupla con la posición (fila, columna) de la reserva disponible, o None si no se encuentra ninguna.

    Excepciones:
    - Si el método de búsqueda no es válido, se lanza un ValueError.
    - Si el número de fila no es válido, se lanza un ValueError.
    """
            disponible=None
            if metodo_busqueda.lower()=="f":
                if num_fila!=None and str(num_fila).isdigit():
                    if int(num_fila)>0 and int(num_fila)<=len(matriz):
                        fila=int(num_fila)-1
                        for columna in range(len(matriz[fila])):
                            if matriz[fila][columna].estado==None:
                                return fila,columna
                    else:
                        raise ValueError("La fila pedida no es ubicable en la matriz.")
                else:
                    raise ValueError("No se recibió número de fila o no se recibió en el formato correcto.")
            
            elif metodo_busqueda.lower()=="a":
                for fila in range(len(matriz)):
                    for columna in range(len(matriz[fila])):
                        carpasomb=matriz[fila][columna] 
                        if carpasomb.estado==None:
                            return fila,columna
            else:
                raise ValueError("El método de búsqueda ingresado no es válido.")
            return disponible


#este precio despues se lo pasamos a la reserva que creemos
    def calcular_precio(self,reserva, precioxdia):
        """
    Método para calcular el precio de una reserva.

    Parámetros:
    - reserva: Objeto de la clase Reserva.
    - precioxdia: Precio por día en formato de cadena.

    Retorno:
    - Precio total de la reserva.

    Excepciones:
    - Si el precio ingresado no cumple con el formato requerido, se lanza un ValueError.
    """
        if chequear_flotante(precioxdia):
            precio=reserva.estadia*float(precioxdia)
            return precio
        else:
            raise ValueError("El precio ingresado no cumple con el formato requerido.")

#le pasás el precio, el dni, el número de días, la fila que eligió(si eligió), y hace la reserva     
    def asignar_reserva(self,tipo_reserva,metodo, dias, dni_cliente,cotizacion_dia,fila_elegida=None):
        """
    Método para asignar una reserva.

    Parámetros:
    - tipo_reserva: Tipo de reserva (sombrella: "S" o carpa: "C").
    - metodo: Método de búsqueda de posición disponible (fila: "F" o aleatorio: "A").
    - dias: Número de días de estadía.
    - dni_cliente: DNI del cliente como una cadena.
    - cotizacion_dia: Cotización por día en formato de cadena.
    - fila_elegida: Número de fila elegida (opcional) como una cadena.

    Retorno:
    - Objeto de la clase Reserva.

    Excepciones:
    - Si el DNI ingresado no es válido (no numérico), se lanza un ValueError.
    - Si el cliente ya tiene una reserva a su nombre, se lanza un ValueError.
    """
        if str(dni_cliente).isdigit():  #verifico que el dni sea numerico
            if dni_cliente not in self.reservas_vigentes.keys(): #veo si el cliente tiene una reserva a su nombre
                matriz=self.matrizdetrabajo(tipo_reserva)
                fila,columna=self.buscar_posicion_disponible(matriz,metodo,fila_elegida)
                num_reserva=str(fila)+str(columna)+str(dni_cliente)
                reser=Reserva(num_reserva,dias,tipo_reserva,self.dicclientes[int(dni_cliente)])
                print("El número de reserva asignado es: ", num_reserva)
                try:
                    preciototal=self.calcular_precio(reser,cotizacion_dia)
                except ValueError as e:
                    print("Error!", e)
                print("El precio de su estadía es: $", preciototal)
                matriz[fila][columna].estado=reser
                reser.precio=preciototal
                self.dicclientes[dni_cliente].deuda=preciototal
                print("Fecha de finalización de la reserva (puede modificarse): ", reser.vencimiento)   
                self.reservas_vigentes[reser.cliente.dni]=reser
                return reser
            else:
                raise ValueError("El cliente ya tiene una reserva a su nombre, puede extender su vencimiento con un recargo o reservar nuevamente al finalizar su estadía.")
        else:
            raise ValueError("El DNI ingresado no es válido.")

#viene el cliente y pide modificar su tiempo de estadia
    def modificar_estadia(self,dias_agregados, dni_cliente, precio_actual):
        """
    Método para modificar la estadía de una reserva.

    Parámetros:
    - dias_agregados: Número de días a agregar a la estadía.
    - dni_cliente: DNI del cliente como una cadena.
    - precio_actual: Precio actual por día en formato de cadena.

    Excepciones:
    - Si el cliente no tiene una reserva vigente a su nombre para modificar, se lanza un ValueError.
    """
        if dni_cliente in self.reservas_vigentes.keys():
            reserva_modificada=self.reservas_vigentes[dni_cliente]
            reserva_modificada.estadia+=int(dias_agregados)
            reserva_modificada.vencimiento+=datetime.timedelta(days=int(dias_agregados))
            print("El nuevo vencimiento de su estadía es: {}".format(reserva_modificada.vencimiento))
            precioextra=float(precio_actual)*float(dias_agregados)
            reserva_modificada.precio+=precioextra
            self.dicclientes[dni_cliente].deuda+=precioextra
            print("Los días agregados se cobrarán al precio actual por día, el precio agregado es {}$, y la deuda actual del cliente es de {}$".format(precioextra, self.dicclientes[dni_cliente].deuda))
        else:
            raise ValueError("Ese cliente no tiene una reserva vigente a su nombre para modificar.")

#con esta función, antes de cerrar el programa revisamos las matrices para ver si están vencidas, si hay algo vencido lo sacamos y ponemos None
    def revisar_matriz(self,tipo):
       """
    Método para revisar la matriz de trabajo y eliminar las reservas vencidas.

    Parámetros:
    - tipo: Tipo de reserva ("S" para sombrillas, "C" para carpas).

    Comentarios:
    - Si una reserva está vencida, se eliminará de la matriz y se removerá de las reservas vigentes.

    """
       matriz=self.matrizdetrabajo(tipo)
       for fila in range(len(matriz)):
           for columna in range(len(matriz[fila])):
               carpasomb=matriz[fila][columna] 
               if carpasomb.estado!=None:
                    if carpasomb.estado.vencimiento==datetime.datetime.now(): #ya está vencida
                        dnicliente=carpasomb.estado.cliente.dni
                        carpasomb.estado==None
                        self.reservas_vigentes.pop(dnicliente)

#le saca toda o parte de la deuda al cliente
    def cobrar(self, dni_cliente, monto_abonado):
        """
    Método para registrar el cobro de una deuda por parte de un cliente.

    Parámetros:
    - dni_cliente: DNI del cliente.
    - monto_abonado: Monto abonado por el cliente.

    Comentarios:
    - Si el monto abonado es válido y mayor a cero, se registra el pago y se actualiza la deuda del cliente.
    - Si el monto abonado supera la deuda actual del cliente, se genera un ValueError.
    - Si el cliente no tiene deuda pendiente, se genera un ValueError.
    - Si el cliente no está registrado, se genera un KeyError.

    """
        if int(dni_cliente) in self.dicclientes.keys():
            if self.dicclientes[int((dni_cliente))].deuda!=0:
                if chequear_flotante(monto_abonado):
                    if float(monto_abonado)>0 and float(monto_abonado)<=self.dicclientes[int(dni_cliente)].deuda:
                        self.dicclientes[int(dni_cliente)].deuda-=float(monto_abonado)
                        print("Ahora, la deuda restante es de: {}$".format(self.dicclientes[int(dni_cliente)].deuda))
                    else:
                        raise ValueError("El monto ingresado no es válido.")
                else:
                    raise ValueError("El monto ingresado no cumple con el formato requerido.")
            else:
                raise ValueError("El cliente no tiene una deuda que saldar.")
        else:
            raise KeyError("El cliente no se encuentra registrado.")            

#elimina al empleado que se pida desde el menú (el DNI que llega es un string)
    def eliminar_empleado(self,dni_recibido):
        """
    Método para eliminar un empleado del sistema.

    Parámetros:
    - dni_recibido: DNI del empleado a eliminar.

    Comentarios:
    - Si el DNI recibido es válido y se encuentra registrado, se elimina el empleado y se devuelve el objeto del empleado eliminado.
    - Si el DNI recibido no corresponde a un empleado registrado, se genera un ValueError.
    - Si el DNI recibido no cumple con el formato requerido, se genera un ValueError.

    """
        if dni_recibido.isdigit():
            if int(dni_recibido) in self.dicemp.keys():
                emp_eliminado=self.dicemp.pop(int(dni_recibido))
                return emp_eliminado
            else:
                raise ValueError("El DNI ingresado no se encuentra registrado.")
        else:
            raise ValueError("El DNI ingresado no cumple con el formato requerido.")

#le pasás el tipo de dato que querés cambiar (números asociados a las opciones en el menú) y el valor cargado
#corrobora la info que le llega, si lo cambia devuelve true y si no lo cambia False
    def modificar_datos_cliente(self,dni_cliente,nuevo_dato,tipo_dato):
        """
    Método para modificar los datos de un cliente.

    Parámetros:
    - dni_cliente: DNI del cliente cuyos datos se van a modificar.
    - nuevo_dato: Nuevo valor para el dato a modificar.
    - tipo_dato: Tipo de dato a modificar (1: nombre, 2: sexo, 3: número de teléfono, 4: número de tarjeta).

    Comentarios:
    - Si el DNI del cliente está registrado en el sistema, se modifica el dato correspondiente según el tipo de dato especificado.
    - Si el tipo de dato ingresado no es válido, se genera un ValueError.
    - Si el cliente no se encuentra registrado, se genera un ValueError.
    - Si el nuevo dato ingresado no cumple con los requerimientos, se genera un ValueError específico según el tipo de dato.

    Retorna:
    - True si la modificación se realizó correctamente.
    - False si no se realizó la modificación debido a un ValueError.
        """
        if int(dni_cliente) in self.dicclientes.keys():
            if tipo_dato=="1":
                self.dicclientes[int(dni_cliente)].nombre=nuevo_dato
                carga=True
            elif tipo_dato=="2":
                if nuevo_dato.lower().strip() not in ["f","m"]:
                    carga=False
                    raise ValueError("El sexo ingresado no es válido.")
                self.dicclientes[int(dni_cliente)].sexo=nuevo_dato
                carga=True
            elif tipo_dato=="3":
                if not(nuevo_dato.isdigit()) or len(nuevo_dato)!=10:
                    carga=False
                    raise ValueError("El número de teléfono ingresado no cumple con los requerimientos")
                self.dicclientes[int(dni_cliente)].tel=nuevo_dato
                carga=True
            elif tipo_dato=="4":
                if not(nuevo_dato.isdigit()) or len(nuevo_dato)!=16:
                    carga=False
                    raise ValueError("El número de tarjeta no cumple con el formato requerido.")
                self.dicclientes[int(dni_cliente)].num_tarjeta=nuevo_dato
                carga=True
            else:
                raise ValueError("La opción ingresada no es válida.")
            return carga
        else:
            raise ValueError("Ese cliente no se encuentra registrado.")

#para cambiar la contraseña del empleado
    def cambiar_contraseña(self, dni_empleado):
        """
    Método para cambiar la contraseña de un empleado.

    Parámetros:
    - dni_empleado: DNI del empleado cuya contraseña se va a cambiar.

    Comentarios:
    - Si el DNI del empleado no está registrado en el sistema, se genera un ValueError.
    - Se solicita al usuario ingresar la contraseña anterior para verificar su validez.
    - Si la contraseña anterior coincide con la contraseña actual del empleado, se solicita al usuario ingresar la nueva contraseña.
    - La nueva contraseña debe tener al menos 5 caracteres.
    - Se actualiza la contraseña del empleado y del usuario correspondiente en el diccionario dicemp y dicusuarios, respectivamente.
    - Si la contraseña anterior ingresada no coincide con la contraseña actual del empleado, se genera un ValueError.

    """
        if int(dni_empleado) not in self.dicemp.keys():
            raise ValueError("El empleado no se encuentra registrado.")
        else:
            contraseña_antigua=input("Ingresar la contraseña anterior: ")
            if self.dicemp[int(dni_empleado)].contra==contraseña_antigua:
                #contraseña_nueva=crear()
                contraseña_nueva=input("Ingresar la nueva contraseña (5 caracteres mínimo): ")
                while len(contraseña_nueva)<5:
                    contraseña_nueva=input("Contraseña inválida, vuelva a ingresarla (5 caracteres mínimo): ")
                print("La nueva contraseña es: ", contraseña_nueva)
                self.dicemp[int(dni_empleado)].contra=contraseña_nueva
                self.dicusuarios[self.dicemp[int(dni_empleado)].codemp]=contraseña_nueva
            else:
                raise ValueError("La contraseña ingresada no coincide con la contraseña actual del empleado. No podrá modificarse.")


    
#función para poder visualizar las reservas vigentes       
    def ver_reserva(balneario):
            """
    Método para ver las reservas vigentes en el balneario.

    Parámetros:
    - balneario: Objeto balneario que contiene las reservas vigentes.

    Comentarios:
    - Se recorren las claves del diccionario de reservas vigentes.
    - Para cada reserva, se verifica el tipo de reserva y se imprime en pantalla el tipo de reserva y los detalles de la misma.

    """
            for reserva in balneario.reservas_vigentes.keys():
                if balneario.reservas_vigentes[reserva].tipo_reserva == "c":
                    print("Reserva carpa: ",balneario.reservas_vigentes[reserva])
                else:
                    print("Reserva sombrilla: ",balneario.reservas_vigentes[reserva])

#
    def ver_Grafico_Reservas(balneario):
            """
    Método para visualizar un gráfico de las reservas vigentes en el balneario.

    Parámetros:
    - balneario: Objeto balneario que contiene las reservas vigentes.

    Comentarios:
    - Se crean listas para almacenar la cantidad de días y los códigos de reserva de las reservas de carpa y sombrilla.
    - Se recorren las claves del diccionario de reservas vigentes.
    - Para cada reserva, se obtienen los días de estadía y el código de reserva.
    - Se agregan los datos a las listas correspondientes según el tipo de reserva.
    - Se grafican las barras utilizando las listas de datos.
    - Se muestra el gráfico.
    - Se devuelven las listas de datos.

    """
            lista_cd = []  # Lista de cantidad de días de reservas de carpa
            lista_sd = []  # Lista de cantidad de días de reservas de sombrilla
            lista_c = []  # Lista de códigos de reserva de carpa
            lista_s = []  # Lista de códigos de reserva de sombrilla
            for reserva in balneario.reservas_vigentes.keys():
                res=balneario.reservas_vigentes[reserva]
                if balneario.reservas_vigentes[reserva].tipo_reserva == "c":
                    lista_cd+=[balneario.reservas_vigentes[reserva].estadia]
                    lista_c+=[balneario.reservas_vigentes[reserva].num_reserva]
                else:
                    lista_sd+=[balneario.reservas_vigentes[reserva].estadia]
                    lista_s+=[balneario.reservas_vigentes[reserva].num_reserva]         
            # print("Reserva carpa: ", lista_c, lista_cd)
            # print("Reserva sombrilla: ", lista_s, lista_sd)
            plt.title("Catidad de dias asociados a cada reserva (verde=carpas / naranja=sombrillas)")
            plt.xlabel("Codigo de reserva")
            plt.ylabel("Cantidad de dias")
            plt.bar(lista_c, lista_cd, color="green")
            plt.bar(lista_s, lista_sd, color="orange")
            plt.show()
            return lista_cd, lista_c, lista_s, lista_sd  



if __name__=="__main__":
    balneario=Balneario("Balneario Carilo")

    #balneario=bal.leer_archivos("archivobalneario.pkl")
    #balneario.crear_backup_contraseñas()
    #balneario.registrar_cliente("Juan Quiroga", "22222222","m","1138338366","1231231231231231")
    balneario.cargar_empleado("Josefina Marta", "22278723", "F")
    for i in balneario.dicemp.keys():
        print(balneario.dicemp[i])
    print("El empleado eliminado es:",balneario.eliminar_empleado("22278723"))
    for i in balneario.dicemp.keys():
        print(balneario.dicemp[i])
    
