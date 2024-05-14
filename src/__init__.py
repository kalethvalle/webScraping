from flask import Flask
from config import getConfig
from flask_swagger_ui import get_swaggerui_blueprint
import os


def create_app():
    # Obtener la configuración según el ambiente
    config = getConfig()

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config)
    app.config.from_mapping(
        SECRET_KEY='test',
        # DATABASE=os.path.join(app.instance_path, 'demo.sqlite'),
    )
    
    from src.routes import process
    from src.routes import auth
    from src.routes import spec
    swaggerui_blueprint = get_swaggerui_blueprint(
        config.SWAGGER_URL,
        config.API_URL,
        config={
            'app_name': "Tecnical Test"  # Configuración opcional para el nombre de la aplicación
        }
    )
    
    app.register_blueprint(process.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(spec.bp)
    app.register_blueprint(swaggerui_blueprint, url_prefix=config.SWAGGER_URL)

    return app
