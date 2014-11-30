__author__ = 'timothyahong'
from utilities.extractors import extract_cap_values, extract_other_sensors, volume_from_filename
from post_process import print_results
from utilities.csv_helpers import array_to_csv
from regression.math_helpers import transpose


def run_direct_volume_regression(data_files, data_parameters, stabilizer, regression_runner):
    #we want to build a big list of the volumes as the y and all of the sensors and fuctions as the xs
    volume_array = []
    format_length = len(stabilizer.generate_input_titles(data_parameters['Format']))
    regression_xs = [[]]*format_length

    for (data_file_name, data_file) in data_files.items():
        if len(data_file) > 0:
            volume = volume_from_filename(data_file_name)
            volume_array += [volume]*len(data_file[0])
            #get our inputs from all sensor data and append to our big mondo list
            for index, x_input_for_volume in enumerate(stabilizer.generate_inputs([], data_file)):
                #append this x for this volume to the list currently maintained by regression_xs
                #for some reason we get a couple extra values randomly...
                if index < format_length:
                    regression_xs[index] = regression_xs[index] + list(x_input_for_volume)

    #now run regression on this bro
    regression_results = regression_runner.run([volume_array], regression_xs)
    merged_array = [volume_array, regression_results['stabilized_caps'][0]]
    array_to_csv('output/direct_regression.csv', ['volume', 'estimated_volume'], transpose(merged_array))


