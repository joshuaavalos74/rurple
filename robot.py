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

	def dibujar (self):
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

	def agregar_monedas(self, moneda):
		for i in self.monedas:
			self.moneda+=1
		return self.monedas.append(moneda)			


	def pick (self, x, y):
		if self.x == x and self.y == y:
			for moneda in self.monedas






		


		