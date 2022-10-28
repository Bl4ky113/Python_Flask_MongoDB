
import os

class Config (object):
    DEBUGING = True
    SECRET_KEY = 'i123cu4tk29120'
    MONGO_DB_URI = os.environ['PLATZI_DB_URI']
