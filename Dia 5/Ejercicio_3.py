def repetidos():


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



