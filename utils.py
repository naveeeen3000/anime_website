from pymongo import MongoClient
from decouple import config

def get_database(collection_name):
    connection_url=config("MONGODB_URL").format(config("MONGODB_PASSWORD"))


    client=MongoClient(connection_url)

    if client:
        database=client[config("MONGODB_DB")][collection_name]
        return database
        
    else:return False