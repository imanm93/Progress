
from flask import (Blueprint, request, jsonify, current_app)
from ..extensions import db

"""
Institution API Endpoint
"""

institution = Blueprint('institution', __name__, url_prefix='/api/v1/institution')

@institution.route('/', methods=['GET'])
def index():

    #current_app.logger.info('GET /api/v1/institution/ HTTP/1.1 - 200')

    institution = []
    for data in db.institution.find():
        institution.append(data.get("name"))

    return jsonify(institution), 200
