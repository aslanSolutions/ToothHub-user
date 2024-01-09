import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()


class Config:
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=5)

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    DATABASE_URI = 'mongodb://localhost:27017'
    PORT=5005

class ProductionConfig(Config):
    MONGO_DB_USERNAME = os.getenv('MONGO_DB_USERNAME', 'default_username')
    MONGO_DB_PASSWORD = os.getenv('MONGO_DB_PASSWORD', 'default_password')
    DATABASE_PORT =  os.getenv('DATABASE_PORT', '27017')
    DATABASE_URI = f'mongodb+srv://{MONGO_DB_USERNAME}:{MONGO_DB_PASSWORD}@aslan.im1wsjq.mongodb.net/{DATABASE_PORT}'
    DEBUG = False
    TESTING = False
    PORT=5005

def get_config():
    envi = os.environ.get('FLASK_ENV', 'development')
    if envi == 'production':
        return ProductionConfig
    else:
        return DevelopmentConfig
