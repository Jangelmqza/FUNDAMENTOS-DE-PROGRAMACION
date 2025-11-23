'''
    Programa que lee n numeros y cada vez que el usuario introduzca el numero indica si es
    par o impar, positivo o negativo
    Al final indicara cuanto sumo y cuantos fueron de cada categoria.
    Y al final la suma de todos los numeros introducidos.
    Si la suma se encuentra dentro de estos rangos, estabiliza el tipo de cantidad:
    <0 y 100 cantidad tipo A
    101 y 1000 cantidad tipo B
    >1001 cantidad tipo C
'''
#contadores
np=0
ni=0
sp=0
si=0
st=0

n=int(input("¿Cuantos números vas a ingresar? "))

for i in range (0, n):
    nm=int(input("\nIngresa el número: "))
    match nm:
        case nm if nm>0:
            print("El número es positivo")
        case nm if nm<0:
            print ("El número es negativo")
            
    match nm%2:
        case 0:
            print(f"El número {nm} es par")
            np=np+1
            sp=nm+sp
        case 1:
            print(f"El número {nm} es impar")
            ni=ni+1
            si=nm+si
#resultados 
print(f"\nEl total de números pares es: {np}")
print(f"El total de números impares es: {ni}")
print(f"\nEl resultado de la suma de los pares es: {sp}")
print(f"El resultado de la suma de los impares es: {si}")

st=si+sp
print(f"El resultado de la suma total es de: {st}")

match st:
    case s if st>=0 and st<=100:
        print("El resultado de la suma es de tipo A")
    
    case s if st>=101 and st<=1000:
        print("El resultado de la suma es de tipo B")

    case s if st>=1001:
        print("El resultado de la suma es de tipo C")