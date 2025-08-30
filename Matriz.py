from ListaSimpleEnlazada import ListaEnlazada
from Frecuencia import Frecuencia

class Matriz:
    def __init__(self, num_filas, num_columnas):
        self.num_filas = num_filas
        self.num_columnas = num_columnas
        self.matriz = ListaEnlazada()
        
        # Crear matriz inicializada con ceros
        for i in range(num_filas):
            fila = ListaEnlazada()
            for j in range(num_columnas):
                frecuencia = Frecuencia("", "0")
                fila.insertar(frecuencia)
            self.matriz.insertar(fila)
    
    def establecer(self, num_fila, num_columna, frecuencia):
        # Establece un valor en la posicion [fila, columna]
        fila = self.matriz.obtener(num_fila)
        if fila:
            # Buscar el nodo en la columna especifica
            columna = fila.primero
            for i in range(num_columna):
                if columna:
                    columna = columna.siguiente
            if columna:
                columna.dato = frecuencia
    
    def obtener(self, num_fila, num_columna):
        # Obtiene el valor en la posicion [fila, columna]
        fila = self.matriz.obtener(num_fila)
        if fila:
            return fila.obtener(num_columna)
        return None
    
    def mostrar(self, titulo, headers_fila, headers_columna):
        # Muestra la matriz de forma tabular
        print(f"\n{titulo}")
        print("=" * 50)
        
        # Headers de columnas
        print("Estacion\\Sensor", end="\t")
        for j in range(self.num_columnas):
            sensor = headers_columna.obtener(j)
            print(f"{sensor.id}", end="\t")
        print()
        
        # Filas con datos
        for i in range(self.num_filas):
            estacion = headers_fila.obtener(i)
            print(f"{estacion.id}", end="\t\t")

    def mostrar(self, titulo, headers_fila, headers_columna):
        # Muestra la matriz de forma tabular
        print(f"\n{titulo}")
        print("=" * 50)
        
        # Headers de columnas
        print("Estacion\\Sensor", end="\t")
        for j in range(self.num_columnas):
            sensor = headers_columna.obtener(j)
            print(f"{sensor.id}", end="\t")
        print()
        
        # Filas con datos
        for i in range(self.num_filas):
            estacion = headers_fila.obtener(i)
            print(f"{estacion.id}", end="\t\t")
            for j in range(self.num_columnas):
                freq = self.obtener(i, j)         # Frecuencia o None
                val = freq.valor if freq else 0   # numérico
                print(f"{val}", end="\t")
            print()


from ListaSimpleEnlazada import ListaEnlazada
from Frecuencia import Frecuencia

class MatrizPatron:
    def __init__(self, num_filas, num_columnas):
        self.num_filas = num_filas
        self.num_columnas = num_columnas
        self.matriz = ListaEnlazada()
        for _ in range(num_filas):
            fila = ListaEnlazada()
            for _ in range(num_columnas):
                fila.insertar(0)  # entero 0
            self.matriz.insertar(fila)

    def establecer(self, i, j, valor_binario):
        fila = self.matriz.obtener(i)
        if fila:
            nodo = fila.primero
            k = 0
            while nodo and k < j:
                nodo = nodo.siguiente
                k += 1
            if nodo:
                nodo.dato = 1 if valor_binario else 0

    def obtener(self, i, j):
        fila = self.matriz.obtener(i)
        return fila.obtener(j) if fila else 0

    def mostrar(self, titulo, headers_fila, headers_columna):
        print(f"\n{titulo}")
        print("=" * 50)
        print("Estacion\\Sensor", end="\t")
        for j in range(self.num_columnas):
            s = headers_columna.obtener(j)
            print(f"{s.id}", end="\t")
        print()
        for i in range(self.num_filas):
            e = headers_fila.obtener(i)
            print(f"{e.id}", end="\t\t")
            for j in range(self.num_columnas):
                print(f"{self.obtener(i, j)}", end="\t")
            print()


# Agrega este método dentro de tu clase Matriz:
def a_patrones(self):
    mp = MatrizPatron(self.num_filas, self.num_columnas)
    for i in range(self.num_filas):
        for j in range(self.num_columnas):
            freq = self.obtener(i, j)              # Frecuencia
            val = freq.valor if freq else 0        # numérico
            mp.establecer(i, j, 1 if val > 0 else 0)
    return mp
# Nota: pega este método a_patrones como method de Matriz (sangría dentro de la clase).

