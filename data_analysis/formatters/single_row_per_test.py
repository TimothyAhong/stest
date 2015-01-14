__author__ = 'timothyahong'
import extract

num_tests_per_mode = 3
num_rows_per_test = 11
num_rows_per_mode = num_tests_per_mode*num_rows_per_test
num_modes = 14


def _is_valid(data_array):
    return True


def _format_test(state, mode_num, test_row):
    pre_array = [mode_num, state['person'], state['status']]
    return pre_array + test_row


def _format_mode(state, mode_num, mode_data):
    formatted_mode_data = []
    tests = extract.tests_from_mode(mode_data)
    for test_row in tests:
        formatted_mode_data.append(_format_test(state, mode_num, test_row))
    return formatted_mode_data


def _format(state, unformatted_data_array):
    formatted_data = []
    #we want to use index 1 for the mode number
    for mode_num in range(1, num_modes+1):
        mode_data = extract.mode(mode_num, num_rows_per_mode, unformatted_data_array)
        #comes back as a tuple, we want a list
        mode_data = list(mode_data)
        formatted_data += _format_mode(state, mode_num, mode_data)
    return formatted_data


def generate_formatted_array(state, unformatted_data_array):
    formatted_data = []
    if not _is_valid(unformatted_data_array):
        print "invalid file"
    else:
        formatted_data = _format(state, unformatted_data_array)
    return formatted_data


