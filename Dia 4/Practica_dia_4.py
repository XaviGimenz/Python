from random import randint

intento = 8
aleatorio = randint(1,101)
nombre = input("dime tu nombre: ")

print(f"Muy bien {nombre}, tienes {intento} para adivinar el numero, suerte")

while intento > 0:
    numero = int(input("Escriba un numero el numero debe estar entre 1 y 100: "))
    if numero <= 100 and numero >= 1:
        if numero == aleatorio:
            print("Acertaste!")
            intento = 0
        elif numero > aleatorio:
            print("el numero es menor")
            intento = intento - 1
            print(f'te quedan {intento} intentos')
        elif numero < aleatorio:
            print("el numero es mayor")
            intento = intento - 1
            print(f'te quedan {intento} intentos')
