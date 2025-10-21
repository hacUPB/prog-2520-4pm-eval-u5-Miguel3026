#1. Abrir el archivo
fp = open("C:\\Users\\migue\\OneDrive\\Desktop\\archivo_1""r")
#2. Leer el archivo
#datos = fp.read(20)
#datos = fp.read()
#fp.readline(5)
#datos = fp.readline(7)
#3 Cerrar el archivo
#cadena = "hola"
#cadena[1]
for linea in fp:
    print(linea[0],end="")

fp.close()

#print(datos)
          