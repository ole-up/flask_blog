import os
from functools import wraps
from secrets import token_hex

from PIL import Image
from flask import current_app, url_for, abort
from flask_mail import Message
from flask_blog import mail
from flask_login import current_user


def save_picture(form_picture):
    random_hex = token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static', 'profile_pics', picture_fn)
    output_size = (150, 150)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Запрос на сброс пароля', sender=current_app.config['MAIL_USERNAME'], recipients=[user.email])
    msg.body = f'''Чтобы сбросить пароль, перейдите по следующей ссылке: 
                {url_for('users.reset_token', token=token, _external=True)}. 
                Если вы не делали этот запрос тогда просто проигнорируйте это письмо и никаких изменений'''
    mail.send(msg)

def admin_login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_admin:
            return abort(403)
        return func(*args, **kwargs)
    return decorated_view
