caf1=float(input("Ingresa el valor de tu primera calificacion: "))
caf2=float(input("Ingresa el valor de tu segunda calificacion: "))
caf3=float(input("Ingresa el valor de tu tercera calificacion: "))

P=caf1+caf2+caf3/3

if P>=21:
    print("Aprobado")
else:
    print("Reprobado")