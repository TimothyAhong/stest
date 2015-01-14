__author__ = 'timothyahong'
from csv_manipulator import csv_informer, csv_io


def run(data_path, formatted_filename, formatter):
    csv_io.create_formatted_file(formatted_filename, data_path)
    format_data_files(data_path, formatted_filename, formatter)


def format_data_files(data_path, formatted_filename, formatter):
    csv_filenames = csv_informer.get_csv_filenames_in(data_path)
    csv_filenames.remove(formatted_filename)
    for csv_filename in csv_filenames:
        append_to_formatted_file(csv_filename, data_path, formatted_filename, formatter)


def append_to_formatted_file(csv_filename, data_path, formatted_filename, formatter):
    unformatted_data_array = csv_io.read(csv_filename, data_path)
    state = csv_informer.get_filename_state(csv_filename)
    formatted_data_array = formatter.generate_formatted_array(state, unformatted_data_array)
    csv_io.append(formatted_filename, data_path, formatted_data_array)
