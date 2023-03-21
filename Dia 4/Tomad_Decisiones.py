x = True
if x:
    print('Correcto')

if 10 < 9 :
    print('Es correcto')

elif 10!=9:
    print("cuatro")

else:
    print('No es correcto')


edad = input("Introduce tu edad: ")
edad = int(edad)
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

nota = input("Introduce tu nota")
nota = int(nota)
if nota < 11 and nota > -1:
    if nota >= 9:
        print("Excelente")
    elif nota < 9 and nota >= 7:
        print('Notable')
    elif nota >= 5 and nota < 7:
        print('Aprobado')
    elif nota < 5:
        print('Suspendido')
else:
    print("Nota no valida")