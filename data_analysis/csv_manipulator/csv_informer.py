__author__ = 'timothyahong'
import re
import glob


def trim_path(path, fullpath_file):
    #remove the path from the file with the path
    segmented_path = fullpath_file.split('/')
    return segmented_path[-1]


def get_csv_filenames_in(path):
    fullpath_filenames = glob.glob(path + "*.csv")
    return [trim_path(path, fullpath_file) for fullpath_file in fullpath_filenames]


def get_filename_state(filename):
    return {
        "person": get_person(filename),
        "status": get_status(filename)
    }


def get_person(filename):
    match = re.search("([a-zA-Z0-9]+)_", filename)
    return match.group(0)


def get_status(filename):
    match = re.search("_([a-zA-Z0-9]+)", filename)
    return match.group(1)