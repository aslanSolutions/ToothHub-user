import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# Retrieve MongoDB URI from environment variable
mongodb_uri = os.getenv('MONGODB_URI')

try:
    client = MongoClient(mongodb_uri)
    db = client.Authentication
    authed_collection  = db.authed
    print("Connected to the database: ", mongodb_uri)
except Exception as e:
    print(f"Error connecting to the database: {e}")

