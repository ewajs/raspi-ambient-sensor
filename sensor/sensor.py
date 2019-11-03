import sys
import Adafruit_DHT
import sqlite3
import time

# Setup DB
conn = sqlite3.connect('temphum.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS Ambient 
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    Temperature REAL NOT NULL,
    Humidity REAL NOT NULL,
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
conn.commit()
DATA_TIME = 300 # In seconds
MEASUREMENTS_PER_INTERVAL = 50 
MEASUREMENT_TIME = DATA_TIME // MEASUREMENTS_PER_INTERVAL

measurements = []
start = time.time()    
while True:
    start_measure = time.time()
    t = Adafruit_DHT.read_retry(11,4)
    elapsed_measure = time.time() - start_measure
    measurements.append(t)
    print('Temp: {0:0.3f} C  Hum: {1:0.3f} %'.format(t[1], t[0]))
    if len(measurements) == MEASUREMENTS_PER_INTERVAL:
        avg_hum = sum([t[0] for t in measurements])/MEASUREMENTS_PER_INTERVAL
        avg_temp = sum([t[1] for t in measurements])/MEASUREMENTS_PER_INTERVAL
        print('Temp: {0:0.3f} C  Hum: {1:0.3f} %'.format(avg_temp, avg_hum))
        # Insert into DB
        c = conn.cursor()
        c.execute('''INSERT INTO Ambient (Humidity,Temperature) VALUES
        ({0:0.3f},{1:0.3f})'''.format(avg_hum,avg_temp))
        conn.commit()
        # Reset queue
        elapsed = time.time() - start
        print("Total elapsed time: " + str(elapsed))
        start = time.time()
        measurements = []
    if MEASUREMENT_TIME - elapsed_measure > 0:
        time.sleep(MEASUREMENT_TIME - elapsed_measure)
