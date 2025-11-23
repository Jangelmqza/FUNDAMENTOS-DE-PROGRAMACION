'''
    Programa que determine el valor de PI, mediante la serie infinita partiendo de un numero n 
'''
n=int(input("Introduce el número de terminos para la serie: "))
pi=0
x=1
for i in range (1, n+1):
    if (i%2==0):
        pi=pi-4/x
    else:
        pi=pi+4/x
    x=x+2

print(pi)
