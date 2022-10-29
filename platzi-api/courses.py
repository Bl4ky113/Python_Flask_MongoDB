
import json
from flask import Blueprint, request
from flask.json import jsonify
from . import db

courses = Blueprint('courses', __name__, url_prefix='/courses')

@courses.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index ():
    request_body = request.get_json()

    course_uid = request.args.get('uid')
    query_course_skip = request.args.get('skip')
    query_course_limit = request.args.get('limit')

    if request.method == 'POST': # Create Course
        pass
    elif request.method == 'PUT': # Update Course Info
        pass
    elif request.method == 'DELETE': # Delete Course
        pass
    elif request.method == 'GET' and course_uid: # Get Course by Id
        pass
    elif request.method == 'GET': # Get list of the Courses
        skip = query_course_skip if query_course_skip else 0
        limit = query_course_limit if query_course_limit else 10

        # result = db.get_courses(skip, limit)
        # return jsonfy({'courses': json.loads(result)})

# @courses.route('/<career_uid>/add_course', methods=['PUT'])
# def add_course_to_career (career_uid):
    # request_body = request.get_json()

    # return jsonfy({'added': })

# @courses.route('/<career_uid>/delete_course', methods=['DELETE'])
# def delete_course_to_career (career_uid):
    # request_body = request.get_json()

    # return jsonfy({'deleted': })
