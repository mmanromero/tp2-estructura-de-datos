from random import randint

def crear_contraseña_empleado():
    """
    Función para crear una nueva contraseña para un empleado.

    Retorna:
    - La contraseña ingresada por el usuario, siempre y cuando tenga al menos 5 caracteres.

    Acciones:
    - Solicita al usuario que ingrese una nueva contraseña.
    - Verifica que la contraseña tenga al menos 5 caracteres.
    - Retorna la contraseña ingresada.
    """
    contra=input("A continuación, ingresar su nueva contraseña (5 caracteres mínimo): ")
    while len(contra)<5:
        contra=input("Contraseña inválida, vuelva a ingresarla (5 caracteres mínimo): ")
    return contra

def chequear_flotante(numero_en_str):
    """
    Función para verificar si un número en formato de cadena puede ser convertido a un número de punto flotante.

    Parámetros:
    - numero_en_str: número representado como una cadena de texto.

    Retorna:
    - True si el número puede ser convertido a un número de punto flotante.
    - False en caso contrario.

    Acciones:
    - Intenta convertir el número a un número de punto flotante.
    - Si la conversión es exitosa, retorna True.
    - Si ocurre un ValueError durante la conversión, retorna False.
    """
    try:
        float(numero_en_str)
    except ValueError:
        return False
    else:
        return True

def generar_cod():
    """
    Función para generar un código aleatorio de 5 dígitos.

    Retorna:
    - Un código de 5 dígitos generado aleatoriamente.

    Acciones:
    - Genera un código de 5 dígitos aleatoriamente utilizando la función randint() del módulo random.
    - Retorna el código generado.
    """
    cod=""
    for i in range(5):
        cod+=str(randint(0,9))
    return cod

def recorrer_diccionario(diccionario):
    """
    Función para recorrer un diccionario e imprimir sus valores.

    Parámetros:
    - diccionario: diccionario a recorrer.

    Acciones:
    - Itera sobre las claves del diccionario.
    - Imprime los valores correspondientes a cada clave.
    """
    for key in diccionario.keys():
        print(diccionario[key])
