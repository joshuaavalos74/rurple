import instrucciones
import mapa
import robot
ins=input("Ingrese las Instrucciones que usara: ")
mui=input("Ingrese que mapa usara: ") 
mapapa=(instrucciones.cargar_mapas(mui))
inst=(instrucciones.cargar_instrucciones(ins))
mapa=Mapa(altura,ancho)
for y in range (len(mapapa)):
	fila = mapapa[y]
	for x in range (len(fila)):
		cas_ver = mapapa[x][y]
		if cas_ver=="*":
			robotses.robot.dibujar(x,y)
			Mapa.crear_robot(x,y)
			Robot.asignar_mapa(x,y)
		else:
			moneds=mapa.contar_monedas_en_mapa	




