from GLOBALS import LOGGING_LEVEL
import subprocess
import re
import os
import logging
import textfsm

logging.basicConfig(level=LOGGING_LEVEL)


def systemctl_list_unit_files():
    """Collect the output of the command 'systemctl list-unit-files'.  Format the output into a list of dictionaries.
    unit_list is a list of dictionaries with 'unit' and 'state' options.
    :return unit_list"""

    # Get the current list of all the Units on this system.
    result = subprocess.getoutput("systemctl --no-legend --no-pager list-unit-files")

    unit_list = []
    for line in result.splitlines():
        line = re.sub(' +', ' ', line)
        tmp_list = line.split(' ')
        unit_list.append({'unit': tmp_list[0], 'state': tmp_list[1]})

    return unit_list


def systemctl_help_output():
    """Collect the output of the command 'systemctl -h'.  Format the output into a list of dictionaries.
    Filter the list to remove unwanted/unsupported options.
    :return help_output"""

    result = subprocess.getoutput("systemctl -h")
    textfsm_template = os.path.join(".", "textfsm_templates", "systemctl_h.textfsm")
    with open(textfsm_template) as template:
        re_table = textfsm.TextFSM(template)

    help_output = re_table.ParseText(text=result)
    # logging.DEBUG(help_output)
    print(help_output)

    """
    I think this list should be formatted like this:
    help_output = [
        {'section': '<section name>',
         'options': {
             'shortcode': '<-h>',
             'longcode': '<--help or list-unit-files>',
             'description': '<blah>'
            }
        },
    ]
    for line in result.splitlines():
        help_output = line
    """

    return help_output
