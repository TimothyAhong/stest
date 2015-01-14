__author__ = 'Tim'
from utilities.experiment_parsers import load_experiment_folder
from utilities.extractors import extract_cap_values, extract_pressure_values, extract_sensor_value_row, sensor_row_to_pairs
from visualization.graph_wrappers import plot_multiple_lines
'/Users/Tim/Google Drive/Sensassure/Venture Related/Product/V4 Prototype/Volume Detection/V4.7/nov24_tim'


def plot_multiple_cap_and_pressure_lines(folder_path, file_name, line_numbers, cap_comparator, pressure_comparator):
    [
        plot_cap_and_pressure_lines(
            folder_path,
            file_name,
            line_number,
            cap_comparator,
            pressure_comparator
        ) for line_number in line_numbers
    ]


def plot_cap_and_pressure_lines(folder_path, file_name, line_number, cap_comparator, pressure_comparator):
    cap_and_pressures = get_cap_and_pressure_lines(folder_path, file_name, line_number, cap_comparator, pressure_comparator)
    plot_multiple_lines([cap_and_pressures['cap'], cap_and_pressures['pressure']], ['caps', 'pressure'])


def get_cap_and_pressure_lines(folder_path, file_name, line_number, cap_comparator, pressure_comparator):
    data = load_experiment_folder(folder_path)
    data_file = data['files'][file_name]
    cap_values = extract_cap_values(data['parameters'], data_file)
    pressure_values = extract_pressure_values(data['parameters'], data_file)
    cap_pairs = get_sensor_pairs(cap_values, line_number)
    pressure_pairs = get_sensor_pairs(pressure_values, line_number)
    return {
        'cap': [cap_comparator(cap_pair) for cap_pair in cap_pairs],
        'pressure': process_pressure_values([pressure_comparator(pressure_pair) for pressure_pair in pressure_pairs])
    }


def process_pressure_values(pressure_values):
    #add a 0 to the beginning
    scale = 10
    return [0] + [
        pressure_val/scale for pressure_val in pressure_values
    ]


def get_sensor_pairs(sensor_values, line_number):
    sensor_row = extract_sensor_value_row(sensor_values, line_number)
    return sensor_row_to_pairs(sensor_row)