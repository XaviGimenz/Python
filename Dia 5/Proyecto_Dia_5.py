from random import shuffle

def pedir_letra(palabra, vida):
    letra = input('escribe una letra: ')
    validar_letra(letra, palabra, vida)
def validar_letra(letra, palabra, vida):
    lista = []
    lista.append(palabra)
    validado = False
    for n in lista:
        if letra in n:
            validado = True
            print(n)
        else:
            pass
    if validado == True:
        chequear_letra(letra, lista)
    else:
        vida -= 1
        print(f"La letra no se encuentra dispoinible - una vida le quedan: {vida}")
        pedir_letra(palabra, vida)
def chequear_letra(letra, lista):

#def ver_si_gano():


lista = ['barco', 'pajaro', 'taxi', 'casa']
shuffle(lista)
palabra = lista[0]
char = []
vida = 6
for n in palabra:
    print('-')
    char.append(n)
pedir_letra(char, vida)