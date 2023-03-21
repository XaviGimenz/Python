monedas = 5
respuesta = 's'
nombre = input("Introduce tu nombre: ")

while monedas > 0:
    print(f'Tengo {monedas} monedas')
    monedas = monedas-1

else:print('Me quede sin monedas')

while respuesta == 's':
    respuesta = input("Quieres seguir? (s/n)")
else:print('Termino el programa')

for letra in nombre:
    if letra == 'r':
        break
    print(letra)