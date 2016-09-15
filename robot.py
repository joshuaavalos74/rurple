class Robot(object):
	def __init__(self, x, y):
		self.x=x
		self.y=y
		self.monedas=0
		self.direccion= "^"
		self.mapa= None

	def asignar_mapa(self, mapa):
		self.mapa = mapa

	def rotar (self):
		if self.direccion == "^":
			self.direccion = ">"
		elif self.direccion == ">":
			self.direccion = "v"
		elif self.direccion == "v":
			self.direccion = "<"
		else:
			self.direccion = "^"	

	def mover (self):
	 	if self.direccion == ">":
	 		self.x+=1
	 	elif self.direccion == "^":
	 		self.y-=1 
	 	elif self.direccion == "<":
	 		self.x-=1
	 	elif self.direccion == "v":
	 		self.y+=1

	
	def pick (self, x, y):
		if self.contar_monedas_mapa(self.x, self.y) > 0:
			self.monedas +=1
			self.mapa.sacar_moneda_mapa(x,y)

	def dibujar (self):
		return self.direccion		







		


		







		


		