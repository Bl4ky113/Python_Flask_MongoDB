
import json
from flask import Blueprint, request
from flask.json import jsonify
from . import db

careers = Blueprint('careers', __name__, url_prefix='/careers')

@careers.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index ():
    request_body = request.get_json()

    career_uid = request.args.get('uid')
    query_career_skip = request.args.get('skip')
    query_career_limit = request.args.get('limit')

    if request.method == 'POST': # Create Careers
        pass
    elif request.method == 'PUT': # Update Careers Info
        pass
    elif request.method == 'DELETE': # Delete Careers
        pass
    elif request.method == 'GET' and career_uid: # Get Careers by Id
        pass
    elif request.method == 'GET': # Get list of the Careers
        skip = query_career_skip if query_career_skip else 0
        limit = query_career_limit if query_career_limit else 10

        # result = db.get_careers(skip, limit)
        # return jsonfy({'careers': json.loads(result)})
