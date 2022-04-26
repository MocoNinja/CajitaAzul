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

# Configuración de fichero [dejar filename para fichero, None para que no haga fichero]
logging.basicConfig(format=FORMAT, level=LEVEL, filemode='a', filename=None)

# Output también a stdout
handle_stdout = logging.StreamHandler(stdout)
handle_stdout.setLevel(LEVEL)
handle_stdout.setFormatter(logging.Formatter(FORMAT))
logging.getLogger().addHandler(handle_stdout)