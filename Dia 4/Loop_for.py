lista = ['a', 'b', 'c']
lista2 = ['Pablo', 'Layra', 'Manuel']
lista3 = [1,2,3,4,5]
mi_valor = 0
dic = {'clave1':'a', 'clave2':'b', 'clave3':'c'}

for letra in lista:
    numero_letra = lista.index(letra)+1
    print(f"letra {numero_letra}: "+ letra)

for nombre in lista2:
    if nombre.startswith('L'):
        print(nombre)

for numero in lista3:
    mi_valor = mi_valor + numero
    print(mi_valor)

print(mi_valor) #a diferente altura no afecta al for

for item in dic.values():
    print(item)