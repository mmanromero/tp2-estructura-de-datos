import sys
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from threading import Thread

# Definición de la clase LoginWindow que hereda de QWidget
class LoginWindow(QWidget):
    register_signal = pyqtSignal() # Declaración de la señal register_signal
    
    def __init__(self): # Constructor de la clase
        super().__init__()
        self.setWindowTitle("Inicio de sesión")  # Configuración de la ventana   
        self.setup_ui() # Configuración de la interfaz de usuario
        self.login_success = False # Inicialización de la variable de estado de inicio de sesión

    # Definición del método setup_ui
    def setup_ui(self):
    # Creación de etiquetas y campos de entrada para el nombre de usuario y contraseña
        label_username = QLabel("Usuario:")
        self.lineedit_username = QLineEdit()
        label_password = QLabel("Contraseña:")
        self.lineedit_password = QLineEdit()
        self.lineedit_password.setEchoMode(QLineEdit.Password)
    
    # Creación de botones para iniciar sesión y registrarse
        button_login = QPushButton("Iniciar sesión")
        button_login.clicked.connect(self.login)

        button_register = QPushButton("Registrarse")
        button_register.clicked.connect(self.register)

    # Configuración del diseño del formulario
        layout = QVBoxLayout()
        layout.addWidget(label_username)
        layout.addWidget(self.lineedit_username)
        layout.addWidget(label_password)
        layout.addWidget(self.lineedit_password)
        layout.addWidget(button_login)
        layout.addWidget(button_register)

    # Configuración del diseño principal de la ventana
        self.setLayout(layout)


    # Definición del método login
    def login(self):
    # Obtención del nombre de usuario y contraseña ingresados por el usuario
        username = self.lineedit_username.text()
        password = self.lineedit_password.text()

    # Aquí puedes realizar la validación de la contraseña y el usuario
        if username == "admin" and password == "12345":
        # Si las credenciales son correctas, se muestra un mensaje de inicio de sesión exitoso
            print("Inicio de sesión exitoso")
            self.login_success = True  # Marca el éxito del inicio de sesión
            self.close()  # Cierra la ventana de inicio de sesión y regresa a la ventana principal
        else:
        # Si las credenciales son incorrectas, se muestra un mensaje de error
            QMessageBox.warning(self, "Error", "Nombre de usuario o contraseña incorrectos.")
            self.lineedit_password.setText("")  # Limpia el campo de contraseña para que el usuario pueda intentarlo nuevamente


    # Método register
    def register(self):
    # Emitir la señal register_signal
        self.register_signal.emit()

# Método get_login_success
    def get_login_success(self):
    # Retorna el valor de login_success
        return self.login_success



# Definición de la clase RegistrationWindow que hereda de QWidget
class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()  # Llamada al constructor de la clase padre para inicializar la instancia de QWidget
        self.setWindowTitle("Registro")  # Establece el título de la ventana como "Registro"
        # Creación de un objeto QLabel con el texto "¡Regístrate en otro lugar!"
        label_register = QLabel("¡Regístrate en otro lugar!")
        # Creación de un objeto QVBoxLayout para organizar los elementos de la ventana de forma vertical
        layout = QVBoxLayout()
        # Agrega el QLabel al QVBoxLayout utilizando el método addWidget
        layout.addWidget(label_register)
        # Establece el QVBoxLayout como el diseño principal de la ventana utilizando el método setLayout
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