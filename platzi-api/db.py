
from bson.json_util import dumps, ObjectId
from flask import current_app, jsonify
from pymongo import MongoClient, DESCENDING
from werkzeug.local import LocalProxy

def get_db():
    """ Configure the Conection to the Mongo DB """
    mongo_uri = current_app.config['MONGO_DB_URI']
    mongo_db = current_app.config['MONGO_DB']

    mongo_client = MongoClient(mongo_uri)

    return mongo_client[mongo_db]

db = LocalProxy(get_db)

def test_db_connection ():
    return jsonify({'collections': db.list_collection_names()})

def add_document (collection_name, bson):
    collection = db[collection_name]

    new_document = collection.insert_one(bson).inserted_id

    return new_document

# Careers Methods

def get_careers (skip, limit):
    pass

def get_career_by_uid (json):
    return None

def add_career (json):
    pass

def add_career_course (career_uid, json):
    pass

def update_career (json):
    pass

def delete_career (json):
    pass

def delete_career_course (career_uid, json):
    pass

# Courses Methods

def get_courses (skip, limit):
    pass

def get_course_by_uid (json):
    return None

def add_course (json):
    pass

def update_course (json):
    pass

def delete_course (json):
    pass
