import os
from dotenv import load_dotenv
from flask import Flask, Response, request
from flask_cors import CORS, cross_origin
from flask_caching import Cache
import requests

load_dotenv()

cache_config = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_REDIS_URL': os.environ.get('REDIS_URL'),
    'CACHE_KEY_PREFIX': 'cc_api_'
}

HOSTNAME = os.environ.get("HOST")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("OS_PASSWD")
AUTH = (USERNAME, PASSWORD)
SQL_ENDPOINT = HOSTNAME + '/_plugins/_sql?format=json'

app = Flask(__name__)
cors = CORS(app)
cache = Cache(app, config=cache_config)


@cache.memoize()
def run_post_request(query: str) -> Response:
    formed_query = dict()
    formed_query['query'] = query
    return requests.post(SQL_ENDPOINT, auth=AUTH, json=formed_query)


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
        query = request.json.get('query')
        print(query)

        res = run_post_request(query)
        return Response(res.text, mimetype='application/json')


# Added a try-except block to handle exceptions.
# Used request.args instead of request.query_string.
# Changed the conditional statement for POST requests to request.method == 'POST' and url == 'sql'.
# def process(url):
#     if request.method == 'GET':
#         args = request.args
#         formed_endpoint = f"{HOSTNAME}/{url}"
#         res = requests.get(formed_endpoint, params=args, auth=AUTH)
#         return Response(res.text, mimetype='application/json')
#     elif request.method == 'POST' and url == 'sql':
#         try:
#             query = request.get_json().get('query')
#             res = run_post_request(query)
#             return Response(res.text, mimetype='application/json')
#         except Exception as e:
#             return Response(f"Error: {e}", status=400, mimetype='application/json')
#     else:
#         return Response("Invalid method or URL", status=404, mimetype='application/json')



if __name__ == '__main__':
    app.run()
