__author__ = 'timothyahong'
import csv
from numbers import is_number


def create_formatted_file(filename, path):
    #TODO create a file, delete existing files
    pass


def read(filename, path):
    #filename must have the filetype (.csv)
    #path must have the trailing slash
    file_array = []
    with open(path + filename, 'rb') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for file_row in csv_reader:
            file_array.append([
                float(el) if is_number(el)
                else el
                for el in file_row
            ])
    return file_array


def append(formatted_filename, path, formatted_data_array):
    #formatted_filename must have the filetype (.csv)
    #path must have the trailing slash
    with open(path + formatted_filename, 'a') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        for row in formatted_data_array:
            csv_writer.writerow(row)