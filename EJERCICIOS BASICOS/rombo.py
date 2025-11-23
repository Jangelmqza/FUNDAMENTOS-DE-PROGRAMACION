tamaño=5
for i in range (1, tamaño + 1):
    for espacio in range (tamaño-i):
        print(" ", end="")
    for asterisco in range (2*i-1):
        print("*", end="")
        
    print()

for i in range (tamaño-1,0,-1):
    for espacio in range (tamaño-i):
        print(" ", end="")
    for asterisco in range (2*i-1):
        print("*", end="")
        
    print()
