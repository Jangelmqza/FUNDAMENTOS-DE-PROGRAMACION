'''
    Programa que lee un número y obtiene su factorial
'''
print("Programa que lee un número y obtiene su factorial")
n=int(input())
f=1
for i in range (1,n+1):
    f=f*i
print(f)