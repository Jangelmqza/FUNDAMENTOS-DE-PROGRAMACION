import math

print("Programa que calcula el resultado de una ecuación cuadratica\n")
a=float(input("Ingresa el valor de a: "))
b=float(input("\nIngresa el valor de b: "))
c=float(input("\nIngresa el valor de c: "))

D=b**2-4*a*c

if D>0:
    x11=-b+math.sqrt(D)
    x1=x11/(2*a)
    x22=-b-math.sqrt(D)
    x2=x22/(2*a)
    print(f"\nLos valores de x pueden ser: x1= {x1}, x2= {x2}")
else:
    print("El resultado en los reales no existe")