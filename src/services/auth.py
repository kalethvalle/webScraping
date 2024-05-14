import jwt
import json
import os
from config import getConfig
from src.core.errors import Unauthorized

class ServiceAuth:
    def __init__(self):
        self.config = getConfig()

    def signIn(self, data):
        users_path = os.path.join(os.path.dirname(__file__), '../collections/users.json')

        with open(users_path, 'r') as file:
            users = json.load(file)
        
        for user in users:
            if user['username'] == data['username'] and user['password'] == data['password']:
                token = jwt.encode({'username': user['username']}, self.config.SECRET_JWT, algorithm='HS256')
                return {'token': token}

        raise Unauthorized('username or password is incorrect')