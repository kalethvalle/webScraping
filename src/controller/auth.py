from src.services.auth import ServiceAuth
from src.core.errors import Unauthorized

class ControllerAuth:
    def __init__(self):
        self.serviceAuth = ServiceAuth()

    def login(self, body):
        try:
            return self.serviceAuth.signIn(data=body)
        except Unauthorized as err:
            raise Unauthorized(err.message)