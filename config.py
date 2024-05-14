import os

class Config:
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_JWT = 'test' # Word secret encode and decode jwt 
    SWAGGER_URL = '/api/docs'  # URL para acceder a la interfaz de Swagger UI
    API_URL = '/swagger.json'  # URL que proporciona la especificación Swagger JSON

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    pass

def getConfig():
    env = os.environ.get('FLASK_ENV', 'dev')
    if env == 'dev':
        return DevelopmentConfig()
    elif env == 'test':
        return TestingConfig()
    elif env == 'prod':
        return ProductionConfig()
    else:
        raise ValueError('Ambiente no válido')
