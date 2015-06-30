import funcXr
import os

a=0
b=0
c=0
k=0


def metodo_2():
	
	os.system('clear')
	print ("\n		      **********  (ax+b)^2+c  **********\n")
	print("		  Introduce los valores de 'a' , 'b' y 'c'\n")
	a = float(input("			   a: "))
	b = input("			   b: ")
	c = input("			   c: ")
	k = input(" 	   Abre hacia arriba '1' , si abre hacia abajo '-1': ")
	
	xl=0.0
	xu=(b*-1.0)
	coordenadaX = ((b*-1)/a)
	
	
	discriminante = ( (4 * k * (a**2) * c) * -1)
		
	if discriminante < 0:
		
		print("\n\n			   El discriminante es: " + str(discriminante))
		print("\n 	    	    Por lo tanto no tiene raices reales.\n")
		print("	   Vertice: (" + str((b*-1)/a) + "," + str(c) + ")	    Interseccion con el eje 'Y' en: "+ str((b**2 + c)))
		print("\n\n\n")
		
	elif discriminante == 0:
		
		print("\n\n				La raiz es: " + str(b*-1))
		print ("\n		     Pues el vertice se encuentra en el eje 'X'\n")
		print("	   Vertice: (" + str((b*-1)/a) + "," + str(c) + ")	    Interseccion con el eje 'Y' en: "+ str((b**2 + c)))
		print("\n\n\n")
		
	else:
		
		print("	   Vertice: (" + str((b*-1)/a) + "," + str(c) + ")	    Interseccion con el eje 'Y' en: "+ str((b**2 + c)))

		comp = ((k*(((a*xl) + (b*xl))**2)+c) * (k*(((a*xu) + (b*xu))**2)+c))  #F(xl) * F(xu)
		
		if(comp > 0):
			
			while(comp > 0):
				
				xl = (xl+(2*xu)+1)
				comp = ((k*(((a*xl) + b)**2)+c)  *  (k*(((a*xu) + b)**2)+c))
				
			funcXr.raiz(xl, xu, a, b, c, k, coordenadaX)
		
		else:
					
			print("\n     Funcion desarrollada: (x^2 + " + str(b*2) + "x " + "+ " + str((b**2)+c) + ")	La comprobacion es: " + str(comp))
		
			print("\n	    Por lo tanto la raiz si esta dentro del intervalo (0," + str(b*-1) + ")\n")
		
			
			funcXr.raiz(xl, xu, a, b, c, k, coordenadaX)
			
		print("\n\n\n")
