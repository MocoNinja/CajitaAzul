from blue_st_sdk.manager import ManagerListener

"""
    Esta clase "extiende/implementa" (python xdxdxdxdxd) al ManagerListener, que es el encargado de recibir las notificaciones del Manager cuando
    * Se descubre un nuevo nodo
    * El scanning empieza / para
"""
class CustomManagerListener(ManagerListener):


    def on_discovery_change(self, manager, enabled):
        if enabled:
            status = "STARTED"
        else:
            status = "STOPPED"

        print(f"=== CAMBIO DETECTADO. Estado: {status} ")



    def on_node_discovered(self, manager, node):
        print(f"=== NODO DETECTADO. Nombre: {node.get_name()}")
