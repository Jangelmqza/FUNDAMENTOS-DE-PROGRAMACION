while True:
    nombre=(input("Ingresa tu nombre completo\n"))
    lista_n=nombre.split(" ")
    formato=1
    for palabra in lista_n:
        if not palabra[0].isupper():
            formato=0
            break
    if formato:
        print("Correcto")
        break
    else:
        print("Vuelve a intentarlo")
        
           