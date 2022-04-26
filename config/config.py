from os import getenv
from typing import final

from .logger import logging

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

TOPIC_ACCEL         : final(str) = getenv("TOPIC_ACCEL")
TOPIC_TEMP          : final(str) = getenv("TOPIC_TEMP")

ALLOWED_DEVICES     : final(list[str]) = getenv("ALLOWED_DEVICES").split(",")