#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from asyncio.log import logger
from blue_st_sdk.manager import Manager, BlueSTInvalidFeatureBitMaskException

from blue_st_sdk.features import feature_accelerometer, feature_gyroscope, feature_temperature, feature_humidity

from sys import exit

from time import sleep
from config.config import ALLOWED_DEVICES
from listeners.CustomManagerListener import CustomManagerListener
from listeners.CustomFeatureListener import CustomFeatureListener

from blue_st_sdk.utils.uuid_to_feature_map import UUIDToFeatureMap
from blue_st_sdk.utils.ble_node_definitions import FeatureCharacteristic

def main():

    features = {0x00800000: feature_accelerometer, 0x00400000: feature_gyroscope, 0x00040000: feature_temperature, 0x00080000: feature_humidity }

    mask_to_features_dic = FeatureCharacteristic.SENSOR_TILE_BOX_MASK_TO_FEATURE_DIC
    mask_to_features_dic[0x00400000] = feature_gyroscope

    handled_devices  = {}
    feature_handlers = {}

    logger.info(f"Dispositivos permitidos: {ALLOWED_DEVICES}...")

    try:
        print("Creando manager...")
        manager = Manager.instance()
        manager_listener = CustomManagerListener()
        manager.add_listener(manager_listener)

        print("Buscando cajicas...")
        manager.discover()

        discovered_devices = manager.get_nodes()

        if not discovered_devices:
            print("No se ha detectado nada, así que pasando del tema...")
            exit(0)
        
        print(f"Se ha(n) descubierto {len(discovered_devices)} dispositivo(s)...")
        for device in discovered_devices:
            print(f"··· {device.get_name()} -- {device.get_tag()}")


        for device in discovered_devices:

            if device.get_name() in ALLOWED_DEVICES:
                print(f"Se permite el dispositivo '{device.get_name()}'!")
                handled_devices[device.get_name()] = device

        for deviceKey in handled_devices:
            device = handled_devices[deviceKey]

            print(f"Conectándose a {device.get_name()}...")
            if not device.connect():
                print("Lo intenté pero no pude :(")
                raise Exception("NOMEPUEDOCONECTARMECAGOENLALECHEMERCHE EXCEPTION")
            
            print("Si seguimos por aquí, pinta bien la cosa. Vamos a ver las features...")

            features = device.get_features()

            for feature in features:
                print(f"Se ha descubierto la feature {feature.get_name()}...")
                custom_feature = CustomFeatureListener(device.get_name())
                feature_handlers[device.get_name()] = custom_feature

                feature.add_listener(custom_feature)
                device.enable_notifications(feature)

        while True:
            for deviceKey in handled_devices:
                device = handled_devices[deviceKey]
                device.wait_for_notifications(0.5)

    except KeyboardInterrupt:
        print("Se ha detectado que se quiere que salir, así que hasta la vista, baby...")
        exit(0)
    except BlueSTInvalidFeatureBitMaskException  as e:
        print(f"Error habilitando todas las features {e}...")
    except Exception as e:
        print(f"Se ha piñado por {e}")
        exit(1)


if __name__ == "__main__":
    main()