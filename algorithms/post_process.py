__author__ = 'timothyahong'
import numpy

def print_results(regression_results, volume_results, stabilized_volume_results):
    #TODO determine the differenes and changes in regression variables
    print("REGRESSION RESULTS\n")
    for (data_file_name, regression_result) in regression_results.items():
        print(data_file_name)
        print(regression_result['slopes'])
    print("\nUNSTABILIZED VOLUME RESULTS\n")
    _print_volume_results(volume_results)
    print("\nSTABILIZED VOLUME RESULTS\n")
    _print_volume_results(stabilized_volume_results)


def _print_volume_results(volume_results):
    for (data_file_name, volume_result) in volume_results.items():
        print("\n"+data_file_name)
        print("average: {0}".format(numpy.mean(volume_result)))
        print("stdev: {0}".format(numpy.std(volume_result)))
        print("min: {0}".format(numpy.min(volume_result)))
        print("max: {0}".format(numpy.max(volume_result)))