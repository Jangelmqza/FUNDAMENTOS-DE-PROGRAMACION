'''
    Programa que obtiene la tabla de multiplicar, pidiendo el número de
    tabla y de donde a donde se realizará la tabla
'''
print("Programa que obtiene la tabla de multiplicar, pidiendo el número de tabla y de donde a donde se realizará la tabla")
n=int(input("De que valor deseas obtener la tabla: "))
n2=int(input("\nDe que valor quieres que inicie la tabla: "))
n3=int(input("\nEn que valor deseas que termine: "))

for i in range (n2,n3+1):
    m=n*i
    print(f"{n}*{i}={m}")