"""http://quantsoftware.gatech.edu/MC1-Homework-1"""

import math as m
import pandas as pd
import numpy as np

# calculate the population standard deviation
def stdev_p(data):
    m1 = data.mean()
    s = 0
    for item in data:
        s = s + (item-m1)*(item-m1)
    std = m.sqrt(s / len(data))
    return std

# calculate the sample standard deviation
def stdev_s(data):
    m1 = data.mean()
    s = 0
    for item in data:
        s = s + (item-m1)*(item-m1)
    std = m.sqrt(s / (len(data)-1))
    return std

if __name__ == "__main__":
    test = [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]
    print "the population stdev is", stdev_p(test)
    print "the sample stdev is", stdev_s(test)