import pymongo as mongoDb

uri = "mongodb+srv://sivacharanappajodu:MBAxqW2290pGMMga@sivacharan.0phxdgg.mongodb.net/?retryWrites=true&w=majority"
Dbconnect = mongoDb.MongoClient(uri)
db = Dbconnect.test
print(db)

d = {
    "Name": "sivacharan",
    "lastName": "Appajodu",
    "Age": 27,
    "Gender": "M"
}
db1 = Dbconnect['monogopractice']
col = db1['Test']
col.insert_one(d)

