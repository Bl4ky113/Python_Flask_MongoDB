""" MongoDB Usage Module """

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
    """ Test the MongoDB conection, see the collections of the DB """
    return jsonify({'collections': db.list_collection_names()})

def add_document (collection_name, document_json):
    """ Add Document to a Collection of the DB """
    collection = db[collection_name]

    new_document_id = collection.insert_one(document_json).inserted_id

    return new_document_id

def query_document (collection_name, json_parameters):
    """ Search Document by json_parameters """
    return db[collection_name].find_one(json_parameters)

def update_document (collection_name, document_id, json_update):
    """ Update (set) a value of a document """
    return db[collection_name].update_one(
            {'_id': ObjectId(document_id)},
            {'$set': json_update}
            ).modified_count

# Careers Methods

def get_careers (skip, limit):
    """ Get the Careers docs from the DB """
    pass

def get_career_by_id (career_id):
    """ Get a Career by its id """
    return query_document('careers', {'_id': ObjectId(career_id)})

def add_career (json):
    """ Add a Career to the DB.
        Checks first if Careers is Already on the DB
    """
    if query_document('careers', json):
        return {'error': 'Career Repeated'}

    return {'_id': str(add_document('careers', json))}


def add_career_course (career_id, json):
    """ Add a Course to the list of Courses of a Career """
    career_doc = query_document('careers', {'_id': ObjectId(career_id)})
    course_id = ObjectId(json['_id'])

    if not career_doc:
        return {'error': 'Career Id Not Found'}

    if course_id in career_doc['courses']:
        return {'error': 'Course Already in Career Course list '}

    career_doc['courses'].append(course_id)

    document_update = {"courses": career_doc['courses']}

    return {"updated": str(update_document('careers', career_id, document_update))}

def update_career (json):
    """ Update the content of a Career """
    career_id = ObjectId(json['_id'])
    career_doc = query_document('careers', {'_id': career_id})
    document_update = json['changes']

    if not career_doc:
        return {"error": "Career Id Not Found"}

    return {"updated": str(update_document('careers', career_id, document_update))}

def delete_career (json):
    """ Delete a Career from the DB """
    pass

def delete_career_course (career_id, json):
    """ Delete a Course from the list of Courses of a Career """
    pass

# Courses Methods

def get_courses (skip, limit):
    """ Get the Courses docs from the DB """
    pass

def get_course_by_id (course_id):
    """ Get a Course by its id """
    return query_document('courses', {'_id': ObjectId(course_id)})

def add_course (json):
    """ Add a Course to the DB.
        Check first if Course is Alredy on DB
    """
    if query_document('courses', json):
        return {'error': 'Course Repeated'}

    return {'_id': str(add_document('courses', json))}

def update_course (json):
    """ Update the Content of a Course """
    course_id = ObjectId(json['_id'])
    course_doc = query_document('courses', {'_id': course_id})
    document_update = json['changes']

    if not course_doc:
        return {"error": "Course Id Not Found"}

    return {"updated": str(update_document('courses', course_id, document_update))}

def delete_course (json):
    """ Delete a Course from the DB """
    pass
