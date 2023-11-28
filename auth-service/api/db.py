
from pymongo import MongoClient

mongodb_uri = "mongodb+srv://ali:ali@aslan.im1wsjq.mongodb.net/Authentication"
client = MongoClient(mongodb_uri)
db = client.Authentication
authed_collection = db.authed
