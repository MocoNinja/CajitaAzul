import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

from config.config import MQTT_BROKER_PORT, MQTT_BROKER_URL, MQTT_CLIENT, MQTT_USER_NAME, MQTT_USER_PASS
from config.logger import logging

client = mqtt.Client(MQTT_CLIENT)

client.username_pw_set(MQTT_USER_NAME, MQTT_USER_PASS)

client.connect(MQTT_BROKER_URL, MQTT_BROKER_PORT)

sent_messages = {}

def send_message(topic, mensaje):
    logging.debug(f"Enviando al topic {topic} el mensaje {mensaje}")
    # TODO: posible configuración
    #client.publish(topic, mensaje, qos=1, retain=True)
    publish.single(topic=topic,
                    payload=mensaje,
                    qos=1,
                    retain=True,
                    hostname=MQTT_BROKER_URL,
                    port=MQTT_BROKER_PORT,
                    auth={
                        "username": MQTT_USER_NAME,
                        "password": MQTT_USER_PASS,
                    }
    )

    if topic in sent_messages:
        sent_messages[topic] = sent_messages[topic] + 1
    else:
        sent_messages[topic] = 0

    logging.info(f"======= Mensajes enviados ========\n{sent_messages}\n====================")