# -*- coding: utf-8 -*-
import json
from flask import Flask, request, abort

app = Flask(__name__)

with open('data.json', "r") as read_file:
    data = json.load(read_file)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/swap", methods=['GET', 'POST'])
def swap():
    if request.method == 'POST':
        receive_data = request.json
        if not isinstance(receive_data, dict):
            return abort(400)
        data[receive_data['year']][receive_data['item']] = receive_data['znach']
        with open("data.json", "w") as write_file:
            json.dump(data, write_file)
        return {}
    elif request.method == 'GET':
        return data


app.run()
