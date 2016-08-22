mapas=[]
def cargar_mapas(mapa):
	ma=open("Mapas/mapa1.txt")	
	for linea in ma:
		g=list(linea.strip())
		mapas.append(g)
	return mapas
	ma.close
