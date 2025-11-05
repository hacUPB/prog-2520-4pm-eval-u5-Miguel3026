
import os
import csv
import math
import matplotlib.pyplot as plt
# Archivos elegidos para el reto
ARCHIVO_TXT = "datosm.txt"
ARCHIVO_CSV = "matriculas.csv"

def listar_archivos(ruta):
    """Lista archivos en la ruta dada (ruta='' para ruta actual)."""
    try:
        if ruta == '':
            ruta = os.getcwd()
        nombres = os.listdir(ruta)
        print("\nArchivos en:", ruta)
        for nombre in nombres:
            print(" -", nombre)
    except Exception as e:
        print("Error al listar archivos:", e)

# .txt


def contar_palabras_caracteres(ruta_archivo):
    """Cuenta palabras, caracteres (con y sin espacios) en un archivo de texto."""
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
    except Exception as e:
        print("No se pudo abrir el archivo:", e)
        return

    # caracteres con espacios
    chars_con = 0
    for c in contenido:
        chars_con = chars_con + 1

    # caracteres sin espacios
    chars_sin = 0
    for c in contenido:
        if c != ' ' and c != '\n' and c != '\t' and c != '\r':
            chars_sin = chars_sin + 1

    # contar palabras 
    palabras = []
    tmp = ''
    i = 0
    while i < len(contenido):
        ch = contenido[i]
        if ch == ' ' or ch == '\n' or ch == '\t' or ch == '\r':
            if tmp != '':
                palabras.append(tmp)
                tmp = ''
        else:
            tmp = tmp + ch
        i = i + 1
    if tmp != '':
        palabras.append(tmp)

    print("Resultados:")
    print(" - Número de palabras:", len(palabras))
    print(" - Caracteres (con espacios):", chars_con)
    print(" - Caracteres (sin espacios):", chars_sin)

def reemplazar_palabra(ruta_archivo, palabra_buscar, palabra_reemplazo):
    """Reemplaza todas las ocurrencias exactas de palabra_buscar por palabra_reemplazo en el archivo."""
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
    except Exception as e:
        print("No se pudo abrir el archivo:", e)
        return

    # reemplazo simple (sustituye todas las apariciones de la subcadena)
    contenido_nuevo = contenido.replace(palabra_buscar, palabra_reemplazo)

    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as f:
            f.write(contenido_nuevo)
        print("Reemplazo completado y guardado en el mismo archivo.")
    except Exception as e:
        print("No se pudo guardar el archivo:", e)

def histograma_vocales(ruta_archivo):
    """Cuenta ocurrencias de vocales y muestra histograma con matplotlib."""
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
    except Exception as e:
        print("No se pudo abrir el archivo:", e)
        return

    # inicializar conteo de vocales (a,e,i,o,u) minúsculas y mayúsculas
    vocales = ['a','e','i','o','u']
    conteos = [0, 0, 0, 0, 0]
    i = 0
    while i < len(contenido):
        ch = contenido[i]
        ch_lower = ch.lower()
        j = 0
        while j < len(vocales):
            if ch_lower == vocales[j]:
                conteos[j] = conteos[j] + 1
            j = j + 1
        i = i + 1

    # Mostrar en consola
    print("Ocurrencias de vocales:")
    j = 0
    while j < len(vocales):
        print(" -", vocales[j], ":", conteos[j])
        j = j + 1

    # Graficar (histograma de barras)
    plt.figure()
    plt.bar(vocales, conteos)
    plt.title("Ocurrencia de vocales")
    plt.xlabel("Vocal")
    plt.ylabel("Cantidad")
    plt.show()

# ----------------------------
# Funciones para .csv
# ----------------------------

def mostrar_primeras_filas_csv(ruta_archivo, n=15):
    """Muestra las n primeras filas de un CSV (incluye encabezado si existe)."""
    try:
        with open(ruta_archivo, 'r', encoding='utf-8', newline='') as csvfile:
            lector = csv.reader(csvfile)
            fila_num = 0
            for fila in lector:
                fila_num = fila_num + 1
                print(fila)
                if fila_num >= n:
                    break
    except Exception as e:
        print("Error leyendo CSV:", e)

def seleccionar_columna_por_nombre(filas, nombre_columna):
    """Dado un listado de filas (la primera fila es encabezados), devuelve índice de columna o -1."""
    if len(filas) == 0:
        return -1
    encabezado = filas[0]
    idx = 0
    while idx < len(encabezado):
        if encabezado[idx] == nombre_columna:
            return idx
        idx = idx + 1
    return -1

def calcular_estadisticas_csv(ruta_archivo, nombre_columna):
    """Calcula conteo, promedio, mediana, desviación estándar, max y min para una columna numérica."""
    try:
        with open(ruta_archivo, 'r', encoding='utf-8', newline='') as csvfile:
            lector = csv.reader(csvfile)
            filas = []
            for fila in lector:
                filas.append(fila)
    except Exception as e:
        print("Error leyendo CSV:", e)
        return None

    if len(filas) == 0:
        print("CSV vacío.")
        return None

    idx = seleccionar_columna_por_nombre(filas, nombre_columna)
    if idx == -1:
        print("No se encontró la columna:", nombre_columna)
        return None

    # Extraer valores numéricos (ignoramos filas con datos no numéricos)
    valores = []
    fila_i = 1  # comenzar después del encabezado
    while fila_i < len(filas):
        fila = filas[fila_i]
        # comprobar que la fila tenga suficiente columnas
        if idx < len(fila):
            celda = fila[idx].strip()
            if celda != '':
                # intentar convertir a float
                try:
                    val = float(celda)
                    valores.append(val)
                except:
                    # ignorar valor si no es numérico
                    pass
        fila_i = fila_i + 1

    if len(valores) == 0:
        print("No se hallaron valores numéricos en la columna seleccionada.")
        return None

    # conteo
    n = 0
    i = 0
    while i < len(valores):
        n = n + 1
        i = i + 1

    # promedio
    suma = 0.0
    i = 0
    while i < len(valores):
        suma = suma + valores[i]
        i = i + 1
    promedio = suma / n

    # ordenar para mediana, min y max
    valores.sort()
    minimo = valores[0]
    maximo = valores[len(valores) - 1]

    # mediana
    if n % 2 == 1:
        medio = (n // 2)
        mediana = valores[medio]
    else:
        medio1 = (n // 2) - 1
        medio2 = (n // 2)
        mediana = (valores[medio1] + valores[medio2]) / 2.0

    # desviación estándar (poblacional)
    suma_cuad = 0.0
    i = 0
    while i < len(valores):
        diff = valores[i] - promedio
        suma_cuad = suma_cuad + (diff * diff)
        i = i + 1
    varianza = suma_cuad / n
    desviacion = math.sqrt(varianza)

    resultados = {
        'count': n,
        'mean': promedio,
        'median': mediana,
        'std': desviacion,
        'min': minimo,
        'max': maximo
    }
    return resultados

def graficar_columna_csv(ruta_archivo, nombre_columna):
    """Grafica la columna seleccionada como scatter. Además intenta reordenar otra columna para hacer un gráfico de barras."""
    try:
        with open(ruta_archivo, 'r', encoding='utf-8', newline='') as csvfile:
            lector = csv.reader(csvfile)
            filas = []
            for fila in lector:
                filas.append(fila)
    except Exception as e:
        print("Error leyendo CSV:", e)
        return

    if len(filas) == 0:
        print("CSV vacío.")
        return

    idx = seleccionar_columna_por_nombre(filas, nombre_columna)
    if idx == -1:
        print("No se encontró la columna:", nombre_columna)
        return

    # Extraer valores numéricos y su índice (para eje X)
    valores = []
    indices = []
    fila_i = 1
    contador = 0
    while fila_i < len(filas):
        fila = filas[fila_i]
        if idx < len(fila):
            celda = fila[idx].strip()
            if celda != '':
                try:
                    val = float(celda)
                    valores.append(val)
                    indices.append(contador)
                    contador = contador + 1
                except:
                    pass
        fila_i = fila_i + 1

    if len(valores) == 0:
        print("No se hallaron valores numéricos en la columna seleccionada.")
        return

    # pedir color y título al usuario
    titulo = input("Ingrese el título para la gráfica (o presione Enter para título por defecto): ")
    if titulo.strip() == '':
        titulo = "Dispersión de " + nombre_columna
    eje_x = input("Nombre del eje X (Enter para 'Índice'):")
    if eje_x.strip() == '':
        eje_x = "Índice"
    eje_y = input("Nombre del eje Y (Enter para nombre de la columna):")
    if eje_y.strip() == '':
        eje_y = nombre_columna
    color = input("Ingrese código o nombre de color para los puntos (ej. 'red' o '#00ff00') o presione Enter para 'blue': ")
    if color.strip() == '':
        color = 'blue'

    # Graficar scatter
    plt.figure()
    plt.scatter(indices, valores, c=color)
    plt.title(titulo)
    plt.xlabel(eje_x)
    plt.ylabel(eje_y)
    plt.show()

    # Intentar reorganizar otra columna para gráfico de barras:
    print("\nAhora se intentará generar un gráfico de barras usando otra columna (frecuencia de categorías).")
    otra_col = input("Ingrese el nombre de la otra columna (por ejemplo, una columna categórica) (o Enter para omitir): ")
    if otra_col.strip() == '':
        print("Se omitió el gráfico de barras.")
        return

    idx2 = seleccionar_columna_por_nombre(filas, otra_col)
    if idx2 == -1:
        print("No se encontró la columna:", otra_col)
        return

    # Contar frecuencias por valores únicos en la otra columna
    frecuencias = {}
    fila_i = 1
    while fila_i < len(filas):
        fila = filas[fila_i]
        if idx2 < len(fila):
            valcat = filas[fila_i][idx2].strip()
            if valcat != '':
                if valcat in frecuencias:
                    frecuencias[valcat] = frecuencias[valcat] + 1
                else:
                    frecuencias[valcat] = 1
        fila_i = fila_i + 1

    # preparar listas para graficar (ordenar por clave para consistencia)
    categorias = []
    cuentas = []
    for clave in frecuencias:
        categorias.append(clave)
        cuentas.append(frecuencias[clave])

    if len(categorias) == 0:
        print("No se hallaron categorías para graficar.")
        return

    # Graficar barras
    plt.figure()
    plt.bar(categorias, cuentas)
    plt.title("Frecuencia de " + otra_col)
    plt.xlabel(otra_col)
    plt.ylabel("Frecuencia")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# ----------------------------
# Menús
# ----------------------------

def submenu_txt(ruta):
    while True:
        print("\n--- Submenú .txt ---")
        print("Archivo cargado:", ruta)
        print("1. Contar número de palabras y caracteres")
        print("2. Reemplazar una palabra por otra")
        print("3. Histograma de ocurrencia de las vocales")
        print("4. Volver al menú principal")
        opcion = input("Elija una opción: ").strip()
        if opcion == '1':
            contar_palabras_caracteres(ruta)
        elif opcion == '2':
            palabra_buscar = input("Palabra a buscar: ")
            palabra_reemplazo = input("Palabra reemplazo: ")
            reemplazar_palabra(ruta, palabra_buscar, palabra_reemplazo)
        elif opcion == '3':
            histograma_vocales(ruta)
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def submenu_csv(ruta):
    while True:
        print("\n--- Submenú .csv ---")
        print("Archivo cargado:", ruta)
        print("1. Mostrar las 15 primeras filas")
        print("2. Calcular estadísticas de una columna")
        print("3. Graficar una columna completa")
        print("4. Volver al menú principal")
        opcion = input("Elija una opción: ").strip()
        if opcion == '1':
            mostrar_primeras_filas_csv(ruta, 15)
        elif opcion == '2':
            nombre_col = input("Ingrese el nombre exacto de la columna (encabezado): ")
            res = calcular_estadisticas_csv(ruta, nombre_col)
            if res is not None:
                print("Resultados estadísticos para columna:", nombre_col)
                print(" - Count:", res['count'])
                print(" - Mean :", res['mean'])
                print(" - Median:", res['median'])
                print(" - Std  :", res['std'])
                print(" - Min  :", res['min'])
                print(" - Max  :", res['max'])
        elif opcion == '3':
            nombre_col = input("Ingrese el nombre exacto de la columna a graficar: ")
            graficar_columna_csv(ruta, nombre_col)
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def main():
 
    print("=== Aplicación CLI de Análisis y Graficación (Unidad 5) ===")

    while True:
        print("\nMenú Principal")
        print("1. Listar archivos en la ruta actual o ingresar una ruta")
        print("2. Procesar archivo de texto (.txt)")
        print("3. Procesar archivo separado por comas (.csv)")
        print("4. Salir")

        opcion = input("Elija una opción: ").strip()

        if opcion == '1':
            ruta = input("Ingrese ruta (Enter para ruta actual): ").strip()
            listar_archivos(ruta)

        elif opcion == '2':
            print("\nSe abrirá automáticamente el archivo de texto predeterminado:", ARCHIVO_TXT)
            submenu_txt(ARCHIVO_TXT)

        elif opcion == '3':
            print("\nSe abrirá automáticamente el archivo CSV predeterminado:", ARCHIVO_CSV)
            submenu_csv(ARCHIVO_CSV)

        elif opcion == '4':
            print("Saliendo. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()