from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class CreateBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=3,max=20)])
    author = StringField('Author', validators=[DataRequired(), Length(min=3,max=20)])
    submit = SubmitField('Create eBook')


class SearchBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=3, max=20)])
    submit = SubmitField('Search for eBook')


