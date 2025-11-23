'''Programa que lee los numeros que indique el usuario e indique cuantos son pares y cuantos impares'''

nv=int(input("¿Cuantos números ingresará? "))
i=1
np=0
ni=0

while (i<=nv):
    n=int(input("Ingresa un número: "))
    if n%2==0:
        np+=1
    else:
        ni+=1
    i+=1
print(f"\nEl total de impares es de: {ni}")
print(f"\nEl total de pares es de: {np}")