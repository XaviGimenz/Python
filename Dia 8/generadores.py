'''def mi_funcion():
    #  return 4
    lista = []
    for x in range(1, 5):
        lista.append(x * 10)
    return lista
def mi_generador():
    # yield 4
    for x in range(1, 5):
        yield x * 10

print(mi_funcion())
print(mi_generador())

g = mi_generador()

print(next(g))
print(next(g))
print(next(g))
print(next(g))'''

def mi_generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g = mi_generador()

print(next(g))
print(next(g))
print('hola mundo')
print(next(g))