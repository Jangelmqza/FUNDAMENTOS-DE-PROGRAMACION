'''Dados dos numeros calcule la suma de todos los numeros que hay entre los dos número, ambos incluidos'''
print("Dados dos números calcule la suma de todos los números que hay entre los dos números (ambos incluídos)")

n1=int(input("Ingresa el primer número: "))
n2=int(input("Ingresa el segundo número: "))

s=0
na=n1
while (na<=n2):
    s=s+na
    na+=1
print(f"El resultado de la suma es: {s}")