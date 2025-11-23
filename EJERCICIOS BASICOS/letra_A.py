'''
    programa que lee una letra a-g TIPO A, h-n TIPO B, o-v TIPO C, x-z TIPO D
'''
l=(input("ingresa una letra: "))

match l:
    case l if l>="a" and l<="g":
        print("ES DE TIPO A")
    case l if l>="h" and l<="n":
        print("ES DE TIPO B")
    case l if l>="o" and l<="v":
        print("ES DE TIPO C")
    case l if l>="x" and l<="z":
        print("ES DE TIPO D")
        