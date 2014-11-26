__author__ = 'Tim'
from utilities.extractors import extract_cap_values, extract_other_sensors
from post_process import print_volume_estimate_and_sensor_data


def run_simple_estimator(data_files, data_parameters, estimator):
    volume_results = {}
    sensor_data = {}
    for (data_file_name, data_file) in data_files.items():
        if len(data_file) > 0:
            cap_values = extract_cap_values(data_parameters, data_file)
            sensor_data[data_file_name] = extract_other_sensors(data_parameters, data_file)
            volume_results[data_file_name] = call_with_cap_value_row(
                estimator.estimate,
                cap_values,
                sensor_data[data_file_name]
            )

    print_volume_estimate_and_sensor_data(
                  data_files=data_files,
                  parameters=data_parameters,
                  volume_results=volume_results,
    )


def call_with_cap_value_row(fun, cap_values, sensor_data):
    volume_estimates = []
    for index, c in enumerate(cap_values[0]):
        cap_row = generate_value_row(index, cap_values)
        sensor_row = generate_value_row(index, sensor_data)
        volume_estimate = fun(cap_row, sensor_row)
        volume_estimates.append(volume_estimate)
    return volume_estimates

def generate_value_row(index, values):
    return [
        sensor[index] for sensor in values
    ]


class SimpleEstimator:
    cap_sensor_base_modification = [-1, -2, -2, -4, -4, -3, -3, -2, -4, -1]

    def estimate(self, cap_values, sensor_data):
        adjusted_values = self._adjust_for_baseline(cap_values)
        return self.estimate_volume(adjusted_values, sensor_data)

    def estimate_volume(self, cap_values, sensor_data):
        adjusted_values = self._adjust_for_baseline(cap_values)
        return self.product_of_pairs_estimation(adjusted_values, 100)

    def product_of_pairs_estimation(self, cap_values, volume_per_pair):
        above_threshold = self.count_above_threshold(cap_values, 5, 11)
        return above_threshold['pairs']*volume_per_pair + above_threshold['singles']*volume_per_pair/4

    def count_above_threshold(self, cap_values, num_caps_per_row, threshold):
        pairs_above_threshold = 0
        singles_above_threshold = 0
        left_caps = cap_values[:num_caps_per_row]
        right_caps = cap_values[num_caps_per_row:]
        for (i, left_cap_value) in enumerate(left_caps):
            right_cap_value = right_caps[i]
            if self.pair_above_threshold(left_cap_value, right_cap_value, threshold):
                pairs_above_threshold += 1
            elif self.single_above_threshold(left_cap_value, right_cap_value, threshold):
                singles_above_threshold += 1
        return {
            'pairs': pairs_above_threshold,
            'singles': singles_above_threshold
        }

    def pair_above_threshold(self, left_cap_value, right_cap_value, threshold):
        return left_cap_value > threshold and right_cap_value > threshold

    def single_above_threshold(self, left_cap_value, right_cap_value, threshold):
         return left_cap_value > threshold or right_cap_value > threshold

    def _adjust_for_baseline(self, cap_values):
        return [sum(x) for x in zip(cap_values, self.cap_sensor_base_modification)]
