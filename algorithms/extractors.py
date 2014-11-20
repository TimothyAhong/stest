__author__ = 'timothyahong'
import re

#test
def extract_cap_values(data_parameters, data_file):
    return data_file[:_num_cap_values(data_parameters)]


def extract_other_sensors(data_parameters, data_file):
    return data_file[_num_cap_values(data_parameters):]


def _num_cap_values(data_parameters):
    count = 0
    for sensor_name in data_parameters['Format']:
        if re.match('\cap', sensor_name) is not None:
            count += 1
    return count


def mode_from_filename(data_file_name):
    match = re.search("_([a-zA-Z]+)", data_file_name)
    return match.group(0)


def volume_from_filename(data_file_name):
    match = re.search("^[0-9]+", data_file_name)
    return int(match.group(0))