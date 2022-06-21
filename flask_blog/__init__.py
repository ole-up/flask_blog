from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from flask_blog.config import Config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__,
                static_url_path='',
                static_folder='../static',
                template_folder='../templates'
                )

    app.config.from_object(Config)

    login_manager.init_app(app)

    from flask_blog.main.routes import main
    app.register_blueprint(main)

    return app
