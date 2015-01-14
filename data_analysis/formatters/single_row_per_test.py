__author__ = 'timothyahong'
import extract

num_frequencies = 10
num_tests_per_mode = 3
num_modes = 14


def _is_valid(data_array):
    return True


def _remove_title_row(test_data):
    test_data.pop(0)
    return test_data


def _format_row(state, mode_num, row):
    pass


def _format_test(state, mode_num, test_data):
    return [
        _format_row(state, mode_num, row)
        for row in _remove_title_row(test_data)
    ]


def _format_mode(state, mode_num, mode_data):
    formatted_mode_data = []
    tests = extract.tests(mode_data)
    for test_data in tests:
        formatted_mode_data += _format_test(state, mode_num, test_data)


def _format(state, unformatted_data_array):
    formatted_data = []
    for mode_num in range(num_modes):
        mode_data = extract.mode(mode_num, num_tests_per_mode, unformatted_data_array)
        formatted_data += _format_mode(state, mode_num, mode_data)
    return formatted_data


def generate_formatted_array(state, unformatted_data_array):
    formatted_data = []
    if not _is_valid(unformatted_data_array):
        print "invalid file"
    else:
        formatted_data = _format(state, unformatted_data_array)
    return formatted_data


