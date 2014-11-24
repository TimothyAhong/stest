__author__ = 'timothyahong'
import numpy
from math_helpers import sigmoid_of_all_values_with_all_other_values, sigmoid_dataset


class BaseStabilizer:
    def generate_inputs(self, data_parameters, data_file):
        pass


#simple stabilizer, simply returns the sensor values ie: runs linear regression
class LinearStabilizer(BaseStabilizer):
    def __init__(self):
        pass

    def generate_inputs(self, cap_values, other_sensor_values):
        regression_xs = [
            list(other_sensor_value_list) for other_sensor_value_list in other_sensor_values
        ]
        #for other_sensor_value in other_sensor_values:
        return regression_xs

    def generate_input_titles(self, sensor_names):
        return [
            sensor_name for sensor_name in sensor_names
        ]


class SigmoidStabilizer(LinearStabilizer):
    def __init__(self):
        pass

    def generate_inputs(self, cap_values, other_sensor_values):

        linear_xs = LinearStabilizer.generate_inputs(self, cap_values, other_sensor_values)

        #attempt to cover 2 ranges
        start = 100
        end = 300
        first_regression_pass = [
            sigmoid_dataset(other_sensor_value, start, end) for other_sensor_value in other_sensor_values
        ]

        #attempt to cover 2 ranges
        start = 400
        end = 600
        second_regression_pass = [
            sigmoid_dataset(other_sensor_value, start, end) for other_sensor_value in other_sensor_values
        ]

        return first_regression_pass + second_regression_pass + linear_xs

class BinxLinearStabilizer(LinearStabilizer):
    def generate_inputs(self, cap_values, other_sensor_values):
        linear_xs = LinearStabilizer.generate_inputs(self,cap_values, other_sensor_values)
        linear_xs.append(numpy.multiply(other_sensor_values[0],other_sensor_values[1]))
        return linear_xs


class SigmoidAndLinearStabilizer(LinearStabilizer):
    def generate_inputs(self, cap_values, other_sensor_values):
        linear_xs = LinearStabilizer.generate_inputs(self, cap_values, other_sensor_values)
        sigmoid_xs = sigmoid_of_all_values_with_all_other_values(other_sensor_values, 300, 500)
        return linear_xs + sigmoid_xs

    def generate_input_titles(self, sensor_names):
        linear_titles = LinearStabilizer.generate_input_titles(self, sensor_names)
        sigmoid_titles = self._generate_sigmoid_titles_for_all_sensors(sensor_names)
        return linear_titles + sigmoid_titles

    def _generate_sigmoid_titles_for_all_sensors(self, sensor_names):
        sigmoid_sensor_titles = []
        for sensor_name in sensor_names:
            sigmoid_sensor_titles += self._generate_sigmoid_titles(sensor_name, sensor_names)
        return sigmoid_sensor_titles

    def _generate_sigmoid_titles(self, sigmoid_sensor_name, sensor_names):
        return [
            "sigmoid of (" + sigmoid_sensor_name + ")*" + sensor_name for sensor_name in sensor_names
        ]