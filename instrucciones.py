def cargar_instrucciones(instruccion):
	instruccioneses=[]
	ins=open(instruccion,"r")
	for linea in ins:
		h=(linea.strip())
		instruccioneses.append(h)
	ins.close()	
	return instruccioneses
def cargar_mapas(mapa):
	mapasas=[]
	j= open(mapa, "r")	
	for linea in j:
		o=list(linea.strip())
		mapasas.append(o)
	return mapasas
	j.close()		