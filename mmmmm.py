def cargar_mapas(mapa):
	mapasas=[]
	j= open(mapa, "r")	
	for linea in j:
		o=list(linea.strip())
		mapasas.append(o)
	return mapasas
	j.close()	


	def crear_robot(self):
		self.robot=robot
	def agregar_monedas(self, monedasas):
		self.monedas.append(monedasas)	