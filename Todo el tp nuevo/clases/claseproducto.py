class Producto():
    def __init__(self) -> None:
        self.estado=None

class Carpa(Producto):
    def __init__(self, estado):
        super.__init__(estado)

class Sombrilla(Producto):
    def __init__(self, estado, sponsor):
        super.__init__(estado)
        if sponsor not in ["garbarino", "cablevisión"]:
            raise ValueError("El Sponsor ingresado no es válido.")
        super.__init__(estado)
        self.sponsor=sponsor