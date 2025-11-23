#Programa que saca el área de tres figuras geometricas
print("Programa que da el área de un triangulo equilatero, un rectangulo y un cuadrado")

l1=float(input("Proporciona el tamaño del lado del cuadrado: "))
b=float(input("Proporciona la base del rectangulo: "))
a=float(input("Proporciona la altura del rectangulo: "))
l2=float(input("Proporciona el lado del triangulo: "))
a2=float(input("Proporciona la altura del triangulo: "))
        
Ac=l1*l2
Ar=b*a
At=(l2*a2)/2

print(f"\nEl área del cuadrado es {Ac}\n")
print(f"El área del rectangulo es {Ar}\n")
print(f"El área del triánfulo es {At}\n")

#Programa creado por Jose Angel Márquez Ramírez