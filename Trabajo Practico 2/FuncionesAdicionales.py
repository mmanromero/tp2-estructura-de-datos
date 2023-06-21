from random import randint

# Función para crear una contraseña de empleado
def crear_contraseña_empleado():
    """
    Esta función solicita al usuario que ingrese una nueva contraseña para un empleado.
    La contraseña debe tener al menos 5 caracteres.
    Si la contraseña no cumple con el requisito, se le pedirá al usuario que ingrese nuevamente.
    Devuelve la contraseña ingresada.
    """
    contra = input("A continuación, ingresar su nueva contraseña (5 caracteres mínimo): ")
    while len(contra) < 5:
        contra = input("Contraseña inválida, vuelva a ingresarla (5 caracteres mínimo): ")
    return contra

# Función para verificar si un número en formato de cadena es un número de punto flotante válido
def chequear_flotante(numero_en_str):
    """
    Esta función verifica si un número representado como una cadena de caracteres es un número de punto flotante válido.
    Devuelve True si es válido, False si no lo es.
    """
    try:
        float(numero_en_str)
    except ValueError:
        return False
    else:
        return True

# Función para generar un código aleatorio de 5 dígitos
def generar_cod():
    """
    Esta función genera un código aleatorio de 5 dígitos.
    Los dígitos están en el rango del 0 al 9.
    Devuelve el código generado.
    """
    cod = ""
    for i in range(5):
        cod += str(randint(0, 9))
    return cod

# Función para recorrer un diccionario e imprimir sus valores
def recorrer_diccionario(diccionario):
    """
    Esta función recorre un diccionario e imprime los valores correspondientes a cada clave.
    Recibe como argumento el diccionario a recorrer.
    """
    for key in diccionario.keys():
        print(diccionario[key])
