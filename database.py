from pymongo import MongoClient
from decouple import config
import copy

DB_HOST = config("DB_HOST", default="localhost")
DB_PORT = config("DB_PORT", default="27017")

client = MongoClient(host=DB_HOST, port=int(DB_PORT))
db = client.term_words


def create_words(data):
    db.words.insert_many(copy.deepcopy(data))


def find_words():
    return list(db.words.find({}, {"_id": False}))


def search_words(query):
    return list(db.words.find(query))
