__author__ = 'timothyahong'
import extract


def _run_value_generator(data_rows, value_generator):
    #run the value generator on each row
    return [value_generator(row) for row in data_rows]


def generate_roc_groups_from_formatted_array(formatted_data_array, positive_statuses, negative_statuses, target_frequency, value_generator):
    formatted_data = extract.single_frequency_from_formatted(formatted_data_array, target_frequency)
    positive_data_rows = extract.rows_by_status_from_formatted(formatted_data, positive_statuses)
    negative_data_rows = extract.rows_by_status_from_formatted(formatted_data, negative_statuses)

    '''
    print("Positive Length:" + str(len(positive_data_rows)))
    print("Negative Length:" + str(len(negative_data_rows)))
    print("Total Length:" + str(len(formatted_data)))
    '''

    return  _run_value_generator(positive_data_rows, value_generator), _run_value_generator(negative_data_rows, value_generator)