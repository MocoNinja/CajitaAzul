from datetime import datetime

from blue_st_sdk.feature import FeatureListener

from data_handlers.sensor_data_handler import handle_sensor_data, DATA

"""
    Esta clase "extiende/implementa" (python xdxdxdxdxd) al FeatureListener, que es el encargado de recibir las notificaciones que manda el Feature cuando se ha actualizado
"""
class CustomFeatureListener(FeatureListener):

    def on_update(self, feature, sample):
        if feature.get_name() == "Accelerometer":
            handle_sensor_data(DATA.ACCELERATION, feature, sample)
        elif feature.get_name() == "Temperature": 
            handle_sensor_data(DATA.TEMPERATURE, feature, sample)

