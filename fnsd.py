tx = input("Ingresa el texto en html que deseas convertir: ")
nivel = int(tx[2])
texto = tx[4:-5]
print(nivel * "#" + texto)