from extras.funcionesextra import buscar_dni, extraer_persona
from claseproducto import Carpa, Sombrilla
from claseempleado import Empleado
from clasereserva import Reserva
from clasecliente import Cliente
import pickle
import datetime
import csv

class Balneario():
    def __init__(self, nombre):         
        self.nombre=nombre
        self.dicemp=dict()
        self.dicclientes=dict()
        self.dicusuarios=dict()
        self.reservas_vigentes=dict()
        self.m_carpas=[[Carpa() for i in range(6)] for i in range(4)]
        self.m_sombrillas=[[Sombrilla() for i in range(5)] for i in range(3)]

#imprimo el nombre del Sistema de asignación de reservas
    def __str__(self) -> str:
        return "Bienvenido a {}".format(self.nombre)
    
#busca info en un pickle, lo carga
    def leer_archivos(self,path):
        try:
            with open(path, "rb") as f:
                infobal=pickle.load(f)
            return infobal
        except FileNotFoundError as e:
            print("Error! El archivo no se encontró.")

#hace persistir info del balneario en un pickle
    def cargar_archivos(self):
        try:
            with open("archivobalneario.pkl", "wb") as f:
                pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)
        except FileNotFoundError:
            print("Error! El arcvhivo no se encontró.")

#carga un archivo csv de contraseñas para poder leerlo nosotros y tenerlo de backup
    def crear_backup_contraseñas(self):
        try:
            with open('usuarios.csv', 'w', newline='') as csvfile:
                fieldnames = ['usuario', 'contraseña']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for empleado in self.dicemp.keys():
                    writer.writerow({'usuario': self.dicemp[empleado].codemp, 'contraseña': self.dicemp[empleado].contra})
        except FileNotFoundError:
            print("Error! No se pudo abrir el archivo.")

#busca el dni que le pidas, sea del empleado o del cliente --> devuelve True o False
    def validar_registro(self, dni_buscado, tipo):
        if tipo=="cliente":
            return buscar_dni(int(dni_buscado), self.dicclientes)
        else:
            return buscar_dni(int(dni_buscado), self.dicemp)

#devuelve el objeto sobre el cual 
    def devolver_objeto_persona(self, dni_buscado, tipo):
        if self.validar_registro(dni_buscado, tipo)==False:
            raise ValueError("El DNI del {} no se encuentra registrado.".format(tipo))
        if tipo=="cliente":
            persona=extraer_persona(int(dni_buscado),self.dicclientes)
        elif tipo== "empleado":
           persona=extraer_persona(int(dni_buscado),self.dicemp)
        return persona

#pidey verifica la contraseña del emp
    def validar_contraseña(self, codemp_ingresado):
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
    
#acción repetitiva --> busca matriz
    def matrizdetrabajo(self,tipo_reserva):
        pass

#visualiza la matriz (0 y días restantes)
    def ver_matriz(self, tipo_reserva):
        pass

#busca lugar en la matriz disponible (asignacion automática o por fila)
    def buscar_posicion_disponible(self, matriz, metodo_busqueda, num_fila=None):
        pass

#este precio despues se lo pasamos a la reserva que creemos
    def calcular_precio(self,reserva, precioxdia):
        pass

#le pasás el precio, el dni, el número de días, la fila que eligió(si eligió), y hace la reserva     
    def asignar_reserva(self,tipo_reserva,metodo, dias, dni_cliente,cotizacion_dia,fila_elegida=None):
        pass

#con esta función, antes de cerrar el programa revisamos las matrices para ver si están vencidas, si hay algo vencido lo sacamos y ponemos None
    def revisar_matriz(self,tipo):
        pass

            