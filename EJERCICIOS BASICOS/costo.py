'''
    Programa que calcula el valor final de varios productos del mismo
    costo
'''
Ac=int(input("Ingresa el número de Articulos comprados: "))
C=float(input("Ingresa el costo del producto: "))

St=Ac*C
IVA=0.15*St
Total=St+IVA

print(f"\nEl subtotal es de: {St}\n")
print(f"El IVA es de: {IVA}\n")
print(f"El valor total es de: {Total}")
 