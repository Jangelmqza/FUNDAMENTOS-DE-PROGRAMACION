'''Programa que obtiene la tabla de multiplicar, pidiendo el numero de tabla y de donde a donde se realizara la tabla'''
n=int(input("¿De que número deseas saber la tabla de multiplicar? "))
ni=int(input("¿Desde que numero deseas iniciar? "))
nf=int(input("¿De que número deseas finalizar? "))

while (ni<=nf):
    r=n*ni
    print(f"{n}x{ni}={r}")
    ni+=1
