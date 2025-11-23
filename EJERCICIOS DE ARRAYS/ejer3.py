'''
    Programa que indica cuantas palabras hay en una cadena de texto
'''
e=1
txt=input("Ingresa una cadena de texto: ")
for p in txt:
    if p==' ':
        e+=1
print(f"El número total de palabras es de {e}")
    