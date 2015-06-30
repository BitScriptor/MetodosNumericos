import funcXr
import os

a=0
b=0
c=0
k=0


def metodo_2():
	
	os.system('clear')#limpiar la consola
	print ("\n		      **********  (ax+b)^2+c  **********\n")#tipo de funcion elegido
	print("		  Introduce los valores de 'a' , 'b' y 'c'\n")
	a = float(input("			   a: "))#peticion de variables
	b = input("			   b: ")
	c = input("			   c: ")
	k = input(" 	   Abre hacia arriba '1' , si abre hacia abajo '-1': ")
	
	xl=0.0#asignacion de variables
	xu=(b*-1.0)
	coordenadaX = ((b*-1)/a)#determinacion de coordenada x
	
	
	discriminante = ( (4 * k * (a**2) * c) * -1)#Determinacion del discriminante
		
	if discriminante < 0:#condicion:  si el determinante es menor que 0 las raices no son reales.
		
		print("\n\n			   El discriminante es: " + str(discriminante))
		print("\n 	    	    Por lo tanto no tiene raices reales.\n")
		print("	   Vertice: (" + str((b*-1)/a) + "," + str(c) + ")	    Interseccion con el eje 'Y' en: "+ str((b**2 + c)))
		print("\n\n\n")
		
	elif discriminante == 0:#condicion: si el discriminante es 0 la raiz se encuentra en el vertice
		
		print("\n\n				La raiz es: " + str(b*-1))
		print ("\n		     Pues el vertice se encuentra en el eje 'X'\n")
		print("	   Vertice: (" + str((b*-1)/a) + "," + str(c) + ")	    Interseccion con el eje 'Y' en: "+ str((b**2 + c)))
		print("\n\n\n")
		
	else:#condicion : para todos los demas casos en quel el discriminante es mayor que 0
		
		print("	   Vertice: (" + str((b*-1)/a) + "," + str(c) + ")	    Interseccion con el eje 'Y' en: "+ str((b**2 + c)))

		comp = ((k*(((a*xl) + (b*xl))**2)+c) * (k*(((a*xu) + (b*xu))**2)+c))#F(xl) * F(xu) comprobacion para determinar si hay cambio de sigo y saber si la raiz
		#                                                                       se encuentra dentro del intervalo establecido
		if(comp > 0):#condicion: si la comprobacion es mayor que 0, procedemos a buscar otro intervalo pues necesitamos que sea negativa
			
			while(comp > 0):# mientras la comprobacon siga siendo mayor que 0, seguimos el ciclo.
				
				xl = (xl+(2*xu)+1)#aumentamos la variable xl para que la comprobacion cambie su valor
				comp = ((k*(((a*xl) + b)**2)+c)  *  (k*(((a*xu) + b)**2)+c))#volvemos a hacer la comprobacion
				
			funcXr.raiz(xl, xu, a, b, c, k, coordenadaX)#una vez que la comprobacion es negativa usamos la funcion para determinar la raiz.
		
		else:#condicion: si la comprobacion es menor que 0.
					
			print("\n     Funcion desarrollada: (x^2 + " + str(b*2) + "x " + "+ " + str((b**2)+c) + ")	La comprobacion es: " + str(comp))
		
			print("\n	    Por lo tanto la raiz si esta dentro del intervalo (0," + str(b*-1) + ")\n")
		
			
			funcXr.raiz(xl, xu, a, b, c, k, coordenadaX)# uso de la funcion para determinar la raiz
			
		print("\n\n\n")
