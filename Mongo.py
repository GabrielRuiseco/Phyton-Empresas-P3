from pymongo import MongoClient


class MongoConect:
    def __init__(self):
        self.CLIENT = MongoClient(
            "mongodb+srv://Admin:123asterisco@practica1-hjadu.mongodb.net/Practica1?retryWrites=true&w=majority")
        self.DB = self.CLIENT['IOT']
        self.EMPRESAS = self.DB['Empresas']

    def create(self, x):
        self.EMPRESAS.insert_one(x)

    def search(self, **kwargs):
        self.results = self.EMPRESAS.find(kwargs)
        for r in self.results:
            print(r)

    def delete(self, **kwargs):
        self.campos = self.EMPRESAS.delete_one(kwargs)

    def update(self, **kwargs):
        self.keys = self.EMPRESAS.update_one(kwargs)

    def deleteMany(self, **kwargs):
        self.keys = self.EMPRESAS.delete_many(kwargs)

    def updateMany(self, **kwargs):
        self.keys = self.EMPRESAS.update_many(kwargs)
