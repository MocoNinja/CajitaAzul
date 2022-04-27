import logging

from datetime import datetime
from sys import stdout
from typing import final

"""
    This file setups and configures the logger
"""
FORMAT = '%(asctime)s | LOGGER: %(name)s |  %(levelname)s: %(message)s'
LEVEL = logging.INFO

date: final(str) = datetime.now().isoformat().replace(":", ".")
filename: final(str) = f"./log/log_{date}.log"

logging.basicConfig(format=FORMAT, level=LEVEL)
