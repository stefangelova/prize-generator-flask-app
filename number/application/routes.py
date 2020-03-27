import string
import random
from application import app

@app.route('/')
def string_num_generator(size=10):
    chars = string.digits
    return ''.join(random.choice(chars) for _ in range(size))
