"""Flask application for managing systemd based Linux systems."""

from GLOBALS import title, HOST, PORT, FLASK_DEBUG, LOGGING_LEVEL
from flask import Flask, render_template, request, url_for
import logging
import helper

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.htm', title=title)


@app.route("/systemctl/list-unit-files")
def _systemctl_list_unit_files():
    # Get a list of registered Units
    systemctl_units = helper.systemctl_list_unit_files()
    return render_template('list_unit_files.htm', title=title, systemd_units=systemctl_units)


@app.route("/daxm")
def _daxm():
    help_output = helper.systemctl_help_output()
    return render_template('daxm.htm', help_output=help_output)


@app.route("/<path:path>")
def catchall(path):
    return render_template("NoneShallPass.htm", path=path)


if __name__ == "__main__":
    logging.basicConfig(level=LOGGING_LEVEL)
    app.run(host=HOST, port=PORT, debug=FLASK_DEBUG)
