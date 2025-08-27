from ListaSimpleEnlazada import ListaEnlazada
from Campo import Campo
from Estacion import Estacion
from Frecuencia import Frecuencia
from Sensor import Sensor
from xml.dom.minidom import parse


class SistemaAgricultura:
    def __init__(self):
        self.campos = ListaEnlazada()
        #self.estaciones = []
        self.archivo_cargado = False

    def cargar_archivo(self, ruta_archivo):

        try:
            dom = parse(ruta_archivo)
            campos_xml = dom.getElementsByTagName("campo")
            
            for campo_xml in campos_xml:
                id_campo = campo_xml.getAttribute('id')
                nombre_campo = campo_xml.getAttribute('nombre')
                campo = campo(id_campo, nombre_campo)
                print(f"Cargando Campo Agricola{id_campo}")
                
                #ecargar 
                print
        

        except Exception as e:
            print(f"Error al cargar el archivo {e}")



    def procesar_datos(self):
        if not self.archivo_cargado:
            print("ERROR Debe cargar un archivo primero.")
            return
        print("[Procesando datos...")
        # Aquí se llamará a procesador.py

    def escribir_archivo_salida(self, ruta):
        print(f"Escribiendo archivo de salida en: {ruta}")
        # Guardar resultados en XML

    def mostrar_datos_estudiante(self):
        print("\nDatos del estudiante:")
        print("Nombre: Pedro Tomás Mejía Tol")
        print("Carnet: 201403515")  
        print("Curso: Introducción a la Programación y Computación 2")
        print("Seccion: N")
        print("4to Semestre")
        print("Se esta trabajando para el enlace a Documentacion XD")

    def generar_grafica(self):
        print("Generando gráfica...")
        # Aquí llamare a graficador