import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# Retrieve MongoDB URI from environment variable
mongodb_uri = os.getenv('MONGODB_URI')


try:
    client = MongoClient(mongodb_uri)
    db = client.Dentists
    users = db.users
    services = db.services
    about = db.about
    clinic = db.clinic
    print("Connected to the database.")
except Exception as e:
    print(f"Error connecting to the database: {e}")

