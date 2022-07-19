from flask import render_template, Blueprint, request

from flask_login import login_required

from flask_blog.models import Post
from flask_blog.users.utils import admin_login_required


main = Blueprint('main', __name__)


@main.route("/")
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html')


@main.route("/contact")
def contact():
    return render_template('contact.html')
