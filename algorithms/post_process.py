__author__ = 'timothyahong'
import numpy
import csv

def print_results(regression_results, parameters, data_files, volume_results, stabilized_volume_results):
    #TODO determine the differenes and changes in regression variables
    print("REGRESSION RESULTS\n")
    for (data_file_name, regression_result) in regression_results.items():
        print(data_file_name)
        print(regression_result['slopes'])
    print("\nUNSTABILIZED VOLUME RESULTS\n")
    _print_volume_results(data_files, parameters, volume_results)
    print("\nSTABILIZED VOLUME RESULTS\n")
    _print_volume_results(data_files, parameters, stabilized_volume_results)


def _print_volume_results(data_files, parameters, volume_results):
    for data_file_name in sorted(volume_results):
        volume_result = volume_results[data_file_name]
        data_file = data_files[data_file_name]
        print("\n"+data_file_name)
        print("average: {0}".format(numpy.mean(volume_result)))
        print("stdev: {0}".format(numpy.std(volume_result)))
        print("min: {0}".format(numpy.min(volume_result)))
        print("max: {0}".format(numpy.max(volume_result)))
        _output_to_csv("output/"+data_file_name, parameters, data_file, volume_result)


def _output_to_csv(filename, parameters, sensor_data, volume_result):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["Volume"] + parameters["Format"])
        for index, volume in enumerate(volume_result):
            writer.writerow([volume] + [sensor_value_column[index] for sensor_value_column in sensor_data])