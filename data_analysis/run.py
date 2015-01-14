__author__ = 'timothyahong'
from convert_eval_output import run
from formatters import single_row_per_test

data_path = '/Users/timothyahong/Google Drive/Sensassure/Venture Related/Product/Prototyping/V4 Prototype/Experiment Reports/Experiments/Data/dry_diaper_jan_10_2015/'
formatted_filename = 'formatted.csv'

run(data_path, formatted_filename, single_row_per_test)