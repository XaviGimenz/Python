'''def suma():
    n1 = int(input('Numero 1: '))
    n2 = int(input('Numero 2: '))
    print(n1 + n2)
    print('Gracias por sumar')



try:
    # Codigo que queremos probar
    suma()
# except:
except TypeError:
    # Codigo a ejecutar si hay error
    print('Estas intentando concatenar tipos distintos')
except ValueError:
    print('Ese no es un numero')
else:
    # Codigo a ejecutar si no hay error
    print('Hiciste bien')
finally:
    # Codigo que se va a ejecutar de todos modos
    print('Eso fue')'''

def pedir_numero():

    while True:
        try:
            numero = int(input('Dame un numero: '))
        except:
            print('Ese no es un numero')
        else:
            print(f'Ingresaste el numero {numero}')
            break

    print('gracias')

pedir_numero()