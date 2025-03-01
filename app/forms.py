from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class StoryForm(FlaskForm):
    title = StringField(
        'Введите название рассказа',
        validators=[
            DataRequired('Обязательное поле'),
            Length(1, 128)
        ]
    )
    text = TextAreaField(
        'Введите текст рассказа',
        validators=[
            DataRequired('Обязательное поле')
        ]
    )
    submit = SubmitField('Опубликовать')