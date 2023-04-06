mi_archivo = open('Prueba.txt')

# leer archivo :
#print(mi_archivo.read())

# leer solo una linea:
una_linea = mi_archivo.readline()
print(una_linea)

# si lees con readline guarda un punto y lee desde donde habias dejado antes
una_linea = mi_archivo.readline()
print(una_linea)

# para saltarse el salto de linea:
una_linea = mi_archivo.readline()
print(una_linea.rsplit())

for l in mi_archivo:
    print("Aqui dice: " + l)



# siempre poner esto al final para no consumir memoria innesesaria:
mi_archivo.close()