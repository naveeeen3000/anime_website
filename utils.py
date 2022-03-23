from pymongo import MongoClient
from decouple import config

def get_database(collection_name):
    connection_url="mongodb+srv://naveen:{}@cluster0.eobif.mongodb.net/test".format(config("MONGODB_PASSWORD"))


    client=MongoClient(connection_url)

    if client:
        database=client['anime_accounts'][collection_name]
        return database
        
    else:return False