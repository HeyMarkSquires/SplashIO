import serial
from time import sleep
import numpy as np
import tensorflow as tf

def parser(data):
    t=data[:-2]
    x=list(map(int, t.split()))
    result=np.array(x)
    return result

#Configuring serial connection
ser = serial.Serial('COM9', 9600)
val=ser.readline().decode("utf-8")
state=np.zeros((20,4))
print(state)
count=0
#Reading information from the sensors and generating a numpy array to determine
#the state of the pool
while True:
    g=ser.readline().decode("utf-8")
    x=parser(g)
    state[count]=x
    print(x)
    if count<20:    
        count+=1
    else:
        count=0
    sleep(.1)
    
