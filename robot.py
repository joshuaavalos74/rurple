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

	def dibujar(self):
		if self.direccion == 'UP':
			return "^"
		elif self.direccion == 'RIGHT':
			return ""

	# def mover (self):
	# 	if self.direccion == ">":
	# 		self.x= x+1
	# 	elif self.direccion == "UP":
	# 		self.y = y+1
	# 	elif self.direccion == "<":
	# 		self.x = x-1
	# 	elif self.direccion == "v":
	# 		self.y = y-1	

			



		


		