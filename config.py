import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    def init_app(app):
        pass

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DB') or "sqlite:////" + os.path.join(base_dir,"data-dev.sqlite")
    DEBUG = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DB') or "sqlite:////" + os.path.join(base_dir,"data-prod.sqlite")


config = {
        'development': DevelopmentConfig,
        'production': ProductionConfig
        }
