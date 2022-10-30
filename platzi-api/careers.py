""" Careers Blueprint for the API endpoint """

import json
from flask import Blueprint, request
from flask.json import jsonify
from .db import \
        add_career, update_career, delete_career, \
        get_careers, get_career_by_uid, \
        add_career_course, delete_career_course

careers = Blueprint('careers', __name__, url_prefix='/careers')

@careers.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index ():
    """ Index Route for the Careers Endpoint """
    request_body = request.get_json()

    career_uid = request.args.get('uid')
    query_career_skip = request.args.get('skip')
    query_career_limit = request.args.get('limit')

    if request.method == 'POST': # Create Careers
        return jsonify({'_uid': add_career(request_body)})
    elif request.method == 'PUT': # Update Careers Info
        return jsonify({'modified': update_career(request_body)})
    elif request.method == 'DELETE': # Delete Careers
        return jsonify({'deleted': delete_career(request_body)})
    elif request.method == 'GET' and career_uid: # Get Careers by Id
        return jsonify(get_career_by_uid(request_body))
    elif request.method == 'GET': # Get list of the Careers
        return jsonify({'career_list': json.loads(
            get_careers(
                query_career_skip if query_career_skip else 0,
                query_career_limit if query_career_limit else 10
                )
            )})

@careers.route('<career_uid>/add_course', methods=['POST'])
def add_course_to_career (career_uid):
    """ Add A Course to a Career """
    request_body = request.get_json()

    return jsonify({'added': add_career_course(career_uid, request_body)})

@careers.route('<career_uid>/delete_course', methods=['DELETE'])
def delete_course_from_career (career_uid):
    """ Delete a Course From a Career """
    request_body = request.get_json()

    return jsonify({'deleted': delete_career_course(career_uid, request_body)})
