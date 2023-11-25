import os
from pymongo import MongoClient
from flask_dotenv import DotEnv

DotEnv()

mongodb_uri = os.getenv("MONGODB_URI")

client = MongoClient(mongodb_uri)
db = client.flask_db
todos = db.todos

