
from bson.json_util import dumps, ObjectId
from flask import current_app
from pymongo import MongoClient, DESCENDING
from werkzeug.local import LocalProxy

def get_db():
    """ Configure the Conection to the Mongo DB """
    platzi_db = current_app.config['MONGO_DB_URI']

    mongo_client = MongoClient(platzi_db)

    return mongo_client.platzi

db = LocalProxy(get_db)

def test_db_conection ():
    return dumps(db.collections_names)
