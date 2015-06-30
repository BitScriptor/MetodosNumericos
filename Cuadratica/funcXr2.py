def raiz(fxl,fxu, fa, fb, fc, fcoordenadaX):
	
	centinela1=0.0
	centinela2=1.0
	
	while (round(centinela1, 4) != round(centinela2, 4)):
	
		fxr = (fxl + fxu)/2
		
		subint = ((fa*(fxl**2)) + (fb*fxl) + fc)  *  ((fa*(fxr**2)) + (fb*fxr) + fc)
		
		if(subint < 0):
			
			fxu=fxr
			
		elif (subint>0):
			
			fxl=fxr
			
		else:
			
			print("				La raiz es: " + str(fxr))
			
		centinela2 = centinela1
		centinela1 = fxr
		
		print ("			         " + str(round(fxr, 5)) + "  y  " + str(round(((fcoordenadaX - fxr) + fcoordenadaX),5)))
		
	
