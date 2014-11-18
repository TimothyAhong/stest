__author__ = 'timothyahong'
from extractors import extract_cap_values, extract_other_sensors
from post_process import print_results
from stabilizers import LinearStabilizer
from regression_runners import LinearRegressionRunner
from volume_estimators import SimpleVolumeEstimator
from experiment_parsers import load_experiment_folder



def run_pressure_sensor_regression(data_files, data_parameters, stabilizer, volume_estimator, regression_runner):
    regression_results = {}
    volume_results = {}
    for data_file in data_files:
        cap_values = extract_cap_values(data_parameters, data_file)
        other_sensor_values = extract_other_sensors(data_parameters, data_file)
        regression_xs = stabilizer.generate_inputs(cap_values, other_sensor_values)
        regression_results[data_file] = regression_runner.run(cap_values, regression_xs)
        volume_results[data_file] = volume_estimator.estimate(stabilized_cap_values)
    print_results(regression_results, volume_results)


stabilizer = LinearStabilizer()
regression_runner = LinearRegressionRunner()
volume_estimator = SimpleVolumeEstimator()
data = load_experiment_folder('path')
run_pressure_sensor_regression(
    data_files=data['files'],
    data_parameters=data['parameters']
)


