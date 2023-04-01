import json
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, Response
import requests

load_dotenv()

app = Flask(__name__)

host_name = os.environ.get("HOST")
username = os.environ.get("USERNAME")
password = os.environ.get("OS_PASSWD")

auth = (username, password)


@app.route('/', defaults={'path': ''})
@app.route('/<path:url>')
def process(url):
    res = requests.get(host_name + f"/{url}", auth=auth)
    return Response(res.text, mimetype='application/json')


if __name__ == '__main__':
    app.run()
