__author__ = 'Tim'
from utilities.extractors import extract_cap_values, extract_other_sensors
from post_process import print_volume_results


#TODO build a list of the cap estimated volumes from the unstabilized results
#TODO run regression on the volumes as y and the inputs as x
def run_volume_estimation_regression(data_files, data_parameters, stabilizer, volume_estimator, regression_runner):
    regression_results = {}
    unstabilized_volume_results = {}
    volume_results = {}
    sensor_data = {}
    for (data_file_name, data_file) in data_files.items():
        if len(data_file) > 0:
            cap_values = extract_cap_values(data_parameters, data_file)
            sensor_data[data_file_name] = extract_other_sensors(data_parameters, data_file)
            unstabilized_volume_results[data_file_name] = volume_estimator.estimate(cap_values)
            regression_xs = stabilizer.generate_inputs(cap_values, sensor_data[data_file_name])
            regression_results[data_file_name] = regression_runner.run([unstabilized_volume_results[data_file_name]], regression_xs)
            volume_results[data_file_name] = regression_results[data_file_name]['stabilized_caps'][0]
    print_volume_results(data_files, data_parameters, volume_results, regression_results)

#TODO run the normal regression (get the stabilized volumes)
#TODO then run regression on those volumes again with the pressure data
def run_pre_and_post_regression(data_files, data_parameters, stabilizer, volume_estimator, regression_runner):
    regression_results_pre = {}
    regression_results_post = {}
    stabilized_volume_results = {}
    volume_results = {}
    sensor_data = {}
    for (data_file_name, data_file) in data_files.items():
        if len(data_file) > 0:

            cap_values = extract_cap_values(data_parameters, data_file)
            sensor_data[data_file_name] = extract_other_sensors(data_parameters, data_file)
            regression_xs = stabilizer.generate_inputs(cap_values, sensor_data[data_file_name])
            regression_results_pre[data_file_name] = regression_runner.run(cap_values, regression_xs)
            stabilized_volume_results[data_file_name] = volume_estimator.estimate(regression_results_pre[data_file_name]['stabilized_caps'])
            volume_results[data_file_name] = volume_estimator.estimate(cap_values)

            regression_results_post[data_file_name] = regression_runner.run([stabilized_volume_results[data_file_name]], regression_xs)
            volume_results[data_file_name] = regression_results_post[data_file_name]['stabilized_caps'][0]
    print_volume_results(data_files, data_parameters, volume_results, regression_results_post)