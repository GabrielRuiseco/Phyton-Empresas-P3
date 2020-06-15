import sys
import Mongo
import datetime
import json

mCon = Mongo.MongoConect()
DB = mCon.CLIENT['IOT']
Empresas = DB['Empresas']
Catalogo = DB['Catalogo']


def find(name, collection):
    kwargs = {"nombre": name}
    obj: dict = Mongo.MongoConect.search(mCon, collection, **kwargs)
    return obj


# ----------------------------------------------------------------------------------------------------------------------
class Compra:
    def __init__(self):
        self.date = datetime.datetime.now()
        self.total = 0
        self.detalle = []

    # def addProduct(self, prod: object):
    #     self.detalle.append(prod)
    #     print(self.detalle)
    #     # self.sumAllProd()

    def findProd(self):
        self.name = input("\nIntroduce el nombre del articulo: ")
        obj = find(self.name, Catalogo)
        return obj

    # def sumAllProd(self):
    #     for x in self.detalle:
    #         self.total: float = self.total + x


# ----------------------------------------------------------------------------------------------------------------------
# class Compras:
#     detail = {}
#
#     def __init__(self, det=None):
#         if det is None:
#             det = {}
#         self.date = None
#         self.total = 0
#         self.detail = det
#
#     def add


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
        self.costo = float(price)


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
        self.empresa = None
        pass

    def agregarCliente(self):
        if self.empresa is None:
            rfc = input("Ingresa el rfc de la empresa: ")
            self.cliente = Menu.cliente()
            kwargs = {"arg1": {"rfc": str(rfc)}, "arg2": {'$push': {"clientes": self.cliente.__dict__}}}
            Mongo.MongoConect.updateMongo(mCon, Empresas, **kwargs)
        else:
            self.cliente = Menu.cliente()
            kwargs = {"arg1": {"name": str(self.empresa.nombre)},
                      "arg2": {'$push': {"clientes": self.cliente.__dict__}}}
            Mongo.MongoConect.updateMongo(mCon, Empresas, **kwargs)

    def agregarEmpresa(self):
        self.empresa = Menu.registro()
        Mongo.MongoConect.create(mCon, Empresas, self.empresa.__dict__)

    def agregarCompra(self):
        self.compra = Compra()
        self.nomemp = input("Nombre de la empresa en que se realiza la compra:")
        self.name = input("Nombre del cliente que realiza la compra:")
        kwargs = {"arg1": {"Clientes": {"nom": str(self.name)}, "name": str(self.nomemp)},
                  "arg2": {"$push": {"compras": self.compra.__dict__}}}
        Mongo.MongoConect.updateMongo(mCon, Empresas, **kwargs)
        self.prod = self.compra.findProd()
        kwargs = {
            "arg1": {"Clientes": {"nom": str(self.name)}, "name": str(self.nomemp), "date": str(self.compra.date)},
            "arg2": {"$push": {"detalle": self.prod}}}
        Mongo.MongoConect.updateMongo(mCon, Empresas, **kwargs)
        opt = input("¿Desea agregar otro producto?")
        while opt != "no":
            self.prod = self.compra.findProd()
            kwargs = {
                "arg1": {"Clientes": {"nom": str(self.name)}, "name": str(self.nomemp), "date": str(self.compra.date)},
                "arg2": {"$push": {"detalle": self.prod}}}
            Mongo.MongoConect.updateMongo(mCon, Empresas, **kwargs)
            opt = input("¿Desea agregar otro producto?")
        kwargs = {
            "arg1": {"Clientes": {"nom": str(self.name)}, "name": str(self.nomemp), "date": str(self.compra.date)},
            "arg2": {"$set": {"total": {"$sum": "$costo"}}}}
        Mongo.MongoConect.updateMongo(mCon, Empresas, **kwargs)

    def printAll(self):
        print("\n" + str(Mongo.MongoConect.search(mCon, Empresas)))


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

    def __repr__(self):
        return "Cliente rfcc:%s nom:%s direc:%s" % (self.rfcc, self.nom, self.direc)


# ----------------------------------------------------------------------------------------------------------------------
class Menu:
    def __init__(self):
        self.showMenu()
        self.inter = Interface()

    def showMenu(self):
        print(
            "\n\nMENU DE REGISTRO\n\n1) Nueva Empresa\n2) Mostrar\n3) Nuevo Producto\n4) Registrar Compra\n5) Registrar Cliente \n6) Fin")

    @staticmethod
    def registro():
        print("\nRegistre una nueva Empresa")
        r = input("Introduce el Rfc: ")
        n = input("Introduce el Nombre: ")
        d = input("Introduce la Dirección: ")
        empresa = Empresa(r, n, d)
        return empresa

    @staticmethod
    def cliente():
        print("\nRegistre un nuevo Cliente")
        r = input("Introduce el Rfc: ")
        n = input("Introduce el Nombre: ")
        d = input("Introduce la Dirección: ")
        cliente = Cliente(r, n, d)
        return cliente

    def addProduct(self):
        print("\nRegistre un nuevo producto")
        name = input("Introduce el nombre: ")
        price = input("Introduce el precio: ")
        self.newProd = Producto(name, price).__dict__
        Mongo.MongoConect.create(mCon, Catalogo, self.newProd)

    # def updateEmpresa(self):
    #     self.name = input("\nIngrese el nombre de la empresa que desea actualizar:")
    #     kwargs = {{"name": self.name}, {"$push": {"clientes": ""}}}

    def mostrar(self):
        print("\n")
        self.inter.printAll()
        self.showMenu()

    def endProg(self):
        print("\n")
        print("Fin del programa")
        sys.exit()
