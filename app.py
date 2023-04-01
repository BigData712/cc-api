import os

from flask import Flask, request
from flask_opensearch import FlaskOpenSearch
from opensearchpy.client.cat import CatClient

app = Flask(__name__)

app.config["OPENSEARCH_HOST"] = os.environ.get("HOST")
app.config["OPENSEARCH_USER"] = os.environ.get("USERNAME")
app.config["OPENSEARCH_PASSWORD"] = os.environ.get("OS_PASSWD")

opensearch = FlaskOpenSearch(
    app=app,
    use_ssl=True,
    verify_certs=False,
    ssl_assert_hostname=False,
    ssl_show_warn=False
)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# issue a query on an index
@app.route('/<index>', methods=['POST'])
def process_query():
    jayson = request.json

@app.route('/indices')
def get_indicides():
    cat_client = CatClient(opensearch)

    return cat_client.indices(format="json")


if __name__ == '__main__':
    app.run()
