class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numerocuenta, balance):
        super().__init__(nombre, apellido)
        self.numerocuenta = numerocuenta
        self.balance = balance
    def cantidad(self):
        print(f'El balance de {self.nombre} es {self.balance}')

    def ingresar(self):
        ingreso = int(input('introduce efectivo: '))
        self.balance = self.balance+ingreso
        print(f'El saldo actual es {self.balance}')

    def retirar(self):
        retirar = False
        while not retirar == True:
            retiro = int(input('introduce importe a retirar '))
            if retiro <= self.balance:
                self.balance = self.balance - retiro
                print(f'Su balance actual es: {self.balance}')
                retirar = True
            else:
                print('no puedes sacar mas dinero del existente')

def inicio():
    print('Nuevo cliente ingrese sus datos porfavor')
    nombre = input('introduce tu nombre: ')
    apellido = input('introduce tu apellido: ')
    numerocuenta = int(input('el numero de cuenta '))
    balance = int(input('introduzca el balance oficial '))

    crear_cliente(nombre, apellido, numerocuenta, balance)

def crear_cliente(nombre, apellido, numerocuenta, balance):
    cliente = Cliente(nombre, apellido, numerocuenta, balance)
    programa(cliente)

def programa(cliente):
    salir = False
    while not salir == True:
        print('''--- Escoja una opcion ---
              '1- Mostrar balance
              '2- Depositar efectivo
              '3- Retirar efectivo
              '4- salir''')
        menu = int(input())

        if menu == 1:
            cliente.cantidad()

        if menu == 2:
            cliente.ingresar()

        if menu == 3:
            cliente.retirar()
        if menu == 4:
            print('Un placer, vuelva cuando quiera')
            salir = True

inicio()




