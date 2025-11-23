n1=int(input("Ingresa el primer número: "))
n2=int(input("\nIngresa el segundo número: "))
print("1.-Suma \n 2.-Resta \n 3.-Multiplicación \n 4.-División")
ca=str(input("\n¿Qué calculo deseas hacer? "))

match ca:
    case "1":
        s=n1+n2
        print(f"El resultado de la suma es: {s}")
    case "2":
        r=n1-n2
        print(f"El resultado de la resta es: {r}")
    case "3":
        m=n1*n2
        print(f"El resultado de la multiplicación es: {m}")
    case "4":
        d=n1/n2
        print(f"El resultado de la división es: {d}")