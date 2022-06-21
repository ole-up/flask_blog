from flask import render_template, Blueprint

from flask_blog.models import User

main = Blueprint('main', __name__)


@main.route("/")
def index():
    return render_template('index.html')


@main.route("/about")
def about():
    return render_template('about.html')


@main.route("/contact")
def contact():
    return render_template('contact.html')
