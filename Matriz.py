from ListaSimpleEnlazada import ListaEnlazada
from Frecuencia import Frecuencia
class Matriz:
    def __init__(self, num_filas, num_columnas):
        self.num_filas = num_filas
        self.num_columnas = num_columnas
        self.matriz = ListaEnlazada()


        # crea matriz inicializada con ceros
        for i in range(num_filas):
            fila = ListaEnlazada()
            for i in range(num_columnas):
                frecuencia = Frecuencia( "", "0")
                fila.insertar(frecuencia)
            self.matriz.insertar(fila)

    def establecer(self, num_fila, num_columna, frecuancia):
        #Establece un valor en la posicion [fila, columna]
        fila = self.matriz.obtener(num_fila)
        if fila:
            # Buscar el nodo en la columna especifica
            columna = fila.primero
            for i in range(num_columna):
                if columna:
                    columna = columna.siguiente
                if columna:
                    columna.dato = frecuancia

    def obtener(self, num_fila, num_columna):
        #Establece un valor en la posicion [fila, columna]
        fila = self.matriz.obtener(num_fila)
        if fila:
            return fila.obtener(num_columna)
        return None
    
    def mostrar(self, titulo, headers_fila, headers_columna):
        #muestra la matriz de forma tabular
        print(f"\n{titulo}")
        print("="*50)

        #headers de columnas
        print("Estacion\\Sensor", end="\t")
        for j in range(self.num_columnas):
            sensor = headers_columna.obtener(j)
            print(f"{sensor.id}", end="\t")

        
        #Filas con datos
        for i in range(self.num_filas):
            estacion = headers_fila.obtener(i)
            print(f"{estacion.id}", end="\t")
            for j in range(self.num_columnas):
                Frecuencia = self.obtener(i,j)
                print(f"{Frecuencia.valor}", end="\t")
                print()