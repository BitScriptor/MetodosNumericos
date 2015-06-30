#!/usr/bin/python

from sympy import *

x = Symbol('x')
ejex=[]
ejey=[]
xmedia = 0.0
ymedia = 0.0
b1num = 0.0
b1den = 0.0

datosx = input("Cuantos datos insertaras?: ")

for i in range (0,datosx):
	columna1 = input("Introduce el dato %d de la primer columna: " %i)
	columna2 = input("Introduce el valor del dato anterior: ")
	print "\n"
	
	ejex.append(columna1)
	ejey.append(columna2)

print "\n\t\tEJE X			EJE Y \n\n"

for i in range (len(ejex)):
	print "\t\t", ejex[i],"\t\t\t", ejey[i],"\n\n"

for i in range(len(ejex)):
	xmedia = (xmedia + ejex[i])
	ymedia = (ymedia + ejey[i])

xmediat = xmedia / len(ejex)
ymediat = ymedia / len(ejex)

print "\nLa media de x es: ", xmediat, "\n\n"
print "La media de y es: ", ymediat, "\n\n"

for i in range(len(ejex)):
	b1num = b1num + (ejex[i] - xmediat) * (ejey[i] - ymediat)
	b1den = b1den + (ejex[i] - xmediat)**2

b1 = (b1num) / (b1den)
b0 = (ymediat -(b1*xmediat))
y = b0 + (b1*x)

print "El valor de b1 es: ", b1, "\n\n"
print "El valor de b0 es: ", b0, "\n\n"
print "La formula es: \t\t y = ", y, "\n\n\n"
