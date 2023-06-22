class Producto():
    def __init__(self):
        """
        Constructor de la clase Producto.

        Parámetros:
        - self: referencia al objeto actual de la clase.

        Acciones:
        - Inicializa un objeto Producto.
        - Establece el estado del producto como None.
        """
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