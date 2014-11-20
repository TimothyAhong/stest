__author__ = 'timothyahong'
from stabilizers import LinearStabilizer
from regression_runners import LinearRegressionRunner
from volume_estimators import SimpleVolumeEstimator
from experiment_parsers import load_experiment_folder, load_output_folder
from pressure_sensor_regression import run_pressure_sensor_regression
from visualization.volume_comparison import generate_volume_comparison, volume_comparison_headers
from csv_helpers import array_to_csv

stabilizer = LinearStabilizer()
regression_runner = LinearRegressionRunner()
volume_estimator = SimpleVolumeEstimator()
data = load_experiment_folder('/Users/timothyahong/Google Drive/Sensassure/Venture Related/Product/V4 Prototype/Volume Detection/V4.5/nov17_danny/wearing')

run_pressure_sensor_regression(
    data_files=data['files'],
    data_parameters=data['parameters'],
    stabilizer=stabilizer,
    volume_estimator=volume_estimator,
    regression_runner=regression_runner
)

output_data = load_output_folder(data['parameters'], 'output')
volume_comparison_output = generate_volume_comparison(output_data['files'])

array_to_csv(
    'output/volume_comparison.csv',
    header_row=volume_comparison_headers,
    rows=volume_comparison_output
)