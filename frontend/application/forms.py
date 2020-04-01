from flask_wtf import FlaskForm
from wtforms import SubmitField
from application import app

class GenerateForm(FlaskForm):
    submit = SubmitField('Generate Prize')
