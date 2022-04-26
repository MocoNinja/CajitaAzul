
from blue_st_sdk.node import NodeListener
from sys import exit

"""
    Esta clase "extiende/implementa" (python xdxdxdxdxd) al NodeListener, que es el encargado de recibir las notificaciones del Manager cuando
    * Un nodo cambia el estado
"""
class CustomNodeListener(NodeListener):


    _SE_HA_CASCADO_STATUS_CODE = 10


    def on_connect(self, node):
        print(f"--- SE HA CONECTADO EL DISPOSITIVO: {node.get_name()}")

    
    def on_disconnect(self, node, unexpected = False):
        print(f"--- SE HA DESCONECTADO EL DISPOSITIVO: {node.get_name()}")
        if (unexpected):
            print(f"--- OJO!!!! QUE NO ME LO ESPERABA :(")
            exit(self._SE_HA_CASCADO_STATUS_CODE)
