#! /usr/bin/python

from sympy import * #importacion de libreria especial

ejex=[] #declaracion de variables (listas)
ejey=[]
x = Symbol('x')

numDatos = input("Cuantos datos deseas ingresar?: ") #Peticion de datos al usuario para determinar el tamanio de las listas

for i in range(0, numDatos):
	columna1 = input("Introduce el dato %d datos para la columna X: " %i) #ciclo for para el llenado.
	columna2 = input("Introduce el valor del dato anterior: ")
	
	ejex.append(columna1) #se anexan los datos a las listas
	ejey.append(columna2)

print "\n\n\t\t EJE X \t\t\t EJE Y \n"

for i in range(len(ejex)): #impresion de los datos capturados
	print "\t\t ", ejex[i], "\t\t\t ", ejey[i], "\n"

lp = 1 #Declaracion de nuevas variables
y =0

for i in range(len(ejex)):
	
	for j in range(len(ejex)):  #ciclos for anidados para poder aplicar la formula.
		
		if(j != i): #condicion para que L0 no tome en cuenta cuando j == i
			lp = lp * ((x -ejex[j]) / (ejex[i] - ejex[j]))
			
		else:
			j = j+1
			
	print "\n\t\tL%d = " %i, lp # impresion de las Formulas obtenidas
	
	y = y + (lp * ejey[i]) #sumatoria de del polinomio de LaGrange
	
	lp=1 #Reseteo de la variable para la siguiente iteracion
	
print "\n\nP(x) = ", y #Impresion de P(x)

evaluar = input ("\n\nCon que valor quieres evaluar la funcion?: ")#Solicitud del valor a interpolar
resp = y.evalf(subs = {x:evaluar}) #Sustitucion del valor a interpolar

print "\n\nEl proximo valor podria ser: ", resp #impresion del valor
