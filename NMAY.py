'''
    Programa que lee n números e indica cual es el mayor
'''
n=int(input("¿Cuantos numeros va a ingresar? "))
n3=0

for i in range (n):
    n2=int(input("Ingrese un número: "))
    if n2>=n3:
        n3=n2
print(f"El número mayor es: {n3}")