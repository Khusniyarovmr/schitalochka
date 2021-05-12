import requests


data = {'year': '05.2021', 'item': 'Apple_musik_w', 'znach': 50000}
requests.post('http://127.0.0.1:5000/swap', json=data)
