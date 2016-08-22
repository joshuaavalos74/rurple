instruccioneses=[]
def cargar_instrucciones(instruccion):
	ins=open("Instrucciones/instructions.txt")
	for linea in ins:
		h=list(linea.strip())
		instruccioneses.append(h)
	return instruccioneses
	ins.close	