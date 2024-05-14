from flask import (
    Blueprint,
    jsonify,
    request, 
)
from src.core.middlewares import verifyToken
from src.controller.process import Process
from http import HTTPStatus

bp = Blueprint('process', __name__)

#instance class controller
process = Process()

@bp.route('/api/process', methods=['GET'])
@verifyToken
def get(user):
    try:
        response = process.get(user)
        return jsonify(response), HTTPStatus.OK
    except Exception as err:
        print(f'Error in list process, {err}')
        return jsonify({"message": f"internal server error"}), HTTPStatus.INTERNAL_SERVER_ERROR