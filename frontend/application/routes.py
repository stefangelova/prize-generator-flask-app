from flask import render_template, request, redirect, url_for
from application import app, db
from flask_wtf import FlaskForm
from wtforms import SubmitField
from application.forms import GenerateForm
from .models import Prize
import requests

@app.route('/', methods=['GET', 'POST'])
def generate():
    form = GenerateForm()
    result = requests.get("http://service3gen:5003").json()
    
    if not result.get('Error'):
        prize = Prize(prize=result.get('Prize'))

        db.session.add(prize)
        db.session.commit()
    else:
        result = "ERROR"
    return render_template ('generate.html', form=form, result=result)
