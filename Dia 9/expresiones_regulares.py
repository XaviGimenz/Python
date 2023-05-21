import re

texto ="Si necesitas ayuda llama al (658)-798-9777 las 24 horas del dia"

patron = 'ayuda'


busqueda = re.search(patron, texto)
print(patron)

print(busqueda.span())
print(busqueda.end())

patron2 = r'\d\d\d-\d\d\d-\d\d\d\d' #re.compile(r'\d{3}\d{3}\d{4}) print(resultado.group(1)

resultado = re.search(patron, texto)
print(resultado)

texto2 = 'no atendemos los lunes por la tarde'

buscar = re.search(r'lunes|martes', texto2)
print(buscar)