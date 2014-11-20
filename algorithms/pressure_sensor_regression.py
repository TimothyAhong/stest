__author__ = 'timothyahong'
from extractors import extract_cap_values, extract_other_sensors
from post_process import print_results


def run_pressure_sensor_regression(data_files, data_parameters, stabilizer, volume_estimator, regression_runner):
    regression_results = {}
    stabilized_volume_results = {}
    volume_results = {}
    sensor_data = {}
    for (data_file_name, data_file) in data_files.items():
        if len(data_file) > 0:
            cap_values = extract_cap_values(data_parameters, data_file)
            sensor_data[data_file_name] = extract_other_sensors(data_parameters, data_file)
            regression_xs = stabilizer.generate_inputs(cap_values, sensor_data[data_file_name])
            regression_results[data_file_name] = regression_runner.run(cap_values, regression_xs)
            stabilized_volume_results[data_file_name] = volume_estimator.estimate(regression_results[data_file_name]['stabilized_caps'])
            volume_results[data_file_name] = volume_estimator.estimate(cap_values)

    print_results(regression_results=regression_results,
                  data_files=data_files,
                  parameters=data_parameters,
                  volume_results=volume_results,
                  stabilized_volume_results=stabilized_volume_results
    )

