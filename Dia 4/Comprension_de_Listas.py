palabra = 'python'
lista = []
lista2 = []
pies = [10,20,30,40,50]

for letra in palabra:
    lista.append(letra)
print(lista)

lista2= [letra for letra in palabra]
print(lista2)

lista2 = [n for n in range(0,21,2)if n * 2 > 10]
print(lista2)

lista2 = [n if n * 2 > 10 else 'no'for n in range(0,21,2)]
print(lista2)

metros = [p * 3.281 for p in pies]
print(metros)