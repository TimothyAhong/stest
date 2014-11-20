__author__ = 'timothyahong'
import numpy
from extractors import mode_from_filename, volume_from_filename

volume_comparison_headers = ["actual", "max", "min", "average", "mode"]


def generate_volume_comparison(output_data_files):
    volume_comparison_output = []
    for (data_file_name, data_file) in output_data_files.items():
        if len(data_file) > 0:
            row = [
                volume_from_filename(data_file_name),
                _max_volume(data_file),
                _min_volume(data_file),
                _average_volume(data_file),
                mode_from_filename(data_file_name),
            ]
            volume_comparison_output.append(row)
    return sorted(volume_comparison_output, key=lambda row: row[0])


#TODO move to extractors
def _max_volume(data_file):
    return numpy.max(data_file[0])


def _min_volume(data_file):
    return numpy.min(data_file[0])


def _average_volume(data_file):
    return numpy.mean(data_file[0])