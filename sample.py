#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from blue_st_sdk.manager import Manager, BlueSTInvalidFeatureBitMaskException

from blue_st_sdk.features import feature_accelerometer, feature_gyroscope, feature_temperature, feature_humidity

from sys import exit

from time import sleep
from listeners.CustomManagerListener import CustomManagerListener
from listeners.CustomFeatureListener import CustomFeatureListener

from blue_st_sdk.utils.uuid_to_feature_map import UUIDToFeatureMap
from blue_st_sdk.utils.ble_node_definitions import FeatureCharacteristic

def main():

    features = {0x00800000: feature_accelerometer, 0x00400000: feature_gyroscope, 0x00040000: feature_temperature, 0x00080000: feature_humidity }

    mask_to_features_dic = FeatureCharacteristic.SENSOR_TILE_BOX_MASK_TO_FEATURE_DIC
    mask_to_features_dic[0x00400000] = feature_gyroscope

    feature_listener = CustomFeatureListener()
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

        # There is no code like hardcode
        for device in discovered_devices:
            if device.get_name() == "lechuga":
                print("ESTE ES EL MÍO...")
                mah_device = device
                break

        if mah_device:
            print("Me conecto al mío")
            ## NO FUNCIONA PORQUE HAY QUE HACERLO AL INSTALAR LA APP CREO YO
            print(f";;;; Añadiendo features...")
            mah_device.add_external_features(mask_to_features_dic)
            print(f";;;; Añadidas features...")

            if not mah_device.connect():
                print("Lo intenté pero no pude :(")
                raise Exception("NOMEPUEDOCONECTARMECAGOENLALECHEMERCHE EXCEPTION")
            
        print("Si seguimos por aquí, pinta bien la cosa. Vamos a ver las features...")

        features = device.get_features()

        for feature in features:
            print(f"Se ha descubierto la feature {feature.get_name()}...")
            feature.add_listener(feature_listener)
            mah_device.enable_notifications(feature)

        while True:
            mah_device.wait_for_notifications(0.5)

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