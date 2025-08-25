from listaSimpleEnlazada import ListaEnlazada

class Campo:
    def __init__(self, id_campo, nombre):
        self.id = id_campo
        self.nombre = nombre
        self.estaciones = ListaEnlazada()
        self.sonsores_suelo = ListaEnlazada()
        self.sonsores_cultivo = ListaEnlazada()
        