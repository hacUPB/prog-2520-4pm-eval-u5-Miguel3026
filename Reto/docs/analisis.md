# Analisis del reto 

## 1. Manejo de archivos

El programa realiza la lectura y escritura de archivos de texto (.txt) y CSV (.csv) utilizando las siguientes funciones: 

- Se usa open() con modos "r" y "w" para leer y escribir archivos.

- En los archivos CSV se utiliza el módulo csv para procesar los datos de manera estructurada.

- Se emplean bloques try-except para manejar errores como archivos inexistentes o rutas incorrectas, evitando interrupciones del programa.

## 2. Estructuras de control

Se implementan condicionales (if, elif, else) para controlar el flujo del programa.
Los bucles while permiten mantener activo el menú hasta que el usuario elija salir.
También se utiliza el control de excepciones (try-except) para validar entradas del usuario y errores.

## 3. Funciones y modularidad

El código está dividido en funciones independientes, lo que hace que sea mas practico y manejable:

Funciones específicas para archivos .txt: contar_palabras_y_caracteres, reemplazar_palabra, histograma_vocales.

Funciones para archivos .csv: mostrar_primeras_filas, calcular_estadisticas, graficar_columna.

Menús organizados en funciones: submenu_txt, submenu_csv, y main.



## 4. Estructuras de datos

- Se emplean listas y diccionarios para almacenar y procesar información:

- En el conteo de vocales se usa una lista (vocales = ['a','e','i','o','u']) y se recorren con ciclos for.

- En los archivos CSV, los datos numéricos se guardan en listas para calcular promedio, mediana y desviación estándar.

- En la función graficar_columna, se usa un diccionario para agrupar valores por rangos.

## 5. Librerías externas y matemáticas

- Se usa el módulo math para calcular la desviación estándar.

- matplotlib.pyplot permite generar gráficos de dispersión, barras e histogramas.


## 6. Interacción con el usuario

El programa utiliza entradas por consola (input()) y menús interactivos para que el usuario elija acciones o columnas a analizar.
Los resultados se muestran en pantalla.

## 7. Otras prácticas

- Se incluye manejo de errores (FileNotFoundError, ValueError, IndexError).

- Se utiliza codificación UTF-8 para evitar problemas con acentos o caracteres especiales.

- El código es comentado y organizado por secciones (TXT, CSV, Menús), dandole claridad y orden.