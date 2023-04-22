class Pajaro:

    alas = True

    def __init__(self, color, especie):
         self.color = color
         self.especie = especie

    def piar(self):
        print('pio')

    def volar(self, metros):
        print(f'El pajaro ha voldado {metros} metros')


piolin = Pajaro('Amarillo', 'Canario')

piolin.piar()
piolin.volar(50)