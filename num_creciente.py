'''
    Escribir un programa que solicite 3 números y determine si se han introducido
    en orden creciente
'''

n1=int(input("\nIngresa un número: "))
n2=int(input("\nIngresa otro número: "))
n3=int(input("\nIngresa otro número: "))

if n3>=n2 and n2>=n1:
    print("Los numeros van en orden creciente")
else:
    print("Los numeros no se han introducido en orden creciente ")