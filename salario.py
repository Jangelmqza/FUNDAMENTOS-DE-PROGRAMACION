print("Programa que calcula el salario de una persona incluyendo las horas extras a partir de +40 hr\n")
na=str(input("Ingresa tu nombre: "))
hrst=float(input("\nIngresa tu número de horas trabajadas: "))

if hrst>=41:
    extra=(hrst-40)*250*1.5
    Sx=40*250+extra
    print(f"\n{na} tu sueldo es de: ${Sx}")
else:
    S=hrst*250
    print(f"\n{na} tu sueldo es de: ${S}")