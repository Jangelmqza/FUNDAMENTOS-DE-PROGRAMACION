'''
    programa que lee n numeros y realiza la siguiente operación:
    -1/2 + 2/2 -3/2 + 4/2...n/2
'''
n=int(input("¿De cuantos numeros desea la operacion? "))
s=0
x=1
for i in range (n+1):
    if (i%2==0):
        s=s+i/2
    else:
        s=s-i/2
print(f"El resultado es: {s}")