"""Flask application for managing systemd based Linux systems."""

from GLOBALS import title, HOST, PORT, FLASK_DEBUG, LOGGING_LEVEL
from flask import Flask, render_template, request, url_for
import logging
import helper

app = Flask(__name__)


@app.route("/")
def index():
    systemctl_supported_options = {
        'list-unit-files [PATTERN...]': 'systemctl/list-unit-files',
    }
    journalctl_supported_options = {}

    return render_template('index.htm',
                           title=title,
                           systemctl_help=helper.systemctl_help_output(),
                           journalctl_help=helper.journalctl_help_output(),
                           systemctl_supported_options=systemctl_supported_options,
                           journalctl_supported_options=journalctl_supported_options)


@app.route("/systemctl/list-unit-files")
def _systemctl_list_unit_files():
    return render_template('list_unit_files.htm',
                           title=title,
                           systemd_units=helper.systemctl_list_unit_files())


@app.route("/<path:path>")
def catchall(path):
    return render_template("NoneShallPass.htm", path=path)


if __name__ == "__main__":
    logging.basicConfig(level=LOGGING_LEVEL)
    app.run(host=HOST, port=PORT, debug=FLASK_DEBUG)
