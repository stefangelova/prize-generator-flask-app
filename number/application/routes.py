import string
import random
from application import app
from flask import jsonify

@app.route('/')
def string_num_generator(size=10):
    chars = string.digits
    return jsonify(''.join(random.choice(chars) for _ in range(size)))

