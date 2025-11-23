'''Programa que lee 10 calificaciones y obtiene su promedio, si es mayor o igual a 7 aprueba y sino reprueba'''
i=1
s=0
while (i<=10):
    n=float(input("Ingrese la calificación: "))
    s=s+n
    i+=1
p=s/10
if p>=7:
    print(f"Usted aprobo con: {p}")
else:
    print(f"Usted reprobo con: {p}")