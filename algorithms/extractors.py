__author__ = 'timothyahong'
import re


def extract_cap_values(data_parameters, data_file):
    return data_file[:_num_cap_values(data_parameters) - 1]


def extract_other_sensors(data_parameters, data_file):
    return data_file[_num_cap_values(data_parameters):]


def _num_cap_values(data_parameters):
    count = 0
    for sensor_name in data_parameters['Format']:
        if re.match('\cap', sensor_name) is not None:
            count += 1
    return count