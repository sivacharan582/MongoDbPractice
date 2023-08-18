import pymongo as Mongodb

uri = "mongodb+srv://sivacharanappajodu:MBAxqW2290pGMMga@sivacharan.0phxdgg.mongodb.net/?retryWrites=true&w=majority"

client = Mongodb.MongoClient(uri)

db = client.test

data = {

        "name": "Alice",
        "major": "Computer Science",
        "age": 21,
        "course": ["C++","Python","BigData"]
}

Doc = client['monogopractice']
col = Doc['Studentdata']
col.insert_one(data)

