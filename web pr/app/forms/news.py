from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FileField,IntegerField,BooleanField,SelectField
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    title = StringField('Название объявления', validators=[DataRequired()])
    image = FileField("Фотография")
    Pr = IntegerField('Цена')
    content = TextAreaField("Описание")
    is_private = BooleanField("Коммерческое")
    city = StringField('Город')
    flat = SelectField(u"Тип", choices=["Дом", "Квартира"])
    room = SelectField(u"Количество комнат", choices=["1", "2", "3", "4", "5", "6"])
    submit = SubmitField('Применить')

