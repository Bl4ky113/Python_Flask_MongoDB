
import os
from flask import Flask, request

from .db import test_db_connection
from . import config
from . import courses, careers

def create_app (test_config=False):
    app = Flask(__name__, instance_relative_config=True)

    # Config And Instance Files
    app.config.from_object(config.Config)

    if not os.path.exists("./instance"):
        os.makedirs("./instance")

    app.register_blueprint(courses.courses)
    app.register_blueprint(careers.careers)

    return app

app = create_app()

@app.route('/test_db', methods=['GET'])
def test_db ():
    print(request.get_json())
    return ""
