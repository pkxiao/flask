from flask import Flask
from flask import send_from_directory
import os


app = Flask(__name__)
base_url = os.path.dirname(os.path.realpath(__name__))
# app.add_url_rule('/favicon.ico', redirect_to='static', filename='news/favicon.ico')


@app.route('/', methods=['GET'])
def index():
    return 'hello flask'


if __name__ == "__main__":
    app.run(port=8000, debug=True)
