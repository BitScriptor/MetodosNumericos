import funcXr2
import os

a=0
b=0
c=0


def metodo_1():
	
	os.system('clear')
	print ("\n		      **********  (ax^2 + bx + c  **********\n")
	print("		  Introduce los valores de 'a' , 'b' y 'c'\n")
	
	a = float (input("			   a: "))
	b = float (input("			   b: "))
	c = float (input("			   c: "))
	
	
	discriminante = (b**2 - (4 * a * c))
	
	coordenadaX = ((b*-1)/(a*2))
	coordenadaY = ((a*(coordenadaX**2)) + (b * coordenadaX) + c)

		
	if discriminante < 0:
		
		print("\n\n			   El discriminante es: " + str(discriminante))
		print("\n 	    	    Por lo tanto no tiene raices reales.\n\n\n")
		print("	   Vertice: (" + str(coordenadaX) + "," + str(coordenadaY) + ")	    Interseccion con el eje 'Y' en: "+ str(c))
		
	elif discriminante == 0:
		
		print("\n\n				La raiz es: " + str(b*-1))#
		print ("\n		     Pues el vertice se encuentra en el eje 'X'\n\n\n")
		print("	   Vertice: (" + str(coordenadaX) + "," + str(coordenadaY) + ")	    Interseccion con el eje 'Y' en: "+ str(c))
		
	else:

		
		xl=0.0
		xu=coordenadaX
		
		print("	   Vertice: (" + str(coordenadaX) + "," + str(coordenadaY) + ")	    Interseccion con el eje 'Y' en: "+ str(c))
		 
		comp = ((a*(xl)**2) + (b*xl) + c)  *  ((a*(xu)**2) + (b*xu) + c)  #F(xl) * F(xu)
		
		if(comp > 0):
			
			while(comp > 0):
	
				xl = (xl+(2*xu)+1)
				comp = ((a*(xl**2)) + (b*xl) + c)  *  ((a*(xu**2)) + (b*xu) + c)
				
			funcXr2.raiz(xl, xu, a, b, c, coordenadaX)
		
		else:
					
			print("			La comprobacion es: " + str(comp))
		
			print("\n	    Por lo tanto la raiz si esta dentro del intervalo (" + str(coordenadaX) + "," + str(coordenadaY) + ")\n")
			
			funcXr2.raiz(xl, xu, a, b, c, coordenadaX)
			
			print("\n\n\n")

