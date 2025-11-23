a=[]
c=[]
cos=[]
subs=[]
t=0

while True:
    op=input("¿Desea agregar un articulo? s/n \n")
    if op== 's':
        ar=input("Agregue el nombre del articulo: ")
        ca=int(input("Agregue la cantidad de articulos: "))
        co=int(input("Agregue el costo del articulo"))
        sub=ca*co
        
        a.append(ar)
        c.append(ca)
        cos.append(co)
        subs.append(sub)
        
    elif op=='n':
        break

t=sum(subs)

print(f"{'--RECIBO--':>20}")
print(f"{'Articulos':>10} {'Cantidad':>10} {'Costo':>9} {'Subtotal':>10}")
for i in range (len(a)):
    print(f"{a[i]:>6} {c[i]:>10} {cos[i]:>10} {subs[i]:>10}")



