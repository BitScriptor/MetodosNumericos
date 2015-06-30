import os
import funcXr
import caso2
import funcXr2
import caso1

os.system('clear')#limpiamos terminal

print("\n		    Elije una forma de ingresar los datos\n")
print(" 				1. ax^2+bx+c \n\n 				2. (ax+b)^2+c")#menu de opciones
opcion = int(input("OPCION: "))


if opcion == 1:#si la opcion es ax^2+bx+c usamos el metodo1 que esta en el archivo raiz
	
	caso1.metodo_1()#implementacion y llamada al metodo1
	
elif opcion == 2:#si la opcion es (ax+b)^2+c usamos el metodo1 que esta en el archivo raiz
	
	caso2.metodo_2()#implementacion y llamada al metodo2

else:
	print("Introduce una funcion valida")
