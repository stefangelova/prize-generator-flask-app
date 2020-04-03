from flask import render_template, request, redirect, url_for
from application import app
from flask_wtf import FlaskForm
from wtforms import SubmitField


@app.route('/', methods=['GET', 'POST'])
def generate():
    form = SubmitForm()
    submit = requests.get("http://service3gen:5003").json()["prize"]
    #db.commit()
    return render_template ('generate.html', form=form, submit=submit)
