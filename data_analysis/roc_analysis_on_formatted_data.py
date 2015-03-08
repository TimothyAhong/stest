__author__ = 'timothyahong'
from csv_manipulator import csv_io
from formatters import formatted_to_roc
from analysis import roc, roc_value_generators
from utilities import transpose
#TODO roc_output.csv file to display these scatters


def run(data_path, filename, target_frequency):
    #target_frequency = 50000 #only care about 100Hz at this stage
    formatted_data_array = csv_io.read(filename, data_path)
    roc_output = run_for_frequency(formatted_data_array, target_frequency)
    #TODO each dataset should be appended horizontally (2 transposes)
    append_to_formatted_file('roc_output.csv', data_path + 'analysis/', roc_output, ['admittance', 'neg phase', 'conductance', 'reactance'])
    return roc_output


def run_for_frequency(formatted_data_array, target_frequency):
    value_generators = [roc_value_generators.admittance, roc_value_generators.negative_phase, roc_value_generators.conductance, roc_value_generators.reactance]
    positive_statuses = ['wet', '100ml', 'urine'] #if the mode contains any of these strings it is wet
    negative_statuses = ['dry']
    return [
        run_roc(formatted_data_array, positive_statuses, negative_statuses, target_frequency, value_generator)
        for value_generator in value_generators
    ]


def run_roc(formatted_data_array, positive_statuses, negative_statuses, target_frequency, value_generator):
    positive_values, negative_values = formatted_to_roc.generate_roc_groups_from_formatted_array(
        formatted_data_array,
        positive_statuses,
        negative_statuses,
        target_frequency,
        value_generator
    )
    fpr, tpr, thresholds, auc = roc.generate_roc(positive_values, negative_values)
    print auc
    return {
        'fpr': fpr,
        'tpr': tpr,
        'thresholds': thresholds,
        'auc': auc
    }


def append_to_formatted_file(filename, data_path, roc_output, variable_names):
    formatted_data_array = _format(roc_output, variable_names)
    csv_io.write_new(filename, data_path, formatted_data_array)


def _format(roc_output, variable_names):
    column_first_array = _collapse_roc_outputs(roc_output, variable_names)
    row_first_array = transpose(column_first_array)
    return row_first_array


def _collapse_roc_outputs(roc_output, variable_names):
    column_first_array = []
    for index, single_roc_output in enumerate(roc_output):
        column_first_array = column_first_array + _collapse_single_roc(single_roc_output, variable_names[index])
    return column_first_array


def _collapse_single_roc(single_roc_output, variable_name):
    return [
        [variable_name, 'FPR'] + single_roc_output['fpr'].tolist(),
        [single_roc_output['auc'], 'TPR'] + single_roc_output['tpr'].tolist(),
        ['', 'Thresholds'] + single_roc_output['thresholds'].tolist()
    ]

'''
def _format_single_roc(single_roc_output, variable_name):
    return [[variable_name], ['FPR', 'TPR', 'Thresholds']] + transpose([
        single_roc_output['fpr'],
        single_roc_output['tpr'],
        single_roc_output['thresholds']
    ])
'''