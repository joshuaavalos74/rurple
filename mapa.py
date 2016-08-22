def cargar_mapas(mapa):
	mapas=[]
	ma=open(mapa,"r")	
	for linea in ma:
		g=list(linea.strip())
		mapas.append(g)
	ma.close()	
	return mapas
	
