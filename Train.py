from __future__ import absolute_import, division, print_function, unicode_literals
import serial
from time import sleep
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import csv

import functools

class_names=['left', 'right' 'up', 'down']
#Loading the dataset
filename="training/data_train.csv"
raw_data = open(filename, 'rt')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)
data = np.array(x).astype('float')
print(data.shape)
