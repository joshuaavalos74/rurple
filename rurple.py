import instrucciones
import mapa
import robot
ins=input("Ingrese las Instrucciones que usara: ")
mui=input("Ingrese que mapa usara: ") 
mapapa=(instrucciones.cargar_mapas(mui))
inst=(instrucciones.cargar_instrucciones(ins))
print (mapapa)



