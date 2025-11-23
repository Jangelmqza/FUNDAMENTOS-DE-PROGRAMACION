while True:
    nombre = input("Escribe tu nombre y apellidos: ")

    es_formato_titulo = True
    esperando_mayuscula = True

    if not nombre.strip():
        continue 

    for caracter in nombre:
        
        if caracter == ' ':
            esperando_mayuscula = True
        
        elif esperando_mayuscula:
            if not caracter.isupper():
                es_formato_titulo = False
                break
            else:
                esperando_mayuscula = False
        
        else:
            if not caracter.islower():
                es_formato_titulo = False
                break

    if es_formato_titulo:
        print("Nombre Correcto")
        break
    else:
        print("Formato incorrecto, intenta de nuevo.")