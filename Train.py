import serial
from time import sleep
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from __future__ import absolute_import, division, print_function, unicode_literals
import functools


print(tf.__version__)

class_names=['left', 'right' 'up', 'down']
#Loading the dataset


model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10)
])
