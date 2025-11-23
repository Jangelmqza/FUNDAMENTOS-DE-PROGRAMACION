'''
    programa que obtiene las siguientes áreas: a)cuadrado, b)rectangulo c)triangulo
'''

a=str(input("Ingrese la figura que desea su área (cuadrado, rectangulo y triangulo): "))

match a:
    case "cuadrado":
        l=float(input("Ingrese el tamaño del lado del cuadrado: "))
        ac=l*l
        print(f"El área del cuadrado es de: {ac}")
    case "rectangulo":
        b=float(input("Ingresa la base del rectangulo "))
        h=float(input("Ingresa la altura del rectangulo: "))
        ar=b*h
        print(f"El área del rectangulo es: {ar}")
    case "triangulo":
        b1=float(input("Ingresa la base del triangulo: "))
        h1=float(input("Ingresa la altura del triangulo: "))
        at=(b1*h1)/2
        print(f"El área del triangulo es: {at}")
