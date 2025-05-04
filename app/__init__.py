from flask import Flask
from config import config


def create_app(mode="default", db_cone_url="sqlite:///db/main.sqlite"):
    app = Flask(__name__)
    app.config.from_object(config[mode])
    
    from .main.routes import bp
    app.register_blueprint(bp)
    
    return app
