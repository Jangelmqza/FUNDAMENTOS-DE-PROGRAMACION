'''
    Programa que pide 3 calificaciones y suma las dos mas altas
'''

c1=float(input("Ingresa tu primera calificación: "))
c2=float(input("\nIngresa tu segunda calificación: "))
c3=float(input("\nIngresa la tercera calificación: "))

if c1>=c2 and c2>=c3:
    s1=c1+c2
    print(f"El resultado de la suma es {s1}")

elif c3>=c2 and c1>=c2:
    s3=c1+c3
    print(f"El resultado de la suma es {s3}")
    
else:
    s4=c2+c3
    print(f"El resultado de la suna es {s4}")


