from flask import (
    Blueprint,
    jsonify,
    request, 
)
from http import HTTPStatus
from src.controller.auth import ControllerAuth
from src.core.errors import Unauthorized

bp = Blueprint('auth', __name__)

#instance class controller
auth = ControllerAuth()

@bp.route('/login', methods=['POST'])
def login():
    try:
        body = request.json
        response = auth.login(body)
        return jsonify(response), HTTPStatus.OK
    except Unauthorized as err:
        return jsonify({"message": err.message}), HTTPStatus.UNAUTHORIZED
    except Exception as err:
        print(f'Error in authentication, {err}')
        return jsonify ({"message": f"internal server error"}), HTTPStatus.INTERNAL_SERVER_ERROR