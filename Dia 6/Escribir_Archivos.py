archivo = open('Prueba.txt', 'w')
archivo.write('Soy el nuevo texto')
archivo.write('''hola
mundo
aqui
estoy''')
archivo.writelines(['hola','mundo','aqui','estoy'])
lista = ['hola','mundo','aqui','estoy']
for p in lista:
    archivo.writelines(p + '\n')

archivo.close()

archivo = open('Prueba.txt', 'a')
archivo.write('Bienvenido')
archivo.close()