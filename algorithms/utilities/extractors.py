__author__ = 'timothyahong'
import re


def extract_cap_values(data_parameters, data_file):
    return data_file[:_num_cap_values(data_parameters)]


def extract_other_sensors(data_parameters, data_file):
    return data_file[_num_cap_values(data_parameters):]


def extract_pressure_values(data_parameters, data_file):
    start = _num_cap_values(data_parameters)
    end = start + _num_pressure_values(data_parameters)
    return data_file[start:end]


def extract_sensor_value_row(sensors_values, row_number):
    return [
        sensor_value[row_number] for sensor_value in sensors_values
    ]


def sensor_row_to_pairs(sensor_row):
    #TODO assumes event numbers here
    num_sensors = len(sensor_row)/2
    return zip(sensor_row[:num_sensors], sensor_row[num_sensors:])


def _num_cap_values(data_parameters):
    count = 0
    for sensor_name in data_parameters['Format']:
        if re.match('\cap', sensor_name) is not None:
            count += 1
    return count


def _num_pressure_values(data_parameters):
    count = 0
    for sensor_name in data_parameters['Format']:
        if re.match('\pressure', sensor_name) is not None:
            count += 1
    return count


def mode_from_filename(data_file_name):
    match = re.search("_([a-zA-Z]+)", data_file_name)
    return match.group(0)


def volume_from_filename(data_file_name):
    match = re.search("^[0-9]+", data_file_name)
    return int(match.group(0))