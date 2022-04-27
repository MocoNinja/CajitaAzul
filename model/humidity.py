from datetime import datetime
from json     import dumps

from model.json.json_converter import sensor_converter

class Humidity:

    def __init__(self, val, id, timestamp, device_id):
        self.id = id
        self.val = float(val)
        self.st_timestamp = timestamp
        self.py_timestamp = datetime.now()
        self.unit = "%"
        self.device_id = device_id
        self.magnitude = "humidity"

    
    def to_json(self):
        return dumps(self.__dict__, default = sensor_converter)

    