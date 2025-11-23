'''
Dados dos números calcule la suma de todos los números que hay entre los dos números (ambos incluídos)
'''
print("Dados dos números calcule la suma de todos los números que hay entre los dos números (ambos incluídos)")

n1=int(input("Ingresa el primer número: "))
n2=int(input("Ingresa el segundo número: "))

s=0

for i in range (n1,n2+1):
    s=s+i

print(f"El resultado de la suma es: {s}")