# Ubicacion del archivo
file = open('/home/arsenius/Documents/regex.txt')

# Lectura linea x linea
print(file.readline())
print(file.readline())
print(file.readline())

# Lectura archivo completo
print(file.read())

# Leerlo linea a linea con un 'for'
for line in file:
    print(line)

# Para cerrar el archivo y liberar espacio en memoria
file.close()

# Para abrirlo y cerrarlo automaticamente
with open('/home/arsenius/Documents/regex.txt') as file:
    for line in file:
        print(line)