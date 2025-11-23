d=int(input("Ingresa el día: "))
m=int(input("\nIngresa el mes: "))
a=int(input("\nIngresa eñ año: "))

if d<30:
    d+=1
else:
    d=1
    if m<12:
        m+=1
    else:
        m=1
        a+=1
fecha=str(d)+"/"+str(m)+"/"+str(a)
print(f"La fecha siguiente es: {fecha}")