from pymongo import MongoClient

client = MongoClient('mongodb+srv://root:root123@aslan.im1wsjq.mongodb.net/', tlsAllowInvalidCertificates=True, serverSelectionTimeoutMS=5000)
db = client.Notification
notification = db.notification