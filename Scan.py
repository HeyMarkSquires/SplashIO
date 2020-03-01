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
#Checking if data.csv already exists. If it doesn't, initialise the headers
headers=["Type", "1Sen1", "2sen1", "3sen1", "4sen1",  "1Sen2", "2sen2", "3sen2", "4sen2",  "1Sen3", "2sen3", "3sen3", "4sen3",
         "1Sen4", "2sen4", "3sen4", "4sen4",  "1Sen5", "2sen5", "3sen5", "4sen5",  "1Sen6", "2sen6", "3sen6", "4sen6",
         "1Sen7", "2sen7", "3sen7", "4sen7",  "1Sen8", "2sen8", "3sen8", "4sen8",  "1Sen9", "2sen9", "3sen9", "4sen9",
         "1Sen10", "2sen10", "3sen10", "4sen10",  "1Sen11", "2sen11", "3sen11", "4sen11",  "1Sen12", "2sen12", "3sen12", "4sen12",
         "1Sen13", "2sen13", "3sen13", "4sen13",  "1Sen14", "2sen14", "3sen14", "4sen14",  "1Sen15", "2sen15", "3sen15", "4sen15",
         "1Sen16", "2sen16", "3sen16", "4sen16",  "1Sen17", "2sen17", "3sen17", "4sen17",  "1Sen18", "2sen18", "3sen18", "4sen18",
         "1Sen19", "2sen19", "3sen19", "4sen19",  "1Sen20", "2sen20", "3sen20", "4sen20"]
with open('data.csv', 'a', newline='') as file:
    wr=csv.writer(file, quoting=csv.QUOTE_ALL)
    wr.writerow(headers)
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
        with open('data.csv', 'a', newline='') as file:
                  wr=csv.writer(file, quoting=csv.QUOTE_ALL)
                  wr.writerow(r)
    sleep(.1)
    
