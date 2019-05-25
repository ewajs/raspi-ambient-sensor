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
while True:
	hum, temp = Adafruit_DHT.read_retry(11,4)
	print('Temp: {0:0.1f} C  Hum: {1:0.1f} %'.format(temp, hum))
	c = conn.cursor()
	c.execute('''INSERT INTO Ambient (Humidity,Temperature) VALUES
		({0:0.1f},{1:0.1f})'''.format(hum,temp))
	conn.commit()
	time.sleep(300)
