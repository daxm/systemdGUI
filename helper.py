import subprocess
import re

def get_units():
    # Get the current list of all the Units on this system.
    result = subprocess.getoutput("systemctl list-unit-files")

    unit_list = []
    for line in result.splitlines():
        line = re.sub(' +', ' ', line)
        tmp_list = line.split(' ')
        if '.' in tmp_list[0]:
            unit_list.append({'unit': tmp_list[0], 'state': tmp_list[1]})

    return unit_list
