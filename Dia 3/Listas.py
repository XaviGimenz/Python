mi_lista = ['a','b','c']
otra_lista = ['hola', 55, 6.1]
print(type(mi_lista))
resultado = len(mi_lista)
print(resultado)
resultado2 = mi_lista[0]
print(resultado2)
resultado3 = mi_lista[0:1]
print(resultado3)

print(mi_lista+otra_lista)

mi_lista2 = mi_lista+otra_lista
print(mi_lista2)

mi_lista2[0] = 'alfa'
print(mi_lista2)

mi_lista2.append('g')
print(mi_lista2)

mi_lista2.pop()
print(mi_lista2)

eliminado = mi_lista[0]
print(eliminado)

lista = ['g', 'o', 'b','m','c']
lista.sort()
print(lista)
lista.reverse()
print(lista)