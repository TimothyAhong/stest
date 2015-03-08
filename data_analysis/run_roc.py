__author__ = 'timothyahong'
from roc_analysis_on_formatted_data import run
from common import data_paths, analysis_paths, formatted_filename


for f in [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]:
    print("\n\nFREQUENCY: " + str(f))
    [
        run(data_path, formatted_filename, f)
        for data_path in analysis_paths
    ]