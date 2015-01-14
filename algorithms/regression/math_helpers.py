__author__ = 'Tim'
import math
import numpy


def sigmoid_of_all_values_with_all_other_values(values, start, end):
    sigmoid_products = []
    for value_list in values:
        sigmoid_products += sigmoid_product_with_other_sensor_values(value_list, values, start, end)
    return sigmoid_products


def sigmoid_product_with_other_sensor_values(sigmoid_target_values, other_sensor_values, start, end):
    sigmoid_values = sigmoid_dataset(sigmoid_target_values, start, end)
    sigmoid_products = multi_dot(other_sensor_values, sigmoid_values)
    return sigmoid_products


def sigmoid_dataset(x_values, start, end):
    return [
        sigmoid(x, start, end) for x in x_values
    ]


def sigmoid(x, start, end):
    diff = float(end) - float(start)
    a = 10.0/diff
    b = start + diff/2
    exponentee = -a*(x-b)
    return 1/(1+math.exp(exponentee))


def multi_dot(xs, y):
    return [
        numpy.multiply(x, y) for x in xs
    ]


def transpose(target_arr):
    return zip(*target_arr)