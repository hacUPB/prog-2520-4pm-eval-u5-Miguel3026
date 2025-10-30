import os
import csv
import statistics
import matplotlib.pyplot as plt

# LISTAR ARCHIVOS
def listar_archivos():
    ruta = input("Ingrese una ruta o deje vacío para usar la ruta actual: ")
    if ruta.strip() == "":
        ruta = os.getcwd()
    try:
        archivos = os.listdir(ruta)
        print("Archivos encontrados en:", ruta)
        # Usamos range() para numerar los archivos
        for i in range(len(archivos)):
            print(f"{i + 1}. {archivos[i]}")
    except FileNotFoundError:
        print("La ruta no existe. Intente nuevamente.")

# SUBMENÚ PARA ARCHIVOS .TXT
def submenu_txt():
    archivo = input("Ingrese el nombre del archivo .txt: ")
    if not archivo.endswith(".txt"):
        print("Debe ser un archivo de texto (.txt)")
        return

    while True:
        print("SUBMENÚ ARCHIVOS DE TEXTO")
        print("1. Contar palabras y caracteres")
        print("2. Reemplazar una palabra por otra")
        print("3. Histograma de vocales")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            contar_palabras_caracteres(archivo)
        elif opcion == "2":
            reemplazar_palabra(archivo)
        elif opcion == "3":
            histograma_vocales(archivo)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# FUNCIONES PARA ARCHIVOS .TXT
def contar_palabras_caracteres(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            texto = f.read()

        palabras = texto.split()
        total_palabras = len(palabras)
        total_caracteres = len(texto)
        sin_espacios = len(texto.replace(" ", ""))

        print("RESULTADOS:")
        print("Total de palabras:", total_palabras)
        print("Total de caracteres con espacios:", total_caracteres)
        print("Total de caracteres sin espacios:", sin_espacios)
    except FileNotFoundError:
        print("Archivo no encontrado. Verifique el nombre.")

def reemplazar_palabra(archivo):
    palabra_buscar = input("Palabra a buscar: ")
    palabra_nueva = input("Palabra nueva: ")

    try:
        with open(archivo, "r", encoding="utf-8") as f:
            texto = f.read()

        nuevo_texto = texto.replace(palabra_buscar, palabra_nueva)

        with open(archivo, "w", encoding="utf-8") as f:
            f.write(nuevo_texto)

        print("Se realizó el cambio.")
    except FileNotFoundError:
        print("Archivo no encontrado.")

def histograma_vocales(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            texto = f.read().lower()

        vocales = ['a', 'e', 'i', 'o', 'u']
        conteos = []

        for v in vocales:
            cantidad = texto.count(v)
            conteos.append(cantidad)

        # Mostramos conteo usando range()
        print("Conteo de vocales:")
        for i in range(len(vocales)):
            print(f"{vocales[i]}: {conteos[i]}")

        plt.bar(vocales, conteos, color="skyblue")
        plt.title("Histograma de ocurrencia de vocales")
        plt.xlabel("Vocales")
        plt.ylabel("Cantidad")
        plt.show()
    except FileNotFoundError:
        print("Archivo no encontrado.")

# SUBMENÚ PARA ARCHIVOS .CSV
def submenu_csv():
    archivo = input("Ingrese el nombre del archivo .csv: ")
    if not archivo.endswith(".csv"):
        print("Debe ser un archivo CSV válido.")
        return

    while True:
        print(" SUBMENÚ ARCHIVOS .CSV ")
        print("1. Mostrar las primeras 15 filas")
        print("2. Calcular estadísticas de una columna")
        print("3. Graficar una columna numérica")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_filas_csv(archivo)
        elif opcion == "2":
            calcular_estadisticas(archivo)
        elif opcion == "3":
            graficar_columna(archivo)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

# FUNCIONES PARA ARCHIVOS .CSV
def mostrar_filas_csv(archivo):
    try:
        with open(archivo, newline='', encoding='utf-8') as f:
            lector = csv.reader(f)
            print("\nPrimeras 15 filas del archivo:")
            # Usamos range() para limitar las 15 primeras filas
            for i in range(15):
                try:
                    fila = next(lector)
                    print(fila)
                except StopIteration:
                    break
    except FileNotFoundError:
        print("Archivo no encontrado.")

def calcular_estadisticas(archivo):
    columna = input("Ingrese el nombre de la columna a analizar: ")

    try:
        with open(archivo, newline='', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            valores = []
            for fila in lector:
                if columna in fila and fila[columna].strip() != "":
                    try:
                        valor = float(fila[columna])
                        valores.append(valor)
                    except:
                        pass

        if len(valores) == 0:
            print("No se encontraron datos numéricos válidos en esa columna.")
            return

        print("\nESTADÍSTICAS DE LA COLUMNA:", columna)
        print("Cantidad de datos:", len(valores))
        print("Promedio:", statistics.mean(valores))
        print("Mediana:", statistics.median(valores))
        if len(valores) > 1:
            print("Desviación estándar:", statistics.stdev(valores))
        else:
            print("Desviación estándar: No aplica (solo un valor).")
        print("Máximo:", max(valores))
        print("Mínimo:", min(valores))
    except FileNotFoundError:
        print("Archivo no encontrado.")

def graficar_columna(archivo):
    columna = input("Ingrese el nombre de la columna numérica a graficar: ")

    try:
        with open(archivo, newline='', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            valores = []
            for fila in lector:
                try:
                    valor = float(fila[columna])
                    valores.append(valor)
                except:
                    pass

        if len(valores) == 0:
            print("No se encontraron datos numéricos válidos.")
            return

        # Gráfico de dispersión
        plt.scatter(range(len(valores)), valores, color='orange')
        plt.title("Gráfico de dispersión - " + columna)
        plt.xlabel("Índice")
        plt.ylabel(columna)
        plt.show()

        # Gráfico de barras (primeros 10 valores)
        plt.bar(range(10), valores[:10], color='green')
        plt.title("Primeros 10 valores - " + columna)
        plt.xlabel("Índice")
        plt.ylabel(columna)
        plt.show()

    except FileNotFoundError:
        print("Archivo no encontrado.")

# FUNCION PRINCIPAL
def main():
    while True:
        print("MENÚ PRINCIPAL")
        print("1. Listar archivos en la ruta actual o en una ruta dada")
        print("2. Procesar archivo de texto (.txt)")
        print("3. Procesar archivo separado por comas (.csv)")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_archivos()
        elif opcion == "2":
            submenu_txt()
        elif opcion == "3":
            submenu_csv()
        elif opcion == "4":
            print("cerrando el programa..")
            break
        else:
            print("Opción no válida")

# EJECUCIÓN PRINCIPAL
if __name__ == "__main__":
    main()


