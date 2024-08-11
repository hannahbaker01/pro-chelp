from pymongo import MongoClient
from Config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client['channel_bot']

def get_databse(name):
    return db[name]