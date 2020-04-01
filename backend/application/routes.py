import requests
from application import app
from requests.exceptions import HTTPError
from flask import jsonify

PRIZES = [10000, 1000, 100, 10, 1]

def get_prize(numbers, letters):
    numbers = [int(n) for n in numbers]
    letters = [ord(l) for l in letters]
    sum_nums = sum(numbers + letters)
    index = sum_nums % len(PRIZES)
    return PRIZES[index]

@app.route('/')
def numlet():
    try:
        response1 = requests.get('http://service1numbers:5002/')
        response1.raise_for_status()
    except HTTPError as http_err:
        return(f'HTTP error occurred: {http_err}')
    except Exception as err:
        return(f'Other error occurred: {err}')
    try:
        response2 = requests.get('http://service2letters:5001/')
        response2.raise_for_status()
    except HTTPError as http_err:
        return(f'HTTP error occurred: {http_err}')
    except Exception as err:
        return(f'Other error occurred: {err}')
    numbers = response1.json()["numbers"]
    letters = response2.json()["letters"]
    prize = get_prize(list(numbers.text), list(letters.text))
    return {'error': False, 'result': str(prize)}
