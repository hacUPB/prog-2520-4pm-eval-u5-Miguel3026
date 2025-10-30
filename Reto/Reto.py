
import os
import csv
import math
import matplotlib.pyplot as plt


def contar_palabras_y_caracteres(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            texto = archivo.read()
            palabras = texto.split()
            total_palabras = len(palabras)
            total_caracteres = len(texto)
            total_sin_espacios = len(texto.replace(" ", ""))
            print("Resultados del análisis del archivo de texto:")
            print(f"Total de palabras: {total_palabras}")
            print(f"Total de caracteres (con espacios): {total_caracteres}")
            print(f"Total de caracteres (sin espacios): {total_sin_espacios}")
    except FileNotFoundError:
        print("Archivo no encontrado. Verifica el nombre o la ruta")


def reemplazar_palabra(nombre_archivo):
    try:
        palabra_buscar = input("Ingresa la palabra ha reemplazar: ")
        palabra_nueva = input("Ingresa la nueva palabra: ")
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            texto = archivo.read()

        texto_modificado = texto.replace(palabra_buscar, palabra_nueva)

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(texto_modificado)

        print("La palabra fue reemplazada correctamente.")
    except FileNotFoundError:
        print("Archivo no encontrado.")


def histograma_vocales(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            texto = archivo.read().lower()
        vocales = ['a', 'e', 'i', 'o', 'u']
        conteo = []
        for v in vocales:
            conteo.append(texto.count(v))

        plt.bar(vocales, conteo, color='orange')
        plt.title("Histograma de ocurrencia de vocales")
        plt.xlabel("Vocal")
        plt.ylabel("Cantidad")
        plt.show()
    except FileNotFoundError:
        print("Archivo no encontrado.")





def mostrar_primeras_filas(nombre_archivo):
    try:
        with open(nombre_archivo, "r", newline='', encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            contador = 0
            for fila in lector:
                print(fila)
                contador += 1
                if contador == 15:
                    break
    except FileNotFoundError:
        print("Archivo no encontrado.")


def calcular_estadisticas(nombre_archivo):
    try:
        with open(nombre_archivo, "r", newline='', encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            encabezados = next(lector)
            print("\nColumnas disponibles:")
            for i in range(len(encabezados)):
                print(f"{i+1}. {encabezados[i]}")

            opcion = int(input("Ingresa el número de la columna a analizar: ")) - 1
            datos = []
            for fila in lector:
                try:
                    valor = float(fila[opcion])
                    datos.append(valor)
                except ValueError:
                    pass  # Ignora valores no numéricos

            if len(datos) == 0:
                print(" No hay datos numéricos en esa columna.")
                return

            datos.sort()
            n = len(datos)
            promedio = sum(datos) / n
            mediana = datos[n // 2] if n % 2 != 0 else (datos[n//2 - 1] + datos[n//2]) / 2
            varianza = sum((x - promedio)**2 for x in datos) / n
            desviacion = math.sqrt(varianza)

            print("Estadísticas de la columna seleccionada:")
            print(f"Número de datos: {n}")
            print(f"Promedio: {promedio:.2f}")
            print(f"Mediana: {mediana:.2f}")
            print(f"Desviación estándar: {desviacion:.2f}")
            print(f"Máximo: {max(datos)}")
            print(f"Mínimo: {min(datos)}")

    except FileNotFoundError:
        print("Archivo no encontrado.")
    except IndexError:
        print("Número de columna inválido.")


def graficar_columna(nombre_archivo):
    try:
        with open(nombre_archivo, "r", newline='', encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            encabezados = next(lector)
            print("\nColumnas disponibles:")
            for i in range(len(encabezados)):
                print(f"{i+1}. {encabezados[i]}")

            opcion = int(input("Ingresa el número de la columna a graficar: ")) - 1
            datos = []
            for fila in lector:
                try:
                    valor = float(fila[opcion])
                    datos.append(valor)
                except ValueError:
                    pass

            if len(datos) == 0:
                print("No se encontraron datos para graficar.")
                return

            # Gráfica de dispersión
            plt.scatter(range(len(datos)), datos, color='blue')
            plt.title("Gráfica de dispersión")
            plt.xlabel("Índice")
            plt.ylabel(encabezados[opcion])
            plt.show()

            # Gráfica de barras (agrupando por decenas)
            grupos = {}
            for valor in datos:
                grupo = int(valor // 10) * 10
                if grupo in grupos:
                    grupos[grupo] += 1
                else:
                    grupos[grupo] = 1

            plt.bar(grupos.keys(), grupos.values(), color='green')
            plt.title("Distribución de valores por rangos")
            plt.xlabel("Rango de valores")
            plt.ylabel("Frecuencia")
            plt.show()
    except FileNotFoundError:
        print("Archivo no encontrado.")


# MENÚ PRINCIPAL Y SUBMENÚS


def listar_archivos():
    ruta = input("Ingresa una ruta o deja vacío para usar la actual: ")
    if ruta == "":
        ruta = os.getcwd()
    try:
        archivos = os.listdir(ruta)
        print("Archivos en la ruta seleccionada:")
        for archivo in archivos:
            print("-", archivo)
    except FileNotFoundError:
        print("No válida.")


def submenu_txt():
    nombre = input("Ingresa el nombre del archivo .txt: ")
    while True:
        print("SUBMENÚ ARCHIVOS .TXT")
        print("1. Contar palabras y caracteres")
        print("2. Reemplazar una palabra")
        print("3. Histograma de vocales")
        print("4. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            contar_palabras_y_caracteres(nombre)
        elif opcion == "2":
            reemplazar_palabra(nombre)
        elif opcion == "3":
            histograma_vocales(nombre)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")


def submenu_csv():
    nombre = input("Ingresa el nombre del archivo .csv: ")
    while True:
        print("SUBMENÚ ARCHIVOS .CSV")
        print("1. Mostrar las 15 primeras filas")
        print("2. Calcular estadísticas de una columna")
        print("3. Graficar una columna")
        print("4. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_primeras_filas(nombre)
        elif opcion == "2":
            calcular_estadisticas(nombre)
        elif opcion == "3":
            graficar_columna(nombre)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")


def main():
    while True:
        print("MENÚ PRINCIPAL")
        print("1. Listar archivos en ruta")
        print("2. Leer archivo de texto (.txt)")
        print("3. Leer archivo CSV (.csv)")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            listar_archivos()
        elif opcion == "2":
            submenu_txt()
        elif opcion == "3":
            submenu_csv()
        elif opcion == "4":
            print("Cerrando programa..")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
