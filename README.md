# Temperature and Humidity Sensoring App for Raspberry Pi

This is a simple script that creates a database and stores time, temperature and humidity using an I2C Sensor hooked to a Raspberry Pi.

Also included, is a flask webserver that will serve the data over HTTP and plot it in a web Browser window.

## Connections
- `+` Pin in the sensor hooks up with RPI3 Pin 4 (5 VDC).
- `-` Pin in the sensor hooks up with RPI3 Pin 6 (GND).
- `out` Pin in the sensor hooks up with RPI3 Pin 7 (GPIO04).

## Running the containers
### With Docker
The sensor container needs acces to the GPIO ports, in order to grant those the container has to be initialized with privileges and the `/dev/mem` volume of the host mounted to the container in the same path:
```
docker container run -it --privileged --device=/dev/mem:/dev/mem ewajs/rpi3sensor
```