def repetidos(numero):
    seleccionado = 2
    contador = 0
    repetido = False
    for n in numero:
        seleccionado = n
        if seleccionado == 0:
            contador = contador + 1
        elif seleccionado != 0:
            contador = 0
    if contador >= 2:
        repetido = True
    print(f"{numero} es tu lista y repetidos es: {repetido}")

numero = []
intento = 0
intentos = 0
variable = 's'
variableTemp= ''
usuario = 0

while intento == 0:
    usuario = int(input("escribe un numero: "))
    if variable == 's':
        numero.append(usuario)
        variableTemp = input("Desea continuay? s/n")
        if variableTemp == 's':
            intento = 0
        elif variableTemp != 's':
            intento = 1

repetidos(numero)

