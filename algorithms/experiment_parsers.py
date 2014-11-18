__author__ = 'timothyahong'
import csv
import os


def load_experiment_folder(folder_path):
    parameters = _load_parameters(folder_path)
    return {
        'parameters': parameters,
        'files': _load_files(folder_path, parameters)
    }
    pass


def _load_parameters(folder_path):
    parameters = {}
    #open the file with a universal newline
    with open('{0}/parameters.csv'.format(folder_path), 'rU') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            #take the first colume as they key and the rest as the values
            parameters[row[0]] = row[1:]
    return parameters


def _load_files(folder_path, parameters):
    data_file_names = _build_data_file_names(parameters['Volumes'])
    return {
        data_file_name: _load_file(folder_path, data_file_name) for data_file_name in data_file_names
    }


def _load_file(folder_path, data_file_name):
    row_first_file = []
    file_path = '{0}/{1}'.format(folder_path, data_file_name)
    file_exists = os.path.isfile(file_path)
    if file_exists:
        with open(file_path, 'rU') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for row in csv_reader:
                row_first_file.append([int(el) for el in row])
    else:
        print("FILE {0} COULD NOT BE FOUND".format(file_path))
    return _transpose(row_first_file)


def _transpose(target_arr):
    return zip(*target_arr)


def _build_data_file_names(volumes):
    data_file_names = []
    for volume in volumes:
        file_template = str(volume) + "_{0}.csv"
        data_file_names.append(file_template.format("stand"))
        data_file_names.append(file_template.format("sit"))
        data_file_names.append(file_template.format("lying"))
    return data_file_names