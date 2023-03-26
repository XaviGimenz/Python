def devolver_alfabetico(palabra):
    palabra_unico = []
    palabra.sort()
    for palabras in palabra:
        if palabras not in palabra_unico:
            palabra_unico.append(palabras)
    print(palabra_unico)

palabra = input("escriba una palabra: ")
lista_palabra = list(palabra)

devolver_alfabetico(lista_palabra)
