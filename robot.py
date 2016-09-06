class Robot(object):
	def __init__(self, x, y):
		self.x=x
		self.y=y
		self.monedas=0
		self.direccion= "UP"
		self.mapa= None

	def asignar_mapa(self, mapa):
		self.mapa = mapa

	def rotar (self):
		if self.direccion == "UP":
			self.direccion = "RIGHT"
		elif self.direccion == "RIGHT":
			self.direccion = "DOWN"
		elif self.direccion == "DOWN":
			self.direccion = "LEFT"
		else:
			self.direccion = "UP"

	def dibujar_rotar (self):
		if self.direccion == 'UP':
			return "^"
		elif self.direccion == 'RIGHT':
			return ">"
		elif self.direccion == 'LEFT':
			return "<"
		else:
			return "v"		

	 def mover (self):
	 	if self.direccion == ">":
	 		self.x += 1
	 	elif self.direccion == "^":
	 		self.y -= 1 
	 	elif self.direccion == "<":
	 		self.x -= 1
	 	elif self.direccion == "v":
			self.y += 1

	
	def pick (self, x, y):
		if self.contar_monedas_mapa(self.x, self.y) > 0:
			self.monedas +=1
			self.mapa.remover_moneda_mapa(x,y)
			







		


		