mensaje="Hola mundo"
print(mensaje)
print(mensaje[0])
print(mensaje[5])
print(len(mensaje))

datos=["Hola", "Mundo", 2025]

print(datos)
print(datos[0])
print(len(datos))

datos[0]= "Adios"
print(datos)

#Tambien se pueden agregar o quitar elementos
datos.append("Python")
print(datos)

datos.pop(1)
print(datos)