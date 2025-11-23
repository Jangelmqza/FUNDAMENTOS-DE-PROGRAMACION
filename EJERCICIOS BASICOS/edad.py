'''
    Escriba un programa que pida la edad e indique en que etapa de su vida se encuentra:
'''

ed=int(input("Introduce tu edad: "))

if ed>=1 and ed<=12:
    print("Usted es un niño")
    
if ed>13 and ed<=18:
    print("Usted es un adolescente")

if ed>=19 and ed<=25:
    print("Usted es un joven")

if ed>=26 and ed<=59:
    print("Usted es un adulto")

if ed>=60:
    print("Usted es de la tercera edad")
    