""" Careers Blueprint for the API endpoint """

import json
from flask import Blueprint, request
from flask.json import jsonify
from .db import \
        add_career, update_career, delete_career, \
        get_careers, get_career_by_id, \
        add_career_course, delete_career_course

careers = Blueprint('careers', __name__, url_prefix='/careers')

@careers.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index ():
    """ Index Route for the Careers Endpoint """
    request_body = request.get_json()

    career_id = request.args.get('id')
    query_career_skip = request.args.get('skip')
    query_career_limit = request.args.get('limit')

    if request.method == 'POST': # Create Careers
        return jsonify(add_career(request_body))

    elif request.method == 'PUT': # Update Careers Info
        return jsonify(update_career(request_body))

    elif request.method == 'DELETE': # Delete Careers
        return jsonify(delete_career(request_body))

    elif request.method == 'GET' and career_id: # Get Careers by Id
        return jsonify(get_career_by_id(career_id))

    elif request.method == 'GET': # Get list of the Careers
        return jsonify(
                get_careers(
                int(query_career_skip) if query_career_skip else 0,
                int(query_career_limit) if query_career_limit else 10
                ))

@careers.route('/add_course/', methods=['PUT'])
def add_course_to_career ():
    """ Add A Course to a Career """
    request_body = request.get_json()
    career_id = request.args.get('id')

    return jsonify(add_career_course(career_id ,request_body))

@careers.route('/delete_course/', methods=['DELETE'])
def delete_course_from_career ():
    """ Delete a Course From a Career """
    request_body = request.get_json()
    career_id = request.args.get('id')

    return jsonify(delete_career_course(career_id, request_body))
