mi_numero = 1.8
print(mi_numero)

print(type(mi_numero))

mi_numero = mi_numero + mi_numero
print(mi_numero)

edad = input("dime tu edad: ")
print(type(edad))

edad = float(edad)

print(type(edad))

nuevo_numero = mi_numero + edad
print(nuevo_numero)

x = 10
y = 5
z = 7

print("Mis numeros son " + str(x) + " y " + str(y))
print("Mis numeros son {} y {}".format(x,y))
print("La suma de {} y {} es igual a {}".format(y,x,y+x))

color = "rojo"
matricula = 53427
print(f"el auto es {color} y su matricula es {matricula}")

print(f"{z} dividido al piso de {y} es igual a {z//y}")
print(f"{z} modulo de {y} es igual a {z%y}")
print(f"{x} elevado a la {y} es igual a {x**y}")
print(f"{x} elevado a la {3} es igual a {x**3}")
print(f"La raiz cuadrade de {x} es {x**0.5}")

resultado = 90/7
redondeo= round(resultado)

valor = round(95.6666666, 2)
print(valor)

num1 = round(13/2.0)
print(type(num1))

nombre = input("Cual es tu nombre? : ")
ventas = input("Cuantas ventas? : ")
ventas = float(ventas)

print(f"Buenas {nombre} tu comision asciende a {round(ventas*13/100, 2)}")

