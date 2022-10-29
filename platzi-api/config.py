
import os

class Config (object):
    DEBUGING = True
    SECRET_KEY = 'helloheicheielelou'
    MONGO_DB_URI = os.environ['MONGO_DB_URI']
