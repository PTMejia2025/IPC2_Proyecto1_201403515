from moduloSistema_agricola import SistemaAgricola

def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Cargar archivo")
    print("2. Procesar archivo")
    print("3. Escribir archivo salida")
    print("4. Mostrar datos estudiante")
    print("5. Generar gráfica")
    print("6. Salida")
    print("==========================")



def main():
    sistema = SistemaAgricola()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            archivo = input("Ingrese ruta del archivo XML: ")
            sistema.cargar_archivo(archivo)
        elif opcion == "2":
            sistema.procesar_datos()
        elif opcion == "3":
            archivo_salida = input("Ingrese nombre del archivo de salida: ")
            sistema.escribir_archivo_salida(archivo_salida)
        elif opcion == "4":
            sistema.mostrar_datos_estudiante()
        elif opcion == "5":
            sistema.generar_grafica()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    main()