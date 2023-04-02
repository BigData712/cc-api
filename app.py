import os
from dotenv import load_dotenv
from flask import Flask, Response, request
from flask_cors import CORS, cross_origin
import requests

load_dotenv()

app = Flask(__name__)
cors = CORS(app)

host_name = os.environ.get("HOST")
username = os.environ.get("USERNAME")
password = os.environ.get("OS_PASSWD")

auth = (username, password)


@app.route('/', defaults={'path': ''})
@app.route('/<path:url>')
@cross_origin()
def process(url):
    args = request.query_string
    formed_str = host_name + f"/{url}?{str(args, 'utf-8')}"
    print(formed_str)

    res = requests.get(formed_str, auth=auth)
    return Response(res.text, mimetype='application/json')


if __name__ == '__main__':
    app.run()
