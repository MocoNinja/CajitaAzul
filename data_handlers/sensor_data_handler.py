from config.config import *
from config.logger import logging

from model.acceleration import Acceleration
from model.humidity import Humidity
from model.magnetic_field import Magnetic_Field
from model.pressure import Pressure
from model.temperature import Temperature

from mqtt.mqtt import send_message


def handle_sensor_data(feature_name, feature, sample, device_id):
    logging.debug(f"Handle Sensor Data for feature: {feature} (Sample: {sample})")

    if feature_name == "Temperature":
        _handle_temperature(sample, device_id)
    elif feature_name == "Accelerometer":
        _handle_acceleration(sample, device_id)
    elif feature_name == "Pressure":
        _handle_pressure(sample, device_id)
    elif feature_name == "Humidity":
        _handle_humidity(sample, device_id)
    elif feature_name == "Magnetometer":
        _handle_magnetic_field(sample, device_id)


def _handle_temperature(sample, device_id):
    data = Temperature(sample._data[0],
                                sample._timestamp,
                                sample._notification_time,
                                device_id
    )
    send_message(TOPIC_TEMPERATURE, data.to_json())
    

def _handle_acceleration(sample, device_id):
    data = Acceleration(sample._data[0],
                                sample._data[1],
                                sample._data[2],
                                sample._timestamp,
                                sample._notification_time,
                                device_id
    )
    send_message(TOPIC_ACCELERATION, data.to_json())


def _handle_magnetic_field(sample, device_id):
    data = Magnetic_Field(sample._data[0],
                                sample._data[1],
                                sample._data[2],
                                sample._timestamp,
                                sample._notification_time,
                                device_id
    )
    send_message(TOPIC_MAGNETIC_FIELD, data.to_json())


def _handle_pressure(sample, device_id):
    data = Pressure(sample._data[0],
                            sample._timestamp,
                            sample._notification_time,
                            device_id
    )
    send_message(TOPIC_PRESSURE, data.to_json())


def _handle_humidity(sample, device_id):
    data = Humidity(sample._data[0],
                            sample._timestamp,
                            sample._notification_time,
                            device_id
    )
    send_message(TOPIC_HUMIDITY, data.to_json())
