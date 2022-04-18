import pymongo
class mongodb:
    def __init__(self,hash,data,time):
        self.data=data
        self.hash=hash
        self.time=time
    def insertData(self):
        myclient = pymongo.MongoClient('mongodb://localhost:27017/')
        mydb = myclient['blockchain']
        mycol = mydb["blocks"]

        mydict = { "hash": hash, "data": data, "time":time }

        x = mycol.insert_one(mydict)
