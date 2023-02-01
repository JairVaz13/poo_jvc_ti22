"""
programa1
nombre: jair vazquez cordero
fecha: 31/01/2023
descripcion:calcular en area y perimero de un cierculo y cuadrado
"""
import math
r=float(input("Ingrese el radio:"))
circumference=2*math.pi*r
area=math.pi*r*r
sarea=4*math.pi*r*r
volume=4/3*math.pi*r**3
print ( "Circunferencia:% .2f" % circumference)
print ( "Área del círculo:% .2f"% area)
print ( "Área de superficie de la bola:% .2f"% sarea)
print ( "Volumen de bola:% .2f" % volume)


