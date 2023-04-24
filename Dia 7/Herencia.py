'''class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')

    def hablar(self):
        print('Este animal emite un sonido')

class Pajaro(Animal):

    def __init__(self,edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def halar(self):
        print('pio')

    def volar(self, metros):
        print(f'El pajaro vuela {metros} metros')

piolin = Pajaro(2, 'Amarillo', 60)
mi_animal = Animal(5, 'verde')'''

class Padre:
    def hablar(self):
        print('Hola')

class Madre:
    def reir(self):
        print('ja ja')

    def hablar(self):
        print('que tal')

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
print(Nieto.__mro__)
mi_nieto.reir()

#print(Pajaro.__bases__)
#print(Animal.__subclasses__())