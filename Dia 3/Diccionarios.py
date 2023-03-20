diccionario = {'c1':'valor1','c2':'valor1'}
print(type(diccionario))
print(diccionario)

resultado = diccionario['c1']
print(resultado)

cliente = {'nombre':'Juan','apellido':'fuentes','peso':88,'talla':1.76}
consulta = (cliente['apellido'])
print(consulta)


dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':1000,'s2':2000}}
print(dic['c2'][1])
print(dic['c3']['s2'])

dic2 = {'c1':['a','b','c'],'c2':['d','e','c']}
valor = dic2['c2'][1]
print(valor.upper())
print(dic2['c2'][0].upper())

dic3 = {1:'a', 2:'b'}
dic3[3] = 'c'
print(dic3)
dic3[2] = 'B'
print(dic3)

print(dic3.keys())
print(dic3.values())
print(dic3.items())