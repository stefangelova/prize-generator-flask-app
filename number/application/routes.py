import string
import random
from application import app

def string_generator(size=10):
    chars = string.ascii_uppercase + string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(size))
