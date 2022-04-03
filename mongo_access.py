from pymongo import MongoClient
client = MongoClient()


def get_database():
    CONNECTION_STRING = "mongodb://<user_name>:<password>@cluster0-shard-00-00.ncz48.mongodb.net:27017,cluster0-shard-00-01.ncz48.mongodb.net:27017,cluster0-shard-00-02.ncz48.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-rk9o8n-shard-0&authSource=admin&retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    dbname = client['<data_base_name_here>']
    return dbname.<collection_name>

