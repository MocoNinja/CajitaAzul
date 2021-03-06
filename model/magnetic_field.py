from datetime import datetime
from json     import dumps

from model.json.json_converter import sensor_converter

class Magnetic_Field:

    def __init__(self, x_val, y_val, z_val, id, timestamp, device_id):
        self.id = id
        self.x_val = float(x_val)
        self.y_val = float(y_val)
        self.z_val = float(z_val)
        self.st_timestamp = timestamp
        self.py_timestamp = datetime.now()
        self.unit = "mGa"
        self.device_id = device_id
        self.magnitude = "magnetic_field"

    
    def to_json(self):
        return dumps(self.__dict__, default = sensor_converter)

    