from datetime import datetime
from json     import dumps

from model.json.json_converter import sensor_converter

class Temperature:

    def __init__(self, temperature_value, id, timestamp):
        self.id = id
        self.temperature_value = float(temperature_value)
        self.st_timestamp = timestamp
        self.py_timestamp = datetime.now()
        self.unit = "ºC"

    
    def to_json(self):
        return dumps(self.__dict__, default = sensor_converter)

    