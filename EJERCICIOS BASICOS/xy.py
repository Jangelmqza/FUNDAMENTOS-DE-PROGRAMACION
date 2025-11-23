#Programa que da los valores de x y y a partir de 6 coeficientes
print("Programa que da los valores de x y y a partir de 6 coeficientes\n")

a=float(input("Dame el valor del primer coeficiente: \n"))
b=float(input("Dame el valor del segundo coeficiente: \n"))
c=float(input("Dame el valor del tercero coeficiente: \n"))
d=float(input("Dame el valor del cuarto coeficiente: \n"))
e=float(input("Dame el valor del quito coeficiente: \n"))
f=float(input("Dame el valor del sexto coeficiente: \n"))

x=((c*e-b*f)/(a*e-b*d))
y=((a*f-c*d)/(a*e-b*d))

print(f"El resultado de x es: {x}\n")
print(f"El resultado de y es: {y}\n")

#Creado por Jose Angel Márquez Ramírez