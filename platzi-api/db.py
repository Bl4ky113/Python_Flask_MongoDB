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

def get_collection_documents (collection_name, skip_docs, limit_docs):
    """ Get a list of Documents from a Collection """
    return list(db[collection_name].find({}, skip=skip_docs, limit=limit_docs))
    # return db[collection_name].find({}, skip=skip_docs, limit=limit_docs)

def query_document (collection_name, json_parameters):
    """ Search Document by json_parameters """
    return db[collection_name].find_one(json_parameters)

def update_document (collection_name, document_id, json_update, unchangeable_values=()):
    """ Update a list of values of a document
        Avoiding unchangeable values, or values
        that can be changed in other way
    """
    document_update = {}

    for change_key in json_update.keys():
        if change_key not in unchangeable_values:
            document_update[change_key] = json_update[change_key]

    return db[collection_name].update_one(
            {'_id': ObjectId(document_id)},
            {'$set': document_update}
            ).modified_count

def delete_document (collection_name, document_id):
    """ Delete Document from the DB """
    return db[collection_name].delete_one({'_id': document_id}).deleted_count

# Careers Methods

def get_careers (skip, limit):
    """ Get the Careers docs from the DB """
    return dumps(get_collection_documents('careers', skip, limit))

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
    course_doc = query_document('courses', {'_id': course_id})

    if not career_doc or not course_doc:
        return {'error': 'Career or Course Id Not Found'}

    course_obj = {'_id': course_id, 'name': course_doc['name']}

    if course_obj in career_doc['courses']:
        return {'error': 'Course Already in Career Course list'}

    career_doc['courses'].append(course_obj)

    document_update = {"courses": career_doc['courses']}

    return {'updated': str(update_document('careers', career_id, document_update))}

def update_career (json):
    """ Update the content of a Career """
    career_id = ObjectId(json['_id'])
    career_doc = query_document('careers', {'_id': career_id})
    document_updates = json['changes']
    unchangeable_values = ('courses', '_id')

    if not career_doc:
        return {'error': 'Career Id Not Found'}

    return {'updated': str(
        update_document('careers', career_id, document_updates, unchangeable_values)
        )}

def delete_career (json):
    """ Delete a Career from the DB """
    career_id = ObjectId(json['_id'])
    career_doc = query_document('careers', {'_id': career_id})

    if not career_doc:
        return {'error': 'Career Id Not Found'}

    return {'deleted': str(delete_document('careers', career_id))}

def delete_career_course (career_id, json):
    """ Delete a Course from the list of Courses of a Career """
    career_doc = query_document('careers', {'_id': ObjectId(career_id)})

    course_id = ObjectId(json['_id'])
    course_doc = query_document('courses', {'_id': course_id})

    if not course_doc or not career_doc:
        return {'error': 'Course or Career Id not Found'}

    course_obj = {'_id': course_id, 'name': course_doc['name']}

    if course_obj not in career_doc['courses']:
        return {'error': 'Course not Found in Career Course List'}

    career_doc['courses'].remove(course_obj)

    document_update = {'courses': career_doc['courses']}

    return {'updated': str(update_document('careers', career_id, document_update))}

# Courses Methods

def get_courses (skip, limit):
    """ Get the Courses docs from the DB """
    return get_collection_documents('courses', skip, limit)

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

def add_course_class (json):
    """ Add Class to a Course """

def update_course (json):
    """ Update the Content of a Course """
    course_id = ObjectId(json['_id'])
    course_doc = query_document('courses', {'_id': course_id})
    document_updates = json['changes']
    unchangeable_values = ('classes', '_id')

    if not course_doc:
        return {'error': 'Career Id Not Found'}

    return {'updated': str(
        update_document('courses', course_id, document_updates, unchangeable_values)
        )}

def delete_course (json):
    """ Delete a Course from the DB """
    course_id = ObjectId(json['_id'])
    course_doc = query_document('courses', {'_id': course_id})

    if not course_doc:
        return {'error': 'Career Id Not Found'}

    return {'deleted': str(delete_document('courses', course_id))}

def delete_course_class (json):
    """ Delete Class from a Course """
