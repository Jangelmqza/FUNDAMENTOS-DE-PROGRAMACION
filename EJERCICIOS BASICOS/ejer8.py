n1=int(input())
n2=int(input())
print("a)suma, b)resta, c)multiplicación, d)división, e)salir")
ca=str(input("opcion: "))

match ca:
    case "a)":
        s=n1+n2
        print(s)
    case "b)":
        r=n1-n2
        print(r)
    case "c)":
        m=n1*n2
        print(m)
    case "d":
        d=n1/n2
        print(d)
    case "e)":
        print("usted ha salido del programa")