import os
from pymongo import MongoClient

# Retrieve MongoDB URI from environment variable
mongodb_uri = os.getenv('MONGODB_URI')

# Connect to MongoDB using the URI from environment variable
client = MongoClient(mongodb_uri, tlsAllowInvalidCertificates=True)
db = client.Authentication
authed_collection = db.authed
