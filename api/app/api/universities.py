
from flask import (Blueprint, request, jsonify)

"""
Universities API Endpoint
"""

universities = Blueprint('universities', __name__, url_prefix='/api/v1/universities')

@universities.route('/', methods=['GET'])
def index():
    data = {
        'message': 'universities'
    }
    return jsonify(data), 200
