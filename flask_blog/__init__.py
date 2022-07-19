from flask import Flask
from flask_admin import Admin

from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from flask_blog.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
mail = Mail()
admin = Admin()


def create_app():
    app = Flask(__name__,
                static_url_path='',
                static_folder='static',
                template_folder='templates'
                )

    app.config.from_object(Config)

    # flask-admin
    from flask import redirect, url_for, request, abort
    from flask_login import current_user
    from flask_admin import AdminIndexView
    from flask_admin.menu import MenuLink
    from flask_admin.contrib.sqla import ModelView
    from flask_blog.models import User, Category, Post

    class MyBlogIndexView(AdminIndexView):

        def is_accessible(self):
            return current_user.is_authenticated and current_user.is_admin

        def inaccessible_callback(self, name, **kwargs):
            if current_user.is_authenticated and not current_user.is_admin:
                return abort(403)
            return redirect(url_for('users.login', next=request.url))

    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Category, db.session))
    admin.add_view(ModelView(Post, db.session))
    admin.add_link(MenuLink(name='Home Page', url='/', category='Exit'))

    # init_app
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    admin.init_app(app, index_view=MyBlogIndexView())

    # blueprint register
    from flask_blog.main.routes import main
    from flask_blog.users.routes import users
    from flask_blog.posts.routes import posts
    from flask_blog.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(errors)

    return app
