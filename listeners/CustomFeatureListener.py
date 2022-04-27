from blue_st_sdk.feature import FeatureListener

from data_handlers.sensor_data_handler import handle_sensor_data

from config.config import DATA_SAMPLING_LIMITATIONS
"""
    Esta clase "extiende/implementa" al FeatureListener, que es el encargado de recibir las notificaciones que manda el Feature cuando se ha actualizado
"""
class CustomFeatureListener(FeatureListener):


    def __init__(self, device_id):
        self.device_id = device_id
        self.handled_features = DATA_SAMPLING_LIMITATIONS


    def on_update(self, feature, sample):
        feature_name = feature.get_name()
        if feature_name in self.handled_features:
            max_ticks = self.handled_features[feature_name][0]
            ticks = self.handled_features[feature_name][1]
            ticks += 1
            if ticks == max_ticks:
                self.handled_features[feature_name][1] = 0
                handle_sensor_data(feature_name, feature, sample, self.device_id)
            else:
                self.handled_features[feature_name][1] = ticks
        else:
            handle_sensor_data(feature_name, feature, sample, self.device_id)
