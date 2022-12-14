""" Courses Blueprint for the API Endpoint """

import json
from flask import Blueprint, request
from flask.json import jsonify
from .db import \
        add_course, update_course, delete_course, \
        get_courses, get_course_by_id

courses = Blueprint('courses', __name__, url_prefix='/courses')

@courses.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index ():
    """ Index Route for the Courses Endpoint """
    request_body = request.get_json()

    course_id = request.args.get('id')
    query_course_skip = request.args.get('skip')
    query_course_limit = request.args.get('limit')

    if request.method == 'POST': # Create Course
        return jsonify(add_course(request_body))

    elif request.method == 'PUT': # Update Course Info
        return jsonify(update_course(request_body))

    elif request.method == 'DELETE': # Delete Course
        return jsonify(delete_course(request_body))

    elif request.method == 'GET' and course_id: # Get Course by Id
        return jsonify(get_course_by_id(course_id))

    elif request.method == 'GET': # Get list of the Courses
        return jsonify({'courses': json.loads(
            get_courses(
                query_course_skip if query_course_skip else 0,
                query_course_limit if query_course_limit else 10
                )
            )})
