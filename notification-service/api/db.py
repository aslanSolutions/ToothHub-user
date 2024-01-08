from pymongo import MongoClient
import os
from dotenv import load_dotenv
from .config import get_config

config = get_config()
load_dotenv()


client = MongoClient(config.DATABASE_URI)
db = client.Notification
notification = db.notification