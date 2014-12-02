__author__ = 'timothyahong'
from regression.stabilizers import LinearStabilizer, SigmoidStabilizer
from regression.regression_runners import LinearRegressionRunner
from volume_estimators import SimpleVolumeEstimator
from utilities.experiment_parsers import load_experiment_folder, load_output_folder
from regression.pressure_sensor_regression import run_pressure_sensor_regression
from regression.direct_volume_regression import run_direct_volume_regression
from regression.volume_estimation_regression import run_volume_estimation_regression, run_pre_and_post_regression
from visualization.volume_comparison import generate_volume_comparison, volume_comparison_headers
from visualization.graph_wrappers import plot_volume_comparison
from utilities.csv_helpers import array_to_csv
from simple_estimator.simple_estimator import SimpleEstimator, run_simple_estimator
from cap_vs_pressure.cap_vs_pressure_viewer import plot_multiple_cap_and_pressure_lines

def average(vs):
    return (vs[0]+vs[1])/2

def cutoff1(vs):
    cutoff = 18
    return 1 if vs[0] > cutoff and vs[1] > cutoff else 0

def counter1(vs):
    count = 0
    cutoff = 14
    if vs[0] > cutoff:
        count += 5
    if vs[1] > cutoff:
        count += 5
    return count

file_name = '105_sitting.csv'
line_numbers = [50, 100, 230, 280, 360] #for 105 sitting
#line_numbers = [100, 520, 840, 880, 921] #for 105 standing
#line_numbers = [30, 80, 100, 165, 500] #for 300 standing
#line_numbers = [10, 48, 97, 118, 130, 148] #for 300 sitting
#line_numbers = [50, 133, 198, 263, 296] #for 105 lying
#line_numbers = [14, 63, 101, 126, 161, 184] #for 300 lying

plot_multiple_cap_and_pressure_lines(
    folder_path='/Users/Tim/Google Drive/Sensassure/Venture Related/Product/V4 Prototype/Volume Detection/V4.7/nov24_tim',
    file_name=file_name,
    line_numbers=line_numbers,
    cap_comparator=counter1,
    pressure_comparator=average
)

'''
stabilizer = SigmoidStabilizer()
#stabilizer = BinxLinearStabilizer()
regression_runner = LinearRegressionRunner()
volume_estimator = SimpleVolumeEstimator()

estimator = SimpleEstimator()
#data = load_experiment_folder('/Users/Tim/Google Drive/Sensassure/Venture Related/Product/V4 Prototype/Volume Detection/V4.7/nov22_danny')
#data = load_experiment_folder('/Users/Tim/Google Drive/Sensassure/Venture Related/Product/V4 Prototype/Volume Detection/V4.6/nov19_danny/withOpAmp')
#data = load_experiment_folder('/Users/Tim/Google Drive/Sensassure/Venture Related/Product/V4 Prototype/Volume Detection/V4.7/nov23_danny')
#data = load_experiment_folder('/Users/Tim/Google Drive/Sensassure/Venture Related/Product/V4 Prototype/Volume Detection/V4.7/nov24_tim')

run_pressure_sensor_regression(
    data_files=data['files'],
    data_parameters=data['parameters'],
    stabilizer=stabilizer,
    volume_estimator=volume_estimator,
    regression_runner=regression_runner
)

run_volume_estimation_regression(
    data_files=data['files'],
    data_parameters=data['parameters'],
    stabilizer=stabilizer,
    volume_estimator=volume_estimator,
    regression_runner=regression_runner
)


run_pre_and_post_regression(
    data_files=data['files'],
    data_parameters=data['parameters'],
    stabilizer=stabilizer,
    volume_estimator=volume_estimator,
    regression_runner=regression_runner
)


run_simple_estimator(
    data_files=data['files'],
    data_parameters=data['parameters'],
    estimator=estimator
)

output_data = load_output_folder(data['parameters'], 'output')
volume_comparison_output = generate_volume_comparison(output_data['files'])
plot_volume_comparison(volume_comparison_headers, volume_comparison_output)

array_to_csv(
    'output/volume_comparison.csv',
    header_row=volume_comparison_headers,
    rows=volume_comparison_output
)


run_direct_volume_regression(
    data_files=data['files'],
    data_parameters=data['parameters'],
    stabilizer=stabilizer,
    regression_runner=regression_runner
)
'''