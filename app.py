import os
from dotenv import load_dotenv
from flask import Flask, Response, request
from flask_cors import CORS, cross_origin
import requests

load_dotenv()

app = Flask(__name__)
cors = CORS(app)

HOSTNAME = os.environ.get("HOST")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("OS_PASSWD")
AUTH = (USERNAME, PASSWORD)
SQL_ENDPOINT = HOSTNAME + '/_plugins/_sql?format=json'


@app.route('/', defaults={'path': ''})
@app.route('/<path:url>', methods=['GET', 'POST'])
@cross_origin()
def process(url):
    if request.method == 'GET':
        args = request.query_string
        formed_endpoint = HOSTNAME + f"/{url}?{str(args, 'utf-8')}"
        print(formed_endpoint)

        res = requests.get(formed_endpoint, auth=AUTH)

        return Response(res.text, mimetype='application/json')
    elif url == 'sql' and request.method == 'POST':
        query = request.json
        print(query)

        res = requests.post(SQL_ENDPOINT, auth=AUTH, json=query)
        return Response(res.text, mimetype='application/json')


if __name__ == '__main__':
    app.run()
