import requests
from application import app

PRIZES = [10000, 1000, 100, 10, 1]

def get_prize(letters, numbers):
    letters = [ord(l) for l in letters]
    numbers = [int(n) for n in numbers]
    sum_nums = sum(letters + numbers)
    index = sum_nums % len(PRIZES)
    return PRIZES[index]

@app.route('/')
def numlet():
    letters = requests.get('http://tsetso-test:5002/').json()["numbers"]
    numbers = requests.get('http://another-test:5001/').json()["letters"]
    prize = get_prize(list(letters.text), list(numbers.text))
    return {'error': False, 'result': str(prize)}

