import paho.mqtt.client as mqtt

from config.config import MQTT_BROKER_PORT, MQTT_BROKER_URL, MQTT_CLIENT, MQTT_USER_NAME, MQTT_USER_PASS

client = mqtt.Client(MQTT_CLIENT)

client.username_pw_set(MQTT_USER_NAME, MQTT_USER_PASS)

client.connect(MQTT_BROKER_URL, MQTT_BROKER_PORT)


def send_message(topic, mensaje):
    print(f"Enviando al topic {topic} el mensaje {mensaje}")
    # TODO: posible configuración
    client.publish(topic, mensaje, qos=1, retain=True)