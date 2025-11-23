'''
Crea un programa que usando bucles nos
permita pedir un número par comprendido entre 100 y 200
y nos muestre todos los números pares comprendidos entre el número facilitado
y 200. Por ejemplo si el número facilitado es 192 nos
debería mostrar 192, 194, 196, 198 y 200
'''
n1=int(input("Ingresa un número par entre 100 y 200: "))

for i in range (n1,200+1,2):
    print (i)
