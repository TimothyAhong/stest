__author__ = 'timothyahong'


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