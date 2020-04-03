from flask import render_template, request, redirect, url_for
from application import app
from flask_wtf import FlaskForm
from wtforms import SubmitField
from application.forms import GenerateForm
import requests

@app.route('/', methods=['GET', 'POST'])
def generate():
    form = GenerateForm()
    result = requests.get("http://service3gen:5003").json() #["prize"]
    #db.session.add()
    #db.session.commit()
    return render_template ('generate.html', form=form, result=result)
