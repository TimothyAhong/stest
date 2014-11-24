__author__ = 'timothyahong'
from regression.stabilizers import LinearStabilizer, SigmoidStabilizer
from regression.regression_runners import LinearRegressionRunner
from volume_estimators import SimpleVolumeEstimator
from utilities.experiment_parsers import load_experiment_folder, load_output_folder
from regression.pressure_sensor_regression import run_pressure_sensor_regression
from regression.direct_volume_regression import run_direct_volume_regression
from visualization.volume_comparison import generate_volume_comparison, volume_comparison_headers
from visualization.graph_wrappers import plot_volume_comparison
from utilities.csv_helpers import array_to_csv

stabilizer = LinearStabilizer()
#stabilizer = BinxLinearStabilizer()
regression_runner = LinearRegressionRunner()
volume_estimator = SimpleVolumeEstimator()
#data = load_experiment_folder('/Users/Tim/Google Drive/Sensassure/Venture Related/Product/V4 Prototype/Volume Detection/V4.7/nov22_danny')
data = load_experiment_folder('/Users/Tim/Google Drive/Sensassure/Venture Related/Product/V4 Prototype/Volume Detection/V4.6/nov19_danny/withOpAmp')

run_pressure_sensor_regression(
    data_files=data['files'],
    data_parameters=data['parameters'],
    stabilizer=stabilizer,
    volume_estimator=volume_estimator,
    regression_runner=regression_runner
)

output_data = load_output_folder(data['parameters'], 'output')
volume_comparison_output = generate_volume_comparison(output_data['files'])

plot_volume_comparison(volume_comparison_headers, volume_comparison_output)

array_to_csv(
    'output/volume_comparison.csv',
    header_row=volume_comparison_headers,
    rows=volume_comparison_output
)

'''
run_direct_volume_regression(
    data_files=data['files'],
    data_parameters=data['parameters'],
    stabilizer=stabilizer,
    regression_runner=regression_runner
)
'''