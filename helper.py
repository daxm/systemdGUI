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

    help_output_raw = re_table.ParseText(text=result)

    # Contatenate desciption into a single item instead of being spread across multiple lines.
    not_done = True
    while not_done:
        not_done = False
        for i, line in enumerate(help_output_raw):
            # Is this a line with only a description?
            if line[0] == '' and line[1] == '' and line[2] == '' and line[3] != '':
                # Pretty up the output by adding a space, if needed, when concatenating.
                if re.search('\S$', help_output_raw[i - 1][3]) and re.search('^\S', line[3]):
                    formatter = '{} {}'
                else:
                    formatter = '{}{}'
                help_output_raw[i - 1][3] = formatter.format(help_output_raw[i - 1][3], line[3])
                # Remove now duplicate row
                del help_output_raw[i]
                not_done = True

    return help_output_raw


def journalctl_help_output():
    """Collect the output of the command 'journalctl -h'.  Format the output into a list of dictionaries.
    Filter the list to remove unwanted/unsupported options.
    :return help_output"""

    result = subprocess.getoutput("journalctl -h")
    textfsm_template = os.path.join(".", "textfsm_templates", "journalctl_h.textfsm")
    with open(textfsm_template) as template:
        re_table = textfsm.TextFSM(template)

    help_output_raw = re_table.ParseText(text=result)

    # Contatenate desciption into a single item instead of being spread across multiple lines.
    not_done = True
    while not_done:
        not_done = False
        for i, line in enumerate(help_output_raw):
            # Is this a line with only a description?
            if line[0] == '' and line[1] == '' and line[2] != '':
                # Pretty up the output by adding a space, if needed, when concatenating.
                if re.search('\S$', help_output_raw[i - 1][2]) and re.search('^\S', line[2]):
                    formatter = '{} {}'
                else:
                    formatter = '{}{}'
                help_output_raw[i - 1][2] = formatter.format(help_output_raw[i - 1][2], line[2])
                # Remove now duplicate row
                del help_output_raw[i]
                not_done = True

    return help_output_raw
