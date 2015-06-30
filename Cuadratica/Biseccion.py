import os
import funcXr
import caso2
import funcXr2
import caso1

os.system('clear')

print("\n		    Elije una forma de ingresar los datos\n")
print(" 				1. ax^2+bx+c \n\n 				2. (ax+b)^2+c")
opcion = int(input("OPCION: "))


if opcion == 1:
	
	caso1.metodo_1()
	
elif opcion == 2:
	
	caso2.metodo_2()

else:
	print("Introduce una funcion valida")
