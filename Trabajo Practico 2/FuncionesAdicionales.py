from random import randint

def crear_contraseña_empleado():
    contra=input("A continuación, ingresar su nueva contraseña (5 caracteres mínimo): ")
    while len(contra)<5:
        contra=input("Contraseña inválida, vuelva a ingresarla (5 caracteres mínimo): ")
    return contra

def chequear_flotante(numero_en_str):
    try:
        float(numero_en_str)
    except ValueError:
        return False
    else:
        return True

def generar_cod():
    cod=""
    for i in range(5):
        cod+=str(randint(0,9))
    return cod

def recorrer_diccionario(diccionario):
    for key in diccionario.keys():
        print(diccionario[key])