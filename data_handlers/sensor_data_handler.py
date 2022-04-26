from enum import Enum

from config.config import TOPIC_ACCEL, TOPIC_TEMP

from model.acceleration import Acceleration
from model.temperature import Temperature

from mqtt.mqtt import send_message


class DATA(Enum):
    ACCELERATION = "acceleration"
    TEMPERATURE  = "temperature"


def handle_sensor_data(data_type: DATA, feature, sample):
    print(f"LLEGA --  FEATURE: {feature} -- SAMPLE {sample}")
    if data_type == DATA.TEMPERATURE:
        _handle_temperature(sample)
    elif data_type == DATA.ACCELERATION:
        _handle_acceleration(sample)


def _handle_temperature(sample):
        data = Temperature(sample._data[0],
                            sample._timestamp,
                            sample._notification_time
        )

        send_message(TOPIC_TEMP, data.to_json())
    
def _handle_acceleration(sample):
        data = Acceleration(sample._data[0],
                                sample._data[1],
                                sample._data[2],
                                sample._timestamp,
                                sample._notification_time
        )

        send_message(TOPIC_ACCEL, data.to_json())