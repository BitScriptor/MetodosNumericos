def raiz(fxl,fxu, fa, fb, fc, fk, fcoordenadaX):#deficion de la funcion que itilizaremos para el caso
	
	centinela1=0.0#declaracion de variables locales
	centinela2=1.0
	
	while (round(centinela1, 4) != round(centinela2, 4)):#damos el numero de iteracion hasta que los tres numeros despues del punto sean estaticos
	
		fxr = (fxl + fxu)/2#sacamos el promedio
		
		subint = ((fk*(((fa*fxl)+fb)**2)+fc))  *  ((fk*(((fa*fxr)+fb)**2)+fc))#determinamos el subintervalo
		
		if(subint < 0):#condicon: si el subintervalo es negativo cambiamos los valores de fxu por los de fxr
			
			fxu=fxr
			
		elif (subint>0):#condicion: si el subintervalo es positivo cambiamos los valores de fxl por los de fxr
			
			fxl=fxr
			
		else:#si el subintervalo es 0, obtuvimos la raiz
			
			print("				La raiz es: " + str(fxr))
			
		centinela2 = centinela1#variables para comparar los valores de los 3 numeros despues del punto.
		centinela1 = fxr
		
		print ("			         " + str(round(fxr, 5)) + "  y   " + str(round(((fcoordenadaX - fxr) + fcoordenadaX),5)))#imprimimos las raices.
		
	
