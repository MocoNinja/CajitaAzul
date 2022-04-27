from os import getenv
from typing import final

from config.logger import logging

"""
    This file sets the configuration (variables) through ENV variables.
    This files reads the .env file if present (not running in a docker container for example).
"""
try:
    from dotenv import load_dotenv

    load_dotenv()
    logging.info("Cargado fichero .env con éxito...")

except Exception as e:
    logging.error(f"Error cargando el entorno: {e}")
    logging.error("No estamos usando dotenv porque no estamos en local...")
    logging.error("Las variables de entorno están fijadas entonces en el lanzamiento del contenedor...")

MQTT_CLIENT         : final(str) = getenv("MQTT_CLIENT")
MQTT_BROKER_URL     : final(str) = getenv("MQTT_BROKER_URL")
MQTT_BROKER_PORT    : final(int) = int(getenv("MQTT_BROKER_PORT"))
MQTT_USER_NAME      : final(str) = getenv("MQTT_USER_NAME")
MQTT_USER_PASS      : final(str) = getenv("MQTT_USER_PASS")

TOPIC_ACCELERATION         : final(str) = getenv("TOPIC_ACCELERATION")
TOPIC_TEMPERATURE          : final(str) = getenv("TOPIC_TEMPERATURE")
TOPIC_MAGNETIC_FIELD       : final(str) = getenv("TOPIC_MAGNETIC_FIELD")
TOPIC_PRESSURE             : final(str) = getenv("TOPIC_PRESSURE")
TOPIC_HUMIDITY             : final(str) = getenv("TOPIC_HUMIDITY")

RETRIES                    : final(int) = int(getenv("RETRIES"))

ALLOWED_DEVICES     : final(list[str]) = getenv("ALLOWED_DEVICES").split(",")

# Limitación del event handling de cada feature
## Key: el feature name
## Value una dupla [TICKS_MAXIMOS, 0]
## El 0 se usa para llevar un conteo de los actuales
DATA_SAMPLING_LIMITATIONS = {
            "Accelerometer": [320,0],
            "Magnetometer":  [180,0],
            "Temperature":   [10,0],
            "Pressure":      [15,0],
            "Humidity":      [15,0],
}

ERROR_CODE_NODE_DISCONNECTED = 10
ERROR_CODE_UNKNOWN_ERROR     = 2 
OK_CODE_OK                   = 0