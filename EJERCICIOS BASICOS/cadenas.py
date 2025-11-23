'''
    Escribe un programa que solicite al usuario dos números una frase. El primer número introducido será la
    posición de inicio de la sub-cadena que debera mostrar el programa y el segundo número indicará la longitud de la
    sub-cadena
'''
n1 = int(input("Ingresa un número: "))
n2 = int(input("Ingresa otro número: "))
f1 = str(input("Ingresa la cadena: "))


print(f1 [n1:n2+n1])
