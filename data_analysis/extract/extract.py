__author__ = 'timothyahong'
from utilities import is_number


def _is_not_title(row):
    #check if the first element is a number
    return is_number(row[0])


def tests_from_mode(data_array):
    data_array.pop(0)
    return [
        row for row in data_array
        if _is_not_title(row)
    ]


def mode(mode_num, num_rows_per_mode, data_array):
    chunked_data_array = modes(num_rows_per_mode, data_array)
    return chunked_data_array[mode_num-1]


def modes(num_rows_per_mode, data_array):
    #chunk each of the modes(set of tests) into its own array
    #dont fully understand, taken from: http://stackoverflow.com/questions/10364391/how-to-split-python-list-into-chunks-of-equal-size
    return zip(*[iter(data_array)]*num_rows_per_mode)
