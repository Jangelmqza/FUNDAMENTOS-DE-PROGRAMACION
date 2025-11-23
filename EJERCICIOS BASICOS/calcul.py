'''
    Programa que obtiene la 1)suma, 2)resta, 3)multiplicacion y 4)dvision de dos numeros.
'''

op=int(input("¿Que opcion deseas realizar?\n1)suma\n2)resta\n3)multiplicacion\n4)division\n"))
n1=int(input("Ingresa el primer valor: "))
n2=int(input("Ingresa el segundo valor: "))

match op:
    case 1:
        s=n1+n2
        print(f"El resultado de la suma es {s}")
    case 2:
        r=n1-n2
        print(f"El resultado de la resta es {r}")
    case 3:
        m=n1*n2
        print(f"El resultado de la multiplicación es {m}")
    case 4:
        d=n1/n2
        print(f"El resultado de la división es de {d}")