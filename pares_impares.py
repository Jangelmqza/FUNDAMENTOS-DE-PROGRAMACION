print("Ingrese 10 numeros para saber cuantos son pares y cuantos impares")
cp=0
ci=0
for i in range (1,11):
    n=int(input())
    n=n%2
    if n==0:
        cp=cp+1
    else:
        ci=ci+1
print(f"La cantidad de pares son: {cp}")
print(f"La cantidad de impares son: {ci}")

    
    