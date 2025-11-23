#Programa que calcula la distancia entre dos puntos
import math 
print("Programa que calcula la distancia entre dos puntos")
x1=float(input("Ingresa el primer valor de x: \n"))
x2=float(input("Ingresa el segundo valor de x: \n"))
y1=float(input("Ingresa el primer valor de y: \n"))
y2=float(input("Ingres el segundo valor de y: \n"))

D = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"La distancia entre los puntos es de {D}")

#Creado por Jose Angel Márquez Ramírez


