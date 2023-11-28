import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve MongoDB URI from environment variable
mongodb_uri = os.getenv('MONGODB_URI')

# Connect to MongoDB using the URI from environment variable
client = MongoClient(mongodb_uri)
db = client.Authentication
authed_collection = db.authed
