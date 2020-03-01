#This file is used to scan in the readings from the ultrasonic sensor and
#store them within a csv file which will be used for training the neural
#network.
import serial
from time import sleep
import numpy as np
import tensorflow as tf
import keyboard as kb
from numpy import asarray
from numpy import savetxt
import csv
def parser(data):
    #t=data[:-2]
    sList=data.split()
    x=list(map(float, sList))
    result=np.array(x)
    return result

#Configuring serial connection
ser = serial.Serial('COM9', 9600)
print("Begin")
val=ser.readline().decode("utf-8")
state=np.zeros((20,4))
count=0
#Reading information from the sensors and generating a numpy array to determine
#the state of the pool
while True:
    if kb.is_pressed('q'):
        print("Hello")
    x=parser(val)
    val=ser.readline().decode("utf-8")
    state[count]=x
    if count<19:    
        count+=1
    else:
        g=state.flatten()
        count=0
        #Creating the array that will be written to the csv file
        r=["Hello"]
        for i in range(len(g)):
            r.append(g[i])
        #Writing the file to a csv
        print(r)
        with open('data.csv', 'a') as file:
                  wr=csv.writer(file, quoting=csv.QUOTE_ALL)
                  wr.writerow(r)
    sleep(.1)
    
