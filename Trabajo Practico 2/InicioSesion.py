from ClaseBalneario import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QGridLayout, QWidget

balneario=Balneario("Balneario Carilo")

# Definimos la función "recorrer_diccionario" que recibe un diccionario como argumento
def recorrer_diccionario(diccionario):
    # Iteramos sobre las claves del diccionario
    for key in diccionario.keys():
        # Imprimimos el valor asociado a cada clave
        print(diccionario[key])

# Intentamos abrir el archivo "archivobalneario.pkl" en modo de lectura binaria
try:
    with open("archivobalneario.pkl", "rb") as f:   # Abrimos el archivo pickle
        # Cargamos el contenido del archivo en la variable "balneario"
        balneario = pickle.load(f)
except FileNotFoundError:
    # Si el archivo no existe, creamos un nuevo balneario y agregamos un empleado predeterminado
    balneario = Balneario("Carpas y sombrillas")
    balneario.cargar_empleado("Leandro Díaz", "21333333", "M")


# Definimos la clase "VentanaInicioSesion" que hereda de QMainWindow
class VentanaInicioSesion(QMainWindow):
    # El constructor recibe un objeto "balneario" de tipo "Balneario"
    def __init__(self, balneario: Balneario):
        super().__init__()
        # Imprimimos las claves y valores del diccionario "dicemp" del objeto "balneario"
        for key, value in balneario.dicemp.items():
            print(key, value)
        # Asignamos el objeto "balneario" al atributo "self.balneario"
        self.balneario = balneario
        # Configuramos el título de la ventana
        self.setWindowTitle("Inicio de Sesión")
        # Creamos el widget principal y lo establecemos como widget central de la ventana
        widget_principal = QWidget()
        self.setCentralWidget(widget_principal)
        # Creamos un layout principal de tipo QGridLayout para organizar los elementos de la ventana
        layout_principal = QGridLayout()
        widget_principal.setLayout(layout_principal)
        # Creamos etiquetas y campos de entrada para el código de empleado y la contraseña
        self.label_empleado = QLabel("Código de empleado:")
        self.input_empleado = QLineEdit()
        self.label_contrasena = QLabel("Contraseña:")
        self.input_contrasena = QLineEdit()
        self.input_contrasena.setEchoMode(QLineEdit.Password)
        # Creamos un botón de iniciar sesión y lo conectamos a la función "iniciar_sesion"
        self.boton_iniciar_sesion = QPushButton("Iniciar Sesión")
        self.boton_iniciar_sesion.clicked.connect(self.iniciar_sesion)
        # Agregamos los elementos al layout principal
        layout_principal.addWidget(self.label_empleado, 0, 0)
        layout_principal.addWidget(self.input_empleado, 0, 1)
        layout_principal.addWidget(self.label_contrasena, 1, 0)
        layout_principal.addWidget(self.input_contrasena, 1, 1)
        layout_principal.addWidget(self.boton_iniciar_sesion, 2, 0, 1, 2)
        # Establecemos el tamaño mínimo de la ventana
        self.setMinimumSize(300, 200)


    def iniciar_sesion(self):
        cod_empleado = self.input_empleado.text()
        contrasena = self.input_contrasena.text()

        if cod_empleado in self.balneario.dicusuarios.keys() and self.balneario.dicusuarios[cod_empleado] == contrasena:
            print("Inicio de sesión exitoso")
        else:
            print(self.balneario)
            print("Empleado o contraseña incorrectos",cod_empleado,cod_empleado in self.balneario.dicusuarios, self.balneario.dicusuarios[int(cod_empleado)], self.balneario.dicemp[cod_empleado] == contrasena)

    def iniciar_sesion(self):
    # Obtener el código de empleado ingresado
        cod_empleado = self.input_empleado.text()
    # Obtener la contraseña ingresada
        contrasena = self.input_contrasena.text()
    # Verificar si el código de empleado está presente en el diccionario dicusuarios y si la contraseña coincide
        if cod_empleado in self.balneario.dicusuarios.keys() and self.balneario.dicusuarios[cod_empleado] == contrasena:
        # Si la verificación es exitosa, imprimir un mensaje de inicio de sesión exitoso
            print("Inicio de sesión exitoso")
        else:
        # Si la verificación falla, imprimir información de depuración para ayudar a identificar el problema
        # Imprimir el objeto balneario (útil para verificar su estado)
            print(self.balneario)
        # Imprimir información adicional para depuración
            print("Empleado o contraseña incorrectos",cod_empleado,cod_empleado in self.balneario.dicusuarios, self.balneario.dicusuarios[int(cod_empleado)], self.balneario.dicemp[cod_empleado] == contrasena)
            #Código de empleado ingresado, Verificar si el código de empleado está en el diccionario dicusuarios, Contraseña asociada al código de empleado, Verificar si la contraseña coincide con la almacenada en dicemp
            
if __name__ == "__main__":

    app = QApplication(sys.argv)
    ventana = VentanaInicioSesion(balneario)
    ventana.show()
    sys.exit(app.exec_())