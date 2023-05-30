from random import randint

#hola

def chequear_flotante(numero_en_str):
    try:
        float(numero_en_str)
    except ValueError:
        return False
    else:
        return True
    
def recorrer_diccionario(diccionario):
    for key in diccionario.keys():
        print(diccionario[key])

def generar_cod():
    cod=""
    for i in range(5):
        cod+=str(randint(0,9))
    return cod

buscar_dni=lambda dni,diccionario:True if dni in diccionario.keys() else False
extraer_persona=lambda dni,diccionario:diccionario[dni] if dni in diccionario.keys() else None 
