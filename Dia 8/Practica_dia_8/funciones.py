import gene_deco

def inicio():
    decoradomedic = gene_deco.deco(gene_deco.turno_medic())
    decoradoperfu = gene_deco.deco(gene_deco.turno_perfu())
    decoradocosme = gene_deco.deco(gene_deco.turno_cosme())
    x = 3
    while not x == 4:
        print('''Bienvenido escoja una opcion: 
            1- Medicinas
            2- Perfumeria
            3- Cosmeticos
            4- Salir
            ''')
        eleccion = int(input('Escoja opcion: '))
        if eleccion == 1:
            decoradomedic()
        if eleccion == 2:
            decoradoperfu()
        if eleccion == 3:
            decoradocosme()
        if eleccion == 4:
            print('Hasta la proxima')
            x = 4

inicio()