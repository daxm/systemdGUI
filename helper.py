from GLOBALS import LOGGING_LEVEL
import subprocess
import re
import os
import logging
import textfsm
import pprint
import collections

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
    '''
    # I'd like to contatenate the desciption line(s) into a single line but I lack the skill to do so right now.  :-(
    # print(help_output_raw)

    #textFSM built list of lists but now we need to clean it up and formatted it better.
    help_output = []
    section = 'daxm'
    section_template = {'section': '',
                        'options': {
                            'shortcode': '',
                            'longcode': '',
                            'command': '',
                            'description': ''}
                        }
    for line in help_output_raw:
        # Are we at a new section?
        if help_output_raw[4] != section:
            section = line[4]
            new_section = section_template
            new_section['section'] = section
        # Add options
        new_section['options']['shortcode'] = line[0]
        new_section['options']['longcode'] = line[1]
        new_section['options']['command'] = line[2]
        # Check to see if this line is only an extension of the description for the previous help_output
        if line[0] == '' and line[1] == '' and line[2] == '':
            new_section['options']['description'] = '{}{}'.format(new_section['options']['description'], line[3])
        else:
            new_section['options']['description'] = line[3]
        print(new_section)
        help_output.append(new_section)
    '''

    return help_output_raw
