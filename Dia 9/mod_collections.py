import collections
from collections import Counter
from collections import defaultdict
from collections import namedtuple
from collections import deque

numeros = [8,9,6,4,3,3,3,4,5,6,6,7,8,8,8,9]
mi_dic= defaultdict(lambda : 'nada')
Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])

print(Counter(numeros))
print(Counter('mississipi'))
frase = 'al pan pan y al vino vino'
print(Counter(frase.split()))

serie = Counter([1,1,1,1,2,2,2,3,3,3,3,3,4])
print(serie.most_common())

mi_dic['uno'] = 'verde'
print(mi_dic['dos'])

print(mi_dic)

ariel = Persona('ariel', 1.76, 79)
print(ariel.nombre)

d = deque('abcdefg')
d.extendleft(range(6))
print('extendleft', d)
d.appendleft('x')
print('appendleft', d)