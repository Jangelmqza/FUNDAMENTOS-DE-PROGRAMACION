n = int(input("Ingresa el número de terminos que deseas que se muestren: "))
n1 = int(input("Ingresa el número con el que deseas iniciar: "))

a = 0
b = 1

tm = 0

print("\nLa serie es:")

for i in range(1000): 
    if tm < n:
        if a >= n1:
            print(a)
            tm = tm + 1
        
        a, b = b, a + b