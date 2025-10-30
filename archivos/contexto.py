lista = ["great balls of fire", "un beso y una flor", "fly love", 
         "another day in paradise", "never enough"]
ruta = "C:\\Users\\migue\\Downloads"
#\ secuencia de escape: \n \t \--> \\
file_name = "canciones.txt"
file_info = ruta + "\\" + file_name
modo = "w"
with open(file_info, modo, encoding="utf-8") as archivo:
    #hacer operaciones con el archivo
    for dato in archivo:
        print(dato, end="---")

#El archivo se cierra automaticamente al salir del bloque with
