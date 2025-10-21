lista = ["great balls of fire", "un beso y una flor", "fly love", 
         "another day in paradise", "never enough"]
ruta = "C:\\Users\\migue\\Downloads"
#\ secuencia de escape: \n \t \--> \\
file_name = "canciones.txt"
file_info = ruta + "\\" + file_name
modo = "w"

#for i in range(len(lista)):
   # lista[i] += "\n"

#print(lista)

fp = open(file_info, modo, encoding="utf-8")
#fp.writelines(lista)
for cancion in lista:
    fp.write(cancion + "\n")
fp.close()