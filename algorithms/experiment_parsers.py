__author__ = 'timothyahong'
import csv

def load_experiment_folder(folder_path):
    parameters = _load_parameters(folder_path)
    return {
        'parameters':parameters
        'files':_load_files(folder_path, parameters)
    }
    '''
     with open('eggs.csv', 'rb') as csvfile:
...     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
...     for row in spamreader:
...         print ', '.join(row)
    '''
    pass


def _load_parameters(folder_path):
    #load
    #convert first column to key
    pass


def _load_files(folder_path, parametrs):
    #for each volume
    #get the name of the file with modes and add to dict with the csv read
    pass