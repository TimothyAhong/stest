__author__ = 'timothyahong'
import numpy
from math_helpers import sigmoid_of_all_values_with_all_other_values


class BaseStabilizer:
    def generate_inputs(self, data_parameters, data_file):
        pass


#simple stabilizer, simply returns the sensor values ie: runs linear regression
class LinearStabilizer(BaseStabilizer):
    def __init__(self):
        pass

    def generate_inputs(self, cap_values, other_sensor_values):
        regression_xs = [
            other_sensor_value for other_sensor_value in other_sensor_values
        ]
        #for other_sensor_value in other_sensor_values:
        return regression_xs

    def generate_input_titles(self, sensor_names):
        return [
            sensor_name for sensor_name in sensor_names
        ]


class BinxLinearStabilizer(LinearStabilizer):
    def generate_inputs(self, cap_values, other_sensor_values):
        linear_xs = LinearStabilizer.generate_inputs(self,cap_values, other_sensor_values)
        linear_xs.append(numpy.multiply(other_sensor_values[0],other_sensor_values[1]))
        return linear_xs


class SigmoidStabilizer(LinearStabilizer):
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