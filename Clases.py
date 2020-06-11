import sys
import Mongo
import json

mCon = Mongo.MongoConect()
DB = mCon.CLIENT['IOT']
Empresas = DB['Empresas']
Catalogo = DB['Catalogo']


class Detalle:
    def __init__(self):
        self.productos = []

    def addProduct(self, productoId, cantidad):
        self.productos.append({productoId, cantidad})


# ----------------------------------------------------------------------------------------------------------------------
class Compras:
    def __init__(self):
        self.date = None
        self.total = 0


# ----------------------------------------------------------------------------------------------------------------------
# class Catalogo:
#     def __init__(self):
#         self.lista = []
#
#     def addProduct(self, producto):
#         self.lista.append(producto)


# ----------------------------------------------------------------------------------------------------------------------
class Producto:
    def __init__(self, name, price):
        self.nombre = name
        self.costo = price


# ----------------------------------------------------------------------------------------------------------------------
class Emp:
    def __init__(self, nam, emp):
        self.edata = emp
        self.ndata = nam

    def __repr__(self):
        return "{Empresa:{ %s: {%s}}" % (self.ndata, self.edata)


# ----------------------------------------------------------------------------------------------------------------------
class Interface:
    def __init__(self):
        self.empresasArr = []

    def agregarCliente(self, rfc, nombre, direccion):
        self.cliente = Cliente(rfc, nombre, direccion)
        self.empresa.clientes.append(self.cliente)

    def agregarEmpresa(self, rfc, nombre, direccion):
        self.empresa = Empresa(rfc, nombre, direccion)
        self.empresas = Emp(self.empresa.nombre, self.empresa)
        self.empresasArr.append(self.empresas)

    def printAll(self):
        if self.empresasArr:
            print(repr(self.empresasArr))
        else:
            print("\nNo existen registros")

    def createAtDB(self):
        self.data = self.empresasArr[-1].__dict__
        print(self.data)
        # self.mc = Mongo.MongoConect()
        # Mongo.MongoConect.create(self.mc, self.data)


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
    compras = []

    def __init__(self, rfc, nombre, direccion, compras=None):
        if compras is None:
            compras = []
        self.rfcc = rfc
        self.nom = nombre
        self.direc = direccion
        self.compras = compras

    def agregarCompra(self, c):
        self.compras.append(c)

    def __repr__(self):
        return "Cliente rfcc:%s nom:%s direc:%s" % (self.rfcc, self.nom, self.direc)


# ----------------------------------------------------------------------------------------------------------------------
class Menu:
    def __init__(self):
        self.showMenu()
        self.inter = Interface()

    def showMenu(self):
        print("\n\nMENU DE REGISTRO\n\n1) Nueva Empresa\n2) Mostrar\n3) Nuevo Producto\n4) Fin")

    def registro(self):
        print("\nRegistre una nueva Empresa")
        r = input("Introduce el Rfc: ")
        n = input("Introduce el Nombre: ")
        d = input("Introduce la Dirección: ")
        self.inter.agregarEmpresa(r, n, d)

    def cliente(self):
        print("\nRegistre un nuevo Cliente")
        r = input("Introduce el Rfc: ")
        n = input("Introduce el Nombre: ")
        d = input("Introduce la Dirección: ")
        self.inter.agregarCliente(r, n, d)

    def addProduct(self):
        print("\nRegistre un nuevo producto")
        name = input("Introduce el nombre: ")
        price = input("Introduce el precio: ")
        self.newProd = Producto(name, price).__dict__
        Mongo.MongoConect.create(mCon, Catalogo, self.newProd)

    def mostrar(self):
        print("\n")
        self.inter.printAll()
        self.showMenu()

    def endProg(self):
        print("\n")
        print("Fin del programa")
        sys.exit()
