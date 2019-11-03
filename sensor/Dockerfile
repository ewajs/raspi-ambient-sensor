FROM frankwolf/rpi-python3

RUN pip3 install --upgrade setuptools \
    && pip3 install Adafruit_DHT

COPY sensor/sensor.py sensor.py

CMD ["python3", "sensor.py"]