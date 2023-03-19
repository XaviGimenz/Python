mi_texto = "Esto es una prueba"
resultado = mi_texto[0]
resultado2 = mi_texto.index("a", 5)
resultado3 = mi_texto.rindex("a")
print(resultado)
print(resultado2)
print(resultado3)

texto = "ABCDEFGHJKLM"
fragmento = texto[2:5]
print(fragmento)
fragmento2 = texto[::-3]
print(fragmento2)
resultado4 = mi_texto.upper()
print(resultado4)
resultado5 = texto.lower()
print(resultado5)
resultado6 = mi_texto.split("t")
print(resultado6)

a = "aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e)

resultado7 = mi_texto.find("s")
print(resultado7)

resultado8 = mi_texto.replace("e", "x")
print(resultado8)


frase = """las nubes altas
atraen cielos cubiertos
la lluvia cae"""

print(frase)

print("nubes" in frase)
print("agua" not in frase)

print(len(frase))