class Producto():
    def __init__(self):
        self.estado=None

class Carpa(Producto):
    pass
class Sombrilla(Producto):
    pass

if __name__=="__main__":
    hola=Carpa()
    chau=Sombrilla()
    print(chau.estado)
    hola.estado="hh"
    print(hola.estado)