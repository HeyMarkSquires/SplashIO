from __future__ import absolute_import, division, print_function, unicode_literals
import serial
from time import sleep
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import csv
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Convolution2D
from keras.layers.convolutional import MaxPooling2D
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from keras import backend as K
from subprocess import check_output

import functools

class_names=['left', 'right' 'up', 'down', 'resting', 'swirling', 'drop', 'take']
#Loading the dataset
filename="training/data_train.csv"
train = pd.read_csv(filename)
train['Type']='Train'

#Defining the model
model = Sequential()
model.add(Dense(100, input_dim=11, activation="relu"))
model.add(Dense(50, activation="relu"))
model.add(Dense(1))
model.summary()
model.compile(loss= "mean_squared_error" , optimizer="adam", metrics=["mean_squared_error"])
model.fit(X_train, y_train, epochs=10)
