from flask import Flask
import requests

app = Flask(__name__)


@app.route("/ping")
def index():
    return "Hello!"


if __name__ == "__main__":

    app.run(debug=True)
