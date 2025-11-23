txt = input("Ingresa una cadena de texto: ")
cp = 0
np = 1
for caracter in txt:
    if caracter != ' ':
        cp += 1
    else:
        if cp > 0:
            print(f"La palabra {np} tiene: {cp} caracteres")
            np += 1
            cp = 0
if cp > 0:
    print(f"La palabra {np} tiene: {cp} caracteres")
