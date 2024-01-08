import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    APIFAIRY_TITLE = 'Patient API'
    APIFAIRY_VERSION = '1.0'

class DevelopmentConfig(Config):
    PORT=5001
    DEBUG = True
    TESTING = True
    DATABASE_URI = 'mongodb://localhost:27017'

class ProductionConfig(Config):
    PORT=5001
    MONGO_DB_USERNAME = os.getenv('MONGO_DB_USERNAME', 'default_username')
    MONGO_DB_PASSWORD = os.getenv('MONGO_DB_PASSWORD', 'default_password')
    DATABASE_PORT =  os.getenv('MONGO_DB_PASSWORD', '27017')
    DATABASE_URI = f'mongodb+srv://{MONGO_DB_USERNAME}:{MONGO_DB_PASSWORD}@aslan.im1wsjq.mongodb.net/{DATABASE_PORT}'
    DEBUG = False
    TESTING = False
    MAIL_DEBUG = False


def get_config():
    envi = os.environ.get('FLASK_ENV', 'development')
    if envi == 'production':
        return ProductionConfig
    else:
        return DevelopmentConfig
