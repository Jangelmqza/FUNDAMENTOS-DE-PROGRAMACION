n=int(input("¿Cuantos alumnos son? "))
A=0
B=0
C=0
D=0
F=0
for i in range (n):
    nm=str(input("¿Cual es el nombre? "))
    c=int(input("¿Cual es la calificacion? (0-100) "))
    
    match c:
        case c if c>=90 and c<=100:
            A=A+1
        case c if c>=80 and c<=89:
            B=B+1
        case c if c>=70 and c<=79:
            C=C+1
        case c if c>=60 and c<=69:
            D=D+1
        case c if c<60:
            F=F+1
            
print(f"El total de calificaciones de A es: {A}")
print(f"El total de calificaciones de B es: {B}")
print(f"El total de calificaciones de C es: {C}")
print(f"El total de calificaciones de D es: {D}")
print(f"El total de calificaciones de F es: {F}")

if A>B and A>C and A>D and A>F:
    print("\nEl promedio de calificacion es de A")
elif B>A and B>C and B>D and B>F:
    print ("\nEl promedio de calificacion es de B")
elif C>A and C>B and C>D and C>F:
    print ("\nEl promedio de calificacion es de C")
elif D>A and D>C and D>B and D>F:
    print ("\nEl promedio de calificacion es de D")
elif F>A and F>C and F>D and F>B:
    print("\nEl promedio de calificacion es de F")



    