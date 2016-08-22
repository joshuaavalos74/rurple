mapas=[]
def cargar_mapas(mapa):
	ma=open(mapa)	
	for linea in ma:
		g=list(linea.strip())
		mapas.append(g)
	ma.close	
	return mapas
	
