'''
    Programa que lee base y exponente y obtiene su potencia
'''
print("Programa que lee base y exponente y obtiene su potencia")
b=int(input("Proporciona la base: "))
e=int(input("Proporciona el exponente: "))
p=1
for i in range (e):
    p=p*b
print(p)

