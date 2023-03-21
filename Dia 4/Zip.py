nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65,30,25]
ciudades = ['Lima', 'Madrid', 'Mexico']

combinados = list(zip(nombres,edades,ciudades))
print(combinados)

for nombre,edad,ciudad in combinados:
    print(f'{nombre} tiene {edad} años y vive en {ciudad}')