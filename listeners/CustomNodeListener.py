from sys import exit

from blue_st_sdk.node import NodeListener

from config.logger import logging
from config.config import ERROR_CODE_NODE_DISCONNECTED

"""
    Esta clase "extiende/implementa" al NodeListener, que es el encargado de recibir las notificaciones del Manager cuando
    * Un nodo cambia el estado (se conecta o se desconecta)
"""
class CustomNodeListener(NodeListener):


    def on_connect(self, node):
        logging.info(f"--- SE HA CONECTADO EL DISPOSITIVO: {node.get_name()}")

    
    def on_disconnect(self, node, unexpected = False):
        logging.info(f"--- SE HA DESCONECTADO EL DISPOSITIVO: {node.get_name()}")
        if (unexpected):
            logging.error(f"--- OJO!!!! DESCONEXIÓN QUE NO SE ESPERABA :(")
            exit(ERROR_CODE_NODE_DISCONNECTED)
