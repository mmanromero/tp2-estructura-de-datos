from ClaseBalneario import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QGridLayout, QWidget

balneario=Balneario("Balneario Carilo")

def recorrer_diccionario(diccionario):
    for key in diccionario.keys():
        print(diccionario[key])

try:
    with open("archivobalneario.pkl", "rb") as f:   #abro el pickle
        balneario=pickle.load(f)
except FileNotFoundError:
        balneario.cargar_empleado("Leandro Díaz", "21333333", "M")

class VentanaInicioSesion(QMainWindow):
    def __init__(self, balneario:Balneario):
        super().__init__()
        for key, value in balneario.dicemp.items():
            print (key,value)
        self.balneario=balneario
        self.setWindowTitle("Inicio de Sesión")

        widget_principal = QWidget()
        self.setCentralWidget(widget_principal)

        layout_principal = QGridLayout()
        widget_principal.setLayout(layout_principal)

        self.label_empleado = QLabel("Código de empleado:")
        self.input_empleado = QLineEdit()

        self.label_contrasena = QLabel("Contraseña:")
        self.input_contrasena = QLineEdit()
        self.input_contrasena.setEchoMode(QLineEdit.Password)

        self.boton_iniciar_sesion = QPushButton("Iniciar Sesión")
        self.boton_iniciar_sesion.clicked.connect(self.iniciar_sesion)

        layout_principal.addWidget(self.label_empleado, 0, 0)
        layout_principal.addWidget(self.input_empleado, 0, 1)
        layout_principal.addWidget(self.label_contrasena, 1, 0)
        layout_principal.addWidget(self.input_contrasena, 1, 1)
        layout_principal.addWidget(self.boton_iniciar_sesion, 2, 0, 1, 2)


        self.setMinimumSize(300, 200)

    def iniciar_sesion(self):
        cod_empleado = self.input_empleado.text()
        contrasena = self.input_contrasena.text()

        if cod_empleado in self.balneario.dicusuarios.keys() and self.balneario.dicusuarios[cod_empleado] == contrasena:
            print("Inicio de sesión exitoso")
        else:
            print(self.balneario)
            print("Empleado o contraseña incorrectos",cod_empleado,cod_empleado in self.balneario.dicusuarios, self.balneario.dicusuarios[int(cod_empleado)], self.balneario.dicemp[cod_empleado] == contrasena)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ventana = VentanaInicioSesion(balneario)
    ventana.show()
    sys.exit(app.exec_())