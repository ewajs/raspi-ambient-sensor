import sys
import Adafruit_DHT
import sqlite3
import time

DATA_TIME = 10 # In seconds
MEASURMENTS_PER_INTERVAL = 10 
MEASURMENT_TIME = DATA_INTERVAL // MEASURMENTS_PER_INTERVAL

measurments = []    
while True:
	t = Adafruit_DHT.read_retry(11,4)
    maesurments.append(t)
    print('Temp: {0:0.3f} C  Hum: {1:0.3f} %'.format(t[1], t[0]))
    if len(measurments) == MEASURMENTS_PER_INTERVAL:
        avg_hum = sum([t[0] for t in measurments])/MEASURMENTS_PER_INTERVAL
        avg_temp = sum([t[1] for t in measurments])/MEASURMENTS_PER_INTERVAL
        print('Temp: {0:0.3f} C  Hum: {1:0.3f} %'.format(avg_temp, avg_hum))
        # TODO:  Insert into DB
        # Reset queue
        measurments = []

    time.sleep(MEASURMENT_TIME)
