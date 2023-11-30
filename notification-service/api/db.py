from pymongo import MongoClient

client = MongoClient('mongodb+srv://aslan:aslan@aslan.im1wsjq.mongodb.net/', 27017)
db = client.Notification
notification = db.notification