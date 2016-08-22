instruccioneses=[]
def cargar_instrucciones(instruccion):
	ins=open(instruccion)
	for linea in ins:
		h=list(linea.strip())
		instruccioneses.append(h)
	ins.close()	
	return instruccioneses
		