nombre=str(input("Ingrese su nombre completo: "))
lista=nombre.split()

if len(lista)>=3:
    apd=lista[-1]
    ap=lista[-2]
    n2=lista[:-2]
print(n2)
print(ap)
print(apd)