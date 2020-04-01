import string
import random
from application import app
from flask import jsonify

@app.route('/')
def string_generator(size=10):
    chars = string.ascii_uppercase + string.ascii_lowercase
    return jsonify(''.join(random.choice(chars) for _ in range(size)))
