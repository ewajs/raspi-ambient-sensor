# PPS - Ezequiel Wajs - UTN FRBA

El siguiente proyecto es un sensor para un invernadero didáctico realizado para la Escuela ORT en el marco de la Práctica Profesional Supervisada (PPS) de la especialidad de Ingeniería Electrónica de la UTN FRBA. Los parámetros sensados por el sistema son la Temperatura y la Humedad del medio ambiente.

La aplicación está diseñada para ser utilizada de manera remota y por lo tanto no es necesario que la Raspberry PI 3 esté conectada a un Monitor u otro periférico (más allá del sensor). El único requisito es que la misma esté conectada a la red, ya sea cableada o por Wi Fi para poder ser accedida.

La administración del sistema puede hacerse a través de SSH por red y el consumo de la aplicación como cliente puede hacerse a través de un Navegador Web ya sea mediante acceder a la IP de la Raspberry o (preferentemente) seteando un DNS local que permita resolver dicha IP Privada.

El siguiente repositorio incluye todos los archivos necesarios para instalar y correr la aplicación, que se compone de tres módulos lógicos:

- El sistema de adquisición.
- La base de datos.
- El servidor web que presenta los resultados.

## Conexionado

- El Pin `+` del sensor se conecta al Pin 4 de la RPI3 (5 VDC).
- El Pin `-` del sensor se conecta al Pin 6 de la RPI3 (GND).
- El Pin `out` del sensor se conecta al Pin 7 de la RPI3 (GPIO04).

## Instalación

El sistema está preparado para correr sobre una Raspberry PI corriendo Raspbian (distribución de Linux oficial de la plataforma).
Los únicos prerrequisitos son clonar el repositorio y tener Docker y Docker Compose instalados en la Raspberry, para eso:

```
git clone https://github.com/ewajs/raspi-ambient-sensor.git
cd raspi-ambient-sensor
sudo install.sh
```

## Inicialización

Para incializar el sistema, se provee del archivo `docker-compose.yml`, que contiene toda la configuración necesaria para que los containers se inicialicen y la base de datos se monte adecuadamente. Por lo tanto para inicializar tanto el sistema de adquisición como el servidor web (ambos conectados a la base de datos) basta con:

```
docker-compose up
```

## Cierre de la aplicación

Para cerrar adecuadamente los containers ingresar el comando:

```
docker-compose down
```
