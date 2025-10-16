#1. Abrir el archivo
fp = open("C:\\Users\\migue\\OneDrive\\Desktop")
#2. Leer el archivo
#datos = fp.read(20)
#datos = fp.read()
#fp.readline(5)
#datos = fp.readline(7)
#3 Cerrar el archivo

for linea in fp:
    print(linea,end="")

fp.close()

print(datos)
          