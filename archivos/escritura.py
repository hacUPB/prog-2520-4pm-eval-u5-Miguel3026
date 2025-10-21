ruta = "C:\\Users\\migue\\Downloads"
#\ secuencia de escape: \n \t \--> \\
file_name = "aviones1.txt"
modo = "x"

fp = open(ruta+"\\"+file_name, modo, encoding="utf-8")
nombre = input("Ingresee el nombre de un avión: ")
peso = int(input("Ingrese el peso del avión: "))
velocidad = float(input("velocidad maxima: "))
fp.write(nombre+"\n")
fp.write(str(peso)) #Los argumentos de write deben ser str 
fp.write("\n")
fp.write(str(velocidad)+"\n") 
#fp.whrite(nombre+"\n"+peso+"\n"+velocidad)
fp.close()
