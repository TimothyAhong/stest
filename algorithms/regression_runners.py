__author__ = 'timothyahong'
from sklearn import linear_model
import numpy


class BaseRegressionRunner:
    def run(self, ys, xs):
        pass


class LinearRegressionRunner(BaseRegressionRunner):
    def __init__(self):
        pass

    def run(self, ys, xs):
        #clf = linear_model.LinearRegression(fit_intercept=False), dont know what the point of this is
        clf = linear_model.LinearRegression()
        regression_details = {
            'stabilized_caps': [],
            'slopes': []
        }
        for y in ys:
            clf.fit(xs, y)
            #stabilized cap array of the form [cap_sensor_number][stabilized_cap_list]
            regression_details['stabilized_caps'].append(self._stabilize_cap_sensors(clf.coef_, y, xs))
            #slope array of the form [cap_sensor_number][regression_slopes]
            regression_details['slopes'].append(clf.coef_)

    def _stabilize_cap_sensors(self, coefs, y, xs):
        stabilized_caps = []
        #return a new set for y with modified values
        for index, cap_value in enumerate(y):
            sensor_values = [x[index] for x in xs]
            stabilized_caps.append(cap_value - numpy.dot(coefs,sensor_values))
        return stabilized_caps