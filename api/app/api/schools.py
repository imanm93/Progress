
from flask import (Blueprint, request, jsonify, current_app)
from ..extensions import db

"""
Schools API Endpoint
"""

schools = Blueprint('schools', __name__, url_prefix='/api/v1/schools')

@schools.route('/', methods=['GET'])
def index():

    #current_app.logger.info('GET /api/v1/schools/ HTTP/1.1 - 200')

    schools = []
    for data in db.schools.find():
        schools.append(data.get("name"))

    return jsonify(schools), 200
