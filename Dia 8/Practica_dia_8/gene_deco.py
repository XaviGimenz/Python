def deco(funcion):

    def deco2():
        print(f'Bienvenido a la farmacia')
        print('Su turno es: ')
        print(next(funcion))
        print('Gracias por su visita')
    return deco2

def turno_medic():
    for x in range (1,101):
        yield x

def turno_cosme():
    for x in range(1, 101):
        yield x

def turno_perfu():
    for x in range(1, 101):
        yield x

