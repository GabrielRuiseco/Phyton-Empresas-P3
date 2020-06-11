from pymongo import MongoClient


class MongoConect:
    def __init__(self):
        self.CLIENT = MongoClient(
            "mongodb+srv://Admin:123asterisco@practica1-hjadu.mongodb.net/Practica1?retryWrites=true&w=majority")

    def create(self, collection, x):
        collection.insert_one(x)

    def search(self, collection, **kwargs):
        self.results = collection.find(kwargs)
        for r in self.results:
            print(r)

    def delete(self, collection, **kwargs):
        self.campos = collection.delete_one(kwargs)

    def update(self, collection, **kwargs):
        self.keys = collection.update_one(kwargs)

    def deleteMany(self, collection, **kwargs):
        self.keys = collection.delete_many(kwargs)

    def updateMany(self, collection, **kwargs):
        self.keys = collection.update_many(kwargs)
