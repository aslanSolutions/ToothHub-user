from pymongo import MongoClient
import os
from dotenv import load_dotenv
from .config import get_config

config = get_config()
load_dotenv()

# Retrieve MongoDB URI from environment variable
mongodb_uri = os.getenv(config.DATABASE_URI)


try:
    client = MongoClient(mongodb_uri)
    db = client.Dentists
    users = db.users
    services = db.services
    clinic = db.clinic
    print("Connected to the database.")
except Exception as e:
    print(f"Error connecting to the database: {e}")

