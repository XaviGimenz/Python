def saludar_persona(nombre):
    '''
    esta funcion sirven para saludar a las personas
    '''
    print("Hola "+nombre)

def sumar(num1,num2):
    return num1*num2

saludar_persona(nombre = input("Inscribe tu nombre: "))

total = sumar(num1 = int(input('escribe un numero: ')), num2 = int(input('escribe el segundo numero: ')))
print(total)