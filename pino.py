tamaño=8
for i in range (1, tamaño + 1):
    for espacio in range (tamaño-i):
        print(" ", end="")
    for asterisco in range (2*i-1):
        print("*", end="")
        
    print()
for y in range (4):
    for c in range (2):
        print(" ", end=" ")
    for x in range (4):
        print ("*",end=" ")
    print(" ")