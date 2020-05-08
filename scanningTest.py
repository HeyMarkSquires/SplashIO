import serial
from time import sleep
import numpy as np
import pickle

filename = 'finalised_model.sav'
model = pickle.load(open(filename, 'rb'))
ser = serial.Serial('COM16', 9600)

def parser(data):
    sList=data.split()
    x=list(map(float, sList))
    result=np.array(x)
    return result

count=0
state=np.zeros((20,4))

while count<20:
            val=ser.readline().decode("utf-8")
            x=parser(val)
            state[count]=x
            if count<19:
                count+=1
            else:
                g=state.flatten()
                c=np.array([g])
                print(c)
                count=0
                prediction=model.predict(c)
                print(np.argmax(prediction))
