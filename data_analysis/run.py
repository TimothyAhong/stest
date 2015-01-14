__author__ = 'timothyahong'
from convert_eval_output import run
from formatters import single_row_per_test

data_path = 'test'
formatted_filename = 'formatted.csv'

run(data_path, formatted_filename, single_row_per_test)