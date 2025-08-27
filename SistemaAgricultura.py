class SistemaAgricola:
    def __init__(self):
        self.estaciones = []
        self.archivo_cargado = False

    def cargar_archivo(self, ruta):
        print(f" Cargando archivo: {ruta}")
        self.archivo_cargado = True
        

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