class Mapa(object):
	def __init__(self, altura, ancho):
		self.ancho=ancho
		self.altura=altura
		self.monedas=[]
		self.robot=None

	def crear_robot(self):
		self.robot=robot
	def agregar_monedas(self, monedasas):
		self.monedas.append(monedasas)	

	def dibujar_mapa(self):
		for y in (self.altura):
			for x in (self.ancho):
				if x == self.robot.x and y == self.robot.y:
					res= self.robot.dibujar()
				elif contar_monedas_mapa(x,y) > 0:
					res = self.contar_monedas_mapa (x,y)
				else:
					res= " "
			res+= "\n"
		return res
	def contar_monedas_mapa(self, x, y):
		mon=0
		for moneda in self.monedas:
			if moneda.x == x and moneda.y== y:
				mon+=1
		return mon		 

			
	def sacar_moneda(self, x, y):
		if self.robot.x == x and self.robot.y == y:
			self.x= -1
			self.y= -1					