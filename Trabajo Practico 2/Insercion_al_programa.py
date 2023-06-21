import sys
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from threading import Thread


class LoginWindow(QWidget):
    register_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de sesión")
        self.setup_ui()
        self.login_success = False

    def setup_ui(self):
        label_username = QLabel("Usuario:")
        self.lineedit_username = QLineEdit()
        label_password = QLabel("Contraseña:")
        self.lineedit_password = QLineEdit()
        self.lineedit_password.setEchoMode(QLineEdit.Password)
        button_login = QPushButton("Iniciar sesión")
        button_login.clicked.connect(self.login)

        button_register = QPushButton("Registrarse")
        button_register.clicked.connect(self.register)

        layout = QVBoxLayout()
        layout.addWidget(label_username)
        layout.addWidget(self.lineedit_username)
        layout.addWidget(label_password)
        layout.addWidget(self.lineedit_password)
        layout.addWidget(button_login)
        layout.addWidget(button_register)

        self.setLayout(layout)

    def login(self):
        username = self.lineedit_username.text()
        password = self.lineedit_password.text()

        # Aquí puedes realizar la validación de la contraseña y el usuario
        if username == "admin" and password == "12345":
            print("Inicio de sesión exitoso")
            self.login_success = True
            self.close()  # Cierra la ventana principal
        else:
            QMessageBox.warning(self, "Error", "Nombre de usuario o contraseña incorrectos.")
            self.lineedit_password.setText("")  # Limpia el campo de contraseña

    def register(self):
        self.register_signal.emit()

    def get_login_success(self):
        return self.login_success


class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro")

        label_register = QLabel("¡Regístrate en otro lugar!")
        layout = QVBoxLayout()
        layout.addWidget(label_register)

        self.setLayout(layout)


# Función para ejecutar la aplicación en segundo plano
def run_app():
    app.exec()


# Crear la aplicación
app = QApplication(sys.argv)

# Crear la instancia de la clase LoginWindow
login_window = LoginWindow()

# Crear la instancia de la clase RegistrationWindow
registration_window = RegistrationWindow()

# Conectar la señal del botón "Registrarse" en LoginWindow a la función para mostrar la ventana de registro
login_window.register_signal.connect(registration_window.show)

# Mostrar la ventana de inicio de sesión
login_window.show()

# Iniciar la aplicación en un hilo separado
app_thread = Thread(target=run_app)
app_thread.start()

# A partir de aquí, puedes continuar con el resto de tu código
# Ejemplo adicional:
# Esperar hasta que el inicio de sesión sea exitoso
while not login_window.get_login_success():
    pass

# Continuar con el resto del código
print("Continuando con el resto del código...")

# Ejecutar otras operaciones mientras la aplicación se ejecuta en segundo plano
while app_thread.is_alive():
    # Ejecutar otras operaciones aquí
    # ...
    QApplication.processEvents()

# Esperar a que el hilo de la aplicación finalice antes de salir
app_thread.join()

# Finalizar el programa