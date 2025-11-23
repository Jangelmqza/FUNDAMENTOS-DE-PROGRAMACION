'''
    programa que lee n números y los suma para obteener su promedio
'''
n=int(input("¿De cuantos numeros deseas sacar el promedio? "))
p=0
for i in range (n):
    d=float(input("Ingresa el primer dato: "))
    p=p+d
p=p/n
print(f"El promedio es de: {p}")