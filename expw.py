print("Programa que lee base y exponente y obtiene su potencia")
b=int(input("Proporciona la base: "))
e=int(input("Proporciona el exponente: "))
p=1
i=0
while (i<e):
    p=p*b
    i+=1
print(p)
