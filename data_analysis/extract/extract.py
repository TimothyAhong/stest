__author__ = 'timothyahong'


def tests_from_mode(data_array):
    data_array.pop(0)
    return data_array


def mode(mode_num, num_tests_per_mode, data_array):
    return modes(num_tests_per_mode, data_array)[mode_num-1]


def modes(num_tests_per_mode, data_array):
    #chunk each of the modes(set of tests) into its own array
    #dont fully understand, taken from: http://stackoverflow.com/questions/10364391/how-to-split-python-list-into-chunks-of-equal-size
    return zip(*[iter(data_array)]*num_tests_per_mode)
