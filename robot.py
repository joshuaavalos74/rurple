class Robot():
	def __init__(self, x, y):
		self.x=x
		self.y=y
		self.monedas=0
		self.direccion= "UP"
		self.mapa= None
	def cargar_mapa(self, mapa):
		self.mapa = mapa


	def mover (self):
		if self.direccion == ">":
			self.x 

	def rotar (self):
		if self.direccion == "UP":
			self.direccion = ">"
		elif self.direccion == ">":
			self.direccion = "v"
		elif self.direccion == "v":
			self.direccion = "<"
		elif self.direccion == "<":
			self.direccion = "UP"


		


		