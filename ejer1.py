'''
    Programa que indica cuantas vocales tiene una cadena de texto
'''
txt=input("Ingresa una oracion: ")
c=0
for letra in txt:
    if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
        c+=1
print (f"El número de vocales es: {c}")

