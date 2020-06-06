import sys


# ----------------------------------------------------------------------------------------------------------------------
class compras:
    def __init__(self):
        self.productos = []
        self.total = 0

    def addProduct(self, producto, cantidad):
        self.productos.append({producto, cantidad})


# ----------------------------------------------------------------------------------------------------------------------
class catalogo:
    def __init__(self):
        self.lista = []


# ----------------------------------------------------------------------------------------------------------------------
class producto:
    def __init__(self):
        self.costo = 0
        self.nombre = ""


# ----------------------------------------------------------------------------------------------------------------------
class Interface:
    def __init__(self):
        self.empresasArr = []
        self.empresas = {}

    def agregarEmpleado(self, rfc, nombre, direccion):
        self.cliente = Cliente(rfc, nombre, direccion)
        self.empresa.clientes.append(self.cliente)

    def agregarEmpresa(self, rfc, nombre, direccion):
        self.empresa = Empresa(rfc, nombre, direccion)
        self.empresas = {self.empresa.nombre, self.empresa}
        self.empresasArr.append(self.empresas)

    def printAll(self):
        if self.empresas != "":
            print(repr(self.empresasArr))
        else:
            print("\nNo existen registros")


# ----------------------------------------------------------------------------------------------------------------------
class Empresa:
    clientes = []

    def __init__(self, rfc, nombre, direccion, clientes=None):
        if clientes is None:
            clientes = []
        self.rfc = rfc
        self.nombre = nombre
        self.direccion = direccion
        self.clientes = clientes

    def agregar(self, c):
        self.clientes.append(c)

    def __repr__(self):
        return "Empresa rfc:%s nombre:%s direccion:%s clientes:%s" % (
            self.rfc, self.nombre, self.direccion, self.clientes)


# ----------------------------------------------------------------------------------------------------------------------
class Cliente:
    def __init__(self, rfc, nombre, direccion):
        self.rfcc = rfc
        self.nom = nombre
        self.direc = direccion

    def __repr__(self):
        return "Cliente rfcc:%s nom:%s direc:%s" % (self.rfcc, self.nom, self.direc)

# ----------------------------------------------------------------------------------------------------------------------
class Menu:
    def __init__(self):
        self.showMenu()
        self.inter = Interface()

    def showMenu(self):
        print("\n\nMENU DE REGISTRO\n\n1) Nueva Empresa\n2) Mostrar\n3) Fin")

    def registro(self):
        print("\nRegistre una nueva Empresa")
        r = input("Introduce el Rfc: ")
        n = input("Introduce el Nombre: ")
        d = input("Introduce la Dirección: ")
        self.inter.agregarEmpresa(r, n, d)

    def empleado(self):
        print("\nRegistre un nuevo Cliente")
        r = input("Introduce el Rfc: ")
        n = input("Introduce el Nombre: ")
        d = input("Introduce la Dirección: ")
        self.inter.agregarEmpleado(r, n, d)

    def mostrar(self):
        print("\n")
        self.inter.printAll()
        self.showMenu()

    def salir(self):
        print("\n")
        print("Fin del programa")
        sys.exit()