__author__ = 'timothyahong'
from sklearn import metrics
import numpy


def _generate_scores(positive_values, negative_values):
    #concat the list with positives first
    all_values = positive_values + negative_values
    #this assumes that all values increase when going from negative case to positive case
    return [
        value for value in all_values
    ]


def _generate_y(positive_values, negative_values):
    #the lib requires 0 for false and 1 for positive
    positive_y = numpy.ones(len(positive_values), dtype=numpy.int).tolist()
    negative_y = numpy.zeros(len(negative_values), dtype=numpy.int).tolist()
    #the associated scores will have positives first
    return positive_y + negative_y


def generate_roc(positive_values, negative_values):
    scores = _generate_scores(positive_values, negative_values)
    y = _generate_y(positive_values, negative_values)
    fpr, tpr, thresholds = metrics.roc_curve(y, scores)
    auc = metrics.roc_auc_score(y, scores)
    return fpr, tpr, thresholds, auc

