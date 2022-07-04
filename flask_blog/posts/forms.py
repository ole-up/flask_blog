from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

from flask_blog.models import Category

categories = {1: 'Бизнес', 2: 'Культура', 3: 'Спорт', 4: 'Еда', 5: 'Политика', 6: 'Знаменитости', 7: 'Стартапы',
              8: 'Путешествия'}


class PostForm(FlaskForm):
    title = StringField('Заголовок:', validators=[DataRequired()])
    category = SelectField('Тема:', coerce=int)
    content = TextAreaField('Текст статьи:', validators=[DataRequired()])
    submit = SubmitField('Опубликовать')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.category.choices = [(category.id, u"%s" % category.name) for category in Category.query.order_by('name')]
        self.category.choices.insert(0, (0, u"Не выбрана"))
