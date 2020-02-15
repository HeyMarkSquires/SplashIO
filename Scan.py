import serial
from time import sleep
import numpy as np
import tensorflow as tf
import keyboard as kb

def parser(data):
    #t=data[:-2]
    sList=data.split()
    x=list(map(float, sList))
    result=np.array(x)
    return result

#Configuring serial connection
ser = serial.Serial('COM9', 9600)
val=ser.readline().decode("utf-8")
state=np.zeros((20,4))
count=0
#Reading information from the sensors and generating a numpy array to determine
#the state of the pool
while True:
    if kb.is_pressed('q'):
        print("Hello")
    x=parser(val)
    print(x)
    '''
    state[count]=x
    print(x)
    if count<20:    
        count+=1
    else:
        print(state)
        count=0
    sleep(.1)'''
    
