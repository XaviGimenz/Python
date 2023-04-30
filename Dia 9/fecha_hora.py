#import datetime
from datetime import datetime
from datetime import date

mi_fecha = datetime(2025, 5, 12, 22, 10, 15)
print(mi_fecha)
mi_fecha = mi_fecha.replace(month=6)
print(mi_fecha)

nacimiento = date (1995,5,3)
defuncion = date(2098,6,8)
vida = defuncion - nacimiento
print(vida.days)
'''mi_hora = datetime.time(17, 35)
print(mi_hora)
print(mi_hora.minute)
print(mi_hora.hour)

mi_dia = datetime.date(2025, 10, 27)
print(mi_dia)
print(mi_dia.today())'''