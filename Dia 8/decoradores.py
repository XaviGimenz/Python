'''def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())


def una_funcion(funcion):
    return funcion

una_funcion(mayuscula('hola'))'''

'''def cambiar_letras(tipo):
    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())
    
    if tipo == 'may':
        return mayuscula
    elif tipo == 'min':
        return minuscula()
    
operacion = cambiar_letras('may')

operacion('palabra')'''

def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion

def mayusculas(texto):
    print(texto.upper())

def minusculas(tecto):
    print(tecto.lower())

mayuscula_decorada = decorar_saludo(mayusculas)
mayusculas('Fede')
mayuscula_decorada('fere')