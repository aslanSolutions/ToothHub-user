import bcrypt

class AuthedUser:
    def __init__(self, username, email, password, type, collection):
        self.username = username
        self.email = email
        self.password_hash = self.set_password(password)
        self.type = type
        self.collection = collection

    def set_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def save(self):
        user_data = {
            "username": self.username,
            "email": self.email,
            "password_hash": self.password_hash,
            "type": self.type
        }
        return self.collection.insert_one(user_data)

    @classmethod
    def find_by_email(cls, email, collection):
        return collection.find_one({"email": email})

    @staticmethod
    def check_password(password, password_hash):
        return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))
