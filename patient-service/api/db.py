from pymongo import MongoClient
import os
from dotenv import load_dotenv
from .config import get_config

config = get_config()
load_dotenv()

client = MongoClient(config.DATABASE_URI)
try:
    client = MongoClient(config.DATABASE_URI)
    db = client.Patients
    users = db.users
    print("Connected to database: ", config.DATABASE_URI)
except Exception as e:
    print(f"Error connecting to the database: {e}")

