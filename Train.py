from __future__ import absolute_import, division, print_function, unicode_literals
import serial
from time import sleep
import csv
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import functools
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import pickle


class_names=['left', 'right' 'up', 'down', 'resting', 'swirling', 'drop', 'take']
col_names=["type", "1sen1", "2sen1", "3sen1", "4sen1",  "1Sen2", "2sen2", "3sen2", "4sen2",  "1sen3", "2sen3", "3sen3", "4sen3",
         "1sen4", "2sen4", "3sen4", "4sen4",  "1Sen5", "2sen5", "3sen5", "4sen5",  "1sen6", "2sen6", "3sen6", "4sen6",
         "1sen7", "2sen7", "3sen7", "4sen7",  "1Sen8", "2sen8", "3sen8", "4sen8",  "1Sen9", "2sen9", "3sen9", "4sen9",
         "1sen10", "2sen10", "3sen10", "4sen10",  "1sen11", "2sen11", "3sen11", "4sen11",  "1sen12", "2sen12", "3sen12", "4sen12",
         "1sen13", "2sen13", "3sen13", "4sen13",  "1sen14", "2sen14", "3sen14", "4sen14",  "1sen15", "2sen15", "3sen15", "4sen15",
         "1sen16", "2sen16", "3sen16", "4sen16",  "1sen17", "2sen17", "3sen17", "4sen17",  "1sen18", "2sen18", "3sen18", "4sen18",
         "1sen19", "2sen19", "3sen19", "4sen19",  "1sen20", "2sen20", "3sen20", "4sen20"]
#Loading the dataset
filename="data.csv"
df=pd.read_csv(filename)
dataset=df.values
#splitting the dataset into input features (x) and features we wish to predict(y)
inX=dataset[:,1:81]
outY=dataset[:,0:1]
#preprocessing the data

X_train, X_val_and_test, Y_train, Y_val_and_test =train_test_split(inX, outY, test_size=0.3)

X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)

print(inX)
print(outY)

#Defining the model
model = Sequential()
model.add(Dense(32, activation="relu", input_dim=80))
model.add(Dense(32, activation="relu"))
model.add(Dense(32, activation="relu"))
model.add(Dense(1, activation="sigmoid"))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(inX, outY, epochs=50, batch_size=10)
_, accuracy = model.evaluate(inX, outY, verbose=0)
print(accuracy)
print('Accuracy: %.2f' % (accuracy*100))

# save the model to disk
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))

