from datetime import datetime
from json     import dumps

from model.json.json_converter import sensor_converter

class Pressure:

    def __init__(self, val, id, timestamp, device_id):
        self.id = id
        self.val = float(val)
        self.st_timestamp = timestamp
        self.py_timestamp = datetime.now()
        self.unit = "mBar"
        self.device_id = device_id
        self.magnitude = "pressure"

    
    def to_json(self):
        return dumps(self.__dict__, default = sensor_converter)

    