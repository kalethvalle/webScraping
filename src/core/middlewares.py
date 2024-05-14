import jwt
from flask import (
    request,
    jsonify
)
from functools import wraps
from http import HTTPStatus
from config import getConfig

def verifyToken(f):
    config = getConfig()
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token not attached'}), HTTPStatus.BAD_REQUEST

        try:
            token = token.split(" ")[1]
            payload = jwt.decode(token, config.SECRET_JWT, algorithms=['HS256'])
            print(payload)
            kwargs['user'] = payload  
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Expired token'}), HTTPStatus.UNAUTHORIZED
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid user'}), HTTPStatus.FORBIDDEN

        return f(*args, **kwargs)

    return decorated_function