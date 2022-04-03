from pymongo import MongoClient
client = MongoClient()


def get_database():
    CONNECTION_STRING = "<CONNECTION STRING HERE>"
    client = MongoClient(CONNECTION_STRING)
    dbname = client['<data_base_name_here>']
    return dbname.<collection_name>

