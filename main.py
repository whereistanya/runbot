import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}! This run job is updated on a github trigger... let's see... what can we make it do?"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
