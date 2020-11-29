from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from config import config

db = SQLAlchemy()
cors = CORS()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    cors.init_app(app)

    from .api.controllers import api as api_blueprint
    from .main.controllers import main as main_blueprint
    app.register_blueprint(api_blueprint,url_prefix='/api/v1')
    app.register_blueprint(main_blueprint)

    return app

