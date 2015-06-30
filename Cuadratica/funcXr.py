def raiz(fxl,fxu, fa, fb, fc, fk, fcoordenadaX):
	
	centinela1=0.0
	centinela2=1.0
	
	while (round(centinela1, 4) != round(centinela2, 4)):
	
		fxr = (fxl + fxu)/2
		
		subint = ((fk*(((fa*fxl)+fb)**2)+fc))  *  ((fk*(((fa*fxr)+fb)**2)+fc))
		
		if(subint < 0):
			
			fxu=fxr
			
		elif (subint>0):
			
			fxl=fxr
			
		else:
			
			print("				La raiz es: " + str(fxr))
			
		centinela2 = centinela1
		centinela1 = fxr
		
		print ("			         " + str(round(fxr, 5)) + "  y   " + str(round(((fcoordenadaX - fxr) + fcoordenadaX),5)))
		
	
