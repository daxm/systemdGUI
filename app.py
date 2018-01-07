"""Flask application for managing systemd based Linux systems."""

from flask import Flask, render_template, request, url_for
import logging

from helper import get_units

app = Flask(__name__)
title = "systemd GUI"
HOST = '0.0.0.0'  # String: Flask server IP/DNS.
PORT = 7890  # Int: Port to run Flask on.
FLASK_DEBUG = 1  # Int: 0 or 1
LOGGING_LEVEL = 'DEBUG'


@app.route("/")
def index():
    # Get a list of registered Units
    systemctl_units = get_units()

    return render_template('index.htm', title=title, systemd_units=systemctl_units)


@app.route("/<path:path>")
def catchall(path):
    return render_template("NoneShallPass.htm", path=path)


if __name__ == "__main__":
    logging.basicConfig(level=LOGGING_LEVEL)
    app.run(host=HOST, port=PORT, debug=FLASK_DEBUG)
