def cargar_instrucciones(instruccion):
	instruccioneses=[]
	ins=open(instruccion,"r")
	for linea in ins:
		h=(linea.strip())
		instruccioneses.append(h)
	ins.close()	
	return instruccioneses
		