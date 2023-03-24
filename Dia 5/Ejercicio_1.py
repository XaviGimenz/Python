def devolver_distintos(lista):
    total = 0
    numero_mayor = 0
    numero_menor = 100
    numero_intermedio = 50
    for n in lista:
        total += n

    if total > 15:
        for n in lista:
            if n > numero_mayor:
                numero_mayor = n
            else:
                pass
        print(numero_mayor)
    elif total < 10:
        for n in lista:
            if n < numero_menor:
                numero_menor = n
            else:
                pass
        print(numero_menor)
    elif total in range(10,15):
        for n in lista:
            if n != numero_intermedio:
                numero_intermedio = n

    else:
        pass

lista_numeros = [1,2,3]
devolver_distintos(lista_numeros)