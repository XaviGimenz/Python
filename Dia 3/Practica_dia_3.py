Texto = input("Ingrese un texto: ")
a = input("Ingrese una letra a su eleccion: ")
b = input("Ingrese otra letra a su eleccion: ")
c = input("Ingrese otra letra a su eleccion: ")


Texto = Texto.lower()
a.lower()
b = b.lower()
c = c.lower()
Textotuple = tuple(Texto)
inta = str(Textotuple.count(a))
print("La letra "+a+" aparece un total de: " + inta)
print("La letra "+b+" aparece un total de: " + str(Textotuple.count(b)))
print(f"La letra {c} aparece un total de: {Textotuple.count(c)}")

Texto1 = list(Texto)
resultado = len(Texto1)
print("Hay un total de: " + str(resultado))

print(Texto1[0])
print(Texto[-1])

Textoreverse = " ".join(Texto1[::-1])

print(Textoreverse)

buscar_python = 'python' in Texto
dic = {True:"Si", False:"no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")



