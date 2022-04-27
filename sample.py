#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from sys import exit
from time import sleep

from blue_st_sdk.manager import Manager, BlueSTInvalidFeatureBitMaskException
from blue_st_sdk.features import feature_accelerometer, feature_gyroscope, feature_temperature, feature_humidity
from blue_st_sdk.utils.uuid_to_feature_map import UUIDToFeatureMap
from blue_st_sdk.utils.ble_node_definitions import FeatureCharacteristic

from config.config import ALLOWED_DEVICES, OK_CODE_OK, ERROR_CODE_UNKNOWN_ERROR, OK_CODE_OK
from config.logger import logging

from listeners.CustomManagerListener import CustomManagerListener
from listeners.CustomFeatureListener import CustomFeatureListener

discovered_devices = []
handled_devices  = {}
feature_handlers = {}

def discover_devices(manager):
    manager.discover()
    global discovered_devices
    discovered_devices = manager.get_nodes()

    if not discovered_devices:
        logging.warning("No se ha detectado nada...")
        exit(OK_CODE_OK)
        
    logging.info(f"Se ha(n) descubierto {len(discovered_devices)} dispositivo(s)...")


def handle_device_features(device):
    features = device.get_features()

    for feature in features:
        logging.info(f"Se ha descubierto la feature {feature.get_name()}...")
        custom_feature = CustomFeatureListener(device.get_name())
        feature_handlers[device.get_name()] = custom_feature

        feature.add_listener(custom_feature)
        device.enable_notifications(feature)


def connect_devices():
    global handled_devices
    global feature_handlers

    for device in discovered_devices:
        if device.get_name() in ALLOWED_DEVICES:
            logging.info(f"Se permite el dispositivo '{device.get_name()}'!")
            handled_devices[device.get_name()] = device
        else:
            logging.warning(f"El dispositivo '{device.get_name()}' no está permitido!")

    for deviceKey in handled_devices:
        device = handled_devices[deviceKey]

        logging.info(f"Conectándose a {device.get_name()}...")

        if not device.connect():
            logging.error("No se pudo establecer la conexión")
            raise Exception(f"Error conectando al dispositivo {device.get_name()}")

        handle_device_features(device)
            
       
def main():
    global handled_devices
    global feature_handlers
    global discovered_devices

    features = {0x00800000: feature_accelerometer, 0x00400000: feature_gyroscope, 0x00040000: feature_temperature, 0x00080000: feature_humidity }

    mask_to_features_dic = FeatureCharacteristic.SENSOR_TILE_BOX_MASK_TO_FEATURE_DIC
    mask_to_features_dic[0x00400000] = feature_gyroscope

    try:
        logging.info("Creando manager...")
        manager = Manager.instance()
        manager_listener = CustomManagerListener()
        manager.add_listener(manager_listener)

        for device in discovered_devices:
            print(f"··· {device.get_name()} -- {device.get_tag()}")

        discover_devices(manager)
        connect_devices()

        while True:
            for deviceKey in handled_devices:
                device = handled_devices[deviceKey]
                device.wait_for_notifications(0.5)

    except KeyboardInterrupt:
        logging.info("Se ha detectado que se quiere que salir, así que hasta la vista, baby...")
        exit(OK_CODE_OK)
    except BlueSTInvalidFeatureBitMaskException  as e:
        logging.error(f"Error habilitando todas las features {e}...")
    except Exception as e:
        logging.error(f"Se ha piñado por {e}")
        exit(ERROR_CODE_UNKNOWN_ERROR)


if __name__ == "__main__":
    main()