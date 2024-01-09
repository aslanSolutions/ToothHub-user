from pymongo import MongoClient
import os
from dotenv import load_dotenv
from .config import get_config

load_dotenv()
config = get_config()

# Retrieve MongoDB URI from environment variable
mongodb_uri = config.DATABASE_URI

try:
    client = MongoClient(mongodb_uri)
    db = client.Authentication
    authed_collection  = db.authed
    print("Connected to the database: ", mongodb_uri)
except Exception as e:
    print(f"Error connecting to the database: {e}")

