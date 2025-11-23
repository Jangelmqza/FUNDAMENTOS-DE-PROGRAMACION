lista=[]
for i in range(5):
    n=int(input("Ingrese un número: "))
    lista.append(n)
d=int(input("Que numero deseas eliminar de la lista"))
lista.remove(d)
print(lista)
