import sys
import pickle
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from ClaseBalneario import Balneario

try:
    with open("archivobalneario.pkl", "rb") as f:   #abro el pickle
        balneario=pickle.load(f)
except FileNotFoundError:
        balneario=Balneario("Bal Carilo")
        balneario.cargar_empleado("Leandro Díaz", "21333333", "M")

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de sesión")
        self.setup_ui()

    def setup_ui(self):
        label_username = QLabel("Código de empleado:")
        self.lineedit_username = QLineEdit()
        label_password = QLabel("Contraseña:")
        self.lineedit_password = QLineEdit()
        self.lineedit_password.setEchoMode(QLineEdit.Password)
        button_login = QPushButton("Iniciar sesión")
        button_login.clicked.connect(self.login)

        layout = QVBoxLayout()
        layout.addWidget(label_username)
        layout.addWidget(self.lineedit_username)
        layout.addWidget(label_password)
        layout.addWidget(self.lineedit_password)
        layout.addWidget(button_login)

        self.setLayout(layout)

    def login(self):
        username = self.lineedit_username.text()
        password = self.lineedit_password.text()
        iniciado=None
        if username in balneario.dicusuarios.keys():
            if balneario.dicusuarios[username]==password:
                print("Inicio de sesión exitoso")
                iniciado=True
                self.close()  # Cierra la ventana principal
            else:
                QMessageBox.warning(self, "Error", "Contraseña incorrecta.")
                self.lineedit_password.setText("")  # Limpia el campo de contraseña
        else:
            QMessageBox.warning(self, "Error", "Código de empleado no registrado.")
            self.lineedit_password.setText("")  # Limpia el campo de contraseña

        # # Aquí puedes realizar la validación de la contraseña y el usuario
        # if username == "admin" and password == "12345":
        #     print("Inicio de sesión exitoso")
        #     self.close()  # Cierra la ventana principal
        # else:
        #     QMessageBox.warning(self, "Error", "Nombre de usuario o contraseña incorrectos.")
        #     self.lineedit_password.setText("")  # Limpia el campo de contraseña
        return iniciado, username

# Crear la aplicación
app = QApplication(sys.argv)

# Crear la instancia de la clase LoginWindow
login_window = LoginWindow()
login_window.show()

# Ejecutar la aplicación
hola,chau=sys.exit(app.exec())