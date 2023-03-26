def devolver_distintos(lista):

    total = 0
    numero_mayor = 0
    numero_menor = 100
    numero_intermedio = 0
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
    elif total in range(9,16):
        for n in lista:
            if n > numero_mayor:
                numero_mayor = n
        for n in lista:
            if n < numero_menor:
                numero_menor = n
        for n in lista:
            if n != numero_menor and n != numero_mayor:
                numero_intermedio = n
        print(numero_intermedio)
    else:
        pass



lista_numeros = []
intentos = 0
numeroañadir3 = 0
numeroañadir2 = 0

numeroañadir = int(input("escribe un numero"))
lista_numeros.append(numeroañadir)

while intentos == 0:
    numeroañadir2 = int(input("escribe otro numero: "))
    if numeroañadir2 != numeroañadir:
        lista_numeros.append(numeroañadir2)
        break
    else:
        print("el numero no puede ser el mismo.")

while intentos == 0:
    numeroañadir3 = int(input("escribe otro numero: "))
    if numeroañadir3 != numeroañadir and numeroañadir3 != numeroañadir2:
        lista_numeros.append(numeroañadir3)
        break
    else:
        print("el numero no puede ser el mismo.")

print(lista_numeros)
devolver_distintos(lista_numeros)