from blue_st_sdk.manager import ManagerListener

from config.logger import logging

"""
    Esta clase "extiende/implementa" al ManagerListener, que es el encargado de recibir las notificaciones del Manager cuando
    * Se descubre un nuevo nodo
    * El scanning empieza / para
"""
class CustomManagerListener(ManagerListener):


    def on_discovery_change(self, manager, enabled):
        if enabled:
            status = "STARTED"
        else:
            status = "STOPPED"

        logging.info(f"=== CAMBIO DETECTADO. Estado: {status} ")



    def on_node_discovered(self, manager, node):
        logging.info(f"=== NODO DETECTADO. Nombre: {node.get_name()}")
