from random import *

colores = ['azul','rojo','verde','amarillo']
numeros = list(range(5,50,5))
aleatorio = randint(1,50)

print(aleatorio)

aleatorio = round(uniform(5,7),1)
print(aleatorio)

aleatorio = choice(colores)
print(aleatorio)

shuffle(numeros)
print(numeros)


