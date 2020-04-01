import os, pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root: @localhost/proj2db" #str(os.getenv('DATABASE_URI'))
db = SQLAlchemy(app)

from application import routes
