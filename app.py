import os

from flask import Flask
from flask_opensearch import FlaskOpenSearch

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


if __name__ == '__main__':
    app.run()
