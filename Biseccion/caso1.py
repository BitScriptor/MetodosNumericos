import funcXr2
import os

a=0
b=0
c=0


def metodo_1():
	
	os.system('clear')#limpiar la consola
	print ("\n		      **********  (ax^2 + bx + c  **********\n")#tipo de funcion elegido
	print("		  Introduce los valores de 'a' , 'b' y 'c'\n")
	
	a = float (input("			   a: "))#peticion de variables
	b = float (input("			   b: "))
	c = float (input("			   c: "))
	
	
	discriminante = (b**2 - (4 * a * c))#Determinacion del discriminante
	
	coordenadaX = ((b*-1)/(a*2))#determinacion de coordenada x
	coordenadaY = ((a*(coordenadaX**2)) + (b * coordenadaX) + c)#determinacion de coordenada y

		
	if discriminante < 0:#condicion:  si el determinante es menor que 0 las raices no son reales.
		
		print("\n\n			   El discriminante es: " + str(discriminante))
		print("\n 	    	    Por lo tanto no tiene raices reales.\n\n\n")
		print("	   Vertice: (" + str(coordenadaX) + "," + str(coordenadaY) + ")	    Interseccion con el eje 'Y' en: "+ str(c))#imprime la coordenada del vertice y la inter. con Y
		
	elif discriminante == 0:#condicion: si el discriminante es 0 la raiz se encuentra en el vertice
		
		print("\n\n				La raiz es: " + str(b*-1))#
		print ("\n		     Pues el vertice se encuentra en el eje 'X'\n\n\n")
		print("	   Vertice: (" + str(coordenadaX) + "," + str(coordenadaY) + ")	    Interseccion con el eje 'Y' en: "+ str(c))#imprime la coordenada del vertice y la inter. con Y
		
	else: #condicion : para todos los demas casos en quel el discriminante es mayor que 0

		
		xl=0.0 #Asignacion de valores a las variables que utilizaremos
		xu=coordenadaX
		
		print("	   Vertice: (" + str(coordenadaX) + "," + str(coordenadaY) + ")	    Interseccion con el eje 'Y' en: "+ str(c))
		 
		comp = ((a*(xl)**2) + (b*xl) + c)  *  ((a*(xu)**2) + (b*xu) + c)  #F(xl) * F(xu) comprobacion para determinar si hay cambio de sigo y saber si la raiz
                #                                                                       se encuentra dentro del intervalo establecido
		if(comp > 0):#condicion: si la comprobacion es mayor que 0, procedemos a buscar otro intervalo pues necesitamos que sea negativa
			
			while(comp > 0):# mientras la comprobacon siga siendo mayor que 0, seguimos el ciclo.
	
				xl = (xl+(2*xu)+1)#aumentamos la variable xl para que la comprobacion cambie su valor
				comp = ((a*(xl**2)) + (b*xl) + c)  *  ((a*(xu**2)) + (b*xu) + c)#volvemos a hacer la comprobacion
				
			funcXr2.raiz(xl, xu, a, b, c, coordenadaX)#una vez que la comprobacion es negativa usamos la funcion para determinar la raiz.
		
		else:#condicion: si la comprobacion es menor que 0.
					
			print("			La comprobacion es: " + str(comp))
		
			print("\n	    Por lo tanto la raiz si esta dentro del intervalo (" + str(coordenadaX) + "," + str(coordenadaY) + ")\n")
			
			funcXr2.raiz(xl, xu, a, b, c, coordenadaX)# uso de la funcion para determinar la raiz
			
			print("\n\n\n")

