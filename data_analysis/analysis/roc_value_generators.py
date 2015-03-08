__author__ = 'timothyahong'
import math


def impedance(row):
    return row[4]


def admittance(row):
    return 1/impedance(row)


def phase(row):
    return row[5]


def negative_phase(row):
    return -phase(row)


def resistance(row):
    return impedance(row)*math.cos(radians(row))


def conductance(row):
    return 1/resistance(row)


def reactance(row):
    return impedance(row)*math.sin(radians(row))


def radians(row):
    return math.radians(phase(row))