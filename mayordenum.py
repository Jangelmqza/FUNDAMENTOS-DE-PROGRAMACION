'''
    Escribir un programa que solicite tres números y determine el mayor de los 3
'''
n1=int(input("Ingresa un número: "))
n2=int(input("\nIngresa otro número: "))
n3=int(input("\nIngresa otro número: "))

if n1>=n2 and n1>=n3:
    print(f"\nEl número mayor es {n1}")
    
if n2>=n1 and n2>=n3:
    print(f"\nEl número mayor es {n2}")

if n3>=n1 and n3>=n2:
    print(f"\nEl número mayor es {n3}")