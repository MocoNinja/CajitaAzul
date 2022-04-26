from dataclasses import dataclass
from datetime import datetime

def sensor_converter(object):
    if isinstance(object, datetime):
        return object.__str__()