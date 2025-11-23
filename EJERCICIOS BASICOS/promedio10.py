'''
    Programa que lee 10 calificaciones y obtiene su promedio, si es mayor o igual a 7 aprueba y sino
    reprueba
'''
print("Programa que lee 10 calificaciones y obtiene su promedio, si es mayor o igual a 7 aprueba y sinoreprueba")
for i in range (1,11):
    c=int(input())
    c=c+c/10-1
print(f"Tu promedio es de: {c}")
