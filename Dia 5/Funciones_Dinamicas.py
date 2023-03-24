def chequear_3_cifras(numero):
    return numero in range(100,1000)

def chequear_3_cifras_2(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False

resultado = chequear_3_cifras(numero = int(input('escribe un numero: ')))
print(resultado)

resultado = chequear_3_cifras_2([20,30,300])
print(resultado)