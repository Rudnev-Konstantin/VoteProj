from flask import Flask
from config import config
from .data.db_connect import DataBaseConnect
from flask_login import LoginManager


def create_app(mode="default", db_cone_url="sqlite:///:memory:"):
    app = Flask(__name__)
    app.config.from_object(config[mode])
    
    app.db_connect = DataBaseConnect(db_cone_url)
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    from .data.models.user import User
    @login_manager.user_loader
    def load_user(user_id):
        with app.db_connect.get_session() as session:
            user = session.get(User, user_id)
        return user
    
    from .main import bp
    app.register_blueprint(bp)
    
    return app
