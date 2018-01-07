"""Flask application for managing systemd based Linux systems."""

from flask import Flask, render_template, request, url_for

app = Flask(__name__)
title = "systemd GUI"
HOST = '0.0.0.0'  # String: Flask server IP/DNS.
PORT = 7890  # Int: Port to run Flask on.
DEBUG = 1  # Int: 0 or 1


@app.route("/")
def index():
        return render_template('index.htm', title=title)


@app.route("/<path:path>")
def catchall(path):
    return render_template("NoneShallPass.htm", path=path)


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)
