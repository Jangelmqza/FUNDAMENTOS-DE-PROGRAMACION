'''
    programa que indica cuantas a-e-i-o-u hay en una cadena de caracteres
'''
a=0
e=0
i=0
o=0
u=0

txt=input("Ingresa una cadena de caracteres: ")
for l in txt:
    match l:
        case 'a':
            a+=1
        case 'e':
            e+=1
        case 'i':
            i+=1
        case 'o':
            o+=1
        case 'u':
            u+=1
            
print(f"El numero de a fue: {a}")
print(f"El numero de e fue: {e}")
print(f"El numero de i fue: {i}")
print(f"El numero de o fue: {o}")
print(f"El numero de u fue: {u}")
