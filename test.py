from pymongo import MongoClient

url=connection_url="mongodb+srv://naveen:{}@cluster0.eobif.mongodb.net/test".format("leomessi10")


client = MongoClient(url)

print(client)
db=client["anime_accounts"]['user']
res=db.insert_one({"one":"one"})
if res:
    print(res.acknowledged)
