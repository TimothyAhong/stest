__author__ = 'timothyahong'

from convert_eval_output import run
from formatters import single_row_per_test
from common import analysis_paths, formatted_filename

[
    run(data_path, formatted_filename, single_row_per_test)
    for data_path in analysis_paths
]
